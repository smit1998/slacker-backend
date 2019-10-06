import pytest
import re 
def user_profile_setname(token, name_first, name_last):
    pass
 
def user_profile_setemail(token, email):
    pass

def user_profile_sethandle(token, handle_str):
    pass
def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    pass

def standup_start(token, channel_id):
    pass

def standup_send(token, channel_id, message):
    pass

def search(token, query_str):
    pass

def admin_userpermission_change(token, u_id, permission_id):
    pass

#helper function for user_profile_setemail

  
# Make a regular expression 
# for validating an Email 
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def isValidEmail(email):  
  
    # pass the regualar expression 
    # and the string in search() method 
    if(re.search(regex,email)):  
        return True 
          
    else:  
        False  
      