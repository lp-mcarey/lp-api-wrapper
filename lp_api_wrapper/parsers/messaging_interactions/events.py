from collections import namedtuple


# ------------------- #
# Parse Event Columns #
# ------------------- #


def parse_columns(columns, data, conversation_id=None):
    parsed_data = {}
    for column in columns:

        if column in data:
            if data[column] in ['', []]:
                parsed_data[column] = None
            else:
                parsed_data[column] = data[column]
        else:
            parsed_data[column] = None

    if conversation_id:
        parsed_data['conversationId'] = conversation_id

    return parsed_data


# ----------------------- #
# Agent Participant Event #
# ----------------------- #


agent_participant_columns = ['conversationId', 'agentDeleted', 'agentFullName', 'agentGroupId', 'agentGroupName',
                             'agentId', 'agentLoginName', 'agentNickname', 'agentPid', 'permission', 'role', 'time',
                             'timeL', 'userType', 'userTypeName']


class AgentParticipant(namedtuple('AgentParticipant', agent_participant_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=agent_participant_columns, data=data, conversation_id=conversation_id))

# -------------- #
# Campaign Event #
# -------------- #


campaign_columns = ['conversationId', 'behaviorSystemDefault', 'campaignEngagementId', 'campaignEngagementName',
                    'campaignId', 'campaignName', 'engagementAgentNote', 'engagementApplicationId',
                    'engagementApplicationName', 'engagementApplicationTypeId', 'engagementApplicationTypeName',
                    'engagementSource', 'goalId', 'goalName', 'lobId', 'lobName', 'locationId', 'locationName',
                    'profileSystemDefault', 'visitorBehaviorId', 'visitorBehaviorName', 'visitorProfileId',
                    'visitorProfileName']


class Campaign(namedtuple('Campaign', campaign_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=campaign_columns, data=data, conversation_id=conversation_id))


# ---------------------- #
# CoBrowse Session Event #
# ---------------------- #


cobrowse_session_columns = ['conversationId', 'agentId', 'capability', 'duration', 'endReason', 'endTime', 'endTimeL',
                            'interactiveTime', 'interactiveTimeL', 'isInteractive', 'sessionId', 'startTime',
                            'startTimeL', 'type']


class CoBrowseSession(namedtuple('CoBrowseSession', cobrowse_session_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=cobrowse_session_columns, data=data, conversation_id=conversation_id))

# -------------------------- #
# Consumer Participant Event #
# -------------------------- #


consumer_participant_columns = ['conversationId', 'avatarURL', 'consumerName', 'email', 'firstName', 'lastName',
                                'participantId', 'phone', 'time', 'timeL', 'token']


class ConsumerParticipant(namedtuple('AgentParticipant', consumer_participant_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=consumer_participant_columns, data=data, conversation_id=conversation_id))

# ------------------------- #
# Conversation Survey Event #
# ------------------------- #


conversation_survey_columns = ['conversationId', 'surveyAnswer', 'surveyQuestion', 'surveyStatus', 'surveyType']


class ConversationSurvey(namedtuple('ConversationSurvey', conversation_survey_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=conversation_survey_columns, data=data, conversation_id=conversation_id))

# ------------------- #
# Customer Info Event #
# ------------------- #


customer_info_columns = ['conversationId', 'accountName', 'balance', 'companyBranch', 'companySize', 'customerId',
                         'customerStatus', 'customerType', 'imei', 'lastPaymentDay', 'lastPaymentMonth',
                         'lastPaymentYear', 'loginStatus', 'registrationDay', 'registrationMonth', 'registrationYear',
                         'role',  'sdeType', 'serverTimeStamp', 'socialId', 'storeNumber', 'storeZipCode', 'userName']


class CustomerInfo(namedtuple('CustomerInfo', customer_info_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=customer_info_columns, data=data, conversation_id=conversation_id))

# ---------- #
# Info Event #
# ---------- #


info_columns = ['conversationId', 'agentDeleted', 'alertedMCS', 'brandId', 'browser', 'closeReason',
                'closeReasonDescription', 'csat', 'csatRate', 'device', 'duration', 'endTime', 'endTimeL',
                'firstConversation', 'isPartial', 'latestAgentFullName', 'latestAgentGroupId', 'latestAgentGroupName',
                'latestAgentId', 'latestAgentLoginName', 'latestAgentNickname', 'latestQueueState', 'latestSkillId',
                'latestSkillName', 'mcs', 'operatingSystem', 'source', 'startTime', 'startTimeL', 'status']


class Info(namedtuple('Info', info_columns)):

    @classmethod
    def parse_from_data(cls, data):
        return cls(**parse_columns(columns=info_columns, data=data))

# ----------------- #
# Interaction Event #
# ----------------- #


interaction_columns = ['conversationId', 'assignedAgentId', 'assignedAgentLoginName', 'assignedAgentNickname',
                       'assignedAgentFullName', 'interactionTime', 'interactionTimeL', 'interactiveSequence']


class Interaction(namedtuple('Interaction', interaction_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=interaction_columns, data=data, conversation_id=conversation_id))

# -------------------- #
# Message Record Event #
# -------------------- #


message_record_columns = ['conversationId', 'device', 'dialogId', 'messageId', 'participantId', 'sentBy', 'seq',
                          'source', 'text', 'time', 'timeL', 'type']


class MessageRecord(namedtuple('MessageRecord', message_record_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=message_record_columns, data=data, conversation_id=conversation_id))

# ------------------- #
# Message Score Event #
# ------------------- #


message_score_columns = ['conversationId', 'mcs', 'messageId', 'messageRawScore', 'time', 'timeL']


class MessageScore(namedtuple('MessageScore', message_score_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=message_score_columns, data=data, conversation_id=conversation_id))

# -------------------- #
# Message Status Event #
# -------------------- #


message_status_columns = ['conversationId', 'messageDeliveryStatus', 'messageId', 'participantId',
                          'participantType', 'seq', 'time', 'timeL']


class MessageStatus(namedtuple('MessageStatus', message_status_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=message_status_columns, data=data, conversation_id=conversation_id))

# ------------------- #
# Personal Info Event #
# ------------------- #


personal_info_columns = ['conversationId', 'company', 'customerAge', 'email', 'gender', 'language', 'name',
                         'phone', 'sdeType', 'serverTimeStamp', 'surname']


class PersonalInfo(namedtuple('PersonalInfo', personal_info_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=personal_info_columns, data=data, conversation_id=conversation_id))


# ------------- #
# Summary Event #
# ------------- #


summary_columns = ['conversationId', 'lastUpdatedTime', 'text']


class Summary(namedtuple('Transfer', summary_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=summary_columns, data=data, conversation_id=conversation_id))


# -------------- #
# Transfer Event #
# -------------- #


transfer_columns = ['conversationId', 'assignedAgentFullName', 'assignedAgentId', 'assignedAgentLoginName',
                    'assignedAgentNickname', 'by', 'reason', 'sourceAgentFullName', 'sourceAgentId',
                    'sourceAgentLoginName', 'sourceAgentNickname', 'sourceSkillId', 'sourceSkillName',
                    'targetSkillId', 'targetSkillName', 'time', 'timeL']


class Transfer(namedtuple('Transfer', transfer_columns)):

    @classmethod
    def parse_from_data(cls, data, conversation_id):
        return cls(**parse_columns(columns=transfer_columns, data=data, conversation_id=conversation_id))
