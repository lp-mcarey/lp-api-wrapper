from collections import namedtuple
import pandas as pd


# ------------------- #
# Parse Event Columns #
# ------------------- #


def parse_columns(columns, data, engagement_id=None, engagement_sequence=None):
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

    if pd.notnull(engagement_sequence):
        parsed_data['engagementSequence'] = engagement_sequence

    return parsed_data


# -------------- #
# Campaign Event #
# -------------- #


campaign_columns = ['engagementId', 'engagementSequence', 'behaviorSystemDefault', 'campaignEngagementId', 'campaignEngagementName',
                    'campaignId', 'campaignName', 'goalId', 'goalName', 'lobId', 'lobName', 'profileSystemDefault',
                    'visitorBehaviorId', 'visitorBehaviorName', 'visitorProfileId', 'visitorProfileName']


class Campaign(namedtuple('Campaign', campaign_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=campaign_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ----------------- #
# Cart Status Event #
# ----------------- #

cart_status_columns = ['engagementId', 'engagementSequence', 'currency', 'isAuthenticated', 'numItems', 'productCategory', 'productName',
                       'productPrice', 'productQuantity', 'productSKU', 'sdeType', 'serverTimeStamp', 'total']


class CartStatus(namedtuple('CartStatus', cart_status_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=cart_status_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ---------------------- #
# CoBrowse Session Event #
# ---------------------- #


cobrowse_session_columns = ['engagementId', 'engagementSequence', 'duration', 'endReason', 'endTime', 'endTimeL', 'interactive', 'sessionId',
                            'startTime', 'startTimeL']


class CoBrowseSession(namedtuple('CoBrowseSession', cobrowse_session_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=cobrowse_session_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------------- #
# Customer Info Event #
# ------------------- #


customer_info_columns = ['engagementId', 'engagementSequence', 'accountName', 'balance', 'companySize', 'currency', 'customerId',
                         'customerStatus', 'customerType', 'imei', 'isAuthenticated', 'lastPaymentDay',
                         'lastPaymentMonth', 'lastPaymentYear', 'registrationDay', 'registrationMonth',
                         'registrationYear', 'role', 'sdeType', 'serverTimeStamp', 'socialId', 'storeNumber',
                         'storeZipCode', 'userName']


class CustomerInfo(namedtuple('CustomerInfo', customer_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=customer_info_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


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


lead_columns = ['engagementId', 'engagementSequence', 'currency', 'isAuthenticated', 'leadId', 'sdeType', 'serverTimeStamp', 'topic', 'value']


class Lead(namedtuple('Lead', lead_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=lead_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ---------------- #
# Line Score Event #
# ---------------- #


line_score_columns = ['engagementId', 'engagementSequence', 'lineRawScore', 'lineSeq', 'mcs']


class LineScore(namedtuple('LineScore', line_score_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=line_score_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------------------ #
# Marketing Campaign Info Event #
# ------------------------ #


marketing_campaign_info_columns = ['engagementId', 'engagementSequence', 'affiliate', 'campaignId', 'isAuthenticated', 'originatingChannel',
                                   'sdeType', 'serverTimeStamp']


class MarketingCampaignInfo(namedtuple('MarketingCampaignInfo', marketing_campaign_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=marketing_campaign_info_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------------- #
# Personal Info Event #
# ------------------- #


personal_info_columns = ['engagementId', 'engagementSequence', 'company', 'customerAgeInYears', 'customerDateOfBirth',
                         'customerMonthOfBirth', 'customerYearOfBirth', 'email', 'gender', 'isAuthenticated',
                         'language', 'name', 'phone', 'sdeType', 'serverTimeStamp', 'surname']


class PersonalInfo(namedtuple('PersonalInfo', personal_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=personal_info_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# -------------- #
# Purchase Event #
# -------------- #


purchase_columns = ['engagementId', 'engagementSequence', 'currency', 'isAuthenticated', 'numItems',  'orderId', 'productCategory',
                    'productName', 'productPrice', 'productQuantity', 'productSKU', 'purchaseTotal', 'sdeType',
                    'serverTimeStamp', 'total']


class Purchase(namedtuple('Purchase', purchase_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=purchase_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# -------------------- #
# Search Content Event #
# -------------------- #


search_content_columns = ['engagementId', 'engagementSequence', 'affiliate', 'campaignId', 'isAuthenticated', 'originatingChannel',
                          'sdeType', 'serverTimeStamp']


class SearchContent(namedtuple('SearchContent', search_content_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=search_content_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ---------------------- #
# Service Activity Event #
# ---------------------- #


service_activity_columns = ['engagementId', 'engagementSequence', 'category', 'isAuthenticated', 'serviceId', 'status', 'sdeType',
                            'serverTimeStamp', 'topic']


class ServiceActivity(namedtuple('ServiceActivity', service_activity_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=service_activity_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------ #
# Survey Event #
# ------------ #


survey_columns = ['engagementId', 'engagementSequence', 'displayName', 'name', 'questionID', 'scope', 'source', 'surveyID', 'surveyType',
                  'time', 'timeL', 'value', 'values']


class Survey(namedtuple('Survey', survey_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=survey_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ---------------- #
# Transcript Event #
# ---------------- #


transcript_columns = ['engagementId', 'engagementSequence', 'agentId', 'by', 'cannedAnswerType', 'controlType', 'lineSeq', 'source',
                      'subType', 'text', 'textType', 'time', 'timeL']


class Transcript(namedtuple('Transcript', transcript_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=transcript_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# -------------------- #
# Viewed Product Event #
# -------------------- #

viewed_product_columns = ['engagementId', 'engagementSequence', 'currency', 'isAuthenticated', 'numItems', 'productCategory', 'productName',
                          'productPrice', 'productQuantity', 'productSKU', 'sdeType', 'serverTimeStamp', 'total']


class ViewedProduct(namedtuple('ViewedProduct', viewed_product_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=cart_status_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------------- #
# Visitor Error Event #
# ------------------- #

visitor_error_columns = ['engagementId', 'engagementSequence', 'code', 'contextId', 'isAuthenticated', 'level', 'message', 'resolved',
                         'sdeType', 'serverTimeStamp']


class VisitorError(namedtuple('VisitorError', visitor_error_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=visitor_error_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))


# ------------------ #
# Visitor Info Event #
# ------------------ #


visitor_info_columns = ['engagementId', 'engagementSequence', 'browser', 'city', 'country', 'countryCode', 'device', 'ipAddress', 'isp',
                        'operatingSystem', 'org', 'state']


class VisitorInfo(namedtuple('VisitorInfo', visitor_info_columns)):

    @classmethod
    def parse_from_data(cls, data, engagement_id, engagement_sequence):
        return cls(**parse_columns(columns=visitor_info_columns, data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence))
