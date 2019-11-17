import pytest 
import codepy as BF

def test_channels_join():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.channel_join(authRegisterDic['token'], 2)

def test_channels_join_private():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'False')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.AccessError): 
        BF.channel_join(authRegisterDic_2['token'], 1)

def test_channels_join_non_admin():
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'False')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.channel_join(authRegisterDic_2['token'], 1)

def test_channels_leave(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.channel_leave(authRegisterDic['token'], 2)

def test_channels_addowner_channel_id_invalid(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.addowners_channel(authRegisterDic['token'], 2, authRegisterDic_2['u_id'])

def test_channels_addowner_alreadyowner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])

def test_channels_addowner_id_not_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.AccessError): 
        BF.addowners_channel(authRegisterDic_2['token'], 1, authRegisterDic_2['u_id'])
        
def test_channels_removeowner_invalid_channel_id(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.removeowners_channel(authRegisterDic['token'], 2, authRegisterDic_2['u_id'])
        
def test_channels_removeowner_user_non_owner(): 
    BF.data['user_info'] = []
    BF.data['channel_info'] = [] 
    authRegisterDic = BF.user_register('cameron.ha@hotmail.com', '1234567', 'cameron', 'burrell')
    authRegisterDic_2 = BF.user_register('cameron.11@hotmail.com.au', '1234567', 'c', 'b')
    result = BF.channels_create(authRegisterDic['token'], 'good team', 'True')
    BF.addowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.removeowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    BF.resetChannel_id(result['channel_id'])
    with pytest.raises(BF.ValueError): 
        BF.removeowners_channel(authRegisterDic['token'], 1, authRegisterDic_2['u_id'])
    


