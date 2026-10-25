# python -m streamlit run UIcore.py
import streamlit as st
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Initialize model
model = ChatOllama(
    model="gemma4:31b",
    base_url="https://ollama.com",
)

# Define movie structure
class Movie(BaseModel):
    title: str
    release_year: int
    genre: str
    director: str
    cast: List[str]
    rating: Optional[float] = None
    summary: str


# Initialize parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """Extract movie information from the given paragraph.

{format_instructions}
"""
    ),
    ("human", "{paragraph}")
])

# Streamlit UI
st.title("🎬 Movie Information Extractor")
st.write("Enter a movie paragraph to extract its important information.")

paragraph = st.text_area(
    "Enter the movie paragraph",
    placeholder=(
        "Example: Interstellar is a science fiction film directed by "
        "Christopher Nolan. Released in 2014, it stars Matthew McConaughey "
        "and Anne Hathaway..."
    ),
    height=180
)

if st.button("Extract Movie Information", type="primary"):
    if not paragraph.strip():
        st.warning("Please enter a paragraph first.")
    else:
        try:
            with st.spinner("Extracting movie information..."):
                final_prompt = prompt.invoke({
                    "paragraph": paragraph,
                    "format_instructions": parser.get_format_instructions()
                })

                response = model.invoke(final_prompt)

                # Parse model output into the Pydantic model
                movie = parser.parse(response.content)

            st.success("Movie information extracted successfully!")

            st.subheader("📽️ Extracted Information")

            st.write("**Title:**", movie.title)
            st.write("**Release Year:**", movie.release_year)
            st.write("**Genre:**", movie.genre)
            st.write("**Director:**", movie.director)

            st.write("**Cast:**")
            for actor in movie.cast:
                st.write(f"- {actor}")

            st.write(
                "**Rating:**",
                movie.rating if movie.rating is not None else "Not available"
            )

            st.write("**Summary:**")
            st.write(movie.summary)

            # Display structured output
            with st.expander("View structured output"):
                st.json(movie.model_dump())

        except Exception as e:
            st.error(f"An error occurred: {e}")
