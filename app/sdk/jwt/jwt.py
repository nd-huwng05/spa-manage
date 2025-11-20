import os
from flask_jwt_extended import JWTManager
from app.sdk import log

class JWTConfig:
    def __init__(self, app):
        jwt_secret = os.getenv("JWT_SECRET_KEY")
        if jwt_secret is None:
            log.errorf("JWT_SECRET_KEY environment variable not set")

        self.jwt_access_token_expires = os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600)
        app.config["JWT_SECRET_KEY"] = jwt_secret
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = self.jwt_access_token_expires
        self.jwt = JWTManager(app)

    def get_jwt(self):
        return self.jwt