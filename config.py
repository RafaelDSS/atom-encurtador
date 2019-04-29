import os


class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/encurtador'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'development'
    SECRET_KEY = 'jdkkwww804488r7648o083e19381e98ljej'


class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = 'production'
    SECRET_KEY = 'jdkkwww804488r7648o083e19381e98ljej'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
