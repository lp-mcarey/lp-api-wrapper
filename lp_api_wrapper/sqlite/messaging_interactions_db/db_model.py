from peewee import *

database_proxy = Proxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


class AgentParticipant(BaseModel):
    conversationId = TextField()
    agentDeleted = BooleanField(null=True)
    agentFullName = TextField(null=True)
    agentGroupId = IntegerField(null=True)
    agentGroupName = TextField(null=True)
    agentId = TextField(null=True)
    agentLoginName = TextField(null=True)
    agentNickname = TextField(null=True)
    agentPid = TextField(null=True)
    permission = TextField(null=True)
    role = TextField(null=True)
    time = TextField(null=True)
    timeL = TextField(null=True)
    userType = TextField(null=True)
    userTypeName = TextField(null=True)


agent_participant_fields = [
    AgentParticipant.conversationId, AgentParticipant.agentDeleted, AgentParticipant.agentFullName,
    AgentParticipant.agentGroupId, AgentParticipant.agentGroupName, AgentParticipant.agentId,
    AgentParticipant.agentLoginName, AgentParticipant.agentNickname, AgentParticipant.agentPid,
    AgentParticipant.permission, AgentParticipant.role, AgentParticipant.time, AgentParticipant.timeL,
    AgentParticipant.userType, AgentParticipant.userTypeName
]


class Campaign(BaseModel):
    conversationId = TextField()
    behaviorSystemDefault = TextField(null=True)
    campaignEngagementId = IntegerField(null=True)
    campaignEngagementName = TextField(null=True)
    campaignId = IntegerField(null=True)
    campaignName = TextField(null=True)
    engagementAgentNote = TextField(null=True)
    engagementApplicationId = TextField(null=True)
    engagementApplicationName = TextField(null=True)
    engagementApplicationTypeId = TextField(null=True)
    engagementApplicationTypeName = TextField(null=True)
    engagementSource = TextField(null=True)
    goalId = IntegerField(null=True)
    goalName = TextField(null=True)
    lobId = IntegerField(null=True)
    lobName = TextField(null=True)
    locationId = IntegerField(null=True)
    locationName = TextField(null=True)
    profileSystemDefault = TextField(null=True)
    visitorBehaviorId = TextField(null=True)
    visitorBehaviorName = TextField(null=True)
    visitorProfileId = IntegerField(null=True)
    visitorProfileName = TextField(null=True)


campaign_fields = [
    Campaign.conversationId, Campaign.behaviorSystemDefault, Campaign.campaignEngagementId,
    Campaign.campaignEngagementName, Campaign.campaignId, Campaign.campaignName, Campaign.engagementAgentNote,
    Campaign.engagementApplicationId, Campaign.engagementApplicationName, Campaign.engagementApplicationTypeId,
    Campaign.engagementApplicationTypeName, Campaign.engagementSource, Campaign.goalId, Campaign.goalName,
    Campaign.lobId, Campaign.lobName, Campaign.locationId, Campaign.locationName, Campaign.profileSystemDefault,
    Campaign.visitorBehaviorId, Campaign.visitorBehaviorName, Campaign.visitorProfileId, Campaign.visitorProfileName
]


class CoBrowseSession(BaseModel):
    conversationId = TextField()
    agentId = TextField(null=True)
    capability = TextField(null=True)
    duration = IntegerField(null=True)
    endReason = TextField(null=True)
    endTime = TextField(null=True)
    endTimeL = IntegerField(null=True)
    interactiveTime = TextField(null=True)
    interactiveTimeL = IntegerField(null=True)
    isInteractive = BooleanField(null=True)
    sessionId = TextField(null=True)
    startTime = TextField(null=True)
    startTimeL = IntegerField(null=True)
    type = TextField(null=True)


cobrowse_session_fields = [
    CoBrowseSession.conversationId, CoBrowseSession.agentId, CoBrowseSession.capability, CoBrowseSession.duration,
    CoBrowseSession.endReason, CoBrowseSession.endTime, CoBrowseSession.endTimeL, CoBrowseSession.interactiveTime,
    CoBrowseSession.interactiveTimeL, CoBrowseSession.isInteractive, CoBrowseSession.sessionId,
    CoBrowseSession.startTime, CoBrowseSession.startTimeL, CoBrowseSession.type
]


class ConsumerParticipant(BaseModel):
    conversationId = TextField()
    avatarURL = TextField(null=True)
    consumerName = TextField(null=True)
    email = TextField(null=True)
    firstName = TextField(null=True)
    lastName = TextField(null=True)
    participantId = TextField(null=True)
    phone = TextField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)
    token = TextField(null=True)


consumer_participant_fields = [
    ConsumerParticipant.conversationId, ConsumerParticipant.avatarURL, ConsumerParticipant.consumerName,
    ConsumerParticipant.email, ConsumerParticipant.firstName, ConsumerParticipant.lastName,
    ConsumerParticipant.participantId, ConsumerParticipant.phone, ConsumerParticipant.time, ConsumerParticipant.timeL,
    ConsumerParticipant.token
]


class ConversationSurvey(BaseModel):
    conversationId = TextField()
    surveyAnswer = TextField(null=True)
    surveyQuestion = TextField(null=True)
    surveyStatus = TextField(null=True)
    surveyType = TextField(null=True)


conversation_survey_fields = [
    ConversationSurvey.conversationId, ConversationSurvey.surveyAnswer, ConversationSurvey.surveyQuestion,
    ConversationSurvey.surveyStatus, ConversationSurvey.surveyType
]


class CustomerInfo(BaseModel):
    conversationId = TextField()
    accountName = TextField(null=True)
    balance = TextField(null=True)
    companyBranch = TextField(null=True)
    companySize = TextField(null=True)
    customerId = TextField(null=True)
    customerStatus = TextField(null=True)
    customerType = TextField(null=True)
    imei = TextField(null=True)
    lastPaymentDay = IntegerField(null=True)
    lastPaymentMonth = IntegerField(null=True)
    lastPaymentYear = IntegerField(null=True)
    loginStatus = TextField(null=True)
    registrationDay = IntegerField(null=True)
    registrationMonth = IntegerField(null=True)
    registrationYear = IntegerField(null=True)
    role = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = TextField(null=True)
    socialId = TextField(null=True)
    storeNumber = TextField(null=True)
    storeZipCode = TextField(null=True)
    userName = TextField(null=True)


customer_info_fields = [
    CustomerInfo.conversationId, CustomerInfo.accountName, CustomerInfo.balance, CustomerInfo.companyBranch,
    CustomerInfo.companySize, CustomerInfo.customerId, CustomerInfo.customerStatus, CustomerInfo.customerType,
    CustomerInfo.imei, CustomerInfo.lastPaymentDay, CustomerInfo.lastPaymentMonth, CustomerInfo.lastPaymentYear,
    CustomerInfo.loginStatus, CustomerInfo.registrationDay, CustomerInfo.registrationMonth,
    CustomerInfo.registrationYear, CustomerInfo.role, CustomerInfo.sdeType, CustomerInfo.serverTimeStamp,
    CustomerInfo.socialId, CustomerInfo.storeNumber, CustomerInfo.storeZipCode, CustomerInfo.userName
]


class Info(BaseModel):
    conversationId = TextField()
    agentDeleted = TextField(null=True)
    alertedMCS = IntegerField(null=True)
    brandId = TextField(null=True)
    browser = TextField(null=True)
    closeReason = TextField(null=True)
    closeReasonDescription = TextField(null=True)
    csat = IntegerField(null=True)
    csatRate = DoubleField(null=True)
    device = TextField(null=True)
    duration = IntegerField(null=True)
    endTime = TextField(null=True)
    endTimeL = IntegerField(null=True)
    firstConversation = TextField(null=True)
    isPartial = TextField(null=True)
    latestAgentFullName = TextField(null=True)
    latestAgentGroupId = IntegerField(null=True)
    latestAgentGroupName = TextField(null=True)
    latestAgentId = IntegerField(null=True)
    latestAgentLoginName = TextField(null=True)
    latestAgentNickname = TextField(null=True)
    latestQueueState = TextField(null=True)
    latestSkillId = IntegerField(null=True)
    latestSkillName = TextField(null=True)
    mcs = IntegerField(null=True)
    operatingSystem = TextField(null=True)
    source = TextField(null=True)
    startTime = TextField(null=True)
    startTimeL = IntegerField(null=True)
    status = TextField(null=True)


info_fields = [
    Info.conversationId, Info.agentDeleted, Info.alertedMCS, Info.brandId, Info.browser, Info.closeReason,
    Info.closeReasonDescription, Info.csat, Info.csatRate, Info.device, Info.duration, Info.endTime, Info.endTimeL,
    Info.firstConversation, Info.isPartial, Info.latestAgentFullName, Info.latestAgentGroupId,
    Info.latestAgentGroupName, Info.latestAgentId, Info.latestAgentLoginName, Info.latestAgentNickname,
    Info.latestQueueState, Info.latestSkillId, Info.latestSkillName, Info.mcs, Info.operatingSystem,
    Info.source, Info.startTime, Info.startTimeL, Info.status
]


class Interaction(BaseModel):
    conversationId = TextField()
    assignedAgentId = TextField(null=True)
    assignedAgentLoginName = TextField(null=True)
    assignedAgentNickname = TextField(null=True)
    assignedAgentFullName = TextField(null=True)
    interactionTime = TextField(null=True)
    interactionTimeL = IntegerField(null=True)
    interactiveSequence = IntegerField(null=True)


interaction_fields = [
    Interaction.conversationId, Interaction.assignedAgentId, Interaction.assignedAgentLoginName,
    Interaction.assignedAgentNickname, Interaction.assignedAgentFullName, Interaction.interactionTime,
    Interaction.interactionTimeL, Interaction.interactiveSequence
]


class MessageRecord(BaseModel):
    conversationId = TextField()
    device = TextField(null=True)
    dialogId = TextField(null=True)
    messageId = TextField(null=True)
    participantId = TextField(null=True)
    sentBy = TextField(null=True)
    seq = IntegerField(null=True)
    source = TextField(null=True)
    text = TextField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)
    type = TextField(null=True)


message_record_fields = [
    MessageRecord.conversationId, MessageRecord.device, MessageRecord.dialogId, MessageRecord.messageId,
    MessageRecord.participantId, MessageRecord.sentBy, MessageRecord.seq, MessageRecord.source, MessageRecord.text,
    MessageRecord.time, MessageRecord.timeL, MessageRecord.type
]


class MessageScore(BaseModel):
    conversationId = TextField()
    mcs = IntegerField(null=True)
    messageId = TextField(null=True)
    messageRawScore = IntegerField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)


message_score_fields = [
    MessageScore.conversationId, MessageScore.mcs, MessageScore.messageId, MessageScore.messageRawScore,
    MessageScore.time, MessageScore.timeL
]


class MessageStatus(BaseModel):
    conversationId = TextField()
    messageDeliveryStatus = TextField(null=True)
    messageId = TextField(null=True)
    participantId = TextField(null=True)
    participantType = TextField(null=True)
    seq = IntegerField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)


message_status_fields = [
    MessageStatus.conversationId, MessageStatus.messageDeliveryStatus, MessageStatus.messageId,
    MessageStatus.participantId, MessageStatus.participantType, MessageStatus.seq, MessageStatus.time,
    MessageStatus.timeL
]


class PersonalInfo(BaseModel):
    conversationId = TextField()
    company = TextField(null=True)
    customerAge = TextField(null=True)
    email = TextField(null=True)
    gender = TextField(null=True)
    language = TextField(null=True)
    name = TextField(null=True)
    phone = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = TextField(null=True)
    surname = TextField(null=True)


personal_info_fields = [
    PersonalInfo.conversationId, PersonalInfo.company, PersonalInfo.customerAge, PersonalInfo.email,
    PersonalInfo.gender, PersonalInfo.language, PersonalInfo.name, PersonalInfo.phone, PersonalInfo.sdeType,
    PersonalInfo.serverTimeStamp, PersonalInfo.surname
]


class Summary(BaseModel):
    conversationId = TextField()
    lastUpdatedTime = IntegerField(null=True)
    text = TextField(null=True)


summary_fields = [Summary.conversationId, Summary.lastUpdatedTime, Summary.text]


class Transfer(BaseModel):
    conversationId = TextField()
    assignedAgentFullName = TextField(null=True)
    assignedAgentId = TextField(null=True)
    assignedAgentLoginName = TextField(null=True)
    assignedAgentNickname = TextField(null=True)
    by = TextField(null=True)
    reason = TextField(null=True)
    sourceAgentFullName = TextField(null=True)
    sourceAgentId = TextField(null=True)
    sourceAgentLoginName = TextField(null=True)
    sourceAgentNickname = TextField(null=True)
    sourceSkillId = IntegerField(null=True)
    sourceSkillName = TextField(null=True)
    targetSkillId = IntegerField(null=True)
    targetSkillName = TextField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)


transfer_fields = [
    Transfer.conversationId,
    Transfer.assignedAgentFullName,
    Transfer.assignedAgentId,
    Transfer.assignedAgentLoginName,
    Transfer.assignedAgentNickname,
    Transfer.by,
    Transfer.reason,
    Transfer.sourceAgentFullName,
    Transfer.sourceAgentId,
    Transfer.sourceAgentLoginName,
    Transfer.sourceAgentNickname,
    Transfer.sourceSkillId,
    Transfer.sourceSkillName,
    Transfer.targetSkillId,
    Transfer.targetSkillName,
    Transfer.time,
    Transfer.timeL
]


def initialize_database(db_name=None):
    if db_name:
        database = SqliteDatabase(db_name)
    else:
        database = SqliteDatabase(':memory:')

    database_proxy.initialize(database)
    database_proxy.connect()
    database_proxy.create_tables(
        [AgentParticipant, Campaign, CoBrowseSession, ConsumerParticipant, ConversationSurvey, CustomerInfo, Info,
         Interaction, MessageRecord, MessageScore, MessageStatus, PersonalInfo, Summary, Transfer]
    )
