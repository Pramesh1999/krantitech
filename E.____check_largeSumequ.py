# taking input from user
num1 = int(input("enter total number of input"))
# create empty list
list1 = []
# using for loop for append input in list1
for i in range(num1):
    a = int(input())
    list1.append(a)
#find max number from list
max_ = max(list1)
sum = 0
for i in range(len(list1)):
    if(list1[i]!=max_):
        sum = sum + list1[i]
# checking number equality
if(sum == max_):
    print("True")
else:
    print("False")
    
    
    #OUTPUT
    """
enter total number of input5
1
5
16
3
7
16
True
"""
