from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main(f):
    return str(f[::-1])

@app.get("/user/{user_name}")
def main(user_name):
    return {"user_": user_name[::-1],
            "ds": user_name.upper()}
