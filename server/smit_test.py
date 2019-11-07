import pytest 
import re

def user_profile_setname_test_1():
    user_setname = auth_login('smitdobaria@gmail.com','hey123')
    token = user_setname['token']
# updating user first name and last name
    user_profile_setname(token,'taraj','naga')
    #returns fist name and last name of given email and password
    assert check_names('smitdobaria@gmail.com','hey123') == 'taraj naga'
#user first name is more than 50 words and last name is less than 50

def user_profile_setname_test_2():
    user_setname = auth_login('smitdobaria@gmail.com','hey123')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname(token,'ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')

def user_profile_setname_test_3():
    user_setname = auth_login('smitdobaria@gmail.com','hey123')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname(token,'mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')

#both are invalid
def user_profile_setname_test_4():
    user_setname = auth_login('smitdob@gmail.com','pass1234')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname(token,'askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')

def user_profile_setname_test_5():
    user_setname = auth_login('smitdob@gmail.com','pass1234')
    token = user_setname['token']
    # first and last names cant be null
    assert user_profile_setname('123@gmail.com','heythere12345','','') == True
    
#############################################################################################

# email is valid and not used already
def user_profile_setemail_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    token = result['token']

    with pytest.raises(ValueError):
            user_profile_setemail(token, 'smit@gmail.com')

# email is valid but not available
def user_profile_setemail_test_2():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    token = result['token']

    with pytest.raises(ValueError):
            user_profile_setemail(token, 'smitdobaria@gmail.com')
# not valid but available
def user_profile_setemail_test_3():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    token = result['token']

    with pytest.raises(ValueError):
            user_profile_setemail(token, 'smitdobgmail.com')           

# for the case of both not valid and not available is not possible because if it is not valid is not used also

############################################################################################

#user set handle
# handle is no more than 20
def user_profile_sethandle_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    handle_str = 'my_handle1234'

    with pytest.raises(ValueError):
        user_profile_sethandle('123',handle_str)

#last name is more than 50 words
def user_profile_sethandle_test_2():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == '20'
    basic_info = user_profile('easy easy easy', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dobsHHHHHHHHHJHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHADSSDHDSHJSDDSHHDSHJSDHJDSHDSHHJDD'
    handle_str = 'myHandle1234567890123456767990'
    with pytest.raises(ValueError):
        user_profile_sethandle('easy easy easy', handle_str)
# last name more than 50 and handle less than 20
def user_profile_sethandle_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
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
def user_profiles_uploadphoto_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = '100'
    result['x_start'] = '0'
    result['y_start'] = '0'
    result['x_end'] = '10'
    result['y_end'] = '10'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','100','0','0','10','10')

# image start and end are not in the dimension
def user_profiles_uploadphoto_test_2():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = '200'
    result['x_start'] = '-100'
    result['y_start'] = '-100'
    result['x_end'] = '10000000'
    result['y_end'] = '10000000'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','200','-100','-100','10000000','10000000')

# image start and end not in dimension and img_url not 200
def user_profiles_uploadphoto_test_3():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    result['img_url'] = '100'
    result['x_start'] = '-100'
    result['y_start'] = '-100'
    result['x_end'] = '10000000'
    result['y_end'] = '10000000'

    with pytest.raises(ValueError):
        user_profiles_uploadphoto('123','100','-100','-100','10000000','10000000')

#########################################################################################
# chanel id is valid
def standup_start_test_1():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',True)
    with pytest.raises(ValueError):
        standup_start('123', ch_id)

def standup_start_test_2():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','e',False)
    with pytest.raises(ValueError):
        standup_start('123', ch_id)

def standup_start_test_3():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',true)
    with pytest.raises(ValueError):
        standup_start('12', ch_id)
# everything is correct    
def standup_send_test_1():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('123','easy',true)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('123', ch_id, message)

#channel id is not correct
def standup_send_test_2():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('12','easy',false)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('123', ch_id, message)
#not the user of the channel
def standup_send_test_3():
    start = auth_login('smitdobaria@gmail.com','22abcd23')
    assert start['token'] == '123'
    ch_id = channels_create('12','easy',false)
    message = 'NO!!!!'
    with pytest.raises(ValueError):
        standup_send('1', ch_id, message)
 
#search test cases
# worng token
def search_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    with pytest.raises(ValueError):
        search('1234', 'heythere')
# Null string
def search_test_2():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'
    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    with pytest.raises(ValueError):
        search('123', ' ')

# tests for admin userpermission changes
# not a valid user id
def admin_userpermission_change_test_1():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(ValueError):
        admin_userpermission_change('123','','1')
    
# not a valid permission
def admin_userpermission_change_test_2():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(ValueError):
        admin_userpermission_change('123','20','3')
#not an admin or owner
def admin_userpermission_change_test_3():
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == '123'
    assert result['u_id'] == '20'

    basic_info = user_profile('123', '20')
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    with pytest.raises(AccessError):
        admin_userpermission_change('123','20','3')


