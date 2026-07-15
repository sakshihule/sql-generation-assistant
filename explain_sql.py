from llm import client

def explain_sql(sql_query):
    prompt = f"""
Explain the following SQL query in simple English in 1-2 sentences.

SQL:
{sql_query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()