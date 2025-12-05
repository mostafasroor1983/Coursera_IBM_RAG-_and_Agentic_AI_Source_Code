from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from prompt_formatter import PromptFormatter


openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper().createInstance()


template = "Tell me an {adjective} joke about the {content}"
prompt = ChatPromptTemplate.from_template(template)
formatter = PromptFormatter(prompt)

# Create the chain with explicit formatting
joke_chain = RunnableLambda(formatter.format) | llm | StrOutputParser()

# Run the chain
response = joke_chain.invoke({"adjective": "funny", "content": "chickens"})
print(response)
