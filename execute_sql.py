import sqlite3

def run_sql(query):
    try:
        # Connect to the database
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Fetch results
        rows = cursor.fetchall()

        # Close connection
        conn.close()

        return rows

    except Exception as e:
        return {
            "success": False,
            "message": "Failed to execute SQL query.",
            "error": str(e)
        }