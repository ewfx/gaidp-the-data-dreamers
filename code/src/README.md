
How to Run:

##Set Up a Virtual Environment

    python -m venv venv
    venv\Scripts\activate

1️⃣ Install Dependencies:
Make sure you have Python installed, then install the required packages:
for local: You also need Ollama installed: (https://ollama.com/download/windows)
pip install fastapi uvicorn pyodbc ollama

2️⃣ Start the FastAPI Backend
Run the FastAPI server using:

uvicorn main:app --reload OR python -m uvicorn main:app --reload
By default, it will be available at:
🔗 http://127.0.0.1:8000

3️⃣ Start the UI
Open index.html in a browser.

The chatbot will welcome you and allow you to ask SQL-related queries.

🔍 Testing the API
You can manually test the API using:

