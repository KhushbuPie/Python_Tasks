import asyncio
import aiofiles

async def write_to_file(filename, data):
    async with aiofiles.open(filename, 'w') as f:
        await f.write(data)

async def read_from_file(filename):
    async with aiofiles.open(filename, 'r') as f:
        data = await f.read()
        return data

async def main():
    filename = 'example.txt'
    data = 'Hello, world!'

    # First, write to the file
    await write_to_file(filename, data)

    # Then, read from the file
    read_task = asyncio.create_task(read_from_file(filename))
    await read_task
    
    print(read_task.result())

if __name__ == '__main__':
    asyncio.run(main())
