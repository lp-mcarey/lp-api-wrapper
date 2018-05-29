from datetime import datetime, timedelta
from lp_api_wrapper import EngagementHistoryDB, UserLogin

# For User Login.
auth = UserLogin(account_id='1234', username='YOURUSERNAME', password='YOURPASSWORD')

# Initialize DB
eh_db = EngagementHistoryDB(auth=auth, db_name='chat.db')

# Create Body for EHAPI
start_from = int((datetime.now() - timedelta(days=.1)).timestamp() * 1000)
start_to = int(datetime.now().timestamp() * 1000)
body = {'start': {'from': start_from, 'to': start_to}}

# Load data into SQLite DB.
eh_db.load_data_into_db(body, debug=True)

sql = """
select * from info;
"""

# Execute SQL and store as a Pandas DF.
df = eh_db.to_df(sql)

# Export Results as csv
df.to_csv('info_chat.csv', index=False)

# Close DB and delete SQLite file.
eh_db.close_db(delete=True)
