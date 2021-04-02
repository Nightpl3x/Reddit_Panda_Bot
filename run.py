import praw
import login
import main

reddit = login.authenticate()
comments_replied_to = main.get_saved_comments()

while True:
    try:
        main.run(reddit,comments_replied_to)
    except Exception as e:
        print(e)
        continue