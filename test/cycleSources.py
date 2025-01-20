from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
sources = []

async def main():
    index = 0

    global sources

    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_SourceList(storeSources)
    api.register_handle_on_sourceinsert(printPayload)

    api.connect()

    await asyncio.sleep(5)

    api.getSourceList()

    while True:
        await asyncio.sleep(5)
        api.changeSource(sourceId=sources[index]["sourceid"])
        index = (index + 1) % len(sources)
        

def storeSources(payload):
    global sources
    sources = payload
    print(sources)

def printPayload(payload):
    print(payload)

asyncio.run(main())