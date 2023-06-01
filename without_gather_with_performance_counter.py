import asyncio #import the asyncio module

#The function is async keyframed to make it as a coroutine
async def TimeCount():
    print("Its 1")
    await asyncio.sleep(1)
    print("Its 2")
    await asyncio.sleep(1) #make the execution wait  for 1 second


async def main():
    await TimeCount()
    await TimeCount()
    await TimeCount() #In a function using asyncio.gather keyword, we will encapsulate all the three functions into 

if __name__ == "__main__":
    import time
    tpc = time.perf_counter()
    asyncio.run(main())
    TimeUp = time.perf_counter() - tpc
    print(f"{__file__} executed in {TimeUp : 0.2f} seconds.")

'''
Output:
Its 1
Its 2
Its 1
Its 2
Its 1
Its 2
C:/.../asyncio_gather_pratice3/without_gather_with_performance_counter.py executed in  6.27 seconds.

'''
