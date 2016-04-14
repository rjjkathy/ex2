Steps to run this project:

1. run: sparse quickstart EX2Tweetwordcount and update files with the ones in this Git Repo ( API credentials contained in tweets.py)

2. create db and table 

mount /dev/xvdf /data
cd /data
./start_postgres.sh 

cd ~
cd EX2Tweetwordcount
python createDAAndTable.py

3. under EX2Tweetwordcount run: sparse run

# wait for a while for data to be collected

4. for getting all info: python finalresults.py
   for getting info regarding on word : python finalresults.py <inputword>
   for getting top 20 results: python finalresults.py arg1 arg2 # just give 2 args, will trigger top 20 selection

   NOTE: Inside the two args mode for getting top 20 entries, there is python plotly library signed in using my credentials. Login credentials imported, should work for running elsewhere. However, in case it does not login, disbale the plot part, and refer to the histogram diagram in git or here https://plot.ly/~rjjkathy/0

5. python python histogram.py <lowlimit> <upperlimit>

NOTE: if re-running sparse run, need to call createDBAndTable.py again to reset table, otherwise sparse local count will be out of sync with table counts
