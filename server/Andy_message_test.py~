import pytes
import dummy_error import AccessError

# when message is more than 1000 characters, just ValueError 
def test_message_send_many_characters():
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    messages = search('good job', 'dummychoice')
    message = messages['message']
    if(len(message) > 1000):
        with pytest.raises(ValueError):
            message_send('good job', chann_id, message)

# send the meessage to another private channel and the authorized user is not in this channel
def test_message_send_to_private_channel_by_user_outside():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    channel_id = channels_create('good job', 'greate channel', False)
    chann_id = channel_id['channel_id']
    messages = search('easy easy easy', 'hahahahaha')
    message = messages['message']
    message_send('easy easy easy', chann_id, message)
 
# send the meessage to another public channel and the authorized user is not in this channel
def test_message_send_to_public_channel_by_user_outside():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    channel_id = channels_create('good job', 'greate channel', True)
    chann_id = channel_id['channel_id']
    messages = search('easy easy easy', 'hahahahaha')
    message = messages['message']
    message_send('easy easy easy', chann_id, message)  
   
# send the meessage to another public channel and the authorized user is in this channel
def test_message_send_to_public_channel_by_user_inside():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    channel_id = channels_create('good job', 'greate channel', True)
    chann_id = channel_id['channel_id']
    channel_join('easy easy easy', chann_id)
    messages = search('easy easy easy', 'hahahahaha')
    message = messages['message']
    message_send('easy easy easy', chann_id, message)  
    
# send the meessage to another private channel and the authorized user is in this channel 
def test_message_send_to_private_channel_by_user_inside():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    channel_id = channels_create('good job', 'greate channel', True)
    chann_id = channel_id['channel_id']
    channel_invite('easy easy easy', chann_id, 23)
    messages = search('easy easy easy', 'hahahahaha')
    message = messages['message']
    message_send('easy easy easy', chann_id, message) 
    
# if the channel doesn't exist, just ValueError
def test_message_sendlater_not_exist():
    result = auth_login('andrewzhu@gmail.com', '66wz3#d')
    assert result['token'] == 'good job'
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2019,10,6,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    with pytest.raises(ValueError):
        message_sendlater('easy easy easy','wrong channel', message, today)

# if the message is more than 1000 characters, then just ValueError
def test_message_sendlater_many_characters():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2020,3,1,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    if(len(message) > 1000):
        with pytest.raises(ValueError):
            message_sendlater('easy easy easy', chann_id, message, today)
            
# if the time sent is a time in the past, need to be considered as a valueError
def test_message_sendlater_time_in_the_past():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    today = datetime.datatime(2018,3,1,18,54,36,280121)
    messages = search('easy easy easy', 'dummychoice')
    message = messages['message']
    with pytest.raises(ValueError):
            message_sendlater('easy easy easy', chann_id, message, today) 
    
