# Database Branch

The database.py file uses sqlite3. The jsonParser file pareses a sample json file and adds all the records into the database.

## How to use database 

```python
from database import DatabaseClass

db = DatabaseClass()
db.Connect_to_Database()

# WORK

db.Close_Connection()
```

## API Functions
**Connect_to_Database()**  
Initialise variables and connect to the database.

**Close_Connection()**  
Close connection to the database.

**Create_Table()**  
Creates table 'Tasks'

**Delete_Table()**  
Deletes table 'Tasks'.

**Add_Record(taskID:str, taskEtag:str, taskTitle:str, taskStatus:str, timeUpdated:str, timeDue:str, timeCompleted:str)**  
Adds new record into table 'Tasks'. taskID is primary key. All parameters need to be formatted as sql values.

**Update_Record(taskID:str, newtaskEtag:str, newtaskTitle:str, newtaskStatus:str, newtimeUpdated:str, newtimeDue:str, newTimeCompleted:str)**  
Updates an existing record identified via taskID. Leave a parameter as "" if it doesn't have to be changed.

**Delete_Record(taskID:str)**  
Deletes a record identified via taskID.

**Get_Records_All()**  
Returns a list of all records. Each record is a tuple.

**Get_Record_ID(taskID:int)**  
Returns a record with same taskID as provided. Record is a tuple.

**Get_Records_Status(taskStatus:str)**  
Returns a list of all records with the same taskStatus as provided. Each record is a tuple.

## Non-API Functions and Variables

**_execute_sql_command(command:str)**  
Executes sql queries.

**_TABLE_NAME and _TABLE_COLUMNS**  
Table name and dictionary of table columns with their sql type. 