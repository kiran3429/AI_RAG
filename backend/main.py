from fastapi import FastAPI

from routers.upload import router as upload_router
from routers.chat import router as chat_router
from routers.recommendation import router as recommendation_router

app = FastAPI(title="RAG Studio API")
app.include_router(recommendation_router)
app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "Backend Running"}