from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)

async def main():

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    #api.register_handle_on_capability(printPayload)

    api.connect()

    while(not api.get_Connected()):
        await asyncio.sleep(5)

    print(api.getVendor())
    print(api.getBoardVersion())
    print(api.getProduceDate())
    print(api.getUniqueDeviceId())
    print(api.getSoftwareVersion())
    print(api.getChipplatform())
    print(api.getDevicemsg())


def printPayload(payload):
    print(payload)

asyncio.run(main())