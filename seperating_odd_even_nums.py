# prog to put even and odd elements into different lists

def sort_list(lst):     # function to sort list
    even_list = []
    odd_list = []

    for i in lst:
        if i % 2 == 0:      # check for even condition
            even_list.append(i)     # appending the number to the even list
        else:
            odd_list.append(i)      # appending the number to the odd list
    return even_list, odd_list


list1 = input('Enter the numbers separated by "," : \n').split(',')

temp = []
for num in list1:
    temp.append(int(num))

# using comprehension
# temp = [int(n) for n in list1]

even, odd = sort_list(temp)
print(f'Even List : {even}\nOdd List : {odd}')
