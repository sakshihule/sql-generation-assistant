from fastapi import FastAPI
from pydantic import BaseModel
from validator import validate_sql

from llm import generate_sql
from execute_sql import run_sql
from explain_sql import explain_sql

app = FastAPI(title="SQL Generation Assistant")

# Input model
class QueryRequest(BaseModel):
    question: str

@app.get("/")
def home():
    return {"message": "SQL Generation Assistant is running!"}

@app.get("/health")
def health():
    return {
        "success": True,
        "status": "healthy",
        "service": "SQL Generation Assistant"
    }

@app.post("/query")
def query_database(request: QueryRequest):
    try:
        # Generate SQL
        sql = generate_sql(request.question)
        
        if sql == "INVALID_QUERY":
            return {"success": False, 
                    "message": "Invalid query generated."}

        is_valid, message = validate_sql(sql)

        if not is_valid:
            return {"success": False, "message": message}

        # Execute SQL
        results = run_sql(sql)

        if not results["success"]:
            return {
            "success": False,
            "question": request.question,
            "generated_sql": sql,
            "results": results["error"]
        }
        
        explanation = explain_sql(sql)
        return {
            "success": True,
            "question": request.question,
            "generated_sql": sql,
            "explanation": explanation,
            "results": results["data"]
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Failed to process the request.",
            "error": str(e)
        }
