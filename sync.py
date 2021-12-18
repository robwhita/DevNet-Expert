import time 

# Adding time function from time module. Allows us to get a timestamp at the beginning of the script. 
start_time = time.time() 


def funct1():
    print('Got into function 1')
    time.sleep(2)
    print('Leaving function 1')

def funct2():
    print('Got into function 2')
    time.sleep(4)
    print('Leaving function 2')

def funct3():
    print('Got into function 3')
    time.sleep(6)
    print('Leaving function 3')


funct1()
funct2()
funct3()

# Takes another timestamp at end of script and subtracts it from previous timestamp
print("--- %s seconds ---" % (time.time() - start_time))





