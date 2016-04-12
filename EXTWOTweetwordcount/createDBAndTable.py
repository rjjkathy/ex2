import psycopg2 
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
 
 
# DB Tcount
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432") 
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) 
cur = conn.cursor() 
cur.execute("DROP DATABASE IF EXISTS Tcount") 
conn.commit() 
cur.execute("CREATE DATABASE Tcount") 
conn.commit() 
cur.close() 
conn.close() 
print '!!!!!!!!!!!!!!!!!!!!!TCount done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' 
 
 
# Table Tweetwordcount
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432") 
cur = conn.cursor() 
cur.execute('''CREATE TABLE Tweetwordcount 
        (word TEXT PRIMARY KEY     NOT NULL, 
        count INT     NOT NULL);''') 
conn.commit() 
conn.close() 
print '!!!!!!!!!!!!!!!!!!!!!Tweetwordcount table done!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!' 

