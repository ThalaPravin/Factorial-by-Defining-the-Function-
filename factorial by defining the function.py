def factr(a):
    factr=1
    for i in range(1,a+1):
        factr=factr*i
    print(factr)    


a=int(input("Enter the number for the factorial"))
factr(a)
