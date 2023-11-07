#!/usr/bin/python3

from engine.file_storage import FileStorage
import base_model as model

obj1 = model.BaseModel()
obj2 = model.BaseModel({"id": "1245-678-9000", "name": "User 1", "created_at": model.datetime.now()})

store = FileStorage()
store.new(obj1)
print(store.all())
print("=" * 5)
store.new(obj2)
print(store.all())
print("=" * 5)
store.save()
store.reload()
print(store.all())
print("=" * 5)
