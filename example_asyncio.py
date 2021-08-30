import asyncio

"""
Simple async task
"""
# get event loop
async_loop = asyncio.get_event_loop()

print("\n========Simple example===========\n")
# create coroutine function
async def foo(num):
    print(f"# {num} First phase invoke")
    await asyncio.sleep(2)
    print(f"# {num} Second phase invoke")


# register coroutine functioni into eveny loop and running
async_loop.run_until_complete(foo(1))


"""
Multi task
"""
print("\n========Multi task===========\n")
# create muitl task
tasks = [asyncio.ensure_future(foo(i)) for i in range(5)]

# package all tasks to one task
task_collection = asyncio.wait(tasks)
async_loop.run_until_complete(task_collection)
async_loop.close()


"""
Python 3.7 support
"""
print("\n========Python3.7 support Multi task===========\n")


async def run_multi_tasks():
    task1 = asyncio.create_task(foo(1))
    task2 = asyncio.create_task(foo(2))
    task3 = asyncio.create_task(foo(3))
    await task1
    await task2
    await task3


asyncio.run(run_multi_tasks())
