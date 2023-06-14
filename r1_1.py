with open('data.txt','r') as f:
    sum = 0

    for i in f.readlines():
        try:
            sum +=  int(i)

        except ValueError:
            pass     
               
print(sum)