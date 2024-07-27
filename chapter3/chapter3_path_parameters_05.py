from fastapi import FastAPI, Path
import uvicorn

app = FastAPI()


@app.get("/license-plates/{license}")
async def get_license_plate_xxxx(license: str = Path(..., min_length=9, max_length=9)):
    return {"license": license}

if  __name__=='__main__':
    uvicorn.run(app="chapter3_path_parameters_05:app", host="127.0.0.1", port=8080, reload=True)