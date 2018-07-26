from datetime import datetime, timedelta
from lp_api_wrapper import MessagingInteractionsDB, UserLogin

# For User Login.
auth = UserLogin(account_id='1234', username='YOURUSERNAME', password='YOURPASSWORD')

# Initialize DB
mi_db = MessagingInteractionsDB(auth=auth, db_name='messaging.db')

# Create Body for MIAPI
start_from = int((datetime.now() - timedelta(days=.1)).timestamp() * 1000)
start_to = int(datetime.now().timestamp() * 1000)
body = {'start': {'from': start_from, 'to': start_to}}

# Load data into SQLite DB.
mi_db.load_data_into_db(body, debug=1)

sql = """
select * from info;
"""

# Execute SQL and store as a Pandas DF.
df = mi_db.to_df(sql)

# Export Results as csv
df.to_csv('info_messaging.csv', index=False)

# Close DB and delete SQLite file.
mi_db.close_db(delete=True)
