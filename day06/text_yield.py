def mygen():
    a=10+20
    yield a
    yield "hello world"
    b=a*10
    yield b
print(mygen())
print(mygen().__next__())
for item in mygen():
    print(item)
print(type(mygen()))