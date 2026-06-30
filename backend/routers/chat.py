from fastapi import APIRouter
from pydantic import BaseModel

from rag_types.Basic_rag.rag import answer_question

router = APIRouter()

class Question(BaseModel):
    question: str


@router.post("/chat")
async def chat(data: Question):

    answer = answer_question(data.question)

    return {
        "answer": answer
    }