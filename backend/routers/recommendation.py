from fastapi import APIRouter

from Services.rag_loader import get_available_rags

router = APIRouter()


@router.get("/rags")
def available_rags():

    return get_available_rags()