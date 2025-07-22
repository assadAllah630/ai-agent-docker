# agent/graph.py: Agent مع دعم OpenRouter chat models
import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph

def agent_node(state: dict) -> dict:
    llm = ChatOpenAI(
        model=os.environ.get("OPENAI_MODEL", "deepseek/deepseek-chat-v3-0324:free"),
        openai_api_base=os.environ.get("OPENAI_API_BASE", "https://openrouter.ai/api/v1"),
    )
    response = llm.invoke(state["input_text"])
    return {"input_text": state["input_text"], "output": response.content}

graph = StateGraph(dict)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.set_finish_point("agent") 