import pickle
with open("/tmp/a.txt","wb") as fobj:
    pickle.dump({"name":"bob","age":18},fobj)
with open("/tmp/a.txt","rb") as fobj:
    print(pickle.load(fobj))
