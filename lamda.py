# basic add operation
x = lambda a, b, c : a + b + c 
print(x(5, 6, 2))

# string operation
str1 = 'GeeksforGeeks'
# lambda returns a function object
upper = lambda string: string.upper()
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1),upper(str1))


# condition check
format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
print("\nInt formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235),"\n")


# list of lamda function
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# is_even_list = [x for x in range(1, 5)]
print(is_even_list[0](),'\n')
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())


# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
print('\n',Max(1, 2),'\n')



List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda list: (sorted(sub_list) for sub_list in list)
# Get the second largest element
secondLargest = lambda x, func : [y[len(y)-2] for y in func(x)]
res = secondLargest(List, sortList)

print('\n',res)

# lamda with filter
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

def is_even(x):
    return(x%2 ==0)
even_list = list(filter(is_even,li))


odd_list_by_lamba = list(filter(lambda x: (x % 2 != 0), li))

print('\n',even_list)
print(odd_list_by_lamba)
