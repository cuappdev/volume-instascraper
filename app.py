from datetime import datetime
from itertools import dropwhile, takewhile

from instaloader import instaloader, Profile

# Create instance
loader = instaloader.Instaloader(
    download_videos=False,
    download_video_thumbnails=False,
    save_metadata=False,
    post_metadata_txt_pattern=""
)

# User input
start_input = input("\nEnter start date in the format m-d-yyyy: ")

# Get datetime objects
start_date = datetime.strptime(start_input, '%m-%d-%Y')

# Fetch usernames from usernames.txt
with open('usernames.txt') as f:
    usernames = f.read().splitlines()

# Download posts from every user within the start and end date
for user in usernames:
    posts = Profile.from_username(loader.context, user).get_posts()

    for post in takewhile(lambda p: p.date > start_date, posts):
        loader.download_post(post, user)
