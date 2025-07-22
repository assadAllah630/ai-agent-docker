# app.py: API بسيط باستخدام FastAPI لاستدعاء LangGraph Agent
from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent.graph import graph

app = FastAPI()
llm_app = graph.compile()

class QueryRequest(BaseModel):
    input_text: str

@app.post("/invoke")
async def invoke_agent(request: QueryRequest):
    state = {"input_text": request.input_text}
    result = llm_app.invoke(state)
    return {"output": result["output"]}

@app.get("/")
def root():
    return {"message": "LangGraph Agent API is running!"} 