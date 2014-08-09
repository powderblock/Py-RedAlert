import feedparser

redditRSS = feedparser.parse('http://www.reddit.com/r/photoshopbattles/new/.rss')

print("New post. "+redditRSS['entries'][0]['title'])
