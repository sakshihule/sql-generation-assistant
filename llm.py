import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(user_question):
    system_prompt = """
You are an expert SQLite SQL generator.

Database Schema:

Table: employees

Columns:
- id (INTEGER)
- name (TEXT)
- department (TEXT)
- salary (INTEGER)
- city (TEXT)

Rules:
1. Generate ONLY valid SQLite SELECT queries.
2. Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, or TRUNCATE.
3. Use ONLY the table 'employees'.
4. Use ONLY these columns:
   id, name, department, salary, city.
5. If the user's request requires a column that does not exist, return:
INVALID_QUERY
6. Return ONLY the SQL query or INVALID_QUERY.
7. Do not explain anything.
8. Do not use markdown.
9. For text comparisons (such as city, department, or name), generate case-insensitive SQL using LOWER().
Example:
SELECT * FROM employees WHERE LOWER(city) = LOWER('Mumbai');
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
    )

    return response.choices[0].message.content.strip()