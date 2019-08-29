import praw
import re
from twilio.rest import Client


from local_settings import *


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)
client = Client(twilio_sid, twilio_auth)
subreddit = reddit.subreddit('buildapcsales')
sought_gpu = ['2070', '2060', '2080']

for submission in subreddit.hot(limit=5):
    title = submission.title
    if(title[title.find('[')+1: title.find(']')]) == 'GPU' and any(entry in title for entry in sought_gpu):
        all_nums = re.findall(r"\d*\.\d+|\d+", title)
        filtered_nums = [entry for entry in all_nums if 250 < float(entry) < 450]
        if filtered_nums:
            client.messages.create(to=my_num,
                                   from_='+12056354084',
                                   body=title +
                                        '\n\n' +
                                        submission.url)

