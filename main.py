import uvicorn # type: ignore
from fastapi import FastAPI # type: ignore
from dotenv import load_dotenv # type: ignore
from src.routes.generate import brd_router # type: ignore
from src.routes.edit_platforms import platforms_router
from src.routes.edit_timeline import timeline_router
from src.routes.edit_func_req import func_req_router
load_dotenv()
app=FastAPI()


@app.get('/')
def read_root():
    return {"message": "Welcome to the Brd generation API"}
app.include_router(router=brd_router)
app.include_router(router=platforms_router)
app.include_router(router=timeline_router)
app.include_router(router=func_req_router)


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8000,reload=True)
