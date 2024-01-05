from fastapi import FastAPI

from api.routers import task, done

app = FastAPI()
app.include_router(task.router)
app.include_router(done.router)



'''@app.get("/hello") #/helloのエンドポイントが"パス" "get"の部分がオペレーション
async def hello():
    return {"message": "hello world!"}'''

