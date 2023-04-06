from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_urls

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.post("/urls")
async def post_urls(request: Request):
    body = await request.body()
    text = body.decode()
    text_array = text.splitlines()
    count = len(text_array)
    if count > 0:
        result = await analyze_urls(text_array)
        return result
    else:
        raise HTTPException(400, "Empty string")