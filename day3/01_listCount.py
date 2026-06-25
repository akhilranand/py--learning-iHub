my_list = ['a','b','a','c','d','e','f','a','c','d','w','z']

# Count of each item
items = []
counts = []

for i in my_list:
    if i not in items:
        items.append(i)
        counts.append(my_list.count(i))

print("Count of each item:")
for i in range(len(items)):
    print(items[i], "=", counts[i])

# Unique items (occur only once)
print("\nUnique items:")
for i in range(len(items)):
    if counts[i] == 1:
        print(items[i])

# Second most occurring item
max_count = max(counts)

second_count = 0
for c in counts:
    if c < max_count and c > second_count:
        second_count = c

print("\nSecond most occurring item:")
for i in range(len(items)):
    if counts[i] == second_count:
        print(items[i], "=", counts[i])