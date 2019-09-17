"""
It is an associative array.
It map keys to their associative values and it does these using
a function called hash function.

Benefits:
1. key to value mapping are unique
2. Typically very fast for large datasets
3. don't order entries in predictable way
"""

item1 = dict({"key1": 1, "key2": 2, "key3": "three"})
print(item1)

item2 = {}
item2["key1"] = 1
item2["key2"] = 2
item2["key3"] = 3
print(item2)

# print(item2["key6"])

item2["key2"] = "two"
print(item2)


for key,value in item2.items():
    print("keys: ", key, "Value : ", value)
