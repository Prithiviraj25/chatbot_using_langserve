from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes

from langchain_community.llms import Ollama
import uvicorn
import os

from dotenv import load_dotenv

load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#creating the route for using Ollama
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A server with only one route using ollama llama3 llm"
)

llm=Ollama(model="llama3") #model is declared 
prompt=ChatPromptTemplate.from_template("Give me the information of {name} animal") #template of the prompt is given
add_routes(
    app,
    prompt|llm,
    path="/animalinfo"
)

if __name__ == "__main__": 
    uvicorn.run(app,host="localhost",port=8000)



