from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate

openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper(max_tokens=10).createInstance()

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a professional movies reviewer and you can check and evaluate anyone.",
        ),
        (
            "user",
            """ I need you to classify a movie review as positive or negative, just mention one word..
                This movie was a complete waste of time. The plot was predictable, the characters were one-dimensional, and the pacing was slow. I wouldn't recommend it to anyone.
            """,
        ),
    ]
)

chain = prompt | llm
response = chain.invoke({})
print(response.content)
