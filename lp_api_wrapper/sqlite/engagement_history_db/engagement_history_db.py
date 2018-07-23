import concurrent.futures
import os
import pandas as pd
from lp_api_wrapper.apis import EngagementHistory
from lp_api_wrapper.parsers import Engagements
from lp_api_wrapper.sqlite.engagement_history_db import db_model as db


class EngagementHistoryDB:

    def __init__(self, auth, db_name=None):
        self.auth = auth
        self.db_name = db_name

        # Remove old DB file if it still exists.
        if os.path.isfile(db_name):
            os.remove(db_name)

        # Create DB and its tables.
        db.initialize_database(db_name)

    def load_data_into_db(self, body, max_workers=10, debug=0):
        """
        Fetches data from the Engagement History API using the body as its parameters.
        As offsets are retrieved, the data is parsed and inserted into their respective tables.

        :param body: dict
        :param max_workers: int
        :param debug: int (Status of API requets: 1=full, 2=summary, default=0)
        """

        # Create EHAPI connection.
        eh_conn = EngagementHistory(auth=self.auth)

        # Grab first offset of data.
        initial_data = eh_conn.engagements(body=body, offset=0)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # If there are no conversations in data range, return nothing.
        if count == 0:
            raise ValueError('[EH DB Status]: There are 0 records!')

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            # Create all future requests for the rest of the offsets in the body's data range.
            future_requests = {
                executor.submit(eh_conn.engagements, body, offset): offset for offset in range(0, count, 100)
            }

            for future in concurrent.futures.as_completed(future_requests):

                # Parse Engagements from Offset result.
                e = Engagements()
                e.append_records(records=[record for record in future.result()['interactionHistoryRecords']])

                # Insert Records into DB.
                self.__insert_engagement_records(engagements=e)

                if debug == 1:
                    start_rows = future_requests[future]
                    end_rows = future_requests[future] + 100
                    print('[EH DB Status]: Inserted {}-{} rows of {}'.format(start_rows, end_rows, count))

    @staticmethod
    def execute_sql(sql):
        """
        Execute SQL and return results as a tuple.

        :param sql: str
        :return: (results, column_names)
        """
        cursor = db.database_proxy.execute_sql(sql=sql)
        results = cursor.fetchall()
        column_names = list(map(lambda name: name[0], cursor.description))
        return results, column_names

    def to_df(self, sql):
        """
        Execute SQL and return results as a Pandas DataFrame.

        :param sql: str
        :return: pd.DataFrame()
        """
        results, column_names = self.execute_sql(sql=sql)
        return pd.DataFrame(results, columns=column_names)

    def close_db(self, delete=False):
        """
        Delete DB file after DB is closed.

        :param delete: bool
        """
        db.database_proxy.close()

        if delete:
            if os.path.isfile(self.db_name):
                os.remove(self.db_name)
                print('{} has been deleted!'.format(self.db_name))

    @staticmethod
    def __insert_engagement_records(engagements):
        """
        Inserts parsed Engagements into the SQLite table.

        :param engagements: Engagements()
        """

        # Campaign
        if engagements.campaign:
            db.Campaign.insert_many(
                rows=[tuple(row) for row in engagements.campaign],
                fields=db.campaign_fields
            ).execute()

        # CartStatus
        if engagements.cart_status:
            db.CartStatus.insert_many(
                rows=[tuple(row) for row in engagements.cart_status],
                fields=db.cart_status_fields
            ).execute()

        # CoBrowseSession
        if engagements.cobrowse_sessions:
            db.CoBrowseSession.insert_many(
                rows=[tuple(row) for row in engagements.cobrowse_sessions],
                fields=db.cobrowse_session_fields
            ).execute()

        # CustomerInfo
        if engagements.customer_info:
            db.CustomerInfo.insert_many(
                rows=[tuple(row) for row in engagements.customer_info],
                fields=db.customer_info_fields
            ).execute()

        # Info
        if engagements.info:
            db.Info.insert_many(
                rows=[tuple(row) for row in engagements.info],
                fields=db.info_fields
            ).execute()

        # Lead
        if engagements.lead:
            db.Lead.insert_many(
                rows=[tuple(row) for row in engagements.lead],
                fields=db.lead_fields
            ).execute()

        # LineScore
        if engagements.line_scores:
            db.LineScore.insert_many(
                rows=[tuple(row) for row in engagements.line_scores],
                fields=db.line_score_fields
            ).execute()

        # MarketingCampaignInfo
        if engagements.marketing_campaign_info:
            db.MarketingCampaignInfo.insert_many(
                rows=[tuple(row) for row in engagements.marketing_campaign_info],
                fields=db.marketing_campaign_info_fields
            ).execute()

        # PersonalInfo
        if engagements.personal_info:
            db.PersonalInfo.insert_many(
                rows=[tuple(row) for row in engagements.personal_info],
                fields=db.personal_info_fields
            ).execute()

        # Purchase
        if engagements.purchase:
            db.Purchase.insert_many(
                rows=[tuple(row) for row in engagements.purchase],
                fields=db.purchase_fields
            ).execute()

        # SearchContent
        if engagements.search_content:
            db.SearchContent.insert_many(
                rows=[tuple(row) for row in engagements.search_content],
                fields=db.search_content_fields
            ).execute()

        # ServiceActivity
        if engagements.service_activity:
            db.ServiceActivity.insert_many(
                rows=[tuple(row) for row in engagements.service_activity],
                fields=db.service_activity_fields
            ).execute()

        # Insert Survey
        if engagements.surveys:
            db.Survey.insert_many(
                rows=[tuple(row) for row in engagements.surveys],
                fields=db.survey_fields
            ).execute()

        # Transcript
        if engagements.transcript:
            db.Transcript.insert_many(
                rows=[tuple(row) for row in engagements.transcript],
                fields=db.transcript_fields
            ).execute()

        # ViewedProduct
        if engagements.viewed_product:
            db.ViewedProduct.insert_many(
                rows=[tuple(row) for row in engagements.viewed_product],
                fields=db.viewed_product_fields
            ).execute()

        # VisitorError
        if engagements.visitor_error:
            db.VisitorError.insert_many(
                rows=[tuple(row) for row in engagements.visitor_error],
                fields=db.visitor_error_fields
            ).execute()

        # VisitorInfo
        if engagements.visitor_info:
            db.VisitorInfo.insert_many(
                rows=[tuple(row) for row in engagements.visitor_info],
                fields=db.visitor_info_fields
            ).execute()
