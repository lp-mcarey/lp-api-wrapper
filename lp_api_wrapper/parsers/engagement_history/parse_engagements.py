from lp_api_wrapper.parsers.engagement_history.events import (
    Campaign, CartStatus, CoBrowseSession, CustomerInfo, Info, Lead, LineScore, MarketingCampaignInfo, PersonalInfo,
    Purchase, SearchContent, ServiceActivity, Survey, Transcript, ViewedProduct, VisitorError, VisitorInfo
)


class Engagements:
    __slots__ = ['campaign', 'cart_status', 'cobrowse_sessions', 'customer_info', 'info', 'lead', 'line_scores',
                 'marketing_campaign_info', 'personal_info', 'purchase', 'search_content', 'service_activity',
                 'surveys', 'transcript', 'viewed_product', 'visitor_error', 'visitor_info']

    def __init__(self):
        self.campaign = []
        self.cart_status = []
        self.cobrowse_sessions = []
        self.customer_info = []
        self.info = []
        self.lead = []
        self.line_scores = []
        self.marketing_campaign_info = []
        self.personal_info = []
        self.purchase = []
        self.search_content = []
        self.service_activity = []
        self.surveys = []
        self.transcript = []
        self.viewed_product = []
        self.visitor_error = []
        self.visitor_info = []

    def append_records(self, records):
        for record in records:
            try:
                engagement_id = record['info']['engagementId']
                engagement_sequence = record['info']['engagementSequence']
            except KeyError:
                raise ValueError('Oops! ~ Not an Engagement!')

            for event, data in record.items():
                if 'campaign' in event:
                    self.__parse_campaign_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'coBrowseSessions' in event:
                    self.__parse_campaign_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'info' in event:
                    self.__parse_info_data(data=data)
                elif 'lineScores' in event:
                    self.__parse_line_score_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'surveys' in event:
                    self.__parse_survey_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'transcript' in event:
                    self.__parse_transcript_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'visitorInfo' in event:
                    self.__parse_visitor_info_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif 'sdes' in event and 'events' in data and data['events']:
                    self.__parse_sde_data(data=data['events'], engagement_id=engagement_id, engagement_sequence=engagement_sequence)

    def __parse_campaign_data(self, data, engagement_id, engagement_sequence):
        event = Campaign.parse_from_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
        self.campaign.append(event)

    def __parse_cobrowse_session_data(self, data, engagement_id, engagement_sequence):
        if 'coBrowseSessionsList' in data and data['coBrowseSessionsList']:
            cb_sessions = data['coBrowseSessionsList']
            events = [CoBrowseSession.parse_from_data(data=item, engagement_id=engagement_id, engagement_sequence=engagement_sequence) for item in cb_sessions]
            self.cobrowse_sessions.extend(events)

    def __parse_info_data(self, data):
        event = Info.parse_from_data(data=data)
        self.info.append(event)

    def __parse_line_score_data(self, data, engagement_id, engagement_sequence):
        events = [LineScore.parse_from_data(data=item, engagement_id=engagement_id, engagement_sequence=engagement_sequence) for item in data]
        self.line_scores.extend(events)

    def __parse_survey_data(self, data, engagement_id, engagement_sequence):
        parsed_surveys = []
        for survey_type, survey_items in data.items():
            for survey in survey_items:
                survey['surveyType'] = survey_type
                parsed_surveys.append(survey)

        events = [Survey.parse_from_data(data=item, engagement_id=engagement_id, engagement_sequence=engagement_sequence) for item in parsed_surveys]
        self.surveys.extend(events)

    def __parse_transcript_data(self, data, engagement_id, engagement_sequence):
        if 'lines' in data and data['lines']:
            events = [Transcript.parse_from_data(data=item, engagement_id=engagement_id, engagement_sequence=engagement_sequence) for item in data['lines']]
            self.transcript.extend(events)

    def __parse_visitor_info_data(self, data, engagement_id, engagement_sequence):
        event = VisitorInfo.parse_from_data(data=data, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
        self.visitor_info.append(event)

    def __parse_sde_data(self, data, engagement_id, engagement_sequence):
        for sde_event in data:
            if 'sdeType' in sde_event:
                sde_type = sde_event['sdeType']
                if sde_type == 'CART_STATUS':
                    self.__parse_sde_cart_status(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'CUSTOMER_INFO':
                    self.__parse_sde_customer_info(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'LEAD':
                    self.__parse_sde_lead(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'MARKETING_CAMPAIGN_INFO':
                    self.__parse_sde_marketing_campaign_info(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'PERSONAL_INFO':
                    self.__parse_sde_personal_info(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'PURCHASE':
                    self.__parse_sde_purchase(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'SEARCH_CONTENT':
                    self.__parse_sde_search_content(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'SERVICE_ACTIVITY':
                    self.__parse_sde_service_activity(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'VISITOR_ERROR':
                    self.__parse_sde_visitor_error(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                elif sde_type == 'VIEWED_PRODUCT':
                    self.__parse_sde_viewed_product(sde=sde_event, engagement_id=engagement_id, engagement_sequence=engagement_sequence)

    def __parse_sde_cart_status(self, sde, engagement_id, engagement_sequence):
        if 'cartStatus' in sde:
            cs_sde = sde['cartStatus']
            cs_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            cs_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            cs_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            cs_sde['productCategory'] = None
            cs_sde['productName'] = None
            cs_sde['productQuantity'] = None
            cs_sde['productPrice'] = None
            cs_sde['productSKU'] = None

            if 'products' in cs_sde and cs_sde['products']:
                for product in cs_sde['products']:

                    if 'quantity' in product:
                        cs_sde['productQuantity'] = product['quantity']

                    if 'product' in product:
                        prod_item = product['product']

                        if 'name' in prod_item:
                            cs_sde['productName'] = prod_item['name']
                        if 'category' in prod_item:
                            cs_sde['productCategory'] = prod_item['category']
                        if 'sku' in prod_item:
                            cs_sde['productSKU'] = prod_item['sku']
                        if 'price' in prod_item:
                            cs_sde['productPrice'] = prod_item['price']

                    event = CartStatus.parse_from_data(data=cs_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                    self.cart_status.append(event)
            else:
                event = CartStatus.parse_from_data(data=cs_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                self.cart_status.append(event)

    def __parse_sde_customer_info(self, sde, engagement_id, engagement_sequence):
        if 'customerInfo' in sde and 'customerInfo' in sde['customerInfo']:
            ci_sde = sde['customerInfo']['customerInfo']
            ci_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            ci_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
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

            event = CustomerInfo.parse_from_data(data=ci_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
            self.customer_info.append(event)

    def __parse_sde_lead(self, sde, engagement_id, engagement_sequence):
        if 'lead' in sde and 'lead' in sde['lead']:
            lead_sde = sde['lead']['lead']
            lead_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            lead_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            lead_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            event = Lead.parse_from_data(data=lead_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
            self.lead.append(event)

    def __parse_sde_marketing_campaign_info(self, sde, engagement_id, engagement_sequence):
        if 'marketingCampaignInfo' in sde and 'marketingCampaignInfo' in sde['marketingCampaignInfo']:
            mci_sde = sde['marketingCampaignInfo']['marketingCampaignInfo']
            mci_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            mci_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            mci_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            event = MarketingCampaignInfo.parse_from_data(data=mci_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
            self.marketing_campaign_info.append(event)

    def __parse_sde_personal_info(self, sde, engagement_id, engagement_sequence):
        if 'personalInfo' in sde and 'personalInfo' in sde['personalInfo']:
            pi_sde = sde['personalInfo']['personalInfo']
            pi_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            pi_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            pi_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            pi_sde['customerAgeInYears'] = None
            pi_sde['customerDateOfBirth'] = None
            pi_sde['customerMonthOfBirth'] = None
            pi_sde['customerYearOfBirth'] = None

            if 'customerAge' in pi_sde and pi_sde['customerAge']:
                customer_age = pi_sde['customerAge']
                if 'customerAgeInYears' in customer_age:
                    pi_sde['customerAgeInYears'] = customer_age['customerAgeInYears']
                elif 'customerDateOfBirth' in customer_age:
                    pi_sde['customerDateOfBirth'] = customer_age['customerDateOfBirth']
                elif 'customerMonthOfBirth' in customer_age:
                    pi_sde['customerMonthOfBirth'] = customer_age['customerMonthOfBirth']
                elif 'customerYearOfBirth' in customer_age:
                    pi_sde['customerYearOfBirth'] = customer_age['customerYearOfBirth']

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
                        event = PersonalInfo.parse_from_data(data=pi_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                        self.personal_info.append(event)
            else:
                event = PersonalInfo.parse_from_data(data=pi_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                self.personal_info.append(event)

    def __parse_sde_purchase(self, sde, engagement_id, engagement_sequence):
        if 'purchase' in sde:
            p_sde = sde['purchase']
            p_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            p_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            p_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None
            p_sde['purchaseTotal'] = p_sde['total'] if 'total' in p_sde else None

            p_sde['numItems'] = None
            p_sde['total'] = None

            p_sde['productCategory'] = None
            p_sde['productName'] = None
            p_sde['productQuantity'] = None
            p_sde['productPrice'] = None
            p_sde['productSKU'] = None

            if 'cart' in p_sde:
                cart = p_sde['cart']

                if 'numItems' in cart:
                    p_sde['numItems'] = cart['numItems']
                if 'total' in cart:
                    p_sde['total'] = cart['total']

                if 'products' in cart and cart['products']:
                    for product in cart['products']:

                        if 'quantity' in product:
                            p_sde['productQuantity'] = product['quantity']

                        if 'product' in product:
                            prod_item = product['product']

                            if 'name' in prod_item:
                                p_sde['productName'] = prod_item['name']
                            if 'category' in prod_item:
                                p_sde['productCategory'] = prod_item['category']
                            if 'sku' in prod_item:
                                p_sde['productSKU'] = prod_item['sku']
                            if 'price' in prod_item:
                                p_sde['productPrice'] = prod_item['price']

                        event = Purchase.parse_from_data(data=p_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                        self.purchase.append(event)
                else:
                    event = Purchase.parse_from_data(data=p_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                    self.purchase.append(event)

    def __parse_sde_search_content(self, sde, engagement_id, engagement_sequence):
        if 'searchContent' in sde and 'keywords' in sde['searchContent']:
            keywords = sde['searchContent']['keywords']

            for keyword in keywords:
                sc_sde = dict(keyword=keyword)
                sc_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
                sc_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
                sc_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

                event = SearchContent.parse_from_data(data=sc_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                self.search_content.append(event)

    def __parse_sde_service_activity(self, sde, engagement_id, engagement_sequence):
        if 'serviceActivity' in sde and 'serviceActivity' in sde['serviceActivity']:
            se_sde = sde['serviceActivity']['serviceActivity']
            se_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            se_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            se_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            event = ServiceActivity.parse_from_data(data=se_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
            self.service_activity.append(event)

    def __parse_sde_visitor_error(self, sde, engagement_id, engagement_sequence):
        print(sde)

        if 'formFillingError' in sde and 'visitorError' in sde['formFillingError']:
            vi_sde = sde['formFillingError']['visitorError']
            vi_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            vi_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            vi_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            event = VisitorError.parse_from_data(data=vi_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
            self.visitor_error.append(event)

    def __parse_sde_viewed_product(self, sde, engagement_id, engagement_sequence):
        if 'viewedProduct' in sde:
            vp_sde = sde['viewedProduct']
            vp_sde['sdeType'] = sde['sdeType'] if 'sdeType' in sde else None
            vp_sde['isAuthenticated'] = sde['isAuthenticated'] if 'isAuthenticated' in sde else None
            vp_sde['serverTimeStamp'] = sde['serverTimeStamp'] if 'serverTimeStamp' in sde else None

            vp_sde['productCategory'] = None
            vp_sde['productName'] = None
            vp_sde['productQuantity'] = None
            vp_sde['productPrice'] = None
            vp_sde['productSKU'] = None

            if 'products' in vp_sde and vp_sde['products']:
                for product in vp_sde['products']:
                    if 'quantity' in product:
                        vp_sde['productQuantity'] = product['quantity']
                    if 'product' in product:
                        prod_item = product['product']

                        if 'name' in prod_item:
                            vp_sde['productName'] = prod_item['name']
                        if 'category' in prod_item:
                            vp_sde['productCategory'] = prod_item['category']
                        if 'sku' in prod_item:
                            vp_sde['productSKU'] = prod_item['sku']
                        if 'price' in prod_item:
                            vp_sde['productPrice'] = prod_item['price']

                    event = ViewedProduct.parse_from_data(data=vp_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                    self.viewed_product.append(event)
            else:
                event = ViewedProduct.parse_from_data(data=vp_sde, engagement_id=engagement_id, engagement_sequence=engagement_sequence)
                self.viewed_product.append(event)
