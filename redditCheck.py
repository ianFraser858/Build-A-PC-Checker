import praw
import re
from datetime import datetime, timedelta
from twilio.rest import Client


from local_settings import *


reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)
client = Client(twilio_sid, twilio_auth)
subreddit = reddit.subreddit('buildapcsales')
sought_gpu = ['1660ti', '1660TI', '2060', '2070', 'ASUS']

for submission in subreddit.new(limit=3):
    title = submission.title
    if(title[title.find('[')+1: title.find(']')]) == 'Monitor' \
            and any(entry in title for entry in sought_gpu)\
            and (datetime.utcnow() - datetime.utcfromtimestamp(submission.created_utc)).total_seconds() < 1800:
        print('hi Jacob')
        all_nums = re.findall(r"\d*\.\d+|\d+", title)
        filtered_nums = [entry for entry in all_nums if 300 < float(entry) < 450]
        if filtered_nums:
            client.messages.create(to=my_num,
                                   from_='+12056354084',
                                   body=title +
                                        '\n\n' +
                                        submission.url)

