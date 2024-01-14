import csv
import tweepy

twitter_Client_ID = 'b3Zfbi05T2hpZEl2ZkJ1VU1mX2M6MTpjaQ'

twitter_Client_Secret = 'dSnq2SmhHboTd-x1wrzpcGOcsKRMsoPp3EuRUR4jdn_4nSOvkK'

twitter_Consumer_Key = 'BtFWfrtfFKHUz9ZxjMjHIfolZ'

twitter_Consumer_Secret = 'ZjmiAtlnvxwSIYraVlE3YQ046zg1asFLoigD5MiasTNCO0Dws2'

twitter_Access_Token = '2249935225-rOZInLXuIlkk1lcDHaAX9KhekcNChnuBoRInAFm'

twitter_Token_Secret = '6i9rsCXbkUMMQR51TPviMqhD87VNNBaMaCjUes4HQeV2J'

twiter_API_Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAPFkrwEAAAAAH%2F5vVRRALtcr2BSZgB2%2BcokSIiE%3DHmGY0j2OsI7ZszkNyDfNKK0m1jl7dqZYh11dKxijgVllAymv1Q'

# Specify keywords related to cyberbullying, hate speech, racism, and sexism
search_keywords = ['cyberbullying', 'hate speech', 'racism', 'sexism']

# Specify the CSV file name to save the collected tweets
csv_file_name = 'index.csv'

api = tweepy.Client(
   bearer_token=twiter_API_Bearer_Token,
   consumer_key=twitter_Consumer_Key,
   consumer_secret=twitter_Consumer_Secret,
   access_token=twitter_Access_Token,
   access_token_secret=twitter_Token_Secret,
   wait_on_rate_limit=True
)

# open the file
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:

    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(['Text', 'Created_at', 'User_Screen_Name', 'User_Location'])

    # Search for tweets using specified keywords
    for keyword in search_keywords:
        # Iterate through the search results
        for tweet in tweepy.Cursor(api.search, q=keyword, lang='en', tweet_mode='extended').items(100):
            # Extract information from the tweet object
            text = tweet.full_text
            created_at = tweet.created_at
            user_screen_name = tweet.user.screen_name
            user_location = tweet.user.location

            # Write the row to the CSV file
            csv_writer.writerow([text, created_at, user_screen_name, user_location])

            # Print the information if needed
            print("Text:", text)
            print("Created_at:", created_at)
            print("User_Screen_Name:", user_screen_name)
            print("User_Location:", user_location)
            print("\n")

print(f'Tweets related to hate speech have been saved to {csv_file_name}')