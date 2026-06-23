from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items = []

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Item:
    """Create an item and return it."""
    try:
        items.append(item)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/', response_model=List[Item])
async def read_items() -> List[Item]:
    """Retrieve all items."""
    try:
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: int) -> Item:
    """Retrieve an item by its ID."""
    try:
        if item_id < 0 or item_id >= len(items):
            raise HTTPException(status_code=404, detail="Item not found")
        return items[item_id]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put('/items/{item_id}', response_model=Item)
async def update_item(item_id: int, item: Item) -> Item:
    """Update an existing item by its ID."""
    try:
        if item_id < 0 or item_id >= len(items):
            raise HTTPException(status_code=404, detail="Item not found")
        items[item_id] = item
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete('/items/{item_id}', response_model=Item)
async def delete_item(item_id: int) -> Item:
    """Delete an item by its ID."""
    try:
        if item_id < 0 or item_id >= len(items):
            raise HTTPException(status_code=404, detail="Item not found")
        return items.pop(item_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))