import pytest 
import re
# assumptions:
#1. the given email and password should be correct for user_profile_setname
#    and user must be registered first.
#2. the new email can not be null and can not be same as the current email for user_setemail
#user first and last names are less than 50
#3. the given is not NULL

def user_profile_setname_test_1():
    user_setname = auth_login('20','hey123')
    token = user_setname['token']
# updating user first name and last name
    user_profile_setname('token','taraj','naga')
    #returns fist name and last name of given email and password
    assert check_names('abcd@gmail.com','idnotknowpass') == taraj naga

#user first name is more than 50 words and last name is less than 50

def user_profile_setname_test_2():
    user_setname = auth_login('1','12345')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')

def user_profile_setname_test_3():
    user_setname = auth_login('2','ljahdf')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')

#both are invalid
def user_profile_setname_test_4():
    user_setname = auth_login('3','5638')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')

def user_profile_setname_test_5():
    user_setname = auth_login('4','3568')
    token = user_setname['token']
    # first and last names cant be null
    assert user_profile_setname('123@gmail.com','heythere12345','','') == True
    
#############################################################################################
# email is valid and not used already
def user_profile_setemail_test_1(token, email):
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 20
    basic_info = user_profile('easy easy easy', 20)
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    #checks if email is valid and not in use already
    assert isValidEmail('smitdobaria123@yahoo.com') == True
    assert isAlreadyEmail('smitdobaria123@yahoo.com') == False

    user_profile_setemail('easy easy easy','smitdobaria123@yahoo.com')
    assert user_profile('easy easy easy', '20') == ('smitdobaria123@yahoo.com','smit','dobaria','20')
# email is valid but not available
def user_profile_setemail_test_2(token, email):
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 20
    basic_info = user_profile('easy easy easy', 20)
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    assert isValidEmail('smitdob12345@gmail.com') == True
    assert isAlreadyEmail('smitdob12345@gmail.com') == False

# email is not valid but is not already used
def user_profile_setemail_test_2(token, email):
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 20
    basic_info = user_profile('easy easy easy', 20)
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'
    
    assert isValidEmail('smit.gmail.com') == True
    assert isAlreadyEmail('smit.gmail.com') == False
# for the case of both not valid and not available is not possible because if it is not valid is not used also

#user set handle
# handle is valid and less than 20 char
def user_profile_sethandle_test_1(token, handle_str):
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 20
    basic_info = user_profile('easy easy easy', 20)
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    assert isValidHandle('12345') == True

    user_profile_sethandle('easy easy easy', '12345')
    assert user_profile('easy easy easy', '20') == ('smitdob@gmail.com','smit','dob','12345')

#handle is more than 20 char
def user_profile_sethandle_test_2(token, handle_str):
    result = auth_login('smitdob@gmail.com', '22abcd23')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 20
    basic_info = user_profile('easy easy easy', 20)
    assert basic_info['name_first'] == 'smit'
    assert basic_info['name_last'] == 'dob'

    assert isValidHandle('h123456789rabschedhjsil') == True

    user_profile_sethandle('easy easy easy', 'h123456789rabschedhjsil')
    assert user_profile('easy easy easy', '20') == ('smitdob@gmail.com','smit','dob','h123456789rabschedhjsil')