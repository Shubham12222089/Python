#dictionary = a changable, unordered collection of unique key,value pairs
#             fast because they usee hashing, allow us to access a value quickly
# disctionary is mutable which means we can change the values.
capitals = {"India" : "New Delhi",
            "USA" : "Washington dc",
            "China":"Beijing",
            "Russia":"Muscow"}
#print(capitals["Russia"])
#print(capitals.get('Germany'))

# print(capitals.keys())
# print(capitals.values())

capitals.update({"Germany":"Berlin"})

# to remove we can use pop()
for key,value in capitals.items():
    print(key,value)