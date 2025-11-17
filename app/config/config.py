import os
from dataclasses import dataclass

@dataclass
class Config:
    jwt_secret: str
    access_token_expire: int
    refresh_token_expire: int


def get_global_config() -> Config:
    jwt_secret = os.getenv("JWT_SECRET_KEY")
    access_exp = os.getenv("ACCESS_TOKEN_EXPIRE")
    refresh_exp = os.getenv("REFRESH_TOKEN_EXPIRE")

    if not jwt_secret:
        raise Exception("JWT_SECRET is not set")

    if not access_exp:
        raise Exception("ACCESS_TOKEN_EXPIRE is not set")

    if not refresh_exp:
        raise Exception("REFRESH_TOKEN_EXPIRE is not set")

    return Config(
        jwt_secret=jwt_secret,
        access_token_expire=int(access_exp),
        refresh_token_expire=int(refresh_exp),
    )
