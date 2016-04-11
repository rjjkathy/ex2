#!/usr/bin/python  
import sys 
import psycopg2 
 
# connect to twitter feed database 
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost",port="5432") 
cur = conn.cursor() 
  
k1 = sys.argv[1]
k2 = sys.argv[2]

cur.execute("SELECT word, count FROM Tweetwordcount WHERE count >= %s AND count <= %s ORDER BY count DESC", (k1, k2)) 
records = cur.fetchall() 
for rec in records: 
   print rec[0], ": ", rec[1] 
conn.commit() 
conn.close() 
