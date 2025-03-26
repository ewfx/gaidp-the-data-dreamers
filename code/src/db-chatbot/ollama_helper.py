import ollama
import re

def get_ai_response(prompt):
    """Generate SQL query using Ollama and extract only the query part."""
    response = ollama.chat(
        model="llama2",
        messages=[{"role": "user", "content": prompt}]
    )

    full_response = response['message']['content'].strip()

    # print("AI Full Response:", full_response)

    sql_match = re.search(r"SELECT\s+.*?;", full_response, re.DOTALL | re.IGNORECASE)
    if sql_match:
        return sql_match.group(0)  
    else:
        return "ERROR: AI failed to generate a valid SQL query"
