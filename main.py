from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def welcome():
    return "Welcome to the Video Game Character Database! Please enter the name of a character to get it's profile. Visit /docs for more info."