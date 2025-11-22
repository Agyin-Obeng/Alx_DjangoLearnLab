COMMAND
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year



EXPECTED RESULT

---

### **📄 retrieve.md**
```md
# RETRIEVE Operation

```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
