import json
# Tweets are stored in in file "fname". In the file used for this script, 
# each tweet was stored on one line
fname = '../data_aquaman/tweets.json'
with open(fname, 'r') as f:
    
    #Create dictionary to later be stored as JSON. All data will be included
    # in the list 'data'
    users_with_geodata = {
        "data": []
    }
    all_users = []
    total_tweets = 0
    geo_tweets  = 0
    for line in f:
        tweet = json.loads(line)
        if tweet['user']['id']:
            total_tweets += 1 
            user_id = tweet['user']['id']
            if user_id not in all_users:
                all_users.append(user_id)
                
                #Give users some data to find them by. User_id listed separately 
                # to make iterating this data later easier
                user_data = {}
                #Iterate through different types of geodata to get the variable primary_geo
                user_data["primary_geo"] = tweet['user']['location']
                #Add only tweets with some geo data to .json. Comment this if you want to include all tweets.
                if user_data["primary_geo"]:
                    users_with_geodata['data'].append(user_data)
                    geo_tweets += 1

# Save data to JSON file
with open('../data_aquaman/tweets_geo_extent.json', 'w') as fout:
    fout.write(json.dumps(users_with_geodata, indent=4))
