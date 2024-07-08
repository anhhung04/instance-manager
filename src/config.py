import os

config = {
    "PORT": 8000,
    "HOST": "0.0.0.0",
    "workers": 4,
    "PROD": os.getenv("PROD", False),
    # "DATABASE_URL": os.getenv("DATABASE_URL", "sqlite:///./dev.db"),
    "DATABASE_URL": os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://dev_user:dev_password@localhost:5432/dev_db",
    ),
    "REDIS_HOST": os.getenv("REDIS_HOST", "localhost"),
    "REDIS_PORT": os.getenv("REDIS_PORT", 6379),
    "MAX_CONNECTIONS_REDIS": os.getenv("MAX_CONNECTIONS_REDIS", 10),
    "JWT_EXPIRATION": os.getenv("JWT_EXPIRATION", 3600 * 24),
    "PASSWORD_SALT": os.getenv("PASSWORD_SALT", "salt"),
    "ALLOWED_ORIGINS": ["*"],
    "CHALLENGES": {
        "DEFAULT_SOURCE_PATH": "/tmp",
    },
    "DOCKER": {
        "HOST": os.getenv("DOCKER_HOST", "unix:///var/run/docker.sock"),
        "USERNAME": os.getenv("DOCKER_USERNAME", ""),
        "PASSWORD": os.getenv("DOCKER_PASSWORD", ""),
        "REGISTRY": os.getenv("DOCKER_REGISTRY", "https://index.docker.io/v1/"),
    },
    "DEBUG": os.getenv("DEBUG", False),
    "PUBLIC_KEY": os.getenv("PUBLIC_KEY", ""),
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY", ""),
    "BOT_TOKEN": os.getenv("BOT_TOKEN", "i_am_bot"),
}
