from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from prompt_formatter import PromptFormatter


openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper().createInstance()


template = """
    You are a professional product reviwer, you have long experience in evaluating products and
    spoting their pros and cons.
    I will share with you a product's review and you will provide the following:
    
    1/ Identify the sentiment (positive, negative, or neutral).
    2/ Extract mentioned product features.
    3/ Provide a one-sentence summary of the review.

    I want yout to provide the response in JSON format and stick to this schema:
    /{{"name":"string","sentiment": "string", "features":"array", "sumamry":"string" /}}
    
    Here is the product's review {review} please do the needful step bt step.

"""

reviews = [
    "I love this smartphone! The camera quality is exceptional and the battery lasts all day. The only downside is that it heats up a bit during gaming.",
    "This laptop is terrible. It's slow, crashes frequently, and the keyboard stopped working after just two months. Customer service was unhelpful.",
]

prompt = ChatPromptTemplate.from_template(template)
formatter = PromptFormatter(prompt)

prodcut_review_chain = RunnableLambda(formatter.format) | llm | StrOutputParser()
for r in reviews:
    response = prodcut_review_chain.invoke({"review": r})
    print(response)
