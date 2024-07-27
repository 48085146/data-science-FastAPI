from typing import Optional

from fastapi import FastAPI, Cookie
import uvicorn

app = FastAPI()


@app.get("/")
async def get_cookie(hello: Optional[str] = Cookie(None)):
    return {"hello": hello}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_headers_cookies_03:app", host="127.0.0.1", port=8080, reload=True)