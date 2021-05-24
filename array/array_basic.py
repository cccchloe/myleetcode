# write to array
list = []
for i in range(10): # 0-9 这里10不计算
    list.append((i,(i+1)**2))
    print(list[i])

# read an array
# method 1
list = ["a","b","c","d"]
print("this is method 1")
for i,v in enumerate(list):
    print(str(i) + "," + str(v))

# method 2
print("this is method 2")
for i in range(len(list)):
    print(list[i])

# method 3
print("this is method 3")
for ele in list:
    print(ele)
