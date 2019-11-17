import pytest 
import user_profile as BF
#everything is valid

#first name is not valid
def test_user_profile_setname_2():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('abc@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.user_login('abc@qq.com', '1234567')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']
    with pytest.raises(BF.ValueError):
        BF.user_profile_setname('1234567', 'abcdefghijklmnopqrstuvwxyz123456789012345678901234567890', 'wei')

# last name is not valid 
def test_user_profile_setname_3():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('abc@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.user_login('abc@qq.com', '1234567')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']
    with pytest.raises(BF.ValueError):
        BF.user_profile_setname('1234567', 'smit', 'wei12345678901234567890qwertyuiopasdfghjklzxcvbnm,.;n;kjscbdcsmcibcsdcnn')        

#both are invalid
def test_user_profile_setname_4():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('abc@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.user_login('abc@qq.com', '1234567')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']
    with pytest.raises(BF.ValueError):
        BF.user_profile_setname('1234567', 'abcdefghijklmnopqrstuvwxyz123456789012345678901234567890', 'jlbdlhdhalsdvavqwvefyqweywgiuuiuggggggdgdggdgwygdiygwdwgdsbxjsxvvhsqwhjvdvwldw12345678901234567890')
    
#############################################################################################

# email is valid and not used already
def test_user_profile_setemail_1():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('smitdob@qq.com', '12345678', 'smit', 'dob')
    result = BF.user_login('smitdob@qq.com', '12345678')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']
    BF.user_profile_setemail(result['token'], 'smitdobaria@qq.com')
    
# email is valid but not available
def test_user_profile_setemail_2():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('smit@qq.com', '12345678', 'smit', 'dob')
    result = BF.user_login('smit@qq.com', '12345678')
    authRegisterDic_2 = BF.user_register('1234566@qq.com', '1234567', 'smit1', 'dob2')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']

    with pytest.raises(ValueError):
            BF.user_profile_setemail(result['token'], '1234566@qq.com')
           

# for the case of both not valid and not available is not possible because if it is not valid is not used also

############################################################################################

#user set handle
# handle is no more than 20
def test_user_profile_sethandle_1():
    result = BF.user_login('smitdob@qq.com', '12345678')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = BF.user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    handle_str = 'my_handle1234'

    with pytest.raises(ValueError):
        BF.user_profile_sethandle('123',handle_str)

#last name is more than 50 words
def test_user_profile_sethandle_2():
    result = BF.user_login('smitdob@qq.com', '12345678')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == '20'
    basic_info = user_profile('easy easy easy', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dobsHHHHHHHHHJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHADSSDHDSHJSDDSHHDSHJSDHJDSHDSHHJDD'
    handle_str = 'myHandle1234567890123456767990'
    with pytest.raises(ValueError):
        user_profile_sethandle('easy easy easy', handle_str)
# last name more than 50 and handle less than 20
def test_user_profile_sethandle_1():
    result = BF.user_login('smitdob@qq.com', '12345678')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'doblashhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhdbhsdchjsadhcavschacvasvchahcahvcvasvcavsgc'

    handle_str = 'my_handle1236'

    with pytest.raises(ValueError):
        user_profile_sethandle('123',handle_str)


#############################################################################################  
# image url returns status other than 200
def test_user_profiles_uploadphoto_1():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = 'https://commons.wikimedia.org/wiki/File:Sunflower_from_Silesia2.jpg'
    result['x_start'] = '0'
    result['y_start'] = '0'
    result['x_end'] = '10'
    result['y_end'] = '10'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','100','0','0','10','10')

# image start and end are not in the dimension
def test_user_profiles_uploadphoto_2():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = 'https://commons.wikimedia.org/wiki/File:Sunflower_from_Silesia2.jpg'
    result['x_start'] = '-100'
    result['y_start'] = '-100'
    result['x_end'] = '10000000'
    result['y_end'] = '10000000'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','200','-100','-100','10000000','10000000')

# image start and end not in dimension and img_url not 200
def test_user_profiles_uploadphoto_3():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = 'https://commons.wikimedia.org/wiki/File:Sunflower_from_Silesia2.jpg'
    result['x_start'] = '-100'
    result['y_start'] = '-100'
    result['x_end'] = '10000000'
    result['y_end'] = '10000000'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','100','-100','-100','10000000','10000000')

#########################################################################################
# chanel id is valid
def test_standup_start_1():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',True)
    with pytest.raises(ValueError):
        standup_start('123', ch_id)

def test_standup_start_2():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','e',False)
    with pytest.raises(ValueError):
        standup_start('123', ch_id)

def test_andup_start_3():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',true)
    with pytest.raises(ValueError):
        standup_start('12', ch_id)

# everything is correct    
def test_standup_send_1():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',true)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('123', ch_id, message)

#channel id is not correct
def test_standup_send_2():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('12','easy',false)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('123', ch_id, message)
#not the user of the channel
def test_standup_send_3():
    start = BF.user_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('12','easy',false)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('1', ch_id, message)

#search test cases
# worng token
def test_search_1():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    with pytest.raises(ValueError):
        search('1234', 'heythere')
# Null string
def test_search_2():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    with pytest.raises(ValueError):
        search('123', ' ')


# tests for admin userpermission changes
# not a valid user id
def test_admin_userpermission_change_1():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(ValueError):
        admin_userpermission_change('123','','1')
    
# not a valid permission
def test_admin_userpermission_change_2():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(ValueError):
        admin_userpermission_change('123','20','3')
#not an admin or owner
def test_admin_userpermission_change_3():
    result = BF.user_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(AccessError):
        admin_userpermission_change('123','20','3')
