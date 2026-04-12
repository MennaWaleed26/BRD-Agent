import uvicorn # type: ignore
from fastapi import FastAPI # type: ignore
from dotenv import load_dotenv # type: ignore
from src.routes.generate import brd_router # type: ignore
from src.helpers.config import settings
from langchain_openai import ChatOpenAI # type: ignore

load_dotenv()
app=FastAPI()


@app.get('/')
def read_root():
    return {"message": "Welcome to the Brd generation API"}
app.include_router(router=brd_router)

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)
