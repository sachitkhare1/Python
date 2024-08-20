import asyncio

# async def main() :
   
#     print ("starting ") 

#     await asyncio.sleep(2)

#     print ("BYE")

# asyncio.run(main())
    
#------------------------------------------
async def after (delay , name) :
    await asyncio.sleep(delay)
    print (name)


async def main () :

    task1 = asyncio.create_task (after (1 , "sachit"))

    task2 = asyncio.create_task (after(2 , "khare"))

    await task1
    await task2

    print ("end")
    
asyncio.run(main())