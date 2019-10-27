import pytest 
<<<<<<< HEAD
from Andy_first_iteration_stub import *
=======
from Andy_backend_functions import *
>>>>>>> Andy


# when channel is created successfully
def test_channels_create_valid():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetUser_id(authRegisterDic['u_id'])
    assert result['channel_id'] == 1

# when channel's name is invalid
def test_channels_create_invalid():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(ValueError):
        channels_create(authRegisterDic['token'], 'good team we are good is right ???', True)
  
# show the details of current channel under the authorised user
def test_channel_details():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetChannel_id(result['channel_id'])
    resetUser_id(authRegisterDic['u_id'])
    display_info = channel_details(authRegisterDic['token'], result['channel_id'])
    assert display_info['name'] == 'good team'
    assert display_info['owner_members'] == [{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]
    assert display_info['all_members'] ==[{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]

    
# channel_id is not a valid channel
def test_channel_details():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei') 
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetUser_id(authRegisterDic['u_id'])
    resetChannel_id(result['channel_id'])
    with pytest.raises(ValueError):
        channel_details(authRegisterDic['token'], 1)
       

# when authorised user is not a member of this channel
def test_channel_details_user_is_not_in_channel():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei') 
    authRegisterDic_02 = user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetChannel_id(result['channel_id'])
    resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(ValueError):
        channel_details(authRegisterDic_02['token'], 2)
                  
# add one user into the private channel, and print the detail of this channel
def test_private_channel_details_invite_one_more_user():
<<<<<<< HEAD
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
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}], 
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
    assert result == {'name': 'a new channel', 'owner_members': [{'u_id': 23, 'name_first':'Andy', 'name_last': 'Wei'}], 
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
    assert result == {'name': 'funny channel', 'owner_members': [{'u_id': 66, 'name_first':'Jack', 'name_last': 'Ma'}], 
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
    if(start > len(message['message'])):
        with pytest.raises(ValueError):
            channel_messages('easy easy easy', chann_id, start)    
=======
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = channels_create(authRegisterDic['token'], 'good team', True)
    authRegisterDic_02 = user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    channel_invite(authRegisterDic['token'], result['channel_id'], authRegisterDic_02['u_id'])
    print(result['channel_id'])
    print(authRegisterDic_02['u_id'])
    display_info = channel_details(authRegisterDic['token'], result['channel_id'])
    resetChannel_id(result['channel_id'])
    resetUser_id(authRegisterDic['u_id'])
    assert display_info['name'] == 'good team'
    assert display_info['owner_members'] == [{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]
    assert display_info['all_members'] ==[{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'},
    {'u_id': 2, 'name_first': 'Andrew', 'name_last': 'Yeh'}]
>>>>>>> Andy
       
# when the channel_id is not refer to a valid channel 
def test_channel_invite_channel_id_invalid():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    authRegisterDic_02 = user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetChannel_id(result['channel_id'])
    resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(ValueError):
        channel_invite(authRegisterDic['token'], 2, authRegisterDic_02['u_id'])
 
# when the u_id is invalid 
def test_channel_invite_u_id_invalid():
    data['user_info'] = []
    data['channel_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    authRegisterDic_02 = user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = channels_create(authRegisterDic['token'], 'good team', True)
    resetChannel_id(result['channel_id'])
    resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(ValueError):
        channel_invite(authRegisterDic['token'], 1, 5)
  
