from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate

openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper().createInstance()


# Increase accuracy of response by showing the intermediates steps and promote the transparency.
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional Math scientist",
        ),
        (
            "user",
            """ 
            Consider the problem: 'A store had 22 apples. 
            They sold 15 apples today and got a new delivery of 8 apples. 
            How many apples are there now?’

            Break down each step of your calculation
            """,
        ),
    ]
)

chain = prompt | llm
response = chain.invoke({})
print(response.content)
