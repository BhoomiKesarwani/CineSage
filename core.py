# structured prompt
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()

model = ChatOllama(
    model="gemma4:31b",
    base_url="https://ollama.com",
)

class Movie(BaseModel):
    title: str
    release_year: int
    genre: str
    director: str
    cast: List[str]
    rating: Optional[float] = None
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

prompt=ChatPromptTemplate.from_messages([
    ("system","""
Extract movie information from the paragraph
{format_instructions}
"""),
("human","""{paragraph}""")
])  

para=input("Enter the paragraph: ")

final_prompt=prompt.invoke(
    { "paragraph": para, 
     "format_instructions": parser.get_format_instructions() 
     }
     )

response = model.invoke(final_prompt)
print(response.content)