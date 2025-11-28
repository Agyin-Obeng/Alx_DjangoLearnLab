COMMAND
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check the updated title
book.title




EXPECTED RESULT

---

Similarly, make sure your other files use `book` as the variable:

- `create.md` → `book = Book.objects.create(...)`
- `retrieve.md` → `book = Book.objects.get(title="1984")`
- `delete.md` → `book = Book.objects.get(title="Nineteen Eighty-Four")`

---

If you want, I can **rewrite all 4 Markdown files** correctly with `book` so the automated check passes.  

Do you want me to do that?






