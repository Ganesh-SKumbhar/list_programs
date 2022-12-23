# prog to merge two lists and sort it

# list 1 -
list1 = input('Enter the numbers separated by "," : \nList1 : \t').split(',')

# using traditional for loop
temp = []
for num in list1:
    temp.append(int(num))

# using list comprehension
# temp = [int(num) for num in list1]

# list 2-
list2 = input('Enter the numbers separated by "," : \nList2 : \t').split(',')
temp2 = []
for num in list2:
    temp.append(int(num))

# list comprehension
# temp2 = [int(num) for num in list2]

# merging the two lists one after another
merged_list = temp + temp2
print('Merging two lists : \t', merged_list)

# sorting  the list using sort() method
merged_list.sort()

print('Sorted merged list is : \t', merged_list)

