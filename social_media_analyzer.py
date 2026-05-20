def load_posts(filename):
    import pandas as pd
    data = pd.read_csv(filename)
    return data


def analyze_posts(posts):
    posts["engagement"] = ((posts["likes"] + posts["comments"] + posts["shares"]) / posts["views"]) * 100
    statements = []
    for i,row in posts.iterrows():
        if row["engagement"]>8:
            statements.append(f"High performing post: {row['title']} at {row['time']}")
        else:
            statements.append(f"Low performing post: {row['title']} at {row['time']}")
    posts["performance"] = statements
    return posts

def best_posting_time(posts):
    best_posting_time = []
    for i,row in posts.iterrows():
        if row["engagement"]> 8:
            best_posting_time.append(f"Best posting time for '{row['title']}': {row['time']}")
    print("\n".join(best_posting_time))

def suggest_improvements(posts):
    imporments = []
    for i,row in posts.iterrows():
        if row["engagement"] < 5:
            imporments.append(f"Consider posting '{row['title']}' at a different time or improving content.")
    print("\n".join(imporments))

posts = load_posts("posts.csv")
analyzed_posts = analyze_posts(posts)
best_posting_time(analyzed_posts)
suggest_improvements(analyzed_posts)