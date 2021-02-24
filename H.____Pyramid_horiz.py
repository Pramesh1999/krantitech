# Pyramid of horizontal tables of number
# taking input from user how many line print
num = int(input("enter number of rows"))
#using logic inside for loop
for row in range(num):
    val = row +1
    dec = num-1
    for col in range(row+1):
        print(format(val,"<4"),end=" ")
        val = val + dec
        dec = dec-1
    print()
    
    
  # OUT PUT
  
  """
enter number of rows4
1    
2    5    
3    6    8    
4    7    9    10  

"""
