COMMAND
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()




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



