from fastapi import FastAPI
import fastapi.middleware.cors

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  # Add your React app's URL here
    "https://m3_fast_api-1-z8464729.deta.app"
    "https://m3-puce.vercel.app/"
    "http://127.0.0.1:2000"
    "https://api_playground-1-w8942475.deta.app/"
]

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello World")
