from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()

# Define a Pydantic model for request validation
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
