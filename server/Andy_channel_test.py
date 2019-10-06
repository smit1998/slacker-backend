import pytest 
import dummy_error import AccessError

# show the details of current channel under the authorised user, and also name is public
def test_public_channel_details():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id'] 
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}], 
    'all_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}]}

# show the details of current channel under the authorised user, and also name is private 
def test_private_channel_details():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    channel_id = channels_create('easy easy easy', 'a new channel', False)
    chann_id = channel_id['channel_id'] 
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}], 
    'all_members': [{'u_id': 23, 'name_first': 'Andy', 'name_last': 'Wei'}]}

# when authorised user is not a member of this channel, just ValueError message
def test_channel_details_user_is_not_in_channel():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id = channels_create('right user' 'funny_channel', True)
    result = channel_id['channel_id']
    with pytest.raises(ValueError):
        channel_details('easy easy easy', result)

# when channel doesn't exist, print error message
def test_channel_details_channel_not_exist():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    with pytest.raises(AccessError):
        channel_details('right user', 29)

# add one user into the private channel, and print the detail of this channel
def test_private_channel_details_invite_one_more_user():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    channel_id = channels_create('easy easy easy', 'a new channel', False) 
    chann_id = channel_id['channel_id']
    channel_invite('right user', chann_id, 66)
    basic_info = user_profile('right user', 66)
    assert basic_info['name_first'] == 'Jack'
    assert basic_info['name_last'] == 'Ma'
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}, {'u_id': 66, 'name_first':'Jack', 'name_last': 'Ma'}]}

# one user join into the public channel, and print the detail of this channel
def test_public_channel_details_add_more_people():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    channel_id = channels_create('easy easy easy', 'a new channel', True) 
    chann_id = channel_id['channel_id']
    channel_join('right user', chann_id)
    basic_info = user_profile('right user', 66)
    assert basic_info['name_first'] == 'Jack'
    assert basic_info['name_last'] == 'Ma'
    basic_info = user_profile('easy easy easy', 23)
    assert basic_info['name_first'] == 'Andy'
    assert basic_info['name_last'] == 'Wei'
    result = channel_details('easy easy easy', chann_id)
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei']}, 
    'all_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}, {'u_id': 66, 'name_first':'Jack', 'name_last': 'Ma'}]}

# get involved more users and have a test of channel_detail()
def test_private_channel_details_invite_more_user():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    result = auth_login('queenking@gmail.com', '234#4$Ss432')
    assert result['token'] == 'great person'
    assert result['u_id'] == 12
    result = auth_login('reallygreat@gmail.com', 'fan123#123')
    assert result['token'] == 'win win'
    assert result['u_id'] == 10
    channel_id = channels_create('right user', 'funny channel', False)
    chann_id = channel_id['channel_id'] 
    channel_invite('easy easy easy', chann_id, 23)
    channel_invite('great person', chann_id, 12)
    channel_invite('win win', chann_id, 10)
    basic_info01 = user_profile('easy easy easy', 23)
    assert basic_info01['name_first'] == 'Andy'
    assert basic_info01['name_last'] == 'Wei'
    basic_info01 = user_profile('right user', 66)
    assert basic_info01['name_first'] == 'Jack'
    assert basic_info01['name_last'] == 'Ma'
    basic_info01 = user_profile('great person', 12)
    assert basic_info01['name_first'] == 'Bill'
    assert basic_info01['name_last'] == 'Chung'
    basic_info01 = user_profile('win win', 10)
    assert basic_info01['name_first'] == 'Cameron'
    assert basic_info01['name_last'] == 'He'
    result = channel_details('right user', chann_id)
    assert result == {'name': 'funny channel', 'owner_members': [{'u_id': 66, 'name_first':'Jack', 'name_last': 'Ma']}, 
    'all_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}, {'u_id': 12, 'name_first':'Bill', 'name_last': 'Chung'},
    {'u_id': 10, 'name_first': 'Cameron', 'name_first': 'He'}]}
    
# return up to 50 messages between start and end under the authorized user
def test_channel_messages_authorized_user():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    messages = search('easy easy easy', 'dummychoice')
    result = channel_messages('easy easy easy', chann_id, 0)
    assert result == {'messages': messages, 'start': 0, 'end': 49}
  
# valueError because of the start is greater than the total number of messages in the channel
def test_channel_messages_start_value_invalid():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    channel_id = channels_create('easy easy easy', 'a new channel', True)
    chann_id = channel_id['channel_id']
    start = 10000 
    message = search('easy easy easy', 'dummychoice')
    if(start > len(message['message']):
        with pytest.raises(ValueError):
            channel_messages('easy easy easy', chann_id, start)    
       
# valueError because of the channel doesn't exist
def test_channel_messages_channel_not_exist():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id01 = channels_create('easy easy easy', 'a new channel', True)
    chann_id01 = channel_id01['channel_id']
    channel_id02 = channels_create('right user', 'another channel', True)
    chann_id02 = channel_id02['channel_id']
    with pytest.raises(ValueError):
        channel_messages('right user', chann_id01, 0)
 
# valueError because of the authorized user is not a number of this current channel
def test_channel_messages_user_not_in_channel():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    channel_id01 = channels_create('easy easy easy', 'a new channel', True)
    chann_id01 = channel_id01['channel_id']
    with pytest.raises(AccessError):
        channels_create('a right user', 'a new channel', True)
        
