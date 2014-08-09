print(">Setting up.")

import feedparser, time

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
        post = newPost

    else:
        print("No new post.")

    time.sleep(1)
