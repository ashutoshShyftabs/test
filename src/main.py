from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="PF2 Backend", version="CONFIG.BUILD_TAG")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "OK", "version": "CONFIG.BUILD_TAG"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        workers=3,
        reload_dirs="./src",
        # app_dir="./src",
    )
