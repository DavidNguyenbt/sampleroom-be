import os
from pathlib import Path

def get_secret(key: str, default=None):
    secret_file = Path("/run/secrets/env")

    if secret_file.exists():
        values = {}

        with open(secret_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or "=" not in line:
                    continue

                k, v = line.split("=", 1)
                values[k.strip()] = v.strip()

        return values.get(key, default)

    return os.getenv(key, default)


class Settings:
    APP_NAME = get_secret("APP_NAME", "FastAPI")

    DB_DRIVER = get_secret("DB_DRIVER")
    DB_SERVER = get_secret("DB_SERVER")
    DB_NAME = get_secret("DB_NAME")
    DB_USER = get_secret("DB_USER")
    DB_PASSWORD = get_secret("DB_PASSWORD")
    DB_ENCRYPT = get_secret("DB_ENCRYPT")
    DB_TRUST_SERVER_CERTIFICATE = get_secret(
        "DB_TRUST_SERVER_CERTIFICATE"
    )


settings = Settings()