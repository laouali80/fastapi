from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID
from models import User, Role, Gender

app = FastAPI()

# config the database
db: List[User] = [
     {
    "id": UUID("c58c70c5-cc9b-42db-bf41-5825df9e0189"),
    "first_name": "Fati",
    "last_name": "alice",
    "middle_name": "bob",
    "gender": "female",
    "roles": [
      "student",
      "user"
    ]
  },
  {
    "id": UUID("7d4ae7eb-4210-452e-970a-0bdc0ca93b03"),
    "first_name": "ali2",
    "last_name": "sani",
    "middle_name": "null",
    "gender": "male",
    "roles": [
      "student"
    ]
  } 
]


@app.get("/")
def test():
    return {"reponse": "success."}


@app.get("/apiv1/users")
def fetch_users():
    return db;


@app.get("/apiv1/users/{user_id}")
def fetch_user(user_id: UUID):
    for user in db:
        if user["id"] == user_id:
            return {"user": user} 
    raise HTTPException(
        status_code=404,
        detail="User Not Found"
    )


@app.post("/apiv1/users")
def create_user(addUser: User):
    db.append(addUser)
    return {"reponse": addUser.id}


@app.put("/apiv1/users/{user_id}")
def update_user(user_id: UUID, updUser: User):
    return {"reponse": "success."}


@app.delete("/apiv1/users/{user_id}")
def delete_user(user_id: UUID):
    for user in db:
        print(type(user))
        # if user["id"] == user_id:
        return {"reponse": "Removed."} 
    raise HTTPException(
        status_code=404,
        detail="User Not Found"
    )


# @app.delete("/apiv1/users/{user_id}")
# def delete_user(user_id: UUID):
#     for index, user in enumerate(db):
#         if user["id"] == user_id:
#             del db[index]
#             return {"response": "Removed"}
        
#     raise HTTPException(
#         status_code=404,
#         detail="User Not Found"
#     )