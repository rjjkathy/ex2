(ns EXTWOTweetwordcount 
2   (:use     [streamparse.specs]) 
3   (:gen-class)) 
4 
 
5 (defn EXTWOTweetwordcount [options] 
6    [ 
7     ;; spout configuration 
8     {"tweet-spout" (python-spout-spec 
9           options 
10           "spouts.tweets.Tweets" 
11           ["tweet"] 
12           :p 3 
13           ) 
14     } 
15     ;; bolt configuration 
16     {"parse-tweet-bolt" (python-bolt-spec 
17           options 
18           {"tweet-spout" :shuffle} 
19           "bolts.parse.ParseTweet" 
20           ["word"] 
21           :p 3 
22           ) 
23      "count-bolt" (python-bolt-spec 
24           options 
25           {"parse-tweet-bolt" ["word"]} 
26           "bolts.wordcount.WordCounter" 
27           ["word" "count"] 
28           :p 2 
29           ) 
30     } 
31   ] 
32 ) 
