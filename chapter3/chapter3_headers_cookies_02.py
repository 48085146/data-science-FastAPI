from fastapi import FastAPI, Header
import uvicorn

app = FastAPI()


@app.get("/")
async def get_header(user_agent: str = Header(...)):
    return {"user_agent": user_agent}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_headers_cookies_02:app", host="127.0.0.1", port=8080, reload=True)