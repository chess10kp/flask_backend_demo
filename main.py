# type: ignore
from fastapi import Fastapi

app = Fastapi()


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    app.run()
