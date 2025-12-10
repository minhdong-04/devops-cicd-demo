# 🐳 Docker Guide - Hướng Dẫn Docker Chi Tiết

> Tài liệu này giải thích chi tiết về Docker và cách sử dụng trong project DevOps CI/CD Demo

---

## 📑 Mục Lục

- [Docker là gì?](#docker-là-gì)
- [Tại sao dùng Docker?](#tại-sao-dùng-docker)
- [Các khái niệm cơ bản](#các-khái-niệm-cơ-bản)
- [Dockerfile Giải Thích](#dockerfile-giải-thích)
- [Docker Commands](#docker-commands)
- [Docker Compose](#docker-compose)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🐳 Docker là gì? 

**Docker** là một platform mã nguồn mở để phát triển, vận chuyển và chạy ứng dụng. Docker cho phép bạn: 

- 📦 **Đóng gói** ứng dụng và dependencies vào containers
- 🚀 **Chạy** ứng dụng ở bất kỳ đâu (local, server, cloud)
- 🔄 **Đảm bảo** môi trường development = production
- ⚡ **Tăng tốc** deployment và scaling

### So sánh Docker vs Virtual Machines

```
┌─────────────────────────────────┐  ┌─────────────────────────────────┐
│     VIRTUAL MACHINE             │  │        DOCKER CONTAINER         │
├─────────────────────────────────┤  ├─────────────────────────────────┤
│  App A   │   App B   │  App C   │  │  App A   │   App B   │  App C   │
├──────────┼───────────┼──────────┤  ├──────────┼───────────┼──────────┤
│  Libs    │   Libs    │   Libs   │  │  Libs    │   Libs    │   Libs   │
├──────────┼───────────┼──────────┤  ├─────────────────────────────────┤
│ Guest OS │  Guest OS │ Guest OS │  │        Docker Engine            │
├─────────────────────────────────┤  ├─────────────────────────────────┤
│        Hypervisor               │  │        Host OS                  │
├─────────────────────────────────┤  ├─────────────────────────────────┤
│        Host OS                  │  │        Infrastructure           │
└─────────────────────────────────┘  └─────────────────────────────────┘

   Nặng, chậm, tốn tài nguyên          Nhẹ, nhanh, tiết kiệm tài nguyên
```

---

## 🎯 Tại sao dùng Docker?

### 1. **"Works on my machine" Problem**

❌ **Trước khi có Docker**:
```
Developer: "Code chạy tốt trên máy tôi!"
Ops Team:   "Nhưng production lại lỗi..."
```

✅ **Với Docker**:
```
Developer: "Đây là Docker image, chạy ở đâu cũng được!"
Ops Team:  "Perfect! Deploy ngay!"
```

### 2. **Consistency (Tính nhất quán)**

- Môi trường development = staging = production
- Không bao giờ lo "missing dependencies"
- Version control cho cả infrastructure

### 3. **Isolation (Cô lập)**

- Mỗi container là một môi trường độc lập
- App A dùng Python 3.8, App B dùng Python 3.11 → Không conflict
- Security:  Container bị hack không ảnh hưởng host

### 4. **Scalability (Khả năng mở rộng)**

- Dễ dàng tạo nhiều instances
- Load balancing đơn giản
- Microservices architecture

### 5. **Speed (Tốc độ)**

- Start container trong vài giây (vs VM vài phút)
- Build once, run anywhere
- CI/CD pipeline nhanh hơn

---

## 📚 Các Khái Niệm Cơ Bản

### 1. **Docker Image**

- **Là gì?** Template chỉ đọc (read-only) để tạo containers
- **Giống như:** Class trong OOP
- **Ví dụ:** `python:3.11-alpine`, `nginx:latest`

```bash
# List images
docker images

# Pull image từ Docker Hub
docker pull python:3.11-alpine

# Remove image
docker rmi <image_name>
```

### 2. **Docker Container**

- **Là gì?** Instance chạy được của một image
- **Giống như:** Object trong OOP
- **Lifecycle:** Created → Running → Stopped → Removed

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# Start/Stop container
docker start <container_id>
docker stop <container_id>

# Remove container
docker rm <container_id>
```

### 3. **Dockerfile**

- **Là gì?** File text chứa instructions để build image
- **Syntax:** Declarative, dễ đọc
- **Best practice:** Multi-stage build

### 4. **Docker Registry**

- **Là gì?** Nơi lưu trữ và phân phối images
- **Docker Hub:** Public registry (như GitHub cho Docker images)
- **Private Registry:** AWS ECR, Google GCR, Harbor... 

### 5. **Docker Compose**

- **Là gì?** Tool để define và run multi-container applications
- **File:** `docker-compose.yml`
- **Use case:** Development environment, testing

---

## 📝 Dockerfile Giải Thích

### Project Dockerfile của chúng ta:

```dockerfile
# ============================================
# STAGE 1: BUILDER
# ============================================
FROM python: 3.11-slim as builder

# Tại sao dùng 'slim'? 
# - Image nhỏ hơn (100MB vs 900MB của python: 3.11 full)
# - Vẫn đủ tools để build dependencies

WORKDIR /app
# Thiết lập working directory = /app
# Tất cả commands sau sẽ chạy trong /app

COPY requirements.txt .
# Copy file requirements.txt vào /app
# Tách riêng step này để tận dụng Docker layer caching
# Nếu requirements không đổi → dùng cache → build nhanh

RUN pip install --no-cache-dir --user -r requirements.txt
# --no-cache-dir: Không lưu cache pip → giảm image size
# --user: Install vào ~/. local thay vì system-wide

# ============================================
# STAGE 2: PRODUCTION
# ============================================
FROM python:3.11-alpine
# Tại sao dùng 'alpine'?
# - Cực kỳ nhỏ gọn (~5MB base)
# - Security:  Ít packages → ít vulnerabilities

# Metadata
LABEL maintainer="DevOps Demo Team"
LABEL description="DevOps CI/CD Demo Application with Python Flask"

WORKDIR /app

# Copy Python packages từ builder stage
COPY --from=builder /root/.local /root/.local
# Multi-stage build: Chỉ copy kết quả, không copy build tools
# → Image production nhỏ gọn

# Copy application code
COPY app.py . 
COPY templates/ templates/

# Environment PATH
ENV PATH=/root/.local/bin:$PATH
# Đảm bảo Python packages có thể được tìm thấy

# Expose port
EXPOSE 5000
# Document port mà container lắng nghe
# Không thực sự open port (phải dùng -p khi run)

# Environment variables
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1
# PYTHONUNBUFFERED=1: Python output trực tiếp, không buffer
# → Xem logs realtime

ENV ENVIRONMENT=production

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/api/health')" || exit 1
# Docker tự động check health mỗi 30 giây
# Nếu fail 3 lần liên tiếp → container = unhealthy

# Run command
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--timeout", "120", "app:app"]
# Dùng gunicorn thay vì Flask development server
# --workers 4: Chạy 4 worker processes
# Production-ready WSGI server
```

### Multi-Stage Build Benefits:

**❌ Dockerfile thông thường**:
```dockerfile
FROM python:3.11
COPY .  .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

Result:  ~900MB image
```

**✅ Multi-stage build**:
```dockerfile
FROM python:3.11-slim as builder
# ...  build dependencies ... 

FROM python:3.11-alpine
COPY --from=builder ... 
# ... only copy results ... 

Result: ~50MB image (giảm 95%!)
```

---

## 🛠️ Docker Commands

### Basic Commands

#### 1. Build Image

```bash
# Build với tag
docker build -t devops-cicd-demo:latest .

# Build với custom Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build không dùng cache
docker build --no-cache -t myapp . 

# Build với build arguments
docker build --build-arg VERSION=1.0 -t myapp .
```

#### 2. Run Container

```bash
# Run basic
docker run devops-cicd-demo

# Run với port mapping
docker run -p 5000:5000 devops-cicd-demo

# Run detached mode (background)
docker run -d -p 5000:5000 --name my-app devops-cicd-demo

# Run với environment variables
docker run -e ENVIRONMENT=production -p 5000:5000 devops-cicd-demo

# Run với volume mount
docker run -v $(pwd):/app -p 5000:5000 devops-cicd-demo

# Run interactive (với shell)
docker run -it devops-cicd-demo /bin/sh
```

#### 3. Container Management

```bash
# List containers
docker ps              # Running containers
docker ps -a           # All containers
docker ps -q           # Only IDs

# Start/Stop
docker start <container_id>
docker stop <container_id>
docker restart <container_id>

# Remove
docker rm <container_id>
docker rm -f <container_id>    # Force remove
docker rm $(docker ps -aq)     # Remove all

# Logs
docker logs <container_id>
docker logs -f <container_id>  # Follow logs
docker logs --tail 100 <container_id>

# Execute command inside container
docker exec -it <container_id> /bin/sh
docker exec <container_id> ls -la
docker exec <container_id> python --version

# Inspect container
docker inspect <container_id>
docker inspect <container_id> | grep IPAddress

# Stats
docker stats                   # Real-time stats
docker stats <container_id>
```

#### 4. Image Management

```bash
# List images
docker images
docker images -a

# Remove images
docker rmi <image_name>
docker rmi $(docker images -q)  # Remove all

# Tag image
docker tag devops-cicd-demo:latest myusername/devops-cicd-demo:v1.0

# Push to registry
docker login
docker push myusername/devops-cicd-demo:v1.0

# Pull from registry
docker pull myusername/devops-cicd-demo:v1.0

# Save/Load images
docker save devops-cicd-demo > image.tar
docker load < image.tar

# Image history
docker history devops-cicd-demo
```

#### 5. Clean Up

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune
docker image prune -a          # All unused

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Remove everything
docker system prune
docker system prune -a --volumes

# Show disk usage
docker system df
```

---

## 🎼 Docker Compose

### docker-compose.yml Explained

```yaml
version: '3.8'
# Version của Docker Compose syntax

services:
  web:
    build: 
      context: .              # Đường dẫn chứa Dockerfile
      dockerfile: Dockerfile  # Tên Dockerfile (default:  Dockerfile)
    
    container_name: devops-demo-app
    # Custom container name
    
    ports: 
      - "5000:5000"
      # Host port :  Container port
      # Truy cập:  localhost:5000 → container: 5000
    
    environment: 
      - ENVIRONMENT=development
      - FLASK_DEBUG=False
      # Environment variables
    
    volumes:
      - ./app. py:/app/app.py
      - ./templates:/app/templates
      # Host path :  Container path
      # Changes trên host → tự động sync vào container
    
    restart: unless-stopped
    # Auto restart container nếu crash
    # Options: no, always, on-failure, unless-stopped
    
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/api/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
      # Docker check health định kỳ

networks:
  default:
    name: devops-demo-network
    # Custom network name
```

### Docker Compose Commands

```bash
# Start services
docker-compose up
docker-compose up -d              # Detached mode
docker-compose up --build         # Rebuild images

# Stop services
docker-compose down
docker-compose down -v            # Remove volumes
docker-compose down --rmi all     # Remove images

# View logs
docker-compose logs
docker-compose logs -f            # Follow
docker-compose logs web           # Specific service

# List services
docker-compose ps

# Execute command
docker-compose exec web /bin/sh
docker-compose exec web python --version

# Restart service
docker-compose restart web

# Scale services
docker-compose up -d --scale web=3

# Validate compose file
docker-compose config
```

### Advanced docker-compose. yml

```yaml
version: '3.8'

services:
  web:
    build:  .
    ports:
      - "5000:5000"
    depends_on:
      - redis
      - db
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    networks:
      - frontend
      - backend
  
  redis:
    image:  redis:alpine
    networks:
      - backend
  
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secretpassword
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend

networks:
  frontend:
  backend: 

volumes:
  postgres-data: 
```

---

## 🏆 Best Practices

### 1. **Dockerfile Best Practices**

#### ✅ DO: 

```dockerfile
# Use specific versions
FROM python:3.11-alpine

# Combine RUN commands to reduce layers
RUN apk add --no-cache gcc musl-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Use . dockerignore
# (Tương tự . gitignore)

# Non-root user
RUN adduser -D appuser
USER appuser

# Health check
HEALTHCHECK CMD curl -f http://localhost/ || exit 1
```

#### ❌ DON'T:

```dockerfile
# Don't use 'latest' tag
FROM python:latest

# Don't install unnecessary packages
RUN apt-get install vim curl wget htop

# Don't copy everything first
COPY . . 
RUN pip install -r requirements.txt

# Don't run as root
# (Security risk)

# Don't include secrets
ENV API_KEY=secret123
```

### 2. **Image Size Optimization**

```bash
# Trước optimization
python: 3.11              920MB
+ Your app code           50MB
= Total                  970MB

# Sau optimization
python:3.11-alpine        47MB
+ Multi-stage build        5MB
+ Your app code            3MB
= Total                   55MB

Giảm 94%!  🎉
```

**Tips để giảm image size**: 

1.  Dùng alpine base images
2. Multi-stage builds
3. . dockerignore file
4. Combine RUN commands
5. Remove cache và temporary files
6. Use --no-cache-dir cho pip

### 3. **Security Best Practices**

```dockerfile
# 1. Don't run as root
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser

# 2. Use specific versions
FROM python:3.11. 5-alpine3.18

# 3. Scan for vulnerabilities
# docker scan devops-cicd-demo

# 4. Use secrets management
# Don't: 
ENV DATABASE_PASSWORD=secret123

# Do:
# Pass at runtime:  docker run -e DATABASE_PASSWORD=$DB_PASS

# 5. Read-only filesystem
docker run --read-only devops-cicd-demo

# 6. Limit resources
docker run --memory="512m" --cpus="1.0" devops-cicd-demo
```

### 4. **Networking**

```bash
# Create custom network
docker network create myapp-network

# Run containers in same network
docker run --network myapp-network --name web myapp
docker run --network myapp-network --name db postgres

# Containers can communicate by name: 
# postgresql://db:5432/mydb
```

### 5. **Volumes & Data Persistence**

```bash
# Named volume
docker volume create myapp-data
docker run -v myapp-data:/app/data myapp

# Bind mount (development)
docker run -v $(pwd):/app myapp

# Read-only mount
docker run -v $(pwd):/app:ro myapp
```

---

## 🔧 Troubleshooting

### Problem 1: Container exits immediately

```bash
# Check logs
docker logs <container_id>

# Run interactive để debug
docker run -it devops-cicd-demo /bin/sh

# Check entrypoint/command
docker inspect <container_id> | grep -A 5 "Cmd"
```

### Problem 2: Cannot connect to container

```bash
# Check if container is running
docker ps

# Check port mapping
docker port <container_id>

# Check container IP
docker inspect <container_id> | grep IPAddress

# Test from inside container
docker exec <container_id> curl localhost:5000
```

### Problem 3: Image size too large

```bash
# Check layers
docker history devops-cicd-demo

# Analyze with dive
docker run --rm -it \
  -v /var/run/docker.sock:/var/run/docker.sock \
  wagoodman/dive:latest devops-cicd-demo
```

### Problem 4: Build cache issues

```bash
# Clear build cache
docker builder prune

# Build without cache
docker build --no-cache -t myapp .

# Check cache usage
docker system df
```

### Problem 5: Permission denied errors

```bash
# Run as root temporarily
docker exec -u root <container_id> /bin/sh

# Fix ownership
docker exec <container_id> chown -R appuser:appuser /app
```

---

## 📚 Resources

### Official Documentation
- [Docker Docs](https://docs.docker.com/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)

### Tools
- [Docker Hub](https://hub.docker.com/) - Public registry
- [Dive](https://github.com/wagoodman/dive) - Analyze image layers
- [Hadolint](https://github.com/hadolint/hadolint) - Dockerfile linter

### Learning
- [Docker Tutorial](https://docker-curriculum.com/)
- [Play with Docker](https://labs.play-with-docker.com/)

---

## 🎯 Summary

### Docker Workflow trong Project: 

```
1. Write Dockerfile
   ↓
2. Build image: docker build -t myapp . 
   ↓
3. Test local:  docker run -p 5000:5000 myapp
   ↓
4. Push to registry: docker push myusername/myapp
   ↓
5. Deploy:  docker pull && docker run (hoặc docker-compose up)
```

### Key Takeaways:

- ✅ Docker giải quyết "works on my machine" problem
- ✅ Containers nhẹ, nhanh, dễ scale hơn VMs
- ✅ Multi-stage builds giảm image size đáng kể
- ✅ Docker Compose đơn giản hóa multi-container apps
- ✅ Always follow security best practices

---

**[⬆ Back to top](#-docker-guide---hướng-dẫn-docker-chi-tiết)**
