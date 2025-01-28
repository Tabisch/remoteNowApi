from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")
    api.register_handle_on_connected(connected)
    api.register_handle_on_disconnected(disconnected)

    api.connect()

    await asyncio.sleep(5)

    api.disconnect()

    while True:
        await asyncio.sleep(5)


def connected():
    print("connected")

def disconnected():
    print("disconnected")

asyncio.run(main())