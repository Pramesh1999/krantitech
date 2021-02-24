#create method and pass the list
#In this method we are using logic of sorting list in desending order
def desending_order(my_list):
    for i in range(len(my_list)-1):
        minimum = i
        for j in range(len(my_list)-1,i,-1):
            if(my_list[j]>my_list[minimum]):
                minimum = j
        if(minimum != i):
            my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
    return  my_list
#create a empty list
my_list = []
# take input how many  total input
num1 = int(input("enter to input number"))
# use for loop for append the input in list
for i in range(num1):
    a = int(input())
    my_list.append(a)
#create object
ob1 = desending_order(my_list)
#print sort list
print(ob1)


#OUT PUT
"""
enter to input number4
1
2
3
4
[4, 3, 2, 1]
"""
