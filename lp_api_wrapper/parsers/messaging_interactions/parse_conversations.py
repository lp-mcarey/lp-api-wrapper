from lp_api_wrapper.parsers.messaging_interactions.events import (
    AgentParticipant, Campaign, CoBrowseSession, ConsumerParticipant, ConversationSurvey, CustomerInfo, Info,
    Interaction, MessageRecord, MessageScore, MessageStatus, PersonalInfo, Summary, Transfer, ResponseTime,Monitoring
)


class Conversations:
    __slots__ = ['agent_participants', 'campaign', 'cobrowse_sessions', 'consumer_participants', 'conversation_surveys',
                 'customer_info', 'info', 'interactions', 'message_records', 'message_scores', 'message_statuses',
                 'personal_info', 'summary', 'transfers', 'responseTime', 'monitoring']

    def __init__(self):
        self.agent_participants = []
        self.campaign = []
        self.cobrowse_sessions = []
        self.consumer_participants = []
        self.conversation_surveys = []
        self.customer_info = []
        self.info = []
        self.interactions = []
        self.message_records = []
        self.message_scores = []
        self.message_statuses = []
        self.personal_info = []
        self.summary = []
        self.transfers = []
        self.responseTime = []
        self.monitoring = []

    def append_records(self, records):
        for record in records:
            try:
                conversation_id = record['info']['conversationId']
            except KeyError:
                raise ValueError('Oops! ~ Not a Conversation!')

            for event, data in record.items():
                if 'agentParticipants' in event:
                    self.__parse_agent_participant_data(data=data, conversation_id=conversation_id)
                elif 'campaign' in event:
                    self.__parse_campaign_data(data=data, conversation_id=conversation_id)
                elif 'coBrowseSessions' in event:
                    self.__parse_cobrowse_session_data(data=data, conversation_id=conversation_id)
                elif 'consumerParticipants' in event:
                    self.__parse_consumer_participant_data(data=data, conversation_id=conversation_id)
                elif 'conversationSurveys' in event:
                    self.__parse_conversation_survey_data(data=data, conversation_id=conversation_id)
                elif 'info' in event:
                    self.__parse_info_data(data=data)
                elif 'interactions' in event:
                    self.__parse_interaction_data(data=data, conversation_id=conversation_id)
                elif 'messageRecords' in event:
                    self.__parse_message_record_data(data=data, conversation_id=conversation_id)
                elif 'messageScores' in event:
                    self.__parse_message_score_data(data=data, conversation_id=conversation_id)
                elif 'messageStatuses' in event:
                    self.__parse_message_status_data(data=data, conversation_id=conversation_id)
                elif 'summary' in event:
                    self.__parse_summary_data(data=data, conversation_id=conversation_id)
                elif 'transfers' in event:
                    self.__parse_transfer_data(data=data, conversation_id=conversation_id)
                elif 'sdes' in event and 'events' in data and data['events']:
                    self.__parse_sde_data(data=data['events'], conversation_id=conversation_id)
                elif 'responseTime' in event:
                    self.__parse_responseTime(data=data, conversation_id=conversation_id)
                elif 'monitoring' in event:
                    self.__parse_monitoring(data=data, conversation_id=conversation_id)

    def __parse_agent_participant_data(self, data, conversation_id):
        for ap_data in data:
            event = AgentParticipant.parse_from_data(data=ap_data, conversation_id=conversation_id)
            self.agent_participants.append(event)

    def __parse_campaign_data(self, data, conversation_id):
        event = Campaign.parse_from_data(data=data, conversation_id=conversation_id)
        self.campaign.append(event)

    def __parse_cobrowse_session_data(self, data, conversation_id):
        if 'coBrowseSessionsList' in data and data['coBrowseSessionsList']:
            for cb_data in data['coBrowseSessionsList']:
                cb_data['capability'] = None

                if 'capabilities' in cb_data and cb_data['capabilities']:
                    for capability in cb_data['capabilities']:
                        cb_data['capability'] = capability
                        event = CoBrowseSession.parse_from_data(data=cb_data, conversation_id=conversation_id)
                        self.cobrowse_sessions.append(event)

                else:
                    event = CoBrowseSession.parse_from_data(data=cb_data, conversation_id=conversation_id)
                    self.cobrowse_sessions.append(event)

    def __parse_consumer_participant_data(self, data, conversation_id):
        for cp_data in data:
            event = ConsumerParticipant.parse_from_data(data=cp_data, conversation_id=conversation_id)
            self.consumer_participants.append(event)

    def __parse_conversation_survey_data(self, data, conversation_id):
        for s_data in data:

            s_data['surveyQuestion'] = None
            s_data['surveyAnswer'] = None

            if 'surveyData' in s_data and s_data['surveyData']:
                for survey_data_item in s_data['surveyData']:
                    if 'question' in survey_data_item:
                        s_data['surveyQuestion'] = survey_data_item['question']

                    if 'answer' in survey_data_item:
                        s_data['surveyAnswer'] = survey_data_item['answer']

                    event = ConversationSurvey.parse_from_data(data=s_data, conversation_id=conversation_id)
                    self.conversation_surveys.append(event)

            else:
                event = ConversationSurvey.parse_from_data(data=s_data, conversation_id=conversation_id)
                self.conversation_surveys.append(event)

    def __parse_info_data(self, data):
        event = Info.parse_from_data(data=data)
        self.info.append(event)

    def __parse_interaction_data(self, data, conversation_id):
        for i_data in data:
            event = Interaction.parse_from_data(data=i_data, conversation_id=conversation_id)
            self.interactions.append(event)

    def __parse_message_record_data(self, data, conversation_id):
        for mr_data in data:
            mr_data['text'] = None
            mr_data['richContent'] = None
            mr_data['quickReplies'] = None
            mr_data['rawMetadata'] = None

            if 'messageData' in mr_data and 'msg' in mr_data['messageData'] and 'text' in mr_data['messageData']['msg']:
                mr_data['text'] = mr_data['messageData']['msg']['text']
            if 'messageData' in mr_data and 'richContent' in mr_data['messageData'] and 'content' in mr_data['messageData']['richContent']:
                mr_data['richContent'] = mr_data['messageData']['richContent']['content']
            if 'messageData' in mr_data and 'quickReplies' in mr_data['messageData'] and 'content' in mr_data['messageData']['quickReplies']:
                mr_data['quickReplies'] = mr_data['messageData']['quickReplies']['content']
            if 'contextData' in mr_data and 'rawMetadata' in mr_data['contextData']:
                mr_data['rawMetadata'] = mr_data['contextData']['rawMetadata']

            event = MessageRecord.parse_from_data(data=mr_data, conversation_id=conversation_id)
            self.message_records.append(event)

    def __parse_message_score_data(self, data, conversation_id):
        for ms_data in data:
            event = MessageScore.parse_from_data(data=ms_data, conversation_id=conversation_id)
            self.message_scores.append(event)

    def __parse_message_status_data(self, data, conversation_id):
        for ms_data in data:
            event = MessageStatus.parse_from_data(data=ms_data, conversation_id=conversation_id)
            self.message_statuses.append(event)

    def __parse_summary_data(self, data, conversation_id):
        event = Summary.parse_from_data(data=data, conversation_id=conversation_id)
        self.summary.append(event)

    def __parse_transfer_data(self, data, conversation_id):
        for t_data in data:
            event = Transfer.parse_from_data(data=t_data, conversation_id=conversation_id)
            self.transfers.append(event)

    def __parse_sde_data(self, data, conversation_id):
        for sde_event in data:
            if 'sdeType' in sde_event:
                sde_type = sde_event['sdeType']
                if sde_type == 'CUSTOMER_INFO':
                    self.__parse_sde_customer_info(sde=sde_event, conversation_id=conversation_id)
                elif sde_type == 'PERSONAL_INFO':
                    self.__parse_sde_personal_info(sde=sde_event, conversation_id=conversation_id)

    def __parse_sde_customer_info(self, sde, conversation_id):
        if 'customerInfo' in sde and 'customerInfo' in sde['customerInfo']:
            ci_sde = sde['customerInfo']['customerInfo']
            ci_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            ci_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            ci_sde['lastPaymentDay'] = None
            ci_sde['lastPaymentMonth'] = None
            ci_sde['lastPaymentYear'] = None

            if 'lastPaymentDate' in ci_sde:
                lp_date = ci_sde['lastPaymentDate']

                if 'day' in lp_date:
                    ci_sde['lastPaymentDay'] = lp_date['day']
                if 'month' in lp_date:
                    ci_sde['lastPaymentMonth'] = lp_date['month']
                if 'year' in lp_date:
                    ci_sde['lastPaymentYear'] = lp_date['year']

            ci_sde['registrationDay'] = None
            ci_sde['registrationMonth'] = None
            ci_sde['registrationYear'] = None

            if 'registrationDate' in ci_sde:
                r_date = ci_sde['registrationDate']

                if 'day' in r_date:
                    ci_sde['lastPaymentDay'] = r_date['day']
                if 'month' in r_date:
                    ci_sde['lastPaymentMonth'] = r_date['month']
                if 'year' in r_date:
                    ci_sde['lastPaymentYear'] = r_date['year']

            event = CustomerInfo.parse_from_data(data=ci_sde, conversation_id=conversation_id)
            self.customer_info.append(event)

    def __parse_sde_personal_info(self, sde, conversation_id):
        if 'personalInfo' in sde and 'personalInfo' in sde['personalInfo']:

            pi_sde = sde['personalInfo']['personalInfo']
            pi_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            pi_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None
            pi_sde['email'] = None
            pi_sde['phone'] = None

            if 'contacts' in pi_sde and pi_sde['contacts']:
                for contact in pi_sde['contacts']:
                    if 'personalContact' in contact:
                        pc = contact['personalContact']
                        if 'email' in pc:
                            pi_sde['email'] = pc['email']
                        if 'phone' in pc:
                            pi_sde['phone'] = pc['phone']
                        event = PersonalInfo.parse_from_data(data=pi_sde, conversation_id=conversation_id)
                        self.personal_info.append(event)
            else:
                event = PersonalInfo.parse_from_data(data=pi_sde, conversation_id=conversation_id)
                self.personal_info.append(event)

    def __parse_responseTime(self, data, conversation_id):
        event = ResponseTime.parse_from_data(data=data, conversation_id=conversation_id)
        self.responseTime.append(event)

    def __parse_monitoring(self, data, conversation_id):
        event = Monitoring.parse_from_data(data=data,conversation_id=conversation_id)
        self.monitoring.append(event)