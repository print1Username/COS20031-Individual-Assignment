# NAIM Holdings Estate Management and AI System

[简体中文](README.zh-CN.md)

This project is a small Flask web application developed for the COS20031 Individual Assessment. It provides a simple estate management interface for NAIM Holdings and connects to the Google Gemini API for AI-based questions.

## Main features

- Open the NAIM Holdings official website from the home page.
- Add an estate with an ID, name, description, and price.
- Display all stored estates.
- Search for an estate by its ID.
- Send questions to Gemini and display the generated answer.
- Store estate records in a local SQLite database.

The current implementation is an educational prototype. Although the assessment discusses Retrieval-Augmented Generation (RAG), this code currently sends the user's question directly to Gemini. It does not yet retrieve information from a document knowledge base or use a vector database.

## Technology stack

- Python
- Flask
- SQLite
- Google Gemini API
- HTML and CSS
- Jinja templates

## Requirements

- Python installed and available in the terminal
- A Google Gemini API key
- Internet access for Gemini questions

The dependencies used by the source code are:

```text
Flask
python-dotenv
google-generativeai
```

## Installation and deployment

### 1. Open the project

Open a terminal in the project root, the folder containing `app.py`.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```bat
python -m venv venv
venv\Scripts\activate
```

macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install Flask python-dotenv google-generativeai
```

The current `requirements.txt` file is empty, so the packages above must be installed manually unless the dependency file is updated later.

### 4. Configure the Gemini API key

Copy `.env.examples` to a new file named `.env`:

Windows PowerShell:

```powershell
Copy-Item .env.examples .env
```

macOS or Linux:

```bash
cp .env.examples .env
```

Edit `.env` and replace the placeholder:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Do not commit `.env` or share the API key. The `.gitignore` file ignores `.env`.

### 5. Start the application

Run this command from the project root:

```bash
python app.py
```

Open <http://127.0.0.1:5000> in a browser.

## How to use the system

### Home page

The home page provides links to the NAIM Holdings official website, estate creation, estate search, and Gemini AI questions.

### Add an estate

1. Open **Add New Real Estate**.
2. Enter the estate ID, name, description, and price.
3. Click **Create**.

The estate ID must be unique because it is the database primary key.

### Search estates

1. Open **Real Estate Search**.
2. Enter an estate ID.
3. Click **Search**.

When the page is opened without a search submission, the current implementation displays all estate records.

### Ask Gemini AI

1. Open **Ask for Gemini AI**.
2. Enter a question.
3. Submit the form.

An internet connection and a valid API key are required.

## Project structure

```text
COS20031-Individual-Assignment/
├── app.py                         # Flask application and routes
├── database/
│   └── estate.db                  # SQLite database file
├── src/
│   ├── estate.py                  # Database operations
│   └── gemini.py                  # Gemini API integration
├── static/
│   ├── styles.css                 # Website styling
│   └── icon.ico                   # Website icon
├── template/
│   ├── index.html                 # Home page
│   ├── add_estate.html             # Add estate page
│   ├── search.html                 # Search results page
│   └── ask.html                    # Gemini question page
├── .env.examples                  # Environment variable example
├── .gitignore                     # Ignored files and secrets
├── requirements.txt               # Dependency file; currently empty
├── README.md                      # English documentation
└── README.zh-CN.md                # Simplified Chinese documentation
```

## Important development notes

- Running `app.py` directly calls `create_estate()`, which drops and recreates `Estate_Table` and inserts three sample records. Existing estate data can therefore be erased when the application is restarted this way.
- Flask debug mode is enabled in the current code. This is suitable for local development only, not production deployment.
- The database uses a relative path, so the application should be started from the project root.
- The current prototype does not include user authentication, CSRF protection, or complete production-grade input validation.
- Gemini failures and invalid database input are not fully handled by the current code.

## Assessment context

The assessment document discusses how RAG could support property information retrieval, customer service, decision support, and project management. The current implementation demonstrates the web interface, SQLite estate management, and Gemini interaction that form the basis for further development.
