from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    DATABASE_URL: str
    ACCESS_TOKEN_TIME: int
    REFRESH_TOKEN_TIME: int
    SECRET_KEY: str
    ALGORITHM: str
    BROKER: str
    EMAIL_PASS: str

    model_config = {
        'env_file': '.env'
    }

setting = Setting()

DATABASE_URL = setting.DATABASE_URL
ACCESS_TOKEN_TIME = setting.ACCESS_TOKEN_TIME
REFRESH_TOKEN_TIME = setting.REFRESH_TOKEN_TIME
SECRET_KEY = setting.SECRET_KEY
ALGORITHM = setting.ALGORITHM
BROKER = setting.BROKER
EMAIL_PASS = setting.EMAIL_PASS