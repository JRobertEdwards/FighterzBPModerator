import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from functionsReddit import  flairs, ranks_and_flairs, set_reddit_user_flair, get_current_user_flair


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Sheet brings in entire worksheet 'users'.
sheet = client.open('Blank Quiz (Responses)').sheet1
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
    #rank_css = rank_ranges(rank)
    rank_css = get_rank_css(rank)
    v_link = row_values[-3]
    # checks if rank meets verification threshold and if false to message user for proof.
    if not verify_rank_with_v_link(v_link, rank):
        unverified = True
    if unverified:
        print(reddit_username, 'is not verified')
        return
    else:
        # pass rank_check user flair and reddit username to change user flair.
        current_flair = get_current_user_flair(reddit_username)
        if current_flair != rank_css:
            set_reddit_user_flair(rank_css, reddit_username)
            print('Rank updated to: ', rank_css, 'for ', reddit_username)
        else:
            print('reddit flair is same as updated flair')


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


# iterates through the flair tuple checking against rank score.
# returns flair_name
def get_rank_css(rank):
    rank = int(rank)
    flair_and_rank = ranks_and_flairs
    flair_name = ''
    for flair in flair_and_rank.items():
        if rank >= flair[0]:
            flair_name = flair[1]
            continue
        else:
            if flair[0] >= rank:
                return flair_name
        
