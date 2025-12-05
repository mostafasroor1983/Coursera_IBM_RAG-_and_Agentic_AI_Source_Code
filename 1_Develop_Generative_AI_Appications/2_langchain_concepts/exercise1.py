# In this exercise I am going to compate the respones coming from 2 different LLMs.
# Llama and Mistral

# from openaiclient_wrapper import OpenAIChatWrapper
from ollamaclient_wrapper import ChatOllamaWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

mistralclient_llm = ChatOllamaWrapper(model="mistral").createInstance()
phiclient_llm = ChatOllamaWrapper(model="phi").createInstance()

template = "What is the weather look like today in {city}?"
prompt = ChatPromptTemplate.from_template(template)

parser = StrOutputParser()

mistral_chain = prompt | mistralclient_llm | parser
phiclient_chain = prompt | phiclient_llm | parser

r1 = mistral_chain.invoke({"city": "Dubai"})
r2 = phiclient_chain.invoke({"city": "Dubai"})

print(r1)
print("#" * 50)
print(r2)
