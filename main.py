from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

#db
db_config = {
    "host": "mysql-service",
    "user": "root",
    "password": "password",
    "database": "pro-db"
}

class Item(BaseModel):
    name: str
    description: str = None

#health check
@app.get("/health")
def health_check():
    return {"status": "healthy"}

#생성
@app.post("/items/")
def create_item(item: Item):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (item.name, item.description))
        conn.commit()
        return {"message": "create", "item": item}
    finally:
        cursor.close()
        conn.close()

#조회
@app.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description FROM items WHERE id = %s", (item_id,))
        item = cursor.fetchone()
        if item is None:
            raise HTTPException(status_code=404, detail="Item not found")
        return {"search": item}
    finally:
        cursor.close()
        conn.close()

#수정
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET name = %s, description = %s WHERE id = %s", (item.name, item.description, item_id))
        conn.commit()
        return {"message": "update", "item": item}
    finally:
        cursor.close()
        conn.close()

#삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
        conn.commit()
        return {"message": "delete"}
    finally:
        cursor.close()
        conn.close()

