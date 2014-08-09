import feedparser, time

#Main loop.
while(1):
    #RSS feed to parse.
    redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')

    #Make a string out of some of the items in the RSS feed.
    newPost = "New post. "+redditRSS['entries'][0]['title']+redditRSS.entries[0].published

    #Check if the post has changed since last loop.
    if post != newPost:
        print("New post!")
        post = newPost

    else:
        print("No new post.")

    time.sleep(30)
