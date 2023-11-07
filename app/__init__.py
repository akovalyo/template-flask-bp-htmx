import os
from flask import Flask
from flask_assets import Bundle, Environment
import logging
from logging.handlers import RotatingFileHandler


app = Flask(
    __name__,
    static_folder="static",
)
env_config = os.getenv("PROD_APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

css_bundle = Bundle(
    "css/globals.css",
    "css/nav.css",
    "css/footer.css",
    filters="cssmin",
    output="css/styles.css",
)
assets = Environment(app)
assets.register("main_styles", css_bundle)


from app.main import bp as main_bp

app.register_blueprint(main_bp)

if not app.debug:
    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler("logs/log.log", maxBytes=102400, backupCount=10)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info("Template")
