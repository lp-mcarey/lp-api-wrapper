from collections import namedtuple


# ------------------- #
# Parse Event Columns #
# ------------------- #


def parse_columns(columns, data, engagement_id=None):
    parsed_data = {}
    for column in columns:

        if column in data:
            if data[column] in ['', []]:
                parsed_data[column] = None
            else:
                parsed_data[column] = data[column]
        else:
            parsed_data[column] = None

    if engagement_id:
        parsed_data['engagementId'] = engagement_id

    return parsed_data


# -------------- #
# Campaign Event #
# -------------- #


campaign_columns = ['engagementId', 'behaviorSystemDefault', 'campaignEngagementId', 'campaignEngagementName',
                    'campaignId', 'campaignName', 'goalId', 'goalName', 'lobId', 'lobName', 'profileSystemDefault',
                    'visitorBehaviorId', 'visitorBehaviorName', 'visitorProfileId', 'visitorProfileName']


class Campaign(namedtuple('Campaign', campaign_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=campaign_columns, data=data, engagement_id=engagement_id))


# ----------------- #
# Cart Status Event #
# ----------------- #

cart_status_columns = ['engagementId', 'currency', 'isAuthenticated', 'numItems', 'productCategory', 'productName',
                       'productPrice', 'productQuantity', 'productSKU', 'sdeType', 'serverTimeStamp', 'total']


class CartStatus(namedtuple('CartStatus', cart_status_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=cart_status_columns, data=data, engagement_id=engagement_id))


# ---------------------- #
# CoBrowse Session Event #
# ---------------------- #


cobrowse_session_columns = ['engagementId', 'duration', 'endReason', 'endTime', 'endTimeL', 'interactive', 'sessionId',
                            'startTime', 'startTimeL']


class CoBrowseSession(namedtuple('CoBrowseSession', cobrowse_session_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=cobrowse_session_columns, data=data, engagement_id=engagement_id))


# ------------------- #
# Customer Info Event #
# ------------------- #


customer_info_columns = ['engagementId', 'accountName', 'balance', 'companySize', 'currency', 'customerId',
                         'customerStatus', 'customerType', 'imei', 'isAuthenticated', 'lastPaymentDay',
                         'lastPaymentMonth', 'lastPaymentYear', 'registrationDay', 'registrationMonth',
                         'registrationYear', 'role', 'sdeType', 'serverTimeStamp', 'socialId', 'storeNumber',
                         'storeZipCode', 'userName']


class CustomerInfo(namedtuple('CustomerInfo', customer_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=customer_info_columns, data=data, engagement_id=engagement_id))


# ---------- #
# Info Event #
# ---------- #


info_columns = ['engagementId', 'accountId', 'agentDeleted', 'agentFullName', 'agentGroupId', 'agentGroupName',
                'agentId', 'agentLoginName', 'agentNickName', 'alertedMCS', 'channel', 'chatDataEnriched', 'chatMCS',
                'chatRequestedTime', 'chatRequestedTimeL', 'chatStartPage', 'chatStartUrl', 'duration', 'endReason',
                'endReasonDesc', 'endTime', 'endTimeL', 'ended', 'engagementSequence', 'engagementSet', 'interactive',
                'isAgentSurvey', 'isInteractive', 'isPartial', 'isPostChatSurvey', 'isPreChatSurvey', 'mcs',
                'sharkEngagementId', 'skillId', 'skillName', 'startReason', 'startReasonDesc', 'startTime',
                'startTimeL', 'visitorId', 'visitorName']


class Info(namedtuple('Info', info_columns)):

    @classmethod
    def parse_from_data(cls, data):
        return cls(**parse_columns(columns=info_columns, data=data))


# ---------- #
# Lead Event #
# ---------- #


lead_columns = ['engagementId', 'currency', 'isAuthenticated', 'leadId', 'sdeType', 'serverTimeStamp', 'topic', 'value']


class Lead(namedtuple('Lead', lead_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=lead_columns, data=data, engagement_id=engagement_id))


# ---------------- #
# Line Score Event #
# ---------------- #


line_score_columns = ['engagementId', 'lineRawScore', 'lineSeq', 'mcs']


class LineScore(namedtuple('LineScore', line_score_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=line_score_columns, data=data, engagement_id=engagement_id))


# ------------------------ #
# Marketing Campaign Info Event #
# ------------------------ #


marketing_campaign_info_columns = ['engagementId', 'affiliate', 'campaignId', 'isAuthenticated', 'originatingChannel',
                                   'sdeType', 'serverTimeStamp']


class MarketingCampaignInfo(namedtuple('MarketingCampaignInfo', marketing_campaign_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=marketing_campaign_info_columns, data=data, engagement_id=engagement_id))


# ------------------- #
# Personal Info Event #
# ------------------- #


personal_info_columns = ['engagementId', 'company', 'customerAgeInYears', 'customerDateOfBirth',
                         'customerMonthOfBirth', 'customerYearOfBirth', 'email', 'gender', 'isAuthenticated',
                         'language', 'name', 'phone', 'sdeType', 'serverTimeStamp', 'surname']


class PersonalInfo(namedtuple('PersonalInfo', personal_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=personal_info_columns, data=data, engagement_id=engagement_id))


# -------------- #
# Purchase Event #
# -------------- #


purchase_columns = ['engagementId', 'currency', 'isAuthenticated', 'numItems',  'orderId', 'productCategory',
                    'productName', 'productPrice', 'productQuantity', 'productSKU', 'purchaseTotal', 'sdeType',
                    'serverTimeStamp', 'total']


class Purchase(namedtuple('Purchase', purchase_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=purchase_columns, data=data, engagement_id=engagement_id))


# -------------------- #
# Search Content Event #
# -------------------- #


search_content_columns = ['engagementId', 'affiliate', 'campaignId', 'isAuthenticated', 'originatingChannel',
                          'sdeType', 'serverTimeStamp']


class SearchContent(namedtuple('SearchContent', search_content_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=search_content_columns, data=data, engagement_id=engagement_id))


# ---------------------- #
# Service Activity Event #
# ---------------------- #


service_activity_columns = ['engagementId', 'category', 'isAuthenticated', 'serviceId', 'status', 'sdeType',
                            'serverTimeStamp', 'topic']


class ServiceActivity(namedtuple('ServiceActivity', service_activity_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=service_activity_columns, data=data, engagement_id=engagement_id))


# ------------ #
# Survey Event #
# ------------ #


survey_columns = ['engagementId', 'displayName', 'name', 'questionID', 'scope', 'source', 'surveyID', 'surveyType',
                  'time', 'timeL', 'value']


class Survey(namedtuple('Survey', survey_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=survey_columns, data=data, engagement_id=engagement_id))


# ---------------- #
# Transcript Event #
# ---------------- #


transcript_columns = ['engagementId', 'agentId', 'by', 'cannedAnswerType', 'controlType', 'lineSeq', 'source',
                      'subType', 'text', 'textType', 'time', 'timeL']


class Transcript(namedtuple('Transcript', transcript_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=transcript_columns, data=data, engagement_id=engagement_id))


# -------------------- #
# Viewed Product Event #
# -------------------- #

viewed_product_columns = ['engagementId', 'currency', 'isAuthenticated', 'numItems', 'productCategory', 'productName',
                          'productPrice', 'productQuantity', 'productSKU', 'sdeType', 'serverTimeStamp', 'total']


class ViewedProduct(namedtuple('ViewedProduct', viewed_product_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=cart_status_columns, data=data, engagement_id=engagement_id))


# ------------------- #
# Visitor Error Event #
# ------------------- #

visitor_error_columns = ['engagementId', 'code', 'contextId', 'isAuthenticated', 'level', 'message', 'resolved',
                         'sdeType', 'serverTimeStamp']


class VisitorError(namedtuple('VisitorError', visitor_error_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=visitor_error_columns, data=data, engagement_id=engagement_id))


# ------------------ #
# Visitor Info Event #
# ------------------ #


visitor_info_columns = ['engagementId', 'browser', 'city', 'country', 'countryCode', 'device', 'ipAddress', 'isp',
                        'operatingSystem', 'org', 'state']


class VisitorInfo(namedtuple('VisitorInfo', visitor_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id):
        return cls(**parse_columns(columns=visitor_info_columns, data=data, engagement_id=engagement_id))
