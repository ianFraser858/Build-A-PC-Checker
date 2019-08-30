# r/buildapcsales GPU check
 
 Uses [PRAW](https://praw.readthedocs.io/en/latest/) to scrap the newest 3 posts from [r/buildapcsales](https://www.reddit.com/r/buildapcsales/), look for any that are for a 2060, 2070, or 2080 and then take a guess as the price. 
 
 The script will text my number if the price looks like it falls within a certain range using [Twilio](https://www.twilio.com/).
 
 I have the script set up on an VPS to run through a cron job every 30 minutes. 
 
 To use you'll need
 - PRAW client ID and client secret
 - twilio ID and twilio secret
