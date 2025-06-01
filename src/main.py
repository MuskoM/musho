from fastapi import FastAPI, Response
from uvicorn import run

from api.connector import rt

app = FastAPI(
    title="MUSHO",
    description="MUSHO is short for Muryōkūsho(無量空処) is a knowledge and information management platform.",
)

app.include_router(rt, prefix="/connector")


@app.get("/status")
def app_status():
    return Response(content="OK", status_code=200)


if __name__ == "__main__":
    run("main:app", reload=True)
