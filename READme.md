This is a script that allows the user to update the flairs on the dragonballfighterz subreddit of users that are extracted from a google sheets file.

The google sheets file has been populated by users by form response.

#######

How it works

Essentially this script will first find all the names in the sheet (as they are already known to be in col 2 this can be set easily).

These names are then used to fetch the data from that row for that name in a for loop. What is most important here is
the reddit username, rank (which is usually an integer although not always) and a verification link.

Once this data is extracted the username is checked if it has already been 'seen', if it hasn't then the rank range can be checked
to see which flair that user will fall into.

Once these are found depending on the range a verify link needs to be checked (this is down to the subreddit rules). Although there's possibly 
a way to actually verify these links in a script, I elected to have the 'https://' pattern be enough to count as a verify.

The reddit_username and rank_css is then used to update that reddiitors subreddit flair and send them a message to let them know 
that their flair has been updated.

#######

How to run 

In order to run the script to update user flairs simply call the function: update_user_flair(). This will kick off the process and follow it through to the end.

#######

Exceptions


In the functionsReddit.py file there is a try except block which should only catch something when the reddit_username variable cannot be found. This can be caused by strange formatting errors in google sheets which can arise due to copy/pasting usernames.

If there are any usernames in the sheet that seem as if they have return characters in them despite containing only the username itself, it may be worth removing the username entirely and manually typing it in.


#######

Post execution thoughts

After running the script there were around 14 users out of 400 that were caught where their user flair was updated. 
One user was actually demoted since they had messaged mods directly to have their flair updated after they'd filled in the form.
A check should have been implemented to see whether current user flair was higher than the new user flair to be assigned by the script.

In terms of outsider usability this is very much catered to this one instance and so lacks much re-usability. 
