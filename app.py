"""
Ứng dụng Flask Demo cho DevOps và CI/CD
Tác giả: Nhóm DevOps Demo
"""

from flask import Flask, render_template, jsonify
from datetime import datetime
import os

app = Flask(__name__)

# Configuration
app.config['VERSION'] = '1.0.0'
app.config['ENV'] = os.getenv('ENVIRONMENT', 'development')

@app.route('/')
def index():
    """Trang chủ hiển thị thông tin về DevOps và CI/CD"""
    return render_template('index.html')

@app.route('/api/health')
def health():
    """Health check endpoint cho monitoring"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': app.config['VERSION']
    }), 200

@app.route('/api/info')
def info():
    """Thông tin về ứng dụng"""
    return jsonify({
        'app_name': 'DevOps CI/CD Demo',
        'version': app.config['VERSION'],
        'environment': app.config['ENV'],
        'python_version': '3.11',
        'framework': 'Flask',
        'timestamp': datetime.now().isoformat(),
        'features': [
            'CI/CD Pipeline với GitHub Actions',
            'Docker Containerization',
            'Automated Testing',
            'Health Monitoring'
        ]
    }), 200

@app.route('/api/pipeline')
def pipeline():
    """Mô tả CI/CD pipeline"""
    return jsonify({
        'stages': [
            {
                'name': 'Test',
                'description': 'Chạy unit tests và coverage',
                'tools': ['pytest', 'pytest-cov']
            },
            {
                'name': 'Build',
                'description': 'Build Docker image',
                'tools':  ['Docker', 'docker-compose']
            },
            {
                'name': 'Deploy',
                'description': 'Deploy lên production',
                'tools': ['GitHub Actions', 'Docker Hub']
            }
        ]
    }), 200

@app.errorhandler(404)
def not_found(error):
    """Xử lý lỗi 404"""
    return jsonify({'error': 'Endpoint không tồn tại'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Xử lý lỗi 500"""
    return jsonify({'error': 'Lỗi server nội bộ'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)