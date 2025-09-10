#set {} ,order of element are not maintained that's why indexing and slising are not posible in set 
# set can be mutable in nature 




# # to produse a empty a set in code simply use the set fun set()if use a only{} then it will dictionary
# var=set()
# print(type(var))


#s={12,"the",7,56.8,"i"}             #in the output the order of element is not in sequence of given 
# s.add("rajnandini")                 # add() only add 1 element
# print(s)

# s.update(["shankar","musale"])       # for adding more than 1 element use []brakets 
# print(s)

# s.pop()                            #it remove last element
# print(s)


# s.remove("the")                 # remove element 
# print(s)

# s.clear()                      # it remove all and clear set
# print(s)


s={1,2,3,4,5,6,7}
s2={6,7,8,9,10}
# print(s.union(s2))              #union fun is used to add to set 
# print(s|s2)                        # union show by | or symbol


# print(s.intersection(s2))         # intersection give a comman value in sets
# print(s &s2)                     # it also gives intersection


print(s.difference(s2))
print(s-s2)