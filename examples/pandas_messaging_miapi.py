from datetime import datetime, timedelta
from lp_api_wrapper import UserLogin, MessagingInteractions
import pandas as pd

# For User Login
auth = UserLogin(account_id='1234', username='YOURUSERNAME', password='YOURPASSWORD')

# Create MI Connections
mi_conn = MessagingInteractions(auth=auth)

# Creates Epoch Time from 1 day ago. (If your volume is low, or none. Consider increasing days)
start_from = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)

# Creates Epoch Time right now.
start_to = int(datetime.now().timestamp() * 1000)

# Conversations from date range created above
body = {'start': {'from': start_from, 'to': start_to}}

# Get data!
conversations = mi_conn.all_conversations(body=body, debug=True, parse_data=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# All available Messaging Events into Pandas DataFrames #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Note:  These DFs will populate depending each account.  For example, some accounts do not
# !!!!   use cobrowse, therefore conversations.cobrowse_sessions will be empty.
# !!!!   Then, the cobrowse_session_df will be empty as well.

info_df = pd.DataFrame(conversations.info)
campaign_df = pd.DataFrame(conversations.campaign)
message_records_df = pd.DataFrame(conversations.message_records)
agent_participants_df = pd.DataFrame(conversations.agent_participants)
consumer_participants_df = pd.DataFrame(conversations.consumer_participants)
transfers_df = pd.DataFrame(conversations.transfers)
interactions_df = pd.DataFrame(conversations.interactions)
message_scores_df = pd.DataFrame(conversations.message_scores)
message_statuses_df = pd.DataFrame(conversations.message_statuses)
cobrowse_session_df = pd.DataFrame(conversations.cobrowse_sessions)
summary_df = pd.DataFrame(conversations.summary)
customer_info_df = pd.DataFrame(conversations.customer_info)
personal_info_df = pd.DataFrame(conversations.personal_info)
response_time_df = pd.DataFrame(conversations.responseTime)



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# Example showing all human agent transcripts #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

mr_with_agent_df = pd.merge(
    message_records_df,
    agent_participants_df,
    how='left',
    left_on=['conversationId', 'participantId'],
    right_on=['conversationId', 'agentId']
)

#  No BOT uprisings here!
mr_human_agents_df = mr_with_agent_df.loc[mr_with_agent_df['userTypeName'] == 'Human']
