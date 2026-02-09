l1=[10, 20, "welcome"]
print(l1)
print(l1[0])
print(l1[0:2])
print(l1[-1])

l1.append("allow")
print(l1)

l1.append(2.00)
print(l1)

l1.append(["hello", 50 , 90])
print(l1)

print(l1[5][1])

l1.pop()
print(l1)

l1.pop(2)
print(l1)

l1.insert(2, "python")
print(l1)

l1.insert(3, 60)
print(l1)

l1.remove(60)
print(l1)


l2=[5,10,35,20,15]
#l2.sort()
#print(l2)

#l2.reverse()
#print(l2)

l3=l2
print(l2)
print(l3)

l3[1]=100
print(l2)
print(l3)
print("**************")
l4=l2[:]
print(l2)
print(l4)
l4[1]=500
print(l2)
print(l4)

l1.extend(l4)
print(l1)

l2.append(l4)
print(l2)

l1.clear()
print(l1)

if 20 in l2:
    print("found")
else:
    print("not found")

print("sequence")
for i in l2:
   # print("sequence")
    print(i)

