"""
This example shows how to create a Messaging Interactions transcripts CSV flat file from the lp_api_wrapper library.
"""

from lp_api_wrapper import MessagingInteractions, UserLogin
from datetime import datetime, timedelta
import pandas as pd

# For User Login
auth = UserLogin(account_id='1234', username='YOURUSERNAME', password='YOURPASSWORD')

# Create MI Connections
mi_conn = MessagingInteractions(auth=auth, max_retry=3, wait_factor=15)

# Creates Epoch Time from 1 day ago. (If your volume is low, or none. Consider increasing days)
start_from = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)

# Creates Epoch Time right now.
start_to = int(datetime.now().timestamp() * 1000)

# Conversations from date range created above
body = {'start': {'from': start_from, 'to': start_to}}

# Get data!
conversations = mi_conn.all_conversations(body=body, debug=1, parse_data=True)

# Convert into Pandas DataFrame
df = pd.DataFrame(conversations.message_records)

# File path with file name.
file_path = './transcripts.csv'

# Export into CSV with no index column
df.to_csv(path_or_buf=file_path, index=False)

# Now you have a Transcripts Flat File!
