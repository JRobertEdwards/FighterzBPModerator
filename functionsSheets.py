import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from functionsReddit import  flairs, set_reddit_user_flair


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Sheet brings in entire worksheet 'users'.
sheet = client.open('users').sheet1
# names_have_been_used is a global list that is appended to as each iteration of the names list
# is pushed through. This is used to check against already pushed names.
names_have_been_used = []

# Calls names that can be used to fetch row values.
def update_user_flair():
    names = get_usernames()
    get_each_row_values(names)

# Gets list of all usernames from second column.
# First column entry missed due to header name.
def get_usernames():
    names = sheet.col_values(2)
    return names[1:]


# Reverse iterates through the list of usernames and gets rowID.
# Username is appended to array to use as flag to indicate row has been used.
# Index can be used to limit GoogleApi calls.
def get_each_row_values(names):
    index = 0
    names = names[::-1]
    # This checks the size of the list from the second row on and adds the one back to get an accurate row number.
    row_number = len(names) + 1
    for each_name in names:
        print(index)
        row = sheet.row_values(row_number)
        row_values = row
        index += 1
        row_number -= 1
        if return_this_row(row_values):
            continue
        else:    
            names_have_been_used.append(each_name)
        if index == len(names):
            break


# row_values is the entire rows values.
# Pushes this item into the username and rank function to extract those specific values.
# Other values kept here in case of further use elsewhere.
def return_this_row(row_values):
    unverified = False
    reddit_username = row_values[1]
    reddit_username.strip()
    if name_used(reddit_username):
        return
    # Third column from the end is the v-link column where a html link should be present.
    rank = row_values[2]
    rank_css = rank_ranges(rank)
    v_link = row_values[-3]
    # checks if rank meets verification threshold and if false to message user for proof.
    if not verify_rank_with_v_link(v_link, rank):
        unverified = True
    if unverified:
        print(reddit_username, 'is not verified')
        return
    else:
        # pass rank_check user flair and reddit username to change user flair.
        set_reddit_user_flair(rank_css, reddit_username)
        print('user-flair: ',rank_css, 'username: ', reddit_username)


# Check reddit username against global list of used usernames
def name_used(reddit_username):

    if reddit_username in names_have_been_used:
        print('Name exists: ', reddit_username)
        return True

# name_used and v_link_exists set flags to say that the requirements are met where this item needs to be ignored or
# user needs to be messaged directly.
def verify_rank_with_v_link(v_link, rank):
    rank = int(rank)
    if rank > 600000:
        if 'https://' in v_link:
            print('link is present.')
            return True
        else:
            return False
    else:
        return True

# casting rank to an integer allows the searching of ranges for ranks to return the css_class flair string.
def rank_ranges(rank):
    this_rank = int(rank)
    # saibaman 
    if this_rank >= 0 and this_rank < 30000:
        user_flair = flairs[1]
        return user_flair
    # earthling 
    if this_rank >= 30000 and this_rank < 70000:
        user_flair = flairs[2]
        return user_flair
    # namekian 
    if this_rank >= 70000 and this_rank < 120000:
        user_flair = flairs[3]
        return user_flair
    # saiyan 
    if this_rank >= 120000 and this_rank < 170000:
        user_flair = flairs[4]
        return user_flair
    # friezaclan 
    if this_rank >= 170000 and this_rank < 220000:
        user_flair = flairs[5]
        return user_flair
    # ss 
    if this_rank >= 220000 and this_rank < 270000:
        user_flair = flairs[6]
        return user_flair
    # android 
    if this_rank >= 270000 and this_rank < 330000:
        user_flair = flairs[7]
        return user_flair
    # ss2 
    if this_rank >= 330000 and this_rank < 400000:
        user_flair = flairs[8]
        return user_flair
    # supremekai 
    if this_rank >= 400000 and this_rank < 500000:
        user_flair = flairs[9]
        return user_flair
    # demon 
    if this_rank >= 500000 and this_rank < 600000:
        user_flair = flairs[10]
        return user_flair
    # ssj3 
    if this_rank >= 600000 and this_rank < 700000:
        user_flair = flairs[11]
        return user_flair
    # majin 
    if this_rank >= 700000 and this_rank < 800000:
        user_flair = flairs[12]
        return user_flair
    # ssg-v 
    if this_rank >= 800000 and this_rank < 900000:
        user_flair = flairs[13]
        return user_flair
    # ssb-v 
    if this_rank >= 900000 and this_rank < 1000000:
        user_flair = flairs[14]
        return user_flair
    # livinglegend-v 
    if this_rank >= 1000000 and this_rank < 1200000:
        user_flair = flairs[15]
        return user_flair
    # ssr-v 
    if this_rank >= 1200000 and this_rank < 1400000:
        user_flair = flairs[16]
        return user_flair
    # pridetrooper-v
    if this_rank >= 1400000 and this_rank < 2000000:
        user_flair = flairs[17]
        return user_flair
    # god-v
    if this_rank >= 1200000 and this_rank < 1400000:
        user_flair = flairs[18]
        return user_flair
    else:
        return False