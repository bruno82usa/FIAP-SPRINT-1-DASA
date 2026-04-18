import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Application
    APP_NAME = "DASA Genera AI Assistant"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://genera_user:genera_password@localhost:5433/genera_db")
    
    # Vector Database
    VECTOR_DB_URL = os.getenv("VECTOR_DB_URL", "http://localhost:8002")
    VECTOR_DB_COLLECTION = "genetic_reports"
    
    # Redis
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6380")
    
    # File Storage
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./data/uploads")
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS = {".pdf"}
    
    # AI/ML
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-ada-002")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key-change-in-production")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES", "60"))
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS = int(os.getenv("RATE_LIMIT_REQUESTS", "100"))
    RATE_LIMIT_PERIOD = int(os.getenv("RATE_LIMIT_PERIOD", "60"))
    
    # Monitoring
    SENTRY_DSN = os.getenv("SENTRY_DSN", "")
    PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", "9091"))
    
    # Email
    EMAIL_HOST = os.getenv("EMAIL_HOST", "")
    EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
    EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
    
    @classmethod
    def validate(cls):
        """Validate required configuration"""
        errors = []
        
        # Check required AI keys (at least one)
        if not cls.OPENAI_API_KEY and not cls.ANTHROPIC_API_KEY:
            errors.append("Either OPENAI_API_KEY or ANTHROPIC_API_KEY must be set")
        
        # Check upload folder exists
        if not os.path.exists(cls.UPLOAD_FOLDER):
            os.makedirs(cls.UPLOAD_FOLDER, exist_ok=True)
        
        if errors:
            raise ValueError(f"Configuration errors: {', '.join(errors)}")
        
        return True

config = Config()