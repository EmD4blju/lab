from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, List

#~ --- Setup LLM --- 
llm = ChatOllama(model='llama3:8b')

#~ --- Define the state structure ---
class State(TypedDict):
    messages: Annotated[List, add_messages]
    devices: Annotated[List[str], lambda old, new: new]
   
#~ --- Develop a graph & compile it ---    
graph_builder = StateGraph(State)

def get_devices(state: State):
    devices = ['phone', 'laptop', 'pc']
    return {
        "devices": devices,
        "messages": state["messages"]
    }

def chatbot(state: State):
    return {
        "messages": [llm.invoke(state["messages"])]
    }
    
graph_builder.add_node('chatbot', chatbot)
graph_builder.add_node('get_devices', get_devices)
graph_builder.add_edge(START, 'chatbot')
graph_builder.add_edge('chatbot',  'get_devices')
graph_builder.add_edge('get_devices', END)

graph = graph_builder.compile()

state = {"messages": []}
while True:
    user_input = input('Enter a message: ')
    state["messages"].append({'role':'user', 'content': user_input})
    state = graph.invoke(state)
    print(state['messages'][-1].content)
    print(state['devices'])