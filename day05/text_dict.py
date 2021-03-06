#!/usr/local/bin/python3.6
print(dict([("a","b"),("c","d")]))
print(dict(["ab","cd"]))
print({}.fromkeys(["a","b","c"],1))

adict=dict([("name","sam"),("age",18)])
print("bob" in adict)
print("name" in  adict)
print(len(adict))
for key in adict:
    print("%s:%s" % (key,adict[key]))
print("%(name)s is %(age)s years old" % adict)

bdict=dict(["ab","ac","db","cd","ef"])
print(bdict)
print(bdict.get("a"))
print(bdict.get("g"))
print(bdict.get("g","f"))
print(bdict.keys())
print(bdict.values())
print(bdict.items())
print(bdict.pop("a"))
print(bdict)
bdict.update({"a":"afa"})
print(bdict)