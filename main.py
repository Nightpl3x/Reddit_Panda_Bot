import praw
import time
import os
import random
import panda_facts

def run(reddit,comments_replied_to):
    for comment in reddit.subreddit('test').comments(limit=1):
        if ("!panda" in comment.body.lower()) and (comment.id not in comments_replied_to):

            message1 = (random.choice(panda_facts.panda_facts))
            message2 =  "\n\n---\n\n^(I am a bot and this was an automated message. I am not responsible for the content neither am I an author of this content. If you think this message is problematic, please contact the developer mentioned below.)\n\nAuthor: [u/Nightpl3x](https://www.reddit.com/user/Nightpl3x/) | [GitHub](https://github.com/Nightpl3x/Reddit_Panda_Bot)"
            comment.reply(message1 + message2)

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


