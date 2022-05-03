from app import app

from app.config.config import flask_config

if __name__ == '__main__':
    app.run(host= flask_config["host"], port= flask_config["port"], debug= flask_config["debug"])
    # app.run(host= flask_config["host"], port= flask_config["port"], debug= flask_config["debug"], ssl_context= context)