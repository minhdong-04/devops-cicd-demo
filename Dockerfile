# Multi-stage build để tối ưu kích thước image

# Stage 1: Build stage
FROM python:3.11-slim as builder

# Thiết lập working directory
WORKDIR /app

# Copy requirements và install dependencies
COPY requirements.txt . 

# Install dependencies vào một layer riêng để cache
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production stage
FROM python:3.11-alpine

# Metadata
LABEL maintainer="DevOps Demo Team"
LABEL description="DevOps CI/CD Demo Application with Python Flask"

# Thiết lập working directory
WORKDIR /app

# Copy Python dependencies từ builder stage
COPY --from=builder /root/.local /root/.local

# Copy application code
COPY app.py . 
COPY templates/ templates/

# Đảm bảo Python packages có thể được tìm thấy
ENV PATH=/root/.local/bin:$PATH

# Expose port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT=production

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')" || exit 1

# Run application với gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
