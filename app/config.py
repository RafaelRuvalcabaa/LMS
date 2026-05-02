from pydantic_settings  import BaseSettings

from functools import lru_cache

class Settings(BaseSettings): 
    app_name: str = "Loan System API"
    app_description: str = "Loan System by Rafael Ruvalcaba"
    app_version: str = "1.0.0"
    debug: bool = False

    # Persistencia
    loans_file: str = "loans.json"

    # Email (Fase 05)
    email_from: str = "noreply@loansystem.dev"
    email_enabled: bool = False
    resend_api_key: str = ""

    # Seguridad (Fase 07)
    secret_key: str = "desarrollo-loan-system-2026"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    return Settings()