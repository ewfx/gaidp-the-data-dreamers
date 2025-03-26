from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from database import execute_query
from ollama_helper import get_ai_response

app = FastAPI()

#Serve Chatbot UI
@app.get("/", response_class=HTMLResponse)
def serve_chat_ui():
    with open("templates/chat.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

#Keep Existing API for Queries
@app.get("/query/")
def run_query(natural_query: str):
    """Converts natural language to SQL and executes it."""
    
    ai_prompt = (
        "Generate a **correct** Microsoft SQL Server 2016+ SQL query:\n"
        "Use correct table and column names.\n"
        "Ensure queries follow SQL Server syntax.\n"
        "If listing tables, use 'SELECT * FROM INFORMATION_SCHEMA.TABLES'.\n"
        "f counting records, use 'SELECT COUNT(*) FROM dbo.<table>'.\n"
        f"User request: '{natural_query}'"
    )

    sql_query = get_ai_response(ai_prompt)
    if not sql_query or "ERROR" in sql_query.upper():
        return {"error": "AI failed to generate a valid SQL query"}

    db_response = execute_query(sql_query.strip())
    result = db_response.get('data')

    return {"data": result}





# # from fastapi import FastAPI
# # from database import execute_query
# # from ollama_helper import get_ai_response

# # app = FastAPI()

# # @app.get("/")
# # def home():
# #     return {"message": "SQL Server Database Chatbot API is running"}

# # @app.get("/query/")
# # def run_query(natural_query: str):
# #     """Converts natural language to SQL and executes it."""

# #     # 🔹 AI Prompt for Generating SQL Queries
# #     ai_prompt = (
# #         "Generate a valid Microsoft SQL Server 2016+ SQL query for this request:\n"
# #         "Use correct table and column names.\n"
# #         "Always start the query with 'SELECT'.\n"
# #         "Use 'sys.tables', 'sys.columns', and 'INFORMATION_SCHEMA' where applicable.\n"
# #         "Do NOT use 'table_schema' (this is for PostgreSQL, not SQL Server).\n"
# #         "Ensure SQL syntax is correct and follows best practices.\n"
# #         f"User request: '{natural_query}'"
# #     )

# #     # 🔹 Get AI-generated SQL query
# #     sql_query = get_ai_response(ai_prompt)

# #     # ✅ Check if AI generated a valid SQL query
# #     if not sql_query:
# #         return {"error": "AI failed to generate a valid SQL query"}

# #     # 🔹 Execute the SQL query in the database
# #     db_response = execute_query(sql_query.strip())

# #     return {"sql_query": sql_query, "db_response": db_response}

# from fastapi import FastAPI
# from database import execute_query
# from ollama_helper import get_ai_response

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "SQL Server Database Chatbot API is running"}

# @app.get("/query/")
# def run_query(natural_query: str):
#     """Converts natural language to SQL and executes it."""

#     # 🔹 Improved AI Prompt for Generating SQL Queries
#     # ai_prompt = (
#     #     "Generate a valid Microsoft SQL Server 2016+ SQL query for this request:\n"
#     #     "Use correct table and column names.\n"
#     #     "Always start the query with 'SELECT'.\n"
#     #     "If counting records, use 'SELECT COUNT(*) FROM <table>'.\n"
#     #     "If listing tables, use 'SELECT name FROM sys.tables WHERE is_ms_shipped = 0'.\n"
#     #     "Avoid 'sys.tables' for row counts.\n"
#     #     "Avoid 'EXPLAIN SELECT' (not valid in SQL Server).\n"
#     #     "Do NOT use deprecated system tables (e.g., sysobjects, syscolumns).\n"
#     #     f"User request: '{natural_query}'"
#     # )
#     ai_prompt = (
#     "Generate a **correct** Microsoft SQL Server 2016+ SQL query:\n"
#     "✅ Use correct table and column names.\n"
#     "✅ Ensure queries follow SQL Server syntax.\n"
#     "✅ If listing tables, use 'SELECT * FROM INFORMATION_SCHEMA.TABLES'.\n"
#     "✅ If counting records, use 'SELECT COUNT(*) FROM dbo.<table>'.\n"
#     f"User request: '{natural_query}'"
# )

#     # 🔹 Get AI-generated SQL query
#     sql_query = get_ai_response(ai_prompt)

#     # ✅ Validate AI output
#     if not sql_query or "ERROR" in sql_query.upper():
#         return {"error": "AI failed to generate a valid SQL query"}

#     # 🔹 Execute the SQL query in the database
#     db_response = execute_query(sql_query.strip())

#     return {"sql_query": sql_query, "db_response": db_response}
