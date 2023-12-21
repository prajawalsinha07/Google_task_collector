import json
from database import DatabaseClass
import os

here = os.path.dirname(os.path.abspath(__file__))
db_filename = os.path.join(here, 'jsonOutput')

f = open(db_filename)

data = json.load(f)
db = DatabaseClass()
db.Connect_to_Database()
db.Create_Table()

for i in data["items"]:
    taskID = i["id"]
    taskEtag = i["etag"]
    taskTitle = i["title"]
    taskStatus = i["status"]
    taskUpdated = i["updated"][:-5]
    if "due" in i.keys():
        taskDue = i["due"][:-5]
    else:
        taskDue = None
    if "completed" in i.keys():
        taskCompleted = i["completed"][:-5]
    else:
        taskCompleted = None
    
    db.Add_Record(taskID, taskEtag, taskTitle, taskStatus, taskUpdated, taskDue, taskCompleted)

db.Close_Connection()
f.close()