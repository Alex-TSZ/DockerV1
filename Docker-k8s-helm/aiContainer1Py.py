import asyncio
import logging
from fastapi import FastAPI
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)

model = None

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model

    logging.info("Loading AI model")
    await asyncio.sleep(7)
    model = "Model-loaded"
    logging.info("AI model loaded successfully")

    yield

    logging.info("Shutting down AI")

app.router.lifespan_context = lifespan

@app.get("/")
async def root():
    return {
        "status": "running",
        "model": model
    }

@app.get("/health")
async def health():
    return {"status": "ok"}