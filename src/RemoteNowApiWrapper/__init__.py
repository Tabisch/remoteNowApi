from typing import Callable, Union
import paho.mqtt.client as mqtt
import json

class RemoteNowApi:
    uiServiceBase = "/remoteapp/tv/ui_service"
    platformServiceBase = "/remoteapp/tv/platform_service"
    mobileBase = "/remoteapp/mobile"

    def __init__(self, hostname, identifer="remoteNowApiWrapper"):
        self._hostname = hostname
        self.identifer = identifer

        self._on_SourceList: Union[Callable, None] = None
        self._on_capability: Union[Callable, None] = None
        self._on_tvInfo: Union[Callable, None] = None
        self._on_channelListInfo: Union[Callable, None] = None
        self._on_channelList: Union[Callable, None] = None
        self._on_state: Union[Callable, None] = None

        # command Topics
        self._getTVStateTopic = f"{self.uiServiceBase}/{self.identifer}/actions/gettvstate"
        self._sendAuthenticationCodeTopic = f"{self.uiServiceBase}/{self.identifer}/actions/authenticationcode"
        self._changeSourceTopic = f"{self.uiServiceBase}/{self.identifer}/actions/changesource"
        self._changeChannelTopic = f"{self.uiServiceBase}/{self.identifer}/actions/changechannel"
        self._getSourceList = f"{self.uiServiceBase}/{self.identifer}/actions/sourcelist"
        self._getCapabilityTopic = f"{self.uiServiceBase}/{self.identifer}/actions/capability"
        self._getTvInfoTopic = f"{self.platformServiceBase}/{self.identifer}/actions/gettvinfo"
        self._getChannelListInfoTopic = f"{self.platformServiceBase}/{self.identifer}/actions/getchannellistinfo"
        self._getChannelListTopic = f"{self.platformServiceBase}/{self.identifer}/actions/channellist"

        # information Topics
        self._SourceListTopic = f"{self.mobileBase}/{self.identifer}/ui_service/data/sourcelist"
        self._capabilityTopic = f"{self.mobileBase}/{self.identifer}/ui_service/data/capability"
        self._tvInfoTopic = f"{self.mobileBase}/{self.identifer}/platform_service/data/gettvinfo"
        self._channelListInfoTopic = f"{self.mobileBase}/{self.identifer}/platform_service/data/getchannellistinfo"
        self._channelListTopic = f"{self.mobileBase}/{self.identifer}/platform_service/data/channellist"
        self._stateTopic = "/remoteapp/mobile/broadcast/ui_service/state"

        self._mqttc = mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            client_id=self.identifer,
            clean_session=True,
        )

        self._mqttc.username_pw_set(username="hisenseservice", password="multimqttservice")
        self._mqttc.tls_set(
            ca_certs="hisense.cert"
            )
        self._mqttc.tls_insecure_set(True)

        self._mqttc.on_connect = self.on_connect
        self._mqttc.on_message = self.on_message

    def publish(self, mqttTopic, payload):
        print(mqttTopic)

        if payload == "":
            self._mqttc.publish(topic=mqttTopic)
        else:
            print(payload)
            self._mqttc.publish(topic=mqttTopic, payload=payload)

    def connect(self):
        print("connection")
        self._mqttc.connect_async(self._hostname, 36669, 60)
        self._mqttc.loop_start()

    # request authcode
    def getAuthCode(self):
        self.getTvState()

    # request authentication code
    def getTvState(self):
        mqttTopic = self._getTVStateTopic
        payload = '""'

        self.publish(mqttTopic=mqttTopic, payload=payload)

    # send authentication code
    def sendAuthenticationCode(self, authCode="0000"):
        mqttTopic = self._sendAuthenticationCodeTopic
        payload = {"authNum": f"{authCode}"}

        self.publish(mqttTopic=mqttTopic, payload=json.dumps(payload))

    # change source
    def changeSource(self, sourceId=0):
        mqttTopic = self._changeSourceTopic
        payload = {"sourceid": f"{sourceId}"}

        self.publish(mqttTopic=mqttTopic, payload=json.dumps(payload))

    # change channel
    def changeChannel(self, channel_param=""):
        mqttTopic = self._changeChannelTopic
        payload = {"channel_param": f"{channel_param}"}

        self.publish(mqttTopic=mqttTopic, payload=json.dumps(payload))

    # request sourcelist
    def getSourceList(self):
        mqttTopic = self._getSourceList
        payload = ""

        self.publish(mqttTopic=mqttTopic, payload=payload)

    # request capabilities
    def getCapability(self):
        mqttTopic = self._getCapabilityTopic
        payload = ""

        self.publish(mqttTopic=mqttTopic, payload=payload)

    # request tvinfo
    def getTvInfo(self):
        mqttTopic = self._getTvInfoTopic
        payload = ""

        self.publish(mqttTopic=mqttTopic, payload=payload)

    # request request channel list info
    def getChannelListInfo(self):
        mqttTopic = self._getChannelListInfoTopic
        payload = ""

        self.publish(mqttTopic=mqttTopic, payload=payload)

    # request channellist
    def getChannelList(self, list_para, list_name):
        mqttTopic = self._getChannelListTopic
        payload = {
            "list_para": f"{list_para}",
            "list_name": f"{list_name}",
        }

        self.publish(mqttTopic=mqttTopic, payload=json.dumps(payload))

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self, client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        client.subscribe(self._SourceListTopic)
        client.subscribe(self._capabilityTopic)
        client.subscribe(self._tvInfoTopic)
        client.subscribe(self._channelListInfoTopic)
        client.subscribe(self._channelListTopic)
        client.subscribe(self._stateTopic)

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic)
        payload = json.loads(msg.payload)
        
        match msg.topic:
            case self._SourceListTopic:
                return self.handle_on_SourceList(payload)
            case self._capabilityTopic:
                return self.handle_on_capability(payload)
            case self._tvInfoTopic:
                return self.handle_on_tvInfo(payload)
            case self._channelListInfoTopic:
                return self.handle_on_channelListInfo(payload)
            case self._channelListTopic:
                return self.handle_on_channelList(payload)
            case self._stateTopic:
                return self.handle_on_state(payload)

    # SourceList
    def register_handle_on_SourceList(self, func: Callable):
        self._on_SourceList = func

    def handle_on_SourceList(self, payload):
        if self._on_SourceList:
            self._on_SourceList(payload)

    # Capability
    def register_handle_on_capability(self, func: Callable):
        self._on_capability = func

    def handle_on_capability(self, payload):
        if self._on_capability:
            self._on_capability(payload)

    # TvInfo
    def register_handle_on_tvInfo(self, func: Callable):
        self._on_tvInfo = func

    def handle_on_tvInfo(self, payload):
        if self._on_tvInfo:
            self._on_tvInfo(payload)

    # ChannelListInfo
    def register_handle_on_channelListInfo(self, func: Callable):
        self._on_channelListInfo = func

    def handle_on_channelListInfo(self, payload):
        if self._on_channelListInfo:
            self._on_channelListInfo(payload)

    # ChannelList
    def register_handle_on_channelList(self, func: Callable):
        self._on_channelList = func

    def handle_on_channelList(self, payload):
        if self._on_channelList:
            self._on_channelList(payload)

    # State
    def register_handle_on_state(self, func: Callable):
        self._on_state = func

    def handle_on_state(self, payload):
        if self._on_state:
            self._on_state(payload)
