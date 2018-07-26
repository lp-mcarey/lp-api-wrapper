# lp_api_wrapper: Unofficial LivePerson API Python Wrapper
[![PyPI version](https://badge.fury.io/py/lp_api_wrapper.svg)](https://badge.fury.io/py/lp_api_wrapper)
![Python version](https://img.shields.io/badge/python-3.4%2B-blue.svg)

lp_api_wrapper is a native Python library to interface with LivePerson's APIs.
All methods will return decoded JSON in native Python data structures.

The following APIs are supported:
* Messaging Interactions API
    * conversations - _1 offset of data in start date range_
    * all_conversations - _All offsets of data in start date range_
    * get_conversation_by_conversation_id
    * get_conversations_by_consumer_id
* Engagement History API
    * engagements - _1 offset of data in start date range_
    * all_engagements - _All offsets of data in start date range_
* Agent Metrics API
    * agent_status
    * summary
* Messaging Operations API
    * messaging_conversation
    * messaging_current_queue_health
    * messaging_queue_health
    * messaging_csat_distribution
* Operational Realtime API
    * queue_health
    * engagement_activity
    * agent_activity
    * current_queue_state
    * sla_histogram
* Predefined Content API
    * get_predefined_content_items
* Predefined Categories API
    * categories_list

## Installation
```bash
$ pip install --upgrade lp_api_wrapper
```

## Import lp_api_wrapper
```python
# For Messaging Interactions API
from lp_api_wrapper import MessagingInteractions

# For Engagement History API
from lp_api_wrapper import EngagementHistory

# For Agent Metrics API
from lp_api_wrapper import AgentMetrics

# For Messaging Operations API
from lp_api_wrapper import MessagingOperations

# For Operational Realtime API
from lp_api_wrapper import OperationalRealtime

# For Predefined Content API
from lp_api_wrapper import PredefinedContent

# For Predefined Categories API
from lp_api_wrapper import PredefinedCategories
```

## Login/Authentication
Each class in lp_api_wrapper accepts user login or oauth1 authentication.

Login via the Login Service API:
https://developers.liveperson.com/login-getting-started.html

```python
from lp_api_wrapper import UserLogin

auth = UserLogin(
    account_id='1234', 
    username='YOURUSERNAME', 
    password='YOURPASSWORD'
)
```

Or, login using OAuth1 authentication
```python
from lp_api_wrapper import OAuthLogin

auth = OAuthLogin(
    account_id='1234', 
    app_key='APP_KEY', 
    app_secret='APP_SECRET', 
    access_token='ACCESS_TOKEN', 
    access_token_secret='ACCESS_TOKEN_SECRET'
)
```

## Messaging Interactions API
Create Messaging Interactions Connection
```python
from lp_api_wrapper import MessagingInteractions
mi_conn = MessagingInteractions(auth=auth)
```

#### 1. Conversations
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-conversations.html

Note!
* Will return 1 offset of data.

Arguments:

* body: dict (Note: Check reference for details.)
* offset: int (Default: 0)
* limit: int (Default: 100)
* sort: str (Default: None)

```python
body = {'start': {'from': 1491004800000, 'to': 1491091199000}}
data = mi_conn.conversations(body)
```

#### 2. All Conversations
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-conversations.html

Note!
* Will return all offsets of data as a list of conversations.

Arguments:
* body: dict (Note: Check reference for details.)
* max_workers: int (Max number of API requests at a time. Default:7)
* debug: int (Status of API requests: 1=full, 2=summary, default=0)
* parse_data: bool (Parses data and returns a Conversations data object. Default: False)

```python
body = {'start': {'from': 1491004800000, 'to': 1491091199000}}
data = mi_conn.all_conversations(body)
```

#### 2. Get conversation by conversation id
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-get-conversation-by-conversation-id.html

Arguments:
* conversation_id: str

```python
data = mi_conn.get_conversation_by_conversation_id(conversation_id='1234abc')
```

#### 3. Get conversation by consumer id
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-get-conversations-by-consumer-id.html

Arguments:
* consumer_id: str

```python
data = mi_conn.get_conversations_by_consumer_id(consumer_id='1234abc')
```

## Engagement History API
Create Engagement History Connection.
```python
from lp_api_wrapper import EngagementHistory
mi_conn = EngagementHistory(auth=auth)
```

#### 1. Engagements
Documentation:
* https://developers.liveperson.com/data-engagement-history-methods.html

Note!
* Will return 1 offset of data.

Arguments:

* body: dict (Note: Check reference for details.)
* offset: int (Default: 0)
* limit: int (Default: 100)
* sort: str (Default: None)

```python
body = {'start': {'from': 1491004800000, 'to': 1491091199000}}
data = eh_conn.engagements(body)
```

#### 2. All Engagements
Documentation:
* https://developers.liveperson.com/data-engagement-history-methods.html

Note!
* Will return all offsets of data as a list of engagements.

Arguments:
* body: dict (Note: Check reference for details.)
* max_workers: int (Max number of API requests at a time. Default:7)
* debug: int (Status of API requests: 1=full, 2=summary, default=0)
* parse_data: bool (Parses data and returns an Engagements data object. Default: False)

```python
body = {'start': {'from': 1491004800000, 'to': 1491091199000}}
data = eh_conn.all_engagements(body)
```


## Agent Metrics API
Create Agent Metrics Connection.
```python
from lp_api_wrapper import AgentMetrics
am_conn = AgentMetrics(auth=auth)
```

#### 1. Agent Status
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-methods-agent-status.html

Note!
* If all are left blank, this method will return all agents' status for the account.

Arguments:
* status: List[str] (Default: None)
* agent_ids: List[str] (Default: None)
* skill_ids: List[str] (Default: None)
* agent_group_ids: List[str] (Default: None)
* agent_presence: bool (Default: None)
* connection_states: List[str] (Default: None)

```python
data = am_conn.agent_status(skill_ids=['1234', '5678'])
```


#### 2. Summary
Documentation:
* https://developers.liveperson.com/data-messaging-interactions-methods-summary.html

Note!
* If all are left blank, this method will return the status for the account.

Arguments:
* status: List[str] (Default: None)
* agent_ids: List[str] (Default: None)
* skill_ids: List[str] (Default: None)
* agent_group_ids: List[str] (Default: None)

```python
data = am_conn.summary()
```


## Messaging Operations API
Create Messaging Operations Connection.
```python
from lp_api_wrapper import MessagingOperations
mo_conn = MessagingOperations(auth=auth)
```

#### 1. Messaging Conversation
Documentation:
* https://developers.liveperson.com/data-messaging-operations-messaging-conversation.html

Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* agent_ids: str (Default: None)
* interval: int (Default: None)
* version: int (Default: 1)

```python
data = mo_conn.messaging_conversation(time_frame=1440)
```

#### 2. Messaging Current Queue Health
Documentation
* https://developers.liveperson.com/data-messaging-operations-messaging-current-queue-health.html

Arguments:
* skill_ids: str (Default: None)
* version: int (Default: 1)

```python
data = mo_conn.messaging_current_queue_health()
```

#### 3. Messaging Queue Health
Documentation
* https://developers.liveperson.com/data-messaging-operations-messaging-queue-health.html

Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* interval: int (Default: None)
* version: int (Default: 1)

```python
data = mo_conn.messaging_queue_health()
```


#### 4. Messaging CSAT Distribution
Documentation
* https://developers.liveperson.com/data-messaging-operations-messaging-csat-distribution.html

Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* agent_ids: str (Default: None)
* version: int (Default: 1)

```python
data = mo_conn.messaging_csat_distribution(time_frame=1440)
```


#### 5. Messaging Estimated Wait Time
Documentation
* https://developers.liveperson.com/data-messaging-operations-messaging-estimated-wait-time.html

Arguments:
* skill_ids: str (Default: None)
* version: int (Default: 1)

```python
data = mo_conn.messaging_estimated_wait_time()
```

## Operational Realtime API
Create Operational Realtime Connection.
```python
from lp_api_wrapper import OperationalRealtime
or_conn = OperationalRealtime(auth=auth)
```

#### 1. Queue Health
Documentation:
* https://developers.liveperson.com/data-operational-realtime-queue-health.html


Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* interval: int (Default: None)
* version: int (Default: 1)

```python
data = or_conn.queue_health(time_frame=1440)
```

#### 2. Engagement Activity
Documentation:
* https://developers.liveperson.com/data-operational-realtime-engagement-activity.html

Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* agent_ids: str (Default: None)
* interval: int (Default: None)
* version: int (Default: 1)

```python
data = or_conn.engagement_activity(time_frame=1440)
```

#### 3. Agent Activity
Documentation:
* https://developers.liveperson.com/data-operational-realtime-agent-activity.html

Arguments:
* time_frame: int
* agent_ids: str
* interval: int (Default: None)
* version: int (Default: 1)

```python
data = or_conn.agent_activity(time_frame=1440, agent_ids='123, 456')
```

#### 4. Current Queue State
Documentation:
* https://developers.liveperson.com/data-operational-realtime-current-queue-state.html

Arguments:
* skill_ids: str (Default: None)
* version: int (Default: 1)

```python
data = or_conn.current_queue_state()
```

#### 5. SLA Histogram
Documentation:
* https://developers.liveperson.com/data-operational-realtime-sla-histogram.html

Arguments:
* time_frame: int
* skill_ids: str (Default: None)
* group_ids: str (Default: None)
* histogram: str (Default: None)
* version: int (Default: 1)

```python
data = or_conn.sla_histogram(time_frame=1440)
```

## Predefined Content API
Create Predefined Content Connection.
```python
from lp_api_wrapper import PredefinedContent
pdc_conn = PredefinedContent(auth=auth)
```

#### 1. Get Predefined Content Items
Documentation:
* https://developers.liveperson.com/account-configuration-predefined-content-get-items.html

Arguments:
* include_deleted: bool (Default: None)
* sanitize_data: bool (Default: None)
* lang: str (Default: None)
* select: str (Default: None)
* group_by: str (Default: None)
* skill_ids: str (Default: None)
* ids: str (Default: None)
* version: float (Default: 2.0)

```python
data = pdc_conn.get_predefined_content_items()
```

## Predefined Categories API
Create Predefined Categories Connection.
```python
from lp_api_wrapper import PredefinedCategories
pdc_conn = PredefinedCategories(auth=auth)
```

#### 1. Categories List
Documentation:
* https://developers.liveperson.com/account-configuration-predefined-list.html

Arguments:
* select: str (Default: None)
* include_deleted: bool (Default: None) 
* version: float (Default: 2.0)

```python
data = pdc_conn.categories_list()