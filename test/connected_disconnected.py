from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    sourceid = 2

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_connected(printConnected1)
    api.register_handle_on_connected(printConnected2)
    api.register_handle_on_disconnected(printDisconnected1)
    api.register_handle_on_disconnected(printDisconnected2)

    api.connect()

    while True:
        await asyncio.sleep(5)


def printConnected1():
    print("connected1")

def printConnected2():
    print("connected2")

def printDisconnected1():
    print("disconnected1")

def printDisconnected2():
    print("disconnected2")

asyncio.run(main())