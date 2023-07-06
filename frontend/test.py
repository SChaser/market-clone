from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.memodb
memo_table = db.memos
app = FastAPI()

memos = []

class Memo(BaseModel):
    content:str

@app.put("/memos/{id}")
def update_memo(update_memo:Memo, id:str):
    result = memo_table.update_one({'_id':id}, {'$set': update_memo.dict()})
    if result:
        return "메모 수정에 성공했습니다."
    return "id가 존재하지 않습니다"


@app.delete("/memos/{id}")
def delete_memo(id:str):
    result = memo_table.delete_one({"_id":id})
    if result:
        return "메모 삭제에 성공했습니다"
    return "id가 존재하지 않습니다"

@app.get("/memos")
def read_memo():
    memos = list(memo_table.find())
    return memos

@app.post("/memos")
def create_memo(memo:Memo):
    memo_dict = memo.dict()
    memo_dict["_id"] = str(ObjectId())
    memo_table.insert_one(memo_dict)
    return "메모 추가에 성공했습니다."

app.mount("/", StaticFiles(directory="./static", html=True), name="memo")