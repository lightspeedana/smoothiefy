from flask import Flask, render_template

def page_not_found(e): # If a page doesn't exist on the server, then this handles the error. 
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.register_error_handler(404, page_not_found)

    app.config.from_pyfile('settings.py')

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app