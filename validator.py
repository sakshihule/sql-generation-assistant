def validate_sql(sql_query):
    """
    Allow only SELECT queries.
    """

    sql = sql_query.strip().upper()

    if not sql.startswith("SELECT"):
        return False, "Only SELECT queries are allowed."

    return True, "Valid query."