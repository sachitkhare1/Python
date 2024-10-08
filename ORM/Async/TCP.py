import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        'EP0vfUj_.html', 5346)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))