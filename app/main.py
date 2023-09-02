from fastapi import FastAPI

from app.models.models import User

app = FastAPI()

first_user = User(name="John Doe", age=29)


@app.get("/users")
async def get_users():
    return {"user": first_user}


@app.post("/user")
async def add_user(user: User):
    return {"name": user.name, "age": user.age, "is_adult": user.age >= 18}
