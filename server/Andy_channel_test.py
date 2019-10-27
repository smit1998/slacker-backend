import pytest 
from Andy_backend_functions import *


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
  
