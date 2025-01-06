# 配置
import feedparser

# RSS feed的URL
rss_url = "https://hellogithub.com/rss"

# 解析RSS feed
feed = feedparser.parse(rss_url)

# 输出RSS feed的标题

# 遍历每一篇文章
for entry in feed.entries:
    print("\n")
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published: {entry.published}")
    print(f"Summary: {entry.get('summary', 'No summary available')}")

print("\n")
print(f"Feed Title: {feed.feed.title}")
print(f"Feed Link: {feed.feed.link}")
print(f"Feed Description: {feed.feed.get('description', 'No description available')}")


