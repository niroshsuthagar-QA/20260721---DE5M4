from fastapi import FastAPI

app = FastAPI()

# Fake DB
books = [
    {"id":1, "title":"Harry Potter", "available":True},
    {"id":2, "title":"The Hobbit", "available": True}
]

# Home Route
@app.get("/")
def home():
    return {"message":"Nirosh's Library API"}

# Get all books
@app.get("/books")
def get_books():
    # Connect to a DB
    # Run SQL
    # Get outputs
    # Tidy
    # Format and return
    return books

# Get a specific book id (NEEDS INPUT)
