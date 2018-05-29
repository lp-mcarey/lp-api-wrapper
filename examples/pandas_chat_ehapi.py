from datetime import datetime, timedelta
from lp_api_wrapper import UserLogin, EngagementHistory
import pandas as pd

# For User Login.
auth = UserLogin(account_id='1234', username='YOURUSERNAME', password='YOURPASSWORD')

# Create EH Connection
eh_conn = EngagementHistory(auth=auth)

# Creates Epoch Time from 1 day ago. (If your volume is low, or none. Consider increasing days)
start_from = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)

# Creates Epoch Time right now.
start_to = int(datetime.now().timestamp() * 1000)

# Conversations from date range created above
body = {'start': {'from': start_from, 'to': start_to}}

# Get data!
engagements = eh_conn.all_engagements(body=body, debug=True, parse_data=True)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# All available Engagement Events into Pandas DataFrames #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# Note:  These DFs will populate depending each account.  For example, some accounts do not
# !!!!   use cobrowse, therefore engagements.cobrowse_sessions will be empty.
# !!!!   Then, the cobrowse_session_df will be empty as well.

campaign_df = pd.DataFrame(engagements.campaign)
cart_status_df = pd.DataFrame(engagements.cart_status)
cobrowse_sessions_df = pd.DataFrame(engagements.cobrowse_sessions)
customer_info_df = pd.DataFrame(engagements.customer_info)
info_df = pd.DataFrame(engagements.info)
lead_df = pd.DataFrame(engagements.lead)
line_scores_df = pd.DataFrame(engagements.line_scores)
marketing_campaign_info_df = pd.DataFrame(engagements.marketing_campaign_info)
personal_info_df = pd.DataFrame(engagements.personal_info)
purchase_df = pd.DataFrame(engagements.purchase)
search_content_df = pd.DataFrame(engagements.search_content)
service_activity_df = pd.DataFrame(engagements.service_activity)
surveys_df = pd.DataFrame(engagements.surveys)
transcript_df = pd.DataFrame(engagements.transcript)
viewed_product_df = pd.DataFrame(engagements.viewed_product)
visitor_error_df = pd.DataFrame(engagements.visitor_error)
visitor_info_df = pd.DataFrame(engagements.visitor_info)
