from pydantic import BaseSettings


class AppEnvironment(BaseSettings):

    APP_POSTGRES_USERNAME: str
    APP_POSTGRES_PASSWORD: str
    APP_POSTGRES_DB: str
    APP_POSTGRES_HOST: str 
    APP_POSTGRES_PORT: str

    # APP_MYSQL_USERNAME: str
    # APP_MYSQL_PASSWORD: str
    # APP_MYSQL_DB: str
    # APP_MYSQL_HOST: str 
    # APP_MYSQL_PORT: str

    APP_REDIS_PASSWORD: str
    APP_REDIS_HOST: str
    APP_REDIS_PORT: str
    APP_REDIS_DB: str
    APP_REDIS_DEFENDER_DB: str

    class Config:
        case_sensitive = True

# to auto renew data from .env -> keep call command when run some thing
# env = EnvSetting(_env_file='.env')
env = AppEnvironment(_env_file='.env')

if __name__ == "__main__":
    pass