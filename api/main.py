from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/s2s")
async def receive_data(request: Request):
    # 알리가 쏜 JSON 데이터를 읽습니다
    json_data = await request.json()
    
    # 지금은 테스트니까 받은 데이터를 그대로 로그에 찍습니다
    # 나중에 여기서 DB에 저장하거나 툴로 보내는 로직을 넣으면 됩니다
    print(f"알리 신호 도착: {json_data}")
    
    return {"status": "success", "message": "Data received"}

@app.get("/")
async def root():
    return {"message": "Exmi API Server is Running!"}