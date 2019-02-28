import praw


reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username='',
                     password='',
                     user_agent='')




#these are the flairs css_class names and should be used for updating the user flairs.
flairs = {
    1: "saibaman",
    2: "eathling",
    3: "namekian",
    4: "saiyan",
    5: "friezaclan",
    6: 'ss',
    7: 'android',
    8: 'ss2',
    9: 'supremekai',
    10: 'demon',
    11: 'ss3',
    12: 'majin-v',
    13: 'ssg-v',
    14: 'ssb-v',
    15: 'livinglegend-v',
    16: 'ssr-v',
    17: 'pridetrooper-v',
    18: 'god-v',
}



# Function takes in users rank name and returns rank css-class
def set_reddit_user_flair(rank_css, reddit_username):
    rank_css = str(rank_css)
    reddit_username = str(reddit_username)
    print('username: ', reddit_username, 'rank css: ', rank_css)
    try:
        reddit.subreddit('dragonballfighterz').flair.set(reddit_username, text=None, css_class=rank_css)
        reddit.redditor(reddit_username).message('Rank update!', 'Your rank has been updated in the /r/dragonballfighter'
                                            'z subreddit!')
        print(reddit_username, ' has had their flair changed to: ', rank_css)
    except:
        print('Unable to change user flair for: ', reddit_username)
    return

