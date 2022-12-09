from time import time
def extime(x):
    s= time()
    text = x.split()
    a = " "
    for i in text:
        a = a+str(i[0]).upper()
    print(a)

    e=time()
    execution_time = e - s
    print("Execution Time : ", execution_time)
a=input("")
extime(a)
