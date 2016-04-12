#!/usr/bin/python  
import sys 
import psycopg2 

# Delete below 4 lines if log in fails, to diable historgram plotting as a workaround
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.plotly as py
py.sign_in('rjjkathy', 'oqlhnlo6d9')

# connect to twitter feed database 
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432") 
cur = conn.cursor() 
 
# if there is no specific word that we are looking for, get everything. Otherwise get that target word
if len(sys.argv) == 1: 
         cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY count DESC") 
         results = cur.fetchall() 
         for r in results: 
            print r[0], ",", r[1] 
         conn.commit() 
elif len(sys.argv) == 2:  
         word = sys.argv[1] 
         cur.execute("SELECT * FROM Tweetwordcount WHERE word = %s", [word]) 
         results = cur.fetchall() 
         for r in results: 
            print 'Total number of occurences of ', r[0],': ', r[1] 
         conn.commit() 
elif len(sys.argv) == 3:
         cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY count DESC LIMIT 20")
         results = cur.fetchall()
         xValues = []
         yValues = []

         for r in results:
            print r[0], ",", r[1]
            xValues.append(r[0])
            yValues.append(r[1])
         
		 # ====In case plot account login fails, delete the following chunk: data and py.plot
         data = [
              go.Bar(
                 x = xValues,
                 y = yValues,
              )
         ]
         plot_url = py.plot(data, filename='chart-histogram')
		 #=========================================================================
         conn.commit()

conn.close()
