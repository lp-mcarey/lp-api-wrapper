from peewee import *

database_proxy = Proxy()


class BaseModel(Model):

    class Meta:
        database = database_proxy


class Campaign(BaseModel):
    engagementId = TextField()
    behaviorSystemDefault = TextField(null=True)
    campaignEngagementId = IntegerField(null=True)
    campaignEngagementName = TextField(null=True)
    campaignId = IntegerField(null=True)
    campaignName = TextField(null=True)
    goalId = IntegerField(null=True)
    goalName = TextField(null=True)
    lobId = IntegerField(null=True)
    lobName = TextField(null=True)
    profileSystemDefault = TextField(null=True)
    visitorBehaviorId = IntegerField(null=True)
    visitorBehaviorName = TextField(null=True)
    visitorProfileId = IntegerField(null=True)
    visitorProfileName = TextField(null=True)


campaign_fields = [
    Campaign.engagementId, Campaign.behaviorSystemDefault, Campaign.campaignEngagementId,
    Campaign.campaignEngagementName, Campaign.campaignId, Campaign.campaignName, Campaign.goalId, Campaign.goalName,
    Campaign.lobId, Campaign.lobName, Campaign.profileSystemDefault, Campaign.visitorBehaviorId,
    Campaign.visitorBehaviorName, Campaign.visitorProfileId, Campaign.visitorProfileName
]


class CartStatus(BaseModel):
    engagementId = TextField()
    currency = TextField(null=True)
    isAuthenticated = TextField(null=True)
    numItems = IntegerField(null=True)
    productCategory = TextField(null=True)
    productName = TextField(null=True)
    productPrice = DoubleField(null=True)
    productQuantity = IntegerField(null=True)
    productSKU = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = TextField(null=True)
    total = DoubleField(null=True)


cart_status_fields = [
    CartStatus.engagementId, CartStatus.currency, CartStatus.isAuthenticated, CartStatus.numItems,
    CartStatus.productCategory, CartStatus.productName, CartStatus.productPrice, CartStatus.productQuantity,
    CartStatus.productSKU, CartStatus.sdeType, CartStatus.serverTimeStamp, CartStatus.total
]


class CoBrowseSession(BaseModel):
    engagementId = TextField()
    duration = IntegerField(null=True)
    endReason = TextField(null=True)
    endTime = TextField(null=True)
    endTimeL = IntegerField(null=True)
    interactive = TextField(null=True)
    sessionId = IntegerField(null=True)
    startTime = TextField(null=True)
    startTimeL = IntegerField(null=True)


cobrowse_session_fields = [
    CoBrowseSession.engagementId, CoBrowseSession.duration, CoBrowseSession.endReason, CoBrowseSession.endTime,
    CoBrowseSession.endTimeL, CoBrowseSession.interactive, CoBrowseSession.sessionId, CoBrowseSession.startTime,
    CoBrowseSession.startTimeL
]


class CustomerInfo(BaseModel):
    engagementId = TextField()
    accountName = TextField(null=True)
    balance = DoubleField(null=True)
    companySize = IntegerField(null=True)
    currency = TextField(null=True)
    customerId = TextField(null=True)
    customerStatus = TextField(null=True)
    customerType = TextField(null=True)
    imei = TextField(null=True)
    isAuthenticated = TextField(null=True)
    lastPaymentDay = TextField(null=True)
    lastPaymentMonth = TextField(null=True)
    lastPaymentYear = TextField(null=True)
    registrationDay = TextField(null=True)
    registrationMonth = TextField(null=True)
    registrationYear = TextField(null=True)
    role = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    socialId = TextField(null=True)
    storeNumber = TextField(null=True)
    storeZipCode = TextField(null=True)
    userName = TextField(null=True)


customer_info_fields = [
    CustomerInfo.engagementId, CustomerInfo.accountName, CustomerInfo.balance, CustomerInfo.companySize,
    CustomerInfo.currency, CustomerInfo.customerId, CustomerInfo.customerStatus, CustomerInfo.customerType,
    CustomerInfo.imei, CustomerInfo.isAuthenticated, CustomerInfo.lastPaymentDay, CustomerInfo.lastPaymentMonth,
    CustomerInfo.lastPaymentYear, CustomerInfo.registrationDay, CustomerInfo.registrationMonth,
    CustomerInfo.registrationYear, CustomerInfo.role, CustomerInfo.sdeType, CustomerInfo.serverTimeStamp,
    CustomerInfo.socialId, CustomerInfo.storeNumber, CustomerInfo.storeZipCode, CustomerInfo.userName
]


class Info(BaseModel):
    engagementId = TextField()
    accountId = IntegerField(null=True)
    agentDeleted = TextField(null=True)
    agentFullName = TextField(null=True)
    agentGroupId = TextField(null=True)
    agentGroupName = TextField(null=True)
    agentId = IntegerField(null=True)
    agentLoginName = TextField(null=True)
    agentNickName = TextField(null=True)
    alertedMCS = IntegerField(null=True)
    channel = TextField(null=True)
    chatDataEnriched = TextField(null=True)
    chatMCS = IntegerField(null=True)
    chatRequestedTime = TextField(null=True)
    chatRequestedTimeL = IntegerField(null=True)
    chatStartPage = TextField(null=True)
    chatStartUrl = TextField(null=True)
    duration = IntegerField(null=True)
    endReason = TextField(null=True)
    endReasonDesc = TextField(null=True)
    endTime = TextField(null=True)
    endTimeL = IntegerField(null=True)
    ended = TextField(null=True)
    engagementSequence = TextField(null=True)
    engagementSet = TextField(null=True)
    interactive = TextField(null=True)
    isAgentSurvey = TextField(null=True)
    isInteractive = TextField(null=True)
    isPartial = TextField(null=True)
    isPostChatSurvey = TextField(null=True)
    isPreChatSurvey = TextField(null=True)
    mcs = IntegerField(null=True)
    sharkEngagementId = TextField(null=True)
    skillId = IntegerField(null=True)
    skillName = TextField(null=True)
    startReason = TextField(null=True)
    startReasonDesc = TextField(null=True)
    startTime = TextField(null=True)
    startTimeL = IntegerField(null=True)
    visitorId = TextField(null=True)
    visitorName = TextField(null=True)


info_fields = [
    Info.engagementId, Info.accountId, Info.agentDeleted, Info.agentFullName, Info.agentGroupId, Info.agentGroupName,
    Info.agentId, Info.agentLoginName, Info.agentNickName, Info.alertedMCS, Info.channel, Info.chatDataEnriched,
    Info.chatMCS, Info.chatRequestedTime, Info.chatRequestedTimeL, Info.chatStartPage, Info.chatStartUrl, Info.duration,
    Info.endReason, Info.endReasonDesc, Info.endTime, Info.endTimeL, Info.ended, Info.engagementSequence,
    Info.engagementSet, Info.interactive, Info.isAgentSurvey, Info.isInteractive, Info.isPartial, Info.isPostChatSurvey,
    Info.isPreChatSurvey, Info.mcs, Info.sharkEngagementId, Info.skillId, Info.skillName, Info.startReason,
    Info.startReasonDesc, Info.startTime, Info.startTimeL, Info.visitorId, Info.visitorName
]


class Lead(BaseModel):
    engagementId = TextField()
    currency = TextField(null=True)
    isAuthenticated = TextField(null=True)
    leadId = IntegerField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    topic = TextField(null=True)
    value = DoubleField(null=True)


lead_fields = [
    Lead.engagementId, Lead.currency, Lead.isAuthenticated, Lead.leadId, Lead.sdeType, Lead.serverTimeStamp,
    Lead.topic, Lead.value
]


class LineScore(BaseModel):
    engagementId = TextField()
    lineRawScore = IntegerField(null=True)
    lineSeq = IntegerField(null=True)
    mcs = IntegerField(null=True)


line_score_fields = [LineScore.engagementId, LineScore.lineRawScore, LineScore.lineSeq, LineScore.mcs]


class MarketingCampaignInfo(BaseModel):
    engagementId = TextField()
    affiliate = TextField(null=True)
    campaignId = IntegerField(null=True)
    isAuthenticated = TextField(null=True)
    originatingChannel = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)


marketing_campaign_info_fields = [
    MarketingCampaignInfo.engagementId, MarketingCampaignInfo.affiliate, MarketingCampaignInfo.campaignId,
    MarketingCampaignInfo.isAuthenticated, MarketingCampaignInfo.originatingChannel, MarketingCampaignInfo.sdeType,
    MarketingCampaignInfo.serverTimeStamp
]


class PersonalInfo(BaseModel):
    engagementId = TextField()
    company = TextField(null=True)
    customerAgeInYears = TextField(null=True)
    customerDateOfBirth = TextField(null=True)
    customerMonthOfBirth = TextField(null=True)
    customerYearOfBirth = TextField(null=True)
    email = TextField(null=True)
    gender = TextField(null=True)
    isAuthenticated = TextField(null=True)
    language = TextField(null=True)
    name = TextField(null=True)
    phone = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    surname = TextField(null=True)


personal_info_fields = [
    PersonalInfo.engagementId, PersonalInfo.company, PersonalInfo.customerAgeInYears, PersonalInfo.customerDateOfBirth,
    PersonalInfo.customerMonthOfBirth, PersonalInfo.customerYearOfBirth, PersonalInfo.email, PersonalInfo.gender,
    PersonalInfo.isAuthenticated, PersonalInfo.language, PersonalInfo.name, PersonalInfo.phone, PersonalInfo.sdeType,
    PersonalInfo.serverTimeStamp, PersonalInfo.surname
]


class Purchase(BaseModel):
    engagementId = TextField()
    currency = TextField(null=True)
    isAuthenticated = TextField(null=True)
    numItems = IntegerField(null=True)
    orderId = TextField(null=True)
    productCategory = TextField(null=True)
    productName = TextField(null=True)
    productPrice = DoubleField(null=True)
    productQuantity = IntegerField(null=True)
    productSKU = TextField(null=True)
    purchaseTotal = DoubleField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    total = DoubleField(null=True)


purchase_fields = [
    Purchase.engagementId, Purchase.currency, Purchase.isAuthenticated, Purchase.numItems, Purchase.orderId,
    Purchase.productCategory, Purchase.productName, Purchase.productPrice, Purchase.productQuantity,
    Purchase.productSKU, Purchase.purchaseTotal, Purchase.sdeType, Purchase.serverTimeStamp, Purchase.total
]


class SearchContent(BaseModel):
    engagementId = TextField()
    affiliate = TextField(null=True)
    campaignId = IntegerField(null=True)
    isAuthenticated = TextField(null=True)
    originatingChannel = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)


search_content_fields = [
    SearchContent.engagementId, SearchContent.affiliate, SearchContent.campaignId, SearchContent.isAuthenticated,
    SearchContent.originatingChannel, SearchContent.sdeType, SearchContent.serverTimeStamp
]


class ServiceActivity(BaseModel):
    engagementId = TextField()
    category = TextField(null=True)
    isAuthenticated = TextField(null=True)
    serviceId = TextField(null=True)
    status = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    topic = TextField(null=True)


service_activity_fields = [
    ServiceActivity.engagementId, ServiceActivity.category, ServiceActivity.isAuthenticated, ServiceActivity.serviceId,
    ServiceActivity.status, ServiceActivity.sdeType, ServiceActivity.serverTimeStamp, ServiceActivity.topic
]


class Survey(BaseModel):
    engagementId = TextField()
    displayName = TextField(null=True)
    name = TextField(null=True)
    questionID = IntegerField(null=True)
    scope = TextField(null=True)
    source = TextField(null=True)
    surveyID = TextField(null=True)
    surveyType = TextField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)
    value = TextField(null=True)


survey_fields = [
    Survey.engagementId, Survey.displayName, Survey.name, Survey.questionID, Survey.scope, Survey.source,
    Survey.surveyID, Survey.surveyType, Survey.time, Survey.timeL, Survey.value
]


class Transcript(BaseModel):
    engagementId = TextField()
    agentId = IntegerField(null=True)
    by = TextField(null=True)
    cannedAnswerType = TextField(null=True)
    controlType = TextField(null=True)
    lineSeq = IntegerField(null=True)
    source = TextField(null=True)
    subType = TextField(null=True)
    text = TextField(null=True)
    textType = TextField(null=True)
    time = TextField(null=True)
    timeL = IntegerField(null=True)


transcript_fields = [
    Transcript.engagementId, Transcript.agentId, Transcript.by, Transcript.cannedAnswerType, Transcript.controlType,
    Transcript.lineSeq, Transcript.source, Transcript.subType, Transcript.text, Transcript.textType, Transcript.time,
    Transcript.timeL
]


class ViewedProduct(BaseModel):
    engagementId = TextField()
    currency = TextField(null=True)
    isAuthenticated = TextField(null=True)
    numItems = IntegerField(null=True)
    productCategory = TextField(null=True)
    productName = TextField(null=True)
    productPrice = DoubleField(null=True)
    productQuantity = IntegerField(null=True)
    productSKU = IntegerField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)
    total = DoubleField(null=True)


viewed_product_fields = [
    ViewedProduct.engagementId, ViewedProduct.currency, ViewedProduct.isAuthenticated, ViewedProduct.numItems,
    ViewedProduct.productCategory, ViewedProduct.productName, ViewedProduct.productPrice, ViewedProduct.productQuantity,
    ViewedProduct.productSKU, ViewedProduct.sdeType, ViewedProduct.serverTimeStamp, ViewedProduct.total
]


class VisitorError(BaseModel):
    engagementId = TextField()
    code = TextField(null=True)
    contextId = IntegerField(null=True)
    isAuthenticated = TextField(null=True)
    level = TextField(null=True)
    message = TextField(null=True)
    resolved = TextField(null=True)
    sdeType = TextField(null=True)
    serverTimeStamp = IntegerField(null=True)


visitor_error_fields = [
    VisitorError.engagementId, VisitorError.code, VisitorError.contextId, VisitorError.isAuthenticated,
    VisitorError.level, VisitorError.message, VisitorError.resolved, VisitorError.sdeType, VisitorError.serverTimeStamp
]


class VisitorInfo(BaseModel):
    engagementId = TextField()
    browser = TextField(null=True)
    city = TextField(null=True)
    country = TextField(null=True)
    countryCode = TextField(null=True)
    device = TextField(null=True)
    ipAddress = TextField(null=True)
    isp = TextField(null=True)
    operatingSystem = TextField(null=True)
    org = TextField(null=True)
    state = TextField(null=True)


visitor_info_fields = [
    VisitorInfo.engagementId, VisitorInfo.browser, VisitorInfo.city, VisitorInfo.country, VisitorInfo.countryCode,
    VisitorInfo.device, VisitorInfo.ipAddress, VisitorInfo.isp, VisitorInfo.operatingSystem, VisitorInfo.org,
    VisitorInfo.state
]


def initialize_database(db_name=None):
    if db_name:
        database = SqliteDatabase(db_name)
    else:
        database = SqliteDatabase(':memory:')

    database_proxy.initialize(database)
    database_proxy.connect()
    database_proxy.create_tables(
        [Campaign, CartStatus, CoBrowseSession, CustomerInfo, Info, Lead, LineScore, MarketingCampaignInfo,
         PersonalInfo, Purchase, SearchContent, ServiceActivity, Survey, Transcript, ViewedProduct, VisitorError,
         VisitorInfo]
    )
