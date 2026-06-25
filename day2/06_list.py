l = ['a',123,3.14,1,2,3,1,2,3,"abcd"]
l1=[2,8,6,1]
print("original")
print(l)

l.append("data")
print("append")
print(l)

l.remove(3.14)
print("remove")
print(l)

l.insert(0,"first")
print("insert")
print(l)

l.pop()
print("pop")
print(l)

l.extend([3,2,1])
print("extend")
print(l)


print("index")
print(l.index(1))
print(l)

print("count")
print(l.count(1))


print("sort")
l1.sort()
print(l1)

l1.reverse()
print(l1)

l1.clear()
print(l1)