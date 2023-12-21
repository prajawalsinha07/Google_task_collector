import pandas as pd
from google_service import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = './client_secret_789795652787-f45gsk2bv6ft896v92fjito7g0h0okv6.apps.googleusercontent.com.json'
API_NAME = 'tasks'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/tasks']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""
Tasks Demo: Restaurants To Try:
    San Francisco
        - Pearl San Francisco
        - Burma Superstar
        - House of Prime Rib
    Chicago
    New York

"""

"""
Insert method
"""
tasklistRestaurants = service.tasklists().insert(
    body={'title': 'Restaurants to try'}
).execute()

for i in range(100):
    service.tasklists().insert(body={'title': 'Tasklst #{0}'.format(i+1)}).execute()


"""
List Method
"""
response = service.tasklists().list().execute()
lstItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.tasklists().list(
        maxResults=30,
        pageToken=nextPageToken
    ).execute()
    lstItems.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

print(pd.DataFrame(lstItems).head())

# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 500)
# pd.set_option('display.min_rows', 500)
# pd.set_option('display.max_colwidth', 150)
# pd.set_option('display.width', 120)
# pd.set_option('expand_frame_repr', True)

"""
Delete Method
"""
for item in lstItems:
    try:
        if isinstance(int(item.get('title').replace('Tasklst #', '')), int):
            if int(item.get('title').replace('Tasklst #', '')) > 50:
                # print(int(item.get('title').replace('Tasklst #', '')))
                service.tasklists().delete(tasklist=item.get('id')).execute()
    except:
        pass

response = service.tasklists().list(maxResults=100).execute()
print(pd.DataFrame(response.get('items')))


"""
Update Method
"""
mainTasklist = response.get('items')[1]
mainTasklist['title'] = 'Restaurants to eat'
service.tasklists().update(tasklist=mainTasklist['id'], body=mainTasklist).execute()

"""
Get Method
"""
print(service.tasklists().get(tasklist='ejl0Yjl5RWZ4cmI1Sk1oeg').execute())
