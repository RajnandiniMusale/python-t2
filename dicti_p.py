 
 # dictionary indexing and slicing are not posible,   mutable (can modify,    dupilcate keys not valide)

info={"name":"Rajnandini","age":20,"mark":100, "qulification":"class_1"}
# print(info)
# print(info["name"])


# info.pop("name")              #deleting the key pair
# print(info)


# print(info.get("qulification"))                       # if the given key pair is not in data then it will return the remaining message on output
# print(info.get("pass"),"not present in information")

#info.clear()

# print(info.keys())         # it just print all keys
# print(info.values())        # it gives all values
# print(info.items())           # it returns the all key_value pairs



# for key,values in info.items():           # in this way we can get output of key value pairs with separeted by - symbol
#     print(key,values,sep=" - ")



info["name"]="Nandini"          # it just update the value of name
print(info)


