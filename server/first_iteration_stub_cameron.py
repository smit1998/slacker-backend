from Error import AccessError 
import pytest 

def auth_register(email, password, name_first, name_last): 
    pass 

def auth_passwordreset_request(email): 
    pass 

def auth_passwordreset_reset(reset_code, new_password): 
    pass 

def channel_invite(token, channel_id, u_id): 
    pass 

def channel_messages(token, channel_id, start): 
    pass 

def channel_leave(token, channel_id): 
    pass 

def channel_join(token, channel_id): 
    pass 

def channel_addowner(token, channel_id, u_id): 
    pass 

def channel_removeowner(token, channel_id, u_id): 
    pass 

def channel_create(token, name, is_public): 
    pass 

def message_edit(token, message_id, message): 
    pass 

def admin_userpermission_change(token, u_id, permission_id): 
    pass 

def validToken(token): 
    pass

def validCode(reset_code): 
    pass 
    
