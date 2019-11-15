import pytest 
import backend_functions as BF

# when channel is created successfully
def test_channels_create_valid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetUser_id(authRegisterDic['u_id'])
    assert result['channel_id'] == 1

# when channel's name is invalid
def test_channels_create_invalid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    BF.resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(BF.ValueError):
        BF.channels_create(authRegisterDic['token'], 'good team we are good is right ???', True)
  
# show the details of current channel under the authorised user
def test_channel_details():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    display_info = BF.channel_details(authRegisterDic['token'], result['channel_id'])
    assert display_info['name'] == 'good team'
    assert display_info['owner_members'] == [{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]
    assert display_info['all_members'] ==[{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]

    
# channel_id is not a valid channel
def test_channel_details():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei') 
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError):
        BF.channel_details(authRegisterDic['token'], result['channel_id'])
       

# when authorised user is not a member of this channel
def test_channel_details_user_is_not_in_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei') 
    authRegisterDic_02 = BF.user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(BF.AccessError):
        BF.channel_details(authRegisterDic_02['token'], result['channel_id'])
                 
def test_channel_details():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    authRegisterDic_02 = BF.user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    BF.channel_invite(authRegisterDic['token'], result['channel_id'], authRegisterDic_02['u_id'])
    print(result['channel_id'])
    print(authRegisterDic_02['u_id'])
    display_info = BF.channel_details(authRegisterDic['token'], result['channel_id'])
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    assert display_info['name'] == 'good team'
    assert display_info['owner_members'] == [{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'}]
    assert display_info['all_members'] ==[{'u_id': 1, 'name_first': 'Andy', 'name_last': 'Wei'},
    {'u_id': 2, 'name_first': 'Andrew', 'name_last': 'Yeh'}]
    
       
# when the channel_id is not refer to a valid channel 
def test_channel_invite_channel_id_invalid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    authRegisterDic_02 = BF.user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(BF.ValueError):
        BF.channel_invite(authRegisterDic['token'], 2, authRegisterDic_02['u_id'])

# when the u_id is invalid 
def test_channel_invite_u_id_invalid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    authRegisterDic_02 = BF.user_register('AndrewYeh@unsw.edu.au', '66666666', 'Andrew', 'Yeh') 
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    with pytest.raises(BF.ValueError):
        BF.channel_invite(authRegisterDic['token'], result['channel_id'], 3)
               
# when one authorised user send one message to channel
def test_channel_messages():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei') 
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetChannel_id(result['channel_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    return_dic = BF.channel_messages(authRegisterDic['token'], 1, 0)
    assert return_dic['end'] == 50
    



  
