# Install the specific LangChain integration package
# pip install langchain-ollama

from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage

# Initialize the ChatOllama model (similar to ChatOpenAI)
llm = ChatOllama(model="mistral")

# Invoke the model
response = llm.invoke([HumanMessage(content="Code for fibonacci in python?")])

# Print the response content
print(response.content)
