def user_schema(user) -> dict:
    return {"id":str(user["_id"]),
            "username":user["username"],
            "full_name":user["full_name"],
            "email":user["email"],
            "disabled":user["disabled"]}

#De objeto a JSON (JSON y diccionario de python es lo mismo)