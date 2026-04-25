from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Clean Code", "author": "Robert C. Martin", "category": "Programming", "year": 2008},
    {"title": "The Pragmatic Programmer", "author": "Andrew Hunt", "category": "Programming", "year": 1999},
    {"title": "1984", "author": "George Orwell", "category": "Fiction", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "category": "Fiction", "year": 1960},
    {"title": "Dune", "author": "Frank Herbert", "category": "Science Fiction", "year": 1965},
    {"title": "Sapiens", "author": "Yuval Noah Harari", "category": "History", "year": 2011},
    {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Help", "year": 2018},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasy", "year": 1937},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category": "Fiction", "year": 1988},
    {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Psychology", "year": 2011},
]


# A path parameter is a value written directly in the URL path, like "/books/3".
# FastAPI reads that value from the URL and gives it to the function so we can find one specific item.

# Below we have a path with no parameter. This is a static path because the URL always looks the same.
@app.get("/books")
async def list_books():
    return BOOKS

# Here we have a path parameter, so the URL changes depending on the title we want to search.
@app.get("/books/{title}")
def get_book_by_title(title: str):
    for book in BOOKS:
        if book.get("title").casefold() == title.casefold():
            return book

    return {"message": f"Book titled '{title}' not found"}
        

# A query parameter is extra information added after a `?` in the URL, like "/books?category=Fiction".
# It does not change the route itself; instead, it helps us filter, sort, or search the data.
@app.get("/books/")
def get_books_by_category(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    if not books_to_return:
        return {"message": f"No books found in category '{category}'"}

    return books_to_return


# Here we combine both ideas.
# `author` is a path parameter because it is part of the URL path, and `category` is a query parameter because it comes after `?`.
# This is useful when we want a more specific search, like all Fiction books by George Orwell.
@app.get("/books/by-author/{author}")
def get_books_by_author_and_category(category: str, author: str):
    books_to_return = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold() and book.get("category").casefold() == category.casefold():
            books_to_return.append(book)

    if not books_to_return:
        return {"message": f"No books by '{author}' found in category '{category}'"}

    return books_to_return
