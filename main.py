import praw
import time
import os
import random
import panda_facts

def run(reddit,comments_replied_to):
    for comment in reddit.subreddit('test').comments(limit=1):
        if ("panda fact" in comment.body.lower()) and (comment.id not in comments_replied_to):
            comment.reply(random.choice(panda_facts.panda_facts))

            #comments_replied_to.append(comment.id)
            comments_replied_to = "\n".join(comment.id)

            with open ("comments_replied_to.txt","a") as f:
                f.write(comment.id +"\n")
    time.sleep(30)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

    return comments_replied_to


