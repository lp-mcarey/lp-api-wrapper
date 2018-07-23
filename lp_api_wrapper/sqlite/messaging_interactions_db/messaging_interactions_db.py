import concurrent.futures
import os
import pandas as pd
from lp_api_wrapper.apis import MessagingInteractions
from lp_api_wrapper.parsers import Conversations
from lp_api_wrapper.sqlite.messaging_interactions_db import db_model as db


class MessagingInteractionsDB:

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
        Fetches data from Messaging Interactions API using the body as its parameters.
        As offsets are retrieved, the data is parsed and inserted into their respective tables.

        :param body: dict
        :param max_workers: int
        :param debug: int (Status of API requets: 1=full, 2=summary, default=0)
        """

        # Create MIAPI connection.
        mi_conn = MessagingInteractions(auth=self.auth)

        # Grab first offset of data.
        initial_data = mi_conn.conversations(body=body, offset=0)

        # Number of conversations in date range that was selected in the body start parameters.
        count = initial_data['_metadata']['count']

        # If there are no conversations in data range, return nothing.
        if count == 0:
            raise ValueError('[MI DB Status]: There are 0 records!')

        # Multi-threading to handle multiple requests at a time.
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:

            # Create all future requests for the rest of the offsets in the body's data range.
            future_requests = {
                executor.submit(mi_conn.conversations, body, offset): offset for offset in range(0, count, 100)
            }

            for future in concurrent.futures.as_completed(future_requests):

                # Parse Conversations from Offset result.
                c = Conversations()
                c.append_records(records=[record for record in future.result()['conversationHistoryRecords']])

                # Insert Records into DB.
                self.__insert_conversation_records(conversations=c)

                if debug == 1:
                    start_rows = future_requests[future]
                    end_rows = future_requests[future] + 100
                    print('[MI DB Status]: Inserted {}-{} rows of {}'.format(start_rows, end_rows, count))

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
        Closes SQLite DB.  A delete option if available.

        :param delete: bool (Delete DB file after DB is closed.)
        """
        db.database_proxy.close()

        if delete:
            if os.path.isfile(self.db_name):
                os.remove(self.db_name)
                print('{} has been deleted!'.format(self.db_name))

    @staticmethod
    def __insert_conversation_records(conversations):
        """
        Inserts parsed Conversations into the SQLite table.

        :param conversations: Conversations()
        """

        # AgentParticipant
        if conversations.agent_participants:
            db.AgentParticipant.insert_many(
                rows=[tuple(row) for row in conversations.agent_participants],
                fields=db.agent_participant_fields
            ).execute()

        # Campaign
        if conversations.campaign:
            db.Campaign.insert_many(
                rows=[tuple(row) for row in conversations.campaign],
                fields=db.campaign_fields
            ).execute()

        # CoBrowseSession
        if conversations.cobrowse_sessions:
            db.CoBrowseSession.insert_many(
                rows=[tuple(row) for row in conversations.cobrowse_sessions],
                fields=db.cobrowse_session_fields
            ).execute()

        # ConsumerParticipant
        if conversations.consumer_participants:
            db.ConsumerParticipant.insert_many(
                rows=[tuple(row) for row in conversations.consumer_participants],
                fields=db.consumer_participant_fields
            ).execute()

        # ConversationSurvey
        if conversations.conversation_surveys:
            db.ConversationSurvey.insert_many(
                rows=[tuple(row) for row in conversations.conversation_surveys],
                fields=db.conversation_survey_fields
            ).execute()

        # CustomerInfo
        if conversations.customer_info:
            db.CustomerInfo.insert_many(
                rows=[tuple(row) for row in conversations.customer_info],
                fields=db.customer_info_fields
            ).execute()

        # Info
        if conversations.info:
            db.Info.insert_many(
                rows=[tuple(row) for row in conversations.info],
                fields=db.info_fields
            ).execute()

        # Interaction
        if conversations.interactions:
            db.Interaction.insert_many(
                rows=[tuple(row) for row in conversations.interactions],
                fields=db.interaction_fields
            ).execute()

        # MessageRecord
        if conversations.message_records:
            db.MessageRecord.insert_many(
                rows=[tuple(row) for row in conversations.message_records],
                fields=db.message_record_fields
            ).execute()

        # MessageScore
        if conversations.message_scores:
            db.MessageScore.insert_many(
                rows=[tuple(row) for row in conversations.message_scores],
                fields=db.message_score_fields
            ).execute()

        # MessageStatus
        if conversations.message_statuses:
            db.MessageStatus.insert_many(
                rows=[tuple(row) for row in conversations.message_statuses],
                fields=db.message_status_fields
            ).execute()

        # PersonalInfo
        if conversations.personal_info:
            db.PersonalInfo.insert_many(
                rows=[tuple(row) for row in conversations.personal_info],
                fields=db.personal_info_fields
            ).execute()

        # Summary
        if conversations.summary:
            db.Summary.insert_many(
                rows=[tuple(row) for row in conversations.summary],
                fields=db.summary_fields
            ).execute()

        # Transfer
        if conversations.transfers:
            db.Transfer.insert_many(
                rows=[tuple(row) for row in conversations.transfers],
                fields=db.transfer_fields
            ).execute()
