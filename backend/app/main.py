from fastapi import FastAPI
from .api.endpoints import summarizer
from .core.config import settings
from .core.logger import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="GenAi Assessment API")

app.include_router(summarizer.router, prefix="/api/v1")
# Initialize FastAPI with /api/v1 router for summarizer endpoint
