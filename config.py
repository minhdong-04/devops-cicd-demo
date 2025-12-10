"""
Configuration file cho DevOps CI/CD Demo application
Quản lý các environment variables và settings
"""

import os
from typing import Dict, Any


class Config:
    """Base configuration"""
    
    # Application
    APP_NAME: str = "DevOps CI/CD Demo"
    VERSION: str = "1.0.0"
    
    # Flask
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    FLASK_APP: str = os.getenv('FLASK_APP', 'app.py')
    FLASK_DEBUG: bool = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # Server
    HOST: str = os.getenv('HOST', '0.0.0.0')
    PORT: int = int(os.getenv('PORT', 5000))
    
    # Environment
    ENVIRONMENT: str = os.getenv('ENVIRONMENT', 'development')
    
    # Logging
    LOG_LEVEL:  str = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FORMAT: str = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """
        Get all configuration as dictionary
        
        Returns: 
            dict: Configuration dictionary
        """
        return {
            'app_name': cls.APP_NAME,
            'version': cls.VERSION,
            'environment': cls.ENVIRONMENT,
            'debug': cls.FLASK_DEBUG,
            'host': cls.HOST,
            'port': cls.PORT,
        }


class DevelopmentConfig(Config):
    """Development configuration"""
    FLASK_DEBUG = True
    ENVIRONMENT = 'development'


class ProductionConfig(Config):
    """Production configuration"""
    FLASK_DEBUG = False
    ENVIRONMENT = 'production'


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    ENVIRONMENT = 'testing'


# Config dictionary
config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config(env_name: str = None) -> Config:
    """
    Get configuration based on environment name
    
    Args:
        env_name: Environment name (development/production/testing)
        
    Returns:
        Config object
    """
    if env_name is None:
        env_name = os.getenv('ENVIRONMENT', 'development')
    
    return config_by_name.get(env_name, DevelopmentConfig)