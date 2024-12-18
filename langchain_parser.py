from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

messages = [
    SystemMessage(content="You are a Project Manager!"),
    HumanMessage(content="What is the first thing to do after I decided my niche to start a project?" )
]

parser = StrOutputParser()

chain = model | parser

print(chain.invoke(messages))