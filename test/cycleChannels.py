from RemoteNowApiWrapper import RemoteNowApi
import asyncio

# async main program (potentially fastapi)
channels = []

async def main():
    index = 0

    global channels

    global api
    api = RemoteNowApi(hostname="192.168.200.60", identifer="devtest")

    api.register_handle_on_channelList(storeChannels)
    api.register_handle_on_channelListInfo(requestChannelList)

    api.connect()

    await asyncio.sleep(5)

    api.getChannelListInfo()

    while True:
        await asyncio.sleep(5)
        api.changeChannel(channel_param=channels[index]["channel_param"])
        index = (index + 1) % len(channels)
        

def storeChannels(payload):
    global channels
    channels = payload["list"]
    # print(channels)

def requestChannelList(payload):
    print("requestChannelList")
    api.getChannelList(list_name=payload[0]["list_name"], list_para=payload[0]["list_para"])

asyncio.run(main())