import uvicorn
from fastapi import FastAPI, HTTPException
from kafka_server import Producer
from manager_data import ManagerData

app = FastAPI()

kafka = Producer()  # need to enter host
manager = ManagerData()


@app.get("/get_interesting_data")
def get_interesting_data():
    try:
        data = manager.get_interesting_data()
        kafka.send_data(data, "interesting_data")
        return {"status": "sent", "size": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/get_not_interesting_data")
def get_not_interesting_data():
    try:
        data = manager.get_not_interesting_data()
        kafka.send_data(data, "not_interesting_data")
        return {"status": "sent", "size": len(data)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/get_20_newsgroups")
def get_20_newsgroups():
    try:
        return manager.get_20_newsgroups()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#for testing
if __name__ == "__main__":
    uvicorn.run("main:producer_app", host="0.0.0.0", port=8000, reload=True)
