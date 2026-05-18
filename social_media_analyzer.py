post1 = {
    "title": "10 Tips for Effective Time Management",
    "likes": 150,
    "comments": 20,
    "shares": 30,
    "posting_time": "2024-06-01 10:00:00"
}
post2 = {
    "title": "How to Stay Motivated While Working from Home",
    "likes": 200,
    "comments": 50,
    "shares": 40,
    "posting_time": "2024-06-02 14:00:00"
}
post3 = {
    "title": "The Ultimate Guide to Healthy Eating",
    "likes": 300,
    "comments": 80,
    "shares": 60,
    "posting_time": "2024-06-03 18:00:00"
}

posts = [post1, post2, post3]

def analyze_posts(posts):
    for post in posts:
        engagement = post["likes"] + post["comments"] + post["shares"]
        print(f"Post: {post['title']}")
        print(f"Engagement: {engagement}")
        if engagement > 200:
            print("This post is performing well!\n")
        else:
            print("This post could use some improvement.\n")

analyze_posts(posts)
