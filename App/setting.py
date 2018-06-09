import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_FOLDER = os.path.join(BASE_DIR, "templates")

STATIC_FOLDER = os.path.join(BASE_DIR, "static")


def create_db_uri(dbinfo):

    ENGINE = dbinfo.get("ENGINE") or "mysql"

    DRIVER = dbinfo.get("DRIVER") or "pymysql"

    USER = dbinfo.get("USER") or "root"

    PASSWORD = dbinfo.get("PASSWORD") or "rock1204"

    HOST = dbinfo.get("HOST") or "localhost"

    PORT = dbinfo.get("PORT") or "3306"

    NAME = dbinfo.get("NAME") or "kkkk"

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config():

    DEBUG = False

    TESTING = False

    SECRETY_TYPE = "oiqu89728hfjhajklsdhf"

    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopConfig(Config):

    DEBUG = True

    DATABASES = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "axfflask",
    }

    SQLALCHEMY_DATABASE_URI = create_db_uri(DATABASES)


class TestingConfig(Config):
    DEBUG = True

    DATABASES = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test03",
    }

    SQLALCHEMY_DATABASE_URI = create_db_uri(DATABASES)


class StatusConfig(Config):
    DEBUG = True

    DATABASES = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test03",
    }

    SQLALCHEMY_DATABASE_URI = create_db_uri(DATABASES)


class ProductConfig(Config):
    DEBUG = True

    DATABASES = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "rock1204",
        "HOST": "localhost",
        "PORT": 3306,
        "NAME": "test03",
    }

    SQLALCHEMY_DATABASE_URI = create_db_uri(DATABASES)



class SqliteConfig(Config):

    DEBUG = True


    SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "status": StatusConfig,
    "product": ProductConfig,
    "sqlite": SqliteConfig,
    "default": DevelopConfig,
}


















