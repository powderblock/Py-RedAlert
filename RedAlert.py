import feedparser, time, smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

#Get user information from user:
account = str(raw_input("Enter Google Talk account username: (Example: username123) "))
password = str(raw_input("Enter Google Talk account password: (Example: abc123) "))
print(">Successfully logged in.")
server.login(account+'@gmail.com', password)

#Get number to text:
number = str(raw_input("Enter a number to text. (Example: 1234567890) "))

#Get SMS gateway:
gateway = str(raw_input("Enter SMS gateway domain. (AT&T: txt.att.net, T-Mobile: tmomail.net) "))

mail = number+'@'+gateway

def updateRSS():
    global redditRSS, date, title
    redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')
    title = redditRSS['entries'][0]['title']
    date = redditRSS.entries[0].published

updateRSS()
post = title+' Time and Date posted: '+date


#Main loop.
while(1):
    server.login(account+'@gmail.com', password)
    print(">Loading RSS feed to parse.")
    #RSS feed to parse.
    updateRSS()

    #Make a string out of some of the items in the RSS feed.
    newPost = title+' Time and Date posted: '+date

    #Check if the post has changed since last loop.
    if post != newPost:
        print("New post!\n")
        print newPost
        #Send alert to phone.
        server.sendmail('', mail, newPost)
        post = newPost

    else:
        print("No new post.")

    time.sleep(15)
