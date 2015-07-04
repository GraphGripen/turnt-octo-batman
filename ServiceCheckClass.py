import ServiceCheckConfig

class ServiceInfo:

    def __init__(self):
        self.creationTime = ""
        self.version = ServiceCheckConfig.version
        self.severity = ""
        self.sourceComponentId = {'location' : ServiceCheckConfig.sourceComponentId['location'] , 'locationType' : ServiceCheckConfig.sourceComponentId['locationType'] , 'component' : ServiceCheckConfig.sourceComponentId['component'] , 'subComponent' : ServiceCheckConfig.sourceComponentId['subComponent'] , 'componentIdType' : ServiceCheckConfig.sourceComponentId['componentIdType'] , "componentType" : ServiceCheckConfig.sourceComponentId['componentType'] , 'application' : ServiceCheckConfig.sourceComponentId['application'] , 'instanceId' : ServiceCheckConfig.sourceComponentId['instanceId'] , 'processId' : ServiceCheckConfig.sourceComponentId['processId'] , 'threadId' : ServiceCheckConfig.sourceComponentId['threadId'] }
        self.msg = ""
        self.globalInstanceId = ServiceCheckConfig.globalInstanceId
        self.situation = {'categoryName' : ServiceCheckConfig.situation['categoryName'] , 'situationType' : {'reasoningScope' : ServiceCheckConfig.situation['situationType']['reasoningScope'] , 'reportCategory' : ServiceCheckConfig.situation['situationType']['reportCategory']}}
        self.msgDataElement = {'msgId' : ServiceCheckConfig.msgDataElement['msgId'] , 'msgIdType' : ServiceCheckConfig.msgDataElement['msgIdType']}
        self.repeatCount = ServiceCheckConfig.repeatCount
        self.elapsedTime = ServiceCheckConfig.elapsedTime
        self.sequenceNumber = ServiceCheckConfig.sequenceNumber