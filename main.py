import os
import json
import logging
import requests
from datetime import datetime

from groq import Groq

from typing import Union
from fastapi import APIRouter, FastAPI
from fastapi import HTTPException, status
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO, filename="logs.log")
logger = logging.getLogger(__name__)

BASE_URL_API_DJANGO = os.getenv("BASE_URL_API_DJANGO_STAGING" if os.getenv("DEBUG") != "True" else "BASE_URL_API_DJANGO_PROD")

class Item(BaseModel):
    username: str
    password: str
    context: str | None = None


app = FastAPI()
router = APIRouter()


def api_v1_check_user(username:str, password:str):
    url = f"{BASE_URL_API_DJANGO}/api/v1/check-user/{username}/{password}"
    try:
        return requests.get(
            url=url
            ).json()
    except Exception as e:
        print(e)
        return None
    

@router.post("/api/groq/v1/generate-post-text-with-groq-IA/", summary="Gerar conteúdo com IA", description="Gera um texto baseado no contexto usando IA.")
def api_v1_generate_post_text_with_groq_IA(item: Item):

    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = api_v1_check_user(username=item.username, password=item.password)
    if not user or user.get("message") != "is_valid":
        logger.error(f"ERROR CHECKUSER: {dt} | {user} ")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Credenciais inválidas ou erro ao verificar usuário."
        )
        
    data = {"role": "user", "content": f"{item.context.strip()}"}
    client = Groq(api_key=os.getenv('GROQ_API_KEY_1'))
    try:
        chat_completion = client.chat.completions.create(
            messages=[data],
            model=os.getenv("GROP_API_MODEL"),
            stream=False,
        )
        logger.info(f"create_text_to: {dt} | {item.username}")
        return {"data": {
            "statusCode": 200,
            "content": chat_completion.choices[0].message.content
        }}
    except Exception as e:
        logger.error(f"Error: {dt} | {e}")
        return {"data": {
            "statusCode": 400,
            "content": "",
            "msg": "Erro ao gerar conteúdo! Verifique suas credenciais www.estampaverso.shop ou o conteúdo inserido."
        }}


app.include_router(router)