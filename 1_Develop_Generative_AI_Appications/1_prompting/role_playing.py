from openaiclient_wrapper import OpenAIChatWrapper
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from prompt_formatter import PromptFormatter


openaiclient_wrapper = OpenAIChatWrapper()
llm = OpenAIChatWrapper().createInstance()


role = """
    Dungeon & Dragons game master
    """

tone = "engaging and immersive"
template = """
    You are an expert {role}. I have this question {question}. I would like our conversation to be {tone}.
    Answer:
"""
prompt = PromptTemplate.from_template(template)
formatter = PromptFormatter(prompt)


# Create the LCEL chain
roleplay_chain = RunnableLambda(formatter.format) | llm | StrOutputParser()

# Create an interactive chat loop
while True:
    query = input("Question: ")
    if query.lower() in ["quit", "exit", "bye"]:
        print("Answer: Goodbye!")
        break
    response = roleplay_chain.invoke({"role": role, "question": query, "tone": tone})
    print("Answer: ", response)
