# sort based on 2nd element
# input : - [['A',34],['B',23],['C',78],['D',32]]

lst = [['A', 34], ['B', 23], ['C', 78], ['D', 32]]


for i in range(len(lst)):
    for j in range(0, len(lst)-i-1):
        if lst[j][1] > lst[j+1][1]:
            temp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = temp
print(lst)

# using sort, key and lambda method
lst.sort(key=lambda x:x[1])
print(lst)
