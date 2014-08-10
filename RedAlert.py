print(">Setting up.")

import feedparser, time, smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#Get user information from user:
account = str(raw_input("Enter Google Talk account username: (Example: username123) "))
password = str(raw_input("Enter Google Talk account password: (Example: abc123) "))

#Get number to text:
number = str(raw_input("Enter a number to text. (Example: 1234567890) "))

#Get SMS gateway:
gateway = str(raw_input("Enter SMS gateway domain. (AT&T: txt.att.net, T-Mobile: tmomail.net) "))

redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')
post = "New post. "+redditRSS['entries'][0]['title']+redditRSS.entries[0].published

print(">Entering main while loop.")
#Main loop.
while(1):
    print(">Loading RSS feed to parse.")
    #RSS feed to parse.
    redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')

    #Make a string out of some of the items in the RSS feed.
    newPost = "New post. "+redditRSS['entries'][0]['title']+' Time and Date posted: '+redditRSS.entries[0].published

    #Check if the post has changed since last loop.
    if post != newPost:
        print("New post!\n")
        print newPost
        #Send alert to phone.
        server.login(account+'@gmail.com', password)
        server.sendmail('', number+'@'+gateway, newPost)
        post = newPost

    else:
        print("No new post.")

    time.sleep(15)
