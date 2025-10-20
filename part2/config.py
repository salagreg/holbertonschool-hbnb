import os


class Config:
    """Classe de configuration de base pour l'application Flask."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    """Classe de configuration spécifique à l'environnement de développement"""
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
