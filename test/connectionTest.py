from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
async def main():
    sourceid = 2

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_state(printBroadcast)
    api.register_handle_on_capability(printCapability)

    api.connect()

    await asyncio.sleep(5)

    api.getAuthCode()

    print("Enter AuthCode")
    api.sendAuthenticationCode(authCode=input())

    # api.getCapability()

    while True:
        api.changeSource(sourceId=sourceid)
        sourceid = sourceid + 1
        await asyncio.sleep(5)


def printBroadcast(payload):
    print(payload)

def printCapability(payload):
    print(payload)

asyncio.run(main())