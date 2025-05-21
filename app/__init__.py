from flask import Flask

def create_app():
    print("Creating Flask app...")  # Debugging line
    app = Flask(__name__)

    # Register blueprints or other components
    from .routes import main
    app.register_blueprint(main)

    print("App created successfully.")  # Debugging line
    return app
