import praw


reddit = praw.Reddit(client_id = '',
                     client_secret = '',
                     username='',
                     password='',
                     user_agent='')


#these are the flairs css_class names and should be used for updating the user flairs. The integer indicates their necessary score to reach.
ranks_and_flairs = {
    0: "saibaman",
    30000: "earthling",
    70000: "namekian",
    120000: "saiyan",
    170000: "friezaclan",
    220000: 'ss',
    270000: 'android',
    330000: 'ss2',
    400000: 'supremekai',
    500000: 'demon',
    600000: 'ss3',
    700000: 'majin-v',
    800000: 'ssg-v',
    900000: 'ssb-v',
    1000000: 'livinglegend-v',
    1200000: 'ssr-v',
    1400000: 'pridetrooper-v',
    2000000: 'god-v',
}


def get_current_user_flair(reddit_username):
    user_flair = next(reddit.subreddit('dragonballfighterz').flair(reddit_username))
    return user_flair['flair_css_class']


# Function takes in users rank name and returns rank css-class
def set_reddit_user_flair(rank_css, reddit_username):
    rank_css = str(rank_css)
    reddit_username = str(reddit_username)
    print('username: ', reddit_username, 'rank css: ', rank_css)
    try:
        reddit.subreddit('dragonballfighterz').flair.set(reddit_username, text=None, css_class=rank_css)
        reddit.redditor(reddit_username).message('Rank up!', 'Whoo hoo! Your rank flair has been updated in /r/dragonballfighterz! \n \n'
                                                'If there were any problems, reach out to the mods [here](https://www.reddit.com/message/compose?to=%2Fr%2Fdragonballfighterz).')
        print(reddit_username, ' has had their flair changed to: ', rank_css)
    except:
        print('Unable to change user flair for: ', reddit_username)
    return

