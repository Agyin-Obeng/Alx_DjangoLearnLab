b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
Book.objects.all()


EXPECTED RESULT

---

### **📄 delete.md**
```md
# DELETE Operation

```python
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
Book.objects.all()
