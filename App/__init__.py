from flask import Flask

from App.ext import init_ext
from App.setting import envs, TEMPLATE_FOLDER, STATIC_FOLDER
from App.views import init_blue


def create_app():

    app = Flask(__name__, template_folder=TEMPLATE_FOLDER, static_folder=STATIC_FOLDER)



    app.config.from_object(envs.get("sqlite"))


    init_blue(app)

    init_ext(app)

    return app


