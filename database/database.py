import sqlite3

class DatabaseClass:
    _TABLE_NAME = "Tasks"
    _TABLE_COLUMNS = {
        "taskID":"VARCHAR(255) PRIMARY KEY",
        "taskEtag":"VARCHAR(255)",
        "taskTitle":"VARCHAR(255)",
        "taskStatus":"VARCHAR(255)",
        "timeUpdated":"DATETIME",
        "timeDue":"DATETIME",
        "timeCompleted":"DATETIME"}


    def __init__(self) -> None:
        _connection = None
        _cursor = None

    
    def Connect_to_Database(self): 
        try:
            self._connection = sqlite3.connect('tasks.db')
            self._cursor = self._connection.cursor()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
    

    def Close_Connection(self):
        self._connection.close()
    

    def _execute_sql_command(self, command:str):
        try:
            self._cursor.execute(command)
            self._connection.commit()
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Error Command:", command)


    def Create_Table(self):
        sql_create_table_command = "CREATE TABLE Tasks("
        for column_name,column_type in self._TABLE_COLUMNS.items():
            sql_create_table_command += "'" + column_name + "' " + column_type + ", "
        sql_create_table_command = sql_create_table_command[:-2] + ");"
        self._execute_sql_command(sql_create_table_command)


    def Delete_Table(self):
        sql_drop_table_command = "DROP TABLE Tasks"
        self._execute_sql_command(sql_drop_table_command)


    def Add_Record(self, taskID:str, taskEtag:str, taskTitle:str, taskStatus:str, timeUpdated:str, timeDue:str, timeCompleted:str):
        sql_add_record_command = "INSERT INTO Tasks VALUES ("
        sql_add_record_command += "'" + taskID + "', '" + taskEtag + "', '" + taskTitle + "', '" + taskStatus + "', '" + timeUpdated + "', "
        if timeDue:
            sql_add_record_command += "'" + timeDue + "', "
        else:
            sql_add_record_command += "NULL, "
        if timeCompleted:
            sql_add_record_command += "'" + timeCompleted + "');"
        else:
            sql_add_record_command += "NULL);"
        self._execute_sql_command(sql_add_record_command)


    def Update_Record(self, taskID:str, newtaskEtag:str, newtaskTitle:str, newtaskStatus:str, newtimeUpdated:str, newtimeDue:str, newTimeCompleted:str):
        sql_update_record_command = "UPDATE Tasks SET "
        if newtaskEtag != "":
            sql_update_record_command += "taskEtag = '" + newtaskEtag + "', "
        if newtaskTitle != "":
            sql_update_record_command += "taskTitle = '" + newtaskTitle + "', "
        if newtaskStatus != "":
            sql_update_record_command += "taskStatus = '" + newtaskStatus + "', "
        if newtimeUpdated != "":
            sql_update_record_command += "timeUpdated = '" + newtimeUpdated + "', "
        if newtimeDue != "":
            sql_update_record_command += "timeDue = '" + newtimeDue + "', "
        if newTimeCompleted != "":
            sql_update_record_command += "timeCompleted = '" + newTimeCompleted + "', "
        sql_update_record_command = sql_update_record_command[:-2] + " WHERE taskID = '" + taskID + "';"
        self._execute_sql_command(sql_update_record_command)


    def Delete_Record(self,taskID:int):
        sql_remove_record_command = "DELETE FROM Tasks WHERE taskID='" + taskID + "';"
        self._execute_sql_command(sql_remove_record_command)


    def Get_Records_All(self):
        sql_get_records_all_command = "SELECT * FROM Tasks"
        records = self._cursor.execute(sql_get_records_all_command).fetchall()
        for record in records:
            print(record)


    def Get_Records_Status(self, taskStatus:str):
        sql_get_Records_Status_command = "SELECT * FROM Tasks WHERE taskStatus='" + taskStatus +"';"
        records = self._cursor.execute(sql_get_Records_Status_command).fetchall()
        for record in records:
            print(record)