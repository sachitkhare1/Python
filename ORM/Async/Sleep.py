import asyncio
import datetime

async def currentTime ():
    
    loop = asyncio.get_running_loop()
    endTime = loop +5.0
    
    while True :
        print (datetime.datetime.now())

        if (loop.time() +1.0 >= endTime) :
            
            break
        await asyncio.sleep(1)

asyncio.run (currentTime)

    