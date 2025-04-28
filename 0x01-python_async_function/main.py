import asyncio


async def fetch_data(delay, id):
    print("Fetching data... id", id)
    await asyncio.sleep(delay)
    print("Data fetched, id", id)
    return {"data": "some data", "id": id}


async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print(f"Received result: {result1}")

    result2 = await task2
    print(f"Received result: {result2}")
    print("End of coroutine")


asyncio.run(main())