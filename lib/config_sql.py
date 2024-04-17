import mysql.connector


class ConnectMyDB:
    def __init__ (self, host, user, password, database, port) -> any:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        pass


    def hostname(self) -> any:
        return self.host
    
    def hostuser(self) -> any:
        return self.user
    
    def hostpassword(self) -> any:
        return self.password
    
    def hostdatabase(self) -> any:
        return self.database
    
    def hostport(self) -> any:
        return self.port
    
routesql = {"host" : "127.0.0.1",
            "user" : "root",
            "password" : "",
            "database" : "annon",
            "port" : "3306"
            }



host = routesql["host"]
user = routesql["user"]
password = routesql["password"]
db_name = routesql["database"]
port_num = routesql["port"]



sql_con = ConnectMyDB(host, user, password, db_name, port_num)
host = sql_con.hostname()
user = sql_con.hostuser()
pass_word = sql_con.hostpassword()
dbName = sql_con.hostdatabase()
port = sql_con.hostport()



routesql_conn = {"host" : host,
            "user" : user,
            "password" : pass_word,
            "database" : dbName,
            "port" : port
            }


sql_config = mysql.connector.connect(**routesql_conn)

query = """
        SELECT * FROM `a_search`;
"""

if sql_config:
    #connected
    con_sql = sql_config.cursor()
    con_sql.execute(query)
    #print("connected", end="\n")
    sql_config.close()
else:
    #from mysql.connector import mysql_error
    print("Error")
