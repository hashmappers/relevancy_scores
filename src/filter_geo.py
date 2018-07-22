import json
import re
# Tweets are stored in in file "fname". In the file used for this script, 
# each tweet was stored on one line
fname = '../data_aquaman/tweets.json'
with open(fname, 'r') as f:
    
    #Create dictionary to later be stored as JSON. All data will be included
    # in the list 'data'
    users_with_geodata = []
    all_users = []
    total_tweets = 0
    geo_tweets  = 0
    for line in f:  # read the input file line by line
        tweet = json.loads(line)  # load single tweet into tweet obj
        if tweet['user']['id']:  
            total_tweets += 1 
            user_id = tweet['user']['id']
            if user_id not in all_users:
                all_users.append(user_id)
                
                #Give users some data to find them by. User_id listed separately 
                # to make iterating this data later easier
                # user_data = {
                #     "text" : tweet['text'],
                # }
                filtering = tweet['text'] # can contain usless info like RT@jfdkslfjksld:
                fiiltering2 = re.sub('RT.*?:', '', filtering)
                filttering3 = re.sub('http.*', '', fiiltering2)
                users_with_geodata.append(filttering3)
# Save data to JSON file
with open('../data_aquaman/tweets_geo.json', 'w') as fout:
    fout.write(json.dumps(users_with_geodata, indent=4))
