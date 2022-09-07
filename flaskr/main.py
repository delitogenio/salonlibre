from flask import Flask, request, render_template, redirect
import os
import logging, logging.config

from Metodos.Login import Login

logging.basicConfig(level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s',
                    handlers=[
                        logging.FileHandler('extractdata.log'),
                        logging.StreamHandler()
                    ])


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    SESSION_TYPE = 'filesystem'
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    @app.route('/')
    def hello():
        logging.info(request.url + ' ' + request.method)
        return redirect ('/login/login')

    app.register_blueprint(Login.bplogin)
    if __name__ == "__main__":
        app.run(debug=True)

    return app

create_app()

