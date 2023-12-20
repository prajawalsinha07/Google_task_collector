import sqlite3

TABLE_NAME = "Tasks"
TABLE_COLUMNS = {
    "taskID":"INTEGER PRIMARY KEY",
    "taskSource":"VARCHAR(255)",
    "taskDescription":"VARCHAR(255)",
    "taskState":"VARCHAR(255)",
    "timeAcquired":"DATE",
    "timeCompleted":"DATE"}

connection = sqlite3.connect('tasks.db')

cursor = connection.cursor()

def Execute_sql_command(command:str):
    try:
        cursor.execute(command)
        connection.commit()
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))

def Create_Table():
    sql_create_table_command = "CREATE TABLE Tasks("
    for column_name,column_type in TABLE_COLUMNS.items():
        sql_create_table_command += column_name + " " + column_type + ", "
    sql_create_table_command = sql_create_table_command[:-2] + ");"
    Execute_sql_command(sql_create_table_command)
    #print(sql_create_table_command)

def Delete_Table():
    sql_drop_table_command = "DROP TABLE Tasks"
    Execute_sql_command(sql_drop_table_command)
    #print(sql_drop_table_command)

def Add_Record(taskID:int, taskSource:str, taskDescription:str, taskState:str, timeAcquired:str, timeCompleted:str):
    sql_add_record_command = "INSERT INTO Tasks VALUES ("
    sql_add_record_command += str(taskID) + ', "' + taskSource + '", "' + taskDescription + '", "' + taskState + '", "' + timeAcquired 
    if timeCompleted:
       sql_add_record_command += '", "' + timeCompleted + '");'
    else:
        sql_add_record_command += '", NULL);'
    Execute_sql_command(sql_add_record_command)
    #print(sql_add_record_command)

def Delete_Record(taskID:int):
    sql_remove_record_command = "DELETE FROM Tasks WHERE taskID=" + str(taskID) + ";"
    Execute_sql_command(sql_remove_record_command)
    #print(sql_remove_record_command)

def Get_Records_All():
    sql_get_records_all_command = "SELECT * FROM Tasks"
    records = cursor.execute(sql_get_records_all_command).fetchall()
    for record in records:
        print(record)
    #print(sql_get_records_all_command)

def Get_Records_State(taskState:str):
    sql_get_records_state_command = "SELECT * FROM Tasks WHERE taskState='" + taskState +"';"
    records = cursor.execute(sql_get_records_state_command).fetchall()
    for record in records:
        print(record)
    #print(sql_get_records_state_command)

if(len(cursor.execute("SELECT name FROM sqlite_schema WHERE type='table' AND name='Tasks';").fetchall())<1):
    Create_Table()

# TEMP TESTING CODE
Add_Record(1,"Google Docs","Reply to comment","Pending","2023-12-17","")
Add_Record(2,"Google Drive","Edit comment","Completed","2023-12-17","2023-12-19")
Add_Record(3,"Google Docs","Reply to comment","Pending","2023-12-17","")
Add_Record(4,"Google Drive","Edit comment","Completed","2023-12-17","2023-12-19")
Get_Records_All()
print("")
Get_Records_State("Completed")
print("")
Delete_Record(3)
Delete_Record(4)
Get_Records_All()

connection.close()