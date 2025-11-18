from dataclasses import dataclass


@dataclass
class Config:
    jwt_secret: str
    access_token_expire: int
    refresh_token_expire: int
