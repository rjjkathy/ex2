#!/usr/bin/python  
import sys 
import psycopg2 

# connect to twitter feed database 
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432") 
cur = conn.cursor() 
 
# if there is no specific word that we are looking for, get everything. Otherwise get that target word
if len(sys.argv) == 1: 
         cur.execute("SELECT word, count FROM Tweetwordcount ORDER BY word") 
         results = cur.fetchall() 
         for r in results: 
            print r[0], ",", r[1] 
         conn.commit() 
else: 
         word = sys.argv[1] 
         cur.execute("SELECT * FROM Tweetwordcount WHERE word = %s", [word]) 
         results = cur.fetchall() 
         for r in results: 
            print 'Total number of occurences of ', r[0],': ', r[1] 
         conn.commit() 
 
conn.close() 
