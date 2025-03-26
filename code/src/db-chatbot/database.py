import re
import pyodbc

# Database Connection
def get_db_connection():
    """Establishes a connection to the SQL Server database."""
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=Server;"  # Change to your SQL Server name
        "DATABASE=Hackathon2025;"  # Change to your database name
        "UID=Username;"  # Use correct credentials
        "PWD=Password;"  
    )
    return pyodbc.connect(conn_str)

def correct_legacy_sql(query):
    """Replaces deprecated SQL Server system tables with modern equivalents."""
    replacements = {
        "syscolumns": "sys.columns",
        "sysindexes": "sys.indexes",
        "sysobjects": "sys.objects"
    }
    for old, new in replacements.items():
        query = re.sub(rf'\b{old}\b', new, query, flags=re.IGNORECASE)
    return query
def execute_query(query):
    """Executes SQL and returns results as JSON."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        return {"query": query, "data": [dict(zip(columns, row)) for row in rows]}

    except Exception as e:
        return {"error": str(e)}

    finally:
        conn.close()
