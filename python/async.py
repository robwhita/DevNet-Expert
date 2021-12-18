#Importing asyncio module to make asynchronous functions
import asyncio
import time

start_time = time.time() 


def funct1():
    print('Got into function 1')
    await asyncio.sleep(2)
    print('Leaving function 1')

def funct2():
    print('Got into function 2')
    await asyncio.sleep(4)
    print('Leaving function 2')


def funct3():
    print('Got into function 3')
    await asyncio.sleep(6)
    print('Leaving function 3')


def main():
    await asyncio.gather(funct1(), funct2(), funct3())


if __name__ == "__main__":
    asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))