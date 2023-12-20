from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/tasks']
SERVICE_ACCOUNT_FILE = './dynamic-concept-408619-1888901776bc.json'

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)