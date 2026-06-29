def countDown(num):
    if num == 0:
        print("done")
        return
    else:
        print(num) 
        countDown(num-1)  
countDown(10)

