from fastapi import FastAPI

from app.models.models import User

app = FastAPI()

first_user = User(name="John Doe", id=1)


@app.get("/users")
async def get_users():
    return {"user": first_user}
