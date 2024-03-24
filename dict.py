data1 = ("Hello", 12, 65.4, False, "hi")
#print(data1)
#data1[3] = True
#print(data1)


data2 = ["Hello", 12, 65.4, False, "hi"]
#print(data2)
#print(data2[3])
data2[3] = True
#print(data2)

data3 = (["hello","dear","friend"], False, 16, 23)
#print(data3)
data3[0][1] = "little"
#print(data3)
#print(len(data3))


users = {1:"Anton", 2:"Albert", 3:"Vladislav",4:"Olga"}
print(users)
print(users[4])
users[2] = "Ivan"
print(users)
users["Hello"] = "Sergey"
print(users)
del users[2]
print(users)
for key,value in users.items():
    print(key,value)
users.clear()
print(users)