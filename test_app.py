"""
Unit Tests cho ứng dụng Flask
"""

import pytest
import json
from app import app

@pytest.fixture
def client():
    """Tạo test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test trang chủ"""
    response = client.get('/')
    assert response.status_code == 200

def test_health_endpoint(client):
    """Test health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    assert 'version' in data

def test_info_endpoint(client):
    """Test info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['app_name'] == 'DevOps CI/CD Demo'
    assert 'version' in data
    assert 'features' in data
    assert isinstance(data['features'], list)

def test_pipeline_endpoint(client):
    """Test pipeline endpoint"""
    response = client.get('/api/pipeline')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert 'stages' in data
    assert len(data['stages']) == 3
    
    # Kiểm tra các stages
    stage_names = [stage['name'] for stage in data['stages']]
    assert 'Test' in stage_names
    assert 'Build' in stage_names
    assert 'Deploy' in stage_names

def test_404_error(client):
    """Test xử lý lỗi 404"""
    response = client.get('/api/notfound')
    assert response.status_code == 404
    
    data = json.loads(response.data)
    assert 'error' in data

def test_api_response_format(client):
    """Test format của API responses"""
    endpoints = ['/api/health', '/api/info', '/api/pipeline']
    
    for endpoint in endpoints: 
        response = client.get(endpoint)
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        # Đảm bảo response là valid JSON
        data = json.loads(response.data)
        assert isinstance(data, dict)