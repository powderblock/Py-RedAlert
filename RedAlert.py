import feedparser, time

redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')

post = "New post. "+redditRSS['entries'][0]['title']+redditRSS.entries[0].published
while(1):
    time.sleep(30)
    redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')

    newPost = "New post. "+redditRSS['entries'][0]['title']+redditRSS.entries[0].published

    if post != newPost:
        print("New post!")
        post = newPost

    else:
        print("No new post.")
