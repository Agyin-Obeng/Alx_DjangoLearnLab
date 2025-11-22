COMMAND
b = Book.objects.get(title="1984")
b.title = "book.title"
b.save()
b.title



EXPECTED RESULT
---

### **📄 update.md**
```md
# UPDATE Operation

```python
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()
b.title

