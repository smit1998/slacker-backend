import pytest  
from Error import AccessError 

def test_channel_leave_channel_not_exist(): 
    u_id1, token1 = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    u_id2, token2 = auth_register('nicenice6@gmail.com', '12323452', 'looksn', 'smarts')
    name = 'super room' 
    unexisiting_channel = 'dsvfswvdsgrenvkscn dsknfkewbvkabdwoghodn l' 
    channels_create_dict = channels_create(token1, name, True)
    channelID = channels_create_dict['channel_id']
    
    channel_leave(token2, channelID)
    channel_join(token2, channelID)
    
    with pytest.raises(ValueError): 
        channel_leave(token1, unexisiting_channel)

def test_channel_join_channel_not_exisit(): 
    u_id1, token1 = auth_register('1337@gmail.com', '4253214', 'Yaba', 'Dabadoo')
    u_id2, token2 = auth_register('autobots@gmail.com', '123456', 'thee', 'dudee') 
    name = 'random channel' 
    unexisiting_channel= 'hi this channel does not exist'
    channels_create_dict = channels_create(token1, name, True)
    channelID = channels_create_dict['channel_id']
    
    channel_join(token2, channelID)
    channel_leave(token2, channelID) 
    
    with pytest.raises(ValueError): 
        channel_join(token2, unexisiting_channel)
        
        
def test_channel_join_private_channel_one(): 
    u_id1, token1 = auth_register('bot@gmail.com', '12323we452', 'real', 'bot')
    u_id2, token2 = auth_register('auto@gmail.com', '123456', 'the', 'dude') 
    name = 'admin room' 
    channels_create_dict = channels_create(token, name, False)
    channelID = channels_create_dict['channel_id']
    
    channel_invite(token1, channelID, u_id2)
    channel_join(token1, channelID)
    channel_leave(token2, channelID)
    
    with pytest.raises(ValueError): 
        channel_join(token2, channelID)
    
def test_channel_join_private_channel_two():
    u_id1, token1 = auth_register('human@gmail.com', '12323452', 'legit', 'human')
    u_id2, token2 = auth_register('good@gmail.com', '1234567', 'happy', 'guy') 
    name = 'secret room' 
    channels_create_dict = channels_create(token, name, False)
    channelID = channels_create_dict['channel_id']
    
    channel_invite(token1, channelID, u_id2)
    channel_join(token2, channelID)
    channel_addowner(token1, channelID, u_id2)
    channel_removeowner(token1, channelID, u_id2)
    channel_leave(token2, channelID)
    
    with pytest.raises(AccessError, match=r"*"):
        channel_join(token2, channelID)
        
def test_channel_join_non_admin():
    u_id1, token1 = auth_register('human@gmail.com', '12323452', 'legit', 'human')
    u_id2, token2 = auth_register('good@gmail.com', '1234567', 'happy', 'guy') 
    name = 'mega room' 
    channels_create_dict = channels_create(token, name, False)
    
    admin_userpermission_change(token1, u_id2, permission_id 2)
    channel_join(token2, channelID) # as user 1 has made user admin should be able to join with_out invite
    channel_leave(token2, channelID) 
    admin_userpermission_change(token1, u_id2, permission_id 3)
    
    with pytest.raises(AccessError, match=r"*"):
        channel_join(token2, channelID)
    
    channelID = channels_create_dict['channel_id']
def test_channel_addowner_id_not_exist(): 
    u_id1, token1 = auth_register('niceemail@gmail.com', '12323452', 'nice', 'person')
    u_id2, token2 = auth_register('ndsvvs@gmail.com', '123454542', 'hello', 'hi') 
    name = 'god channel' 
    unexisiting_channel = 'does not exist' 
    channels_create_dict = channels_create(token, name, False)
    channelID = channels_create_dict['channel_id']
    
    channel_addowner(token1, channelID, u_id2)
    channel_removeowner(token1, channelID, u_id2) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token1, unexisiting_channel, u_id2)

def test_channel_addowner_user_already_owner(): 
    u_id1, token1 = auth_register('nicenicenice@gmail.com', '12323452', 'good', 'smart')
    u_id2, token2 = auth_register('niceandcorrect@gmail.com', '12345454', 'hi', 'man') 
    channels_create_dict = channels_create(token1, 'My channel', False)
    channelID = channels_create_dict['channel_id'] 
    channel_addowner(token1, channelID, u_id2) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token1, channelID, u_id2)

def test_channel_addowner_non_owners(): 
    u_id1, token1 = auth_register('great@gmail.com', '12323452', 'goodness', 'me')
    u_id2, token2 = auth_register('niceandcorrect1@gmail.com', '123454542', 'hello', 'guy') 
    channels_create_dict = channels_create(token1, 'This channel', False)
    channelID = channels_create_dict['channel_id'] 
    
    channel_addowner(token1, channelID, u_id2) 
    channel_removeowner(token1, channelID, u_id2)
    
    with pytest.raises(AccessError, match=r"*"):
        channel_addowner(token2, channelID, u_id2) #u_id2 does not have to power to make themselfs owner of the channel (assume the token is a key that give the u_id1 power) 

def test_channel_addowner_non_slack_owner(): 
    u_id1, token1 = auth_register('wide@gmail.com', '12323452', 'trihard', '7')
    u_id2, token2 = auth_register('hardo@gmail.com', '123454542', 'wide', 'hardo') 
    u_id3, token3 = auth_register('34567@gmail.com', '12345678', 'five', 'six')
    channels_create_dict = channels_create(token1, 'yea channel', False)
    channelID = channels_create_dict['channel_id'] 

    admin_userpermission_change(token1, u_id2, permission_id 1)
    channel_addowner(token2, channelID, u_id3)
    channel_removeowner(token2, channelID, u_id3) 
    admin_userpermission_change(token1, u_id2, permission_id 3) 
    
    with pytest.raises(AccessError, match=r"*"):
        channel_addowner(token2, channelID, u_id3)
        
def test_channel_removeowner_id_not_exist(): 
    u_id1, token1 = auth_register('best@gmail.com', '123dsf8', 'correct', 'girl')
    u_id2, token2 = auth_register('niceandcorrect1@gmail.com', '123454542', 'hello', 'guy') 
    name = 'god channel' 
    unexisiting_channel = 'random name that is not a channel' 
    channels_create_dict = channels_create(token1, name, False)
    channelID = channels_create_dict['channel_id']
    
    channel_addowner(token1, channelID, u_id2)
    channel_removeowner(token1, channelID, u_id2) 
    
    with pytest.raises(ValueError): 
        channel_addowner(token1, unexisiting_channel, u_id2)

def test_channel_removeowner_user_not_owner(): 
    u_id1, token1 = auth_register('valid@gmail.com', '12sadsaf8', 'tickle', 'me emlo')
    u_id2, token2 = auth_register('niceandcorrect2@gmail.com', '123454wa542', 'hello', 'world') 
    name = 'legend channel' 
    unexisiting_channel = 'random name that is not a channel' 
    channels_create_dict = channels_create(token1, name, False)
    channelID = channels_create_dict['channel_id']
    
    channel_invite(token1, channelID, u_id2)  #only invted to be a member so cant be removed as an owner as they are not an owner
    
    with pytest.raises(ValueError): 
        channel_removeowner(token1, channelID, u_id2)

def test_channel_removeowner_non_owners(): 
    u_id1, token1 = auth_register('godly@gmail.com', '12323452', 'please', 'finish')
    u_id2, token2 = auth_register('endasap1@gmail.com', '123454542', 'imso', 'done') 
    channels_create_dict = channels_create(token1, 'This channel', False)
    channelID = channels_create_dict['channel_id'] 
    
    #channel_addowner(token1, channelID, u_id2) 
    #channel_removeowner(token1, channelID, u_id2)
    channel_invite(token1, channelID, u_id2)
    with pytest.raises(AccessError, match=r"*"):
        channel_removeowner(token2, channelID, u_id1) #u_id2 does not have to power to remove owners of the channel (assume the token1 is a key that give the the_id1 user power) 

def test_channel_removeowner_non_slack_owner(): 
    u_id1, token1 = auth_register('godly@gmail.com', '12323452', 'please', 'finish')
    u_id2, token2 = auth_register('endasap1@gmail.com', '123454542', 'imso', 'done') 
    u_id3, token3 = auth_register('niceandcorrect1@gmail.com', '123454542', 'hello', 'guy') 
    channels_create_dict = channels_create(token1, 'erobb waiting room', False)
    channelID = channels_create_dict['channel_id'] 
    
    admin_userpermission_change(token1, u_id2, permission_id 1)
    channel_addowner(token2, channelID, u_id3)
    admin_userpermission_change(token1, u_id2, permission_id 3) 
    
    with pytest.raises(AccessError, match=r"*"):
        channel_removeowner(token2, channelID, u_id3)

