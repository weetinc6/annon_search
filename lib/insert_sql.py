import mysql.connector
from config_sql import *



newsql_insert = """
INSERT INTO `a_search` (`sid`, `s_name`, `s_descript`, `s_favicon`, `s_link`) VALUE (NULL, %s, %s, %s, %s);
"""




sql_insert = mysql.connector.connect(**routesql_conn)

class SqlnewData:
    def __init__(self, s_name, s_descript, s_favicon, s_link) -> any:
        self.s_name = s_name
        self.s_descript = s_descript
        self.s_favicon = s_favicon
        self.s_link = s_link
        pass

    def sName(self) -> any:
        sName = self.s_name
        return sName
    
    def sDescript(self) -> any:
        sDes = self.s_descript
        return sDes
    
    def sFavicon(self) -> any:
        sFavicon = self.s_favicon
        return sFavicon
    
    def sLink(self) ->any:
        sLink = self.s_name
        return sLink




s_data = {
    "data_sinfo" : {
    "s_name" : "Google",
    "s_descript" : "Search the world largest info",
    "s_favicon" : "https://www.google.com",
    "s_link" : "https://www.google.com"

    }
}



s_name_t = s_data["data_sinfo"]["s_name"]
s_descript_t = s_data["data_sinfo"]["s_descript"]
s_favicon_t = s_data["data_sinfo"]["s_favicon"]
s_link_t = s_data["data_sinfo"]["s_link"]


dInsert_intosql = SqlnewData(s_name_t, s_descript_t, s_favicon_t, s_link_t)

SName = dInsert_intosql.sName()
SDes = dInsert_intosql.sDescript()
SFavicon = dInsert_intosql.sFavicon()
SLink = dInsert_intosql.sLink()

def executeData(SName, SDes, SFavicon, SLink) -> any:
    s_name_t = SName
    s_descript_t = SDes
    s_favicon_t = SFavicon
    s_link_t = SLink

    sql_insert_values = (s_name_t, s_descript_t, s_favicon_t, s_link_t)

    xcursor = sql_insert.cursor()
    xcursor.execute(newsql_insert, sql_insert_values)

    if xcursor:
        print("data added", end="\n")
    else:
        print("fail to add", end="\n")



executeData(s_name_t, s_descript_t, s_favicon_t, s_link_t)

sql_insert.close()






#print function not needed at the moment
#print(sql_insert_values, end="\n")

