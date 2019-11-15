import pytest 
from Error import AccessError 

def test_messages_edit_not_poster_of_message():
    u_id1, token1 = auth_register('one@gmail.com', '12323452', 'one', 'two')
    u_id2, token2 = auth_register('two@gmail.com', '123sad542', 'three', 'four') 
    channels_create_dict = channels_create(token1, 'Our channel', True)
    channelID = channels_create_dict['channel_id'] 

    channels_messages_dict = channels_messages(token1, channelID, 0) 
    messageID = channels_messages_dict['message_id']
    message = channels_messages_dict['messages']
    
    #add other user to the the channel but they should not be able to edit the message posted 
    channel_invite(token1, channelID, u_id2)
    
    message_edit(token1, messageID, message)
    
    with pytest.raises(ValueError): 
        message_edit(token2, messageID, message)
 
def test_messges_edit_not_owner(): 
    u_id1, token1 = auth_register('12345@gmail.com', '123456', 'one', 'two')
    u_id2, token2 = auth_register('23456@gmail.com', '1234567', 'three', 'four') 
    u_id3, token3 = auth_register('34567@gmail.com', '12345678', 'five', 'six')
    channels_create_dict = channels_create(token1, 'Moe Money Moe Awps', True)
    channelID = channels_create_dict['channel_id'] 

    channels_messages_dict = channels_messages(token1, channelID, 0) 
    messageID = channels_messages_dict['message_id']
    message = channels_messages_dict['messages']

    channel_addowner(token1, channelID, u_id2) #using the admin powers of the creater of the channel token1 give channel owner to u_id2 
    message_edit(token2, messageID, message) #as u_id2 has now been made owner and is able to edit messages that are not there own this edit functions should work 
    channel_removeowner(token1, channelID, u_id2) #u_id1 has removed user u_id2 from being an owner 
    
    with pytest.raises(ValueError): 
        message_edit(token2, messageID, message)
        
def test_messages_edit_not_slack_admin(): 
    u_id1, token1 = auth_register('123456@gmail.com', '123456', 'onetow', 'two')
    u_id2, token2 = auth_register('234567@gmail.com', '1234567', 'threefour', 'four') 
    channels_create_dict = channels_create(token1, 'Tyler1Sleeper', True)
    channelID = channels_create_dict['channel_id'] 

    channels_messages_dict = channels_messages(token1, channelID, 0) 
    messageID = channels_messages_dict['message_id']
    message = channels_messages_dict['messages']
    
    admin_userpermission_change(token1, u_id2, permission_id 2)
    message_edit(token2, messageID, message)
    admin_userpermission_change(token1, u_id2, permission_id 3)
    
    with pytest.raises(AccessError, match=r"*"):
        message_edit(token2, messageID, message)

def test_messages_edit_not_slack_owner(): 
    u_id1, token1 = auth_register('king@gmail.com', '123456', 'hifive', 'two')
    u_id2, token2 = auth_register('gorge@gmail.com', '1234567', 'threefour', 'four') 
    channels_create_dict = channels_create(token1, 'Sleep room', True)
    channelID = channels_create_dict['channel_id'] 

    channels_messages_dict = channels_messages(token1, channelID, 0) 
    messageID = channels_messages_dict['message_id']
    message = channels_messages_dict['messages']
    
    admin_userpermission_change(token1, u_id2, permission_id 1)
    message_edit(token2, messageID, message)
    admin_userpermission_change(token1, u_id2, permission_id 3)
    
    with pytest.raises(AccessError, match=r"*"):
        message_edit(token2, messageID, message)
