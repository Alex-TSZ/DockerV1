import asyncio
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)

model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model

    logging.info("Loading AI model")
    await asyncio.sleep(7)
    model = "Model-loaded"
    logging.info("AI model loaded successfully")

    yield

    logging.info("Shutting down AI")

app = FastAPI(lifespan=lifespan)
