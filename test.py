import json
with open("database.json", "r") as f:
    data = json.load(f)
# Search for a user in the database


def search_user(email):
    for user in data["username"]:
        if user["email"] == email:
            return user
    return None


search_user("admin")
