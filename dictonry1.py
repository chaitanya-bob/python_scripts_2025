d1={}
print(d1)

d1={"name": "chaitanya", "id":7777, "age": 26 }
print(d1)
print(d1["id"])

d1.update({"domain":["devops", "test", "developer"]})
print(d1)

print(d1["domain"][2])

d1.update({"location":{"workplace": "bangalore", "hometown": "chikkamagaluru"}})
print(d1)
print(d1["location"]["hometown"])


print("key and valuea")
for k, v in d1.items():
    print(k, v)

print("************keys*******************")
for w in d1.keys():
    print(w)

print("******************values")
for w in d1.values():
    print(w)

if "chaitanya" in d1:
    print("found")
else:
    print("not found")

d1.popitem()
print(d1)

d1.pop("id")
print(d1) 

d2=d1
print(d2)

