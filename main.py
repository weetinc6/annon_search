from flask import *
from lib.config_sql import *
from bs4 import *
import time
import mysql.connector


import os
trackerID = "4000034345u3tu4rifi45i33495858385930-flr53i4tyu6tu"

tracker_status = trackerID #os.environ(trackerID)



class Trackers:
    def __init__(self, trackerID, trackerName, trackerSource) -> any:
        self.trackerID = trackerID
        self.trackerName = trackerName
        self.trackerSource = trackerSource
        pass


    def trackerID(self) -> any:
        return self.trackerID
    
    def trackerName(self) -> any:
        return self.trackerName

    def trackerSource(self) -> any:
        return self.trackerSource



#test trackers
    
tracker_set = {
    "trackerID" : "Chrome",
    "trackerVersion" : "2.0.1",
    "trackerSource" : "google-chrome-browser"
    }


#test data tokens
    
tracker_id = tracker_set["trackerID"]
tracker_name = tracker_set["trackerSource"]
tracker_so = tracker_set["trackerSource"]

#annon_main header title

title = "Annon search | Annonmyous Search"
    
def trackers_tokens(tid, tname, tsource) -> any:
    tid = tid
    tname = tname
    tsource = tsource


if tracker_status:
     tracker_status #true
else:
    print("tracker is false")

annon_search = Flask(__name__)
@annon_search.route("/", methods={"GET", "POST"})
def main() -> any:
    anon_signature = '''

    / -------]          [ ****ANNON""""      
    /        ]          [ ****ANONYMOUS*****      
    /        ]          [
    /          --------- 
    -------------------------------
    '''
    if request.method == "GET":
        title = "Annon search | Annonmyous Search"
        q = request.args.get("q")
        if q!= q:
            #add nothing to the box
            q = ""
        else:
            q = q

        print("testing tokens")
        time.sleep(3)
        ip = request.remote_addr
        print(trackers_tokens(tid=tracker_id, tname=tracker_name, tsource=tracker_so))
        time.sleep(3)
        print("trackers waiting to block external sites from chrome")
        trackers = 1 #set to ON
        print("You are now anonymous", end="\n")
        print(":-)", end="\n")
        ip = "21.0.1.0.1"
        print(anon_signature, end="\n")
        return render_template("start-page.html",anon_search = 
                               title, q = q, annon_ip = ip)



@annon_search.route("/search", methods={"GET", "POST"})
def search_page() -> any:
    anon_signature = '''

    / -------]          [ ****ANNON""""      
    /        ]          [ ****ANONYMOUS*****      
    /        ]          [
    /          --------- 
    -------------------------------
    '''



    if request.method == "GET":
        title = "Annon search | Annonmyous Search"
        q = request.args.get("q")

        #result from the database
    
        scon = mysql.connector.connect(**routesql_conn)
        xc = scon.cursor()
        key_words = (q)
        s_sql = xc.execute("SELECT * FROM `a_search` WHERE `s_name` LIKE '%"+q+"%'")
        row = xc.fetchall()
       
        scon.close()
        




        #masking your ip to annon ip
        ip = request.remote_addr
        browser_status = request.user_agent
        ip = request.remote_addr
        time.sleep(3)
        print("Disabling based on what i got: ", browser_status, end="\n")
        time.sleep(3)
        print("Done...lets! roll", end="\n")
        if ip == ip and browser_status == browser_status:
            ip = "20.134.54.6"
            browser_status = "OFF" #trackers are now off
            print("You are now anonymous", end="\n")
            time.sleep(3)
            print(":-)", end="\n")
            print(anon_signature, end="\n")
            return render_template("search.html", title = title, q = q, ip = ip, 
                                   browser_status = browser_status, row = row)
        else:
            print("fail to mask you...", end="\n")



annon_search.run(debug=True)

if __name__ == "__main__":
    main()
