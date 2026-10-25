# 🎬 Movie Information Extractor

A simple AI-powered application that extracts structured movie information from a text paragraph using **LangChain, Ollama, Pydantic, and Streamlit**.

The application accepts a paragraph describing a movie and extracts key details such as its title, release year, genre, director, cast, rating, and summary.

## 🚀 Live Demo

Try CineSage here: [Open CineSage](https://cinesage-v2jdyue4gqykryhz33vd7h.streamlit.app/)

## ✨ Features

- **Movie Information Extraction:** Extracts important movie details from natural language text.
- **LLM Integration:** Uses the Gemma model through LangChain's Ollama integration.
- **Structured Output:** Uses Pydantic to define and validate the expected movie data structure.
- **Interactive UI:** Provides a simple, user-friendly interface built with Streamlit.
- **JSON Output:** Displays the extracted information in structured JSON format.
- **Input Validation:** Checks whether the user has entered a paragraph before processing.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web user interface |
| LangChain Core | Prompt templates and LLM workflow |
| LangChain Ollama | Integration with the Ollama-compatible model endpoint |
| Gemma 4 (31B) | Language model for information extraction |
| Pydantic | Structured data validation |
| Python-dotenv | Loading environment variables |

## 📂 Project Structure

```text
CineSage/
│
├── UIcore.py
├── requirements.txt
├── README.md
```

- `UIcore.py` — Contains the Streamlit UI and movie extraction logic.
- `requirements.txt` — Lists the Python dependencies.
- `README.md` — Provides project documentation.
- `.env` — Can store environment variables, such as API credentials if required by your endpoint.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Movie-Information-Extractor
```

Replace `<your-repository-url>` with your actual GitHub repository URL. Alternatively, download the project and open its folder in VS Code.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Ollama

The application is configured to use the following model:

```python
model = ChatOllama(
    model="gemma4:31b",
    base_url="https://ollama.com"
)
```

Ensure that the configured endpoint supports the model and that any required authentication is set up.

For local Ollama usage, install Ollama, ensure the model is available locally, and configure the application to use the local endpoint:

```python
model = ChatOllama(
    model="gemma4:31b",
    base_url="http://localhost:11434"
)
```

If the model is available in your local Ollama installation, you can check it using:

```bash
ollama list
```

### 5. Run the application

Start the Streamlit application:

```bash
streamlit run UIcore.py
```

Open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

## 🚀 How to Use

1. Launch the application.
2. Enter a paragraph describing a movie in the text area.
3. Click **Extract Movie Information**.
4. Wait for the language model to process the paragraph.
5. View the extracted movie details.
6. Expand the structured output section to inspect the JSON representation.

## 📝 Example Input

```text
Interstellar is a science fiction film directed by Christopher Nolan.
Released in 2014, the movie stars Matthew McConaughey, Anne Hathaway,
Jessica Chastain, and Michael Caine. The story follows a group of
astronauts who travel through a wormhole in search of a new home for
humanity as Earth faces environmental collapse.
```

## 📊 Expected Output

The application extracts information in the following structure:

```json
{
  "title": "Interstellar",
  "release_year": 2014,
  "genre": "Science Fiction",
  "director": "Christopher Nolan",
  "cast": [
    "Matthew McConaughey",
    "Anne Hathaway",
    "Jessica Chastain",
    "Michael Caine"
  ],
  "rating": null,
  "summary": "A group of astronauts travels through a wormhole in search of a new home for humanity."
}
```

*Note: This is an illustrative example. Actual results depend on the input paragraph and the language model's response. A rating may be unavailable if the paragraph does not provide one.*

## 🧠 How It Works

1. **Input:** The user provides a movie description.
2. **Prompt Creation:** LangChain combines the system instructions, formatting instructions, and user-provided paragraph.
3. **LLM Processing:** The configured Gemma model analyzes the paragraph and generates a response.
4. **Output Parsing:** `PydanticOutputParser` parses the response into the `Movie` model and validates the fields.
5. **Display:** Streamlit presents the extracted information and structured JSON output.

### Movie Data Model

The application uses the following fields:

| Field | Data Type | Description |
|---|---|---|
| `title` | String | Movie title |
| `release_year` | Integer | Year of release |
| `genre` | String | Movie genre |
| `director` | String | Director's name |
| `cast` | List of strings | Names of cast members |
| `rating` | Optional float | Rating, if available |
| `summary` | String | Brief movie summary |

## 📦 Requirements

The project dependencies are listed in `requirements.txt`:

```text
streamlit
langchain-core
langchain-ollama
pydantic
python-dotenv
```

## ⚠️ Limitations

- Extraction accuracy depends on the quality of the input and model response.
- Missing details may be returned incorrectly or may cause parsing errors.
- The application does not independently verify movie facts against an external database.
- The configured model endpoint must be accessible, and any required credentials must be configured securely.

## 🔮 Future Improvements

- Support extracting information for multiple movies from a single paragraph.
- Add downloadable JSON output.
- Integrate a movie database API for fact verification.
- Improve error handling and structured-output reliability.
- Add a movie search and history feature.

## 👩‍💻 Author

**Bhoomi Kesarwani**

GitHub: [BhoomiKesarwani](https://github.com/BhoomiKesarwani)

## 📄 License

This project is available for educational and learning purposes. Add a suitable open-source license if you plan to distribute or publish it.
