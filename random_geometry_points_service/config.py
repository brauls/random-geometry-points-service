"""Config module that contains configs for the different application environments
"""

class Config(object):
    """The base application configuration
    """
    ENV = "production"
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    """The production configuration
    """
    pass

class DevelopmentConfig(Config):
    """The development configuration
    """
    ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    """The testing configuration
    """
    TESTING = True
