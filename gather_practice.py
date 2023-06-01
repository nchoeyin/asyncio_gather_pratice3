import asyncio #import the asyncio module

#The function is async keyframed to make it as a coroutine
async def TimeCount():
    print("Its 1")
    await asyncio.sleep(1)
    print("Its 2")
    await asyncio.sleep(1) #make the execution wait  for 1 second


async def main():
    await asyncio.gather(TimeCount(),TimeCount(),TimeCount())

if __name__ == "__main__":
    import time
    tpc = time.perf_counter()
    asyncio.run(main())
    TimeUp = time.perf_counter() - tpc
    print(f"{__file__} executed in {TimeUp : 0.2f} seconds.")


'''
Its 1
Its 1
Its 1
Its 2
Its 2
Its 2
C:/../gather_practice.py executed in  2.10 seconds.
'''
