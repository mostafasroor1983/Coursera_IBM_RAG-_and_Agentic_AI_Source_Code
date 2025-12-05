from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from prompt_formatter import PromptFormatter

openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper().createInstance()


content = """
    The rapid advancement of technology in the 21st century has transformed various industries, including healthcare, education, and transportation. 
    Innovations such as artificial intelligence, machine learning, and the Internet of Things have revolutionized how we approach everyday tasks and complex problems. 
    For instance, AI-powered diagnostic tools are improving the accuracy and speed of medical diagnoses, while smart transportation systems are making cities more efficient and reducing traffic congestion. 
    Moreover, online learning platforms are making education more accessible to people around the world, breaking down geographical and financial barriers. 
    These technological developments are not only enhancing productivity but also contributing to a more interconnected and informed society.
"""

template = """Summarize the {content} in one sentence."""

prompt = ChatPromptTemplate.from_template(template)
formatter = PromptFormatter(prompt)

# Create the chain with explicit formatting
joke_chain = RunnableLambda(formatter.format) | llm | StrOutputParser()

# Run the chain
response = joke_chain.invoke({"content": content})
print(response)
