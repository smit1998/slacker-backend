import pytest 
import re

#user first and last names are less than 50

def user_profile_setname_test_1():
    user_setname = auth_login('abcd@gmail.com','idontkonwpass','smit','dobaria')
    token = user_setname['token']
# updating user first name and last name
    user_profile_setname('abcd@gmail.com','idontknowpass','taraj','naga')
    #returns fist name and last name of given email and password
    assert check_names('abcd@gmail.com','idnotknowpass') == ('taraj','naga')

#user first name is more than 50 words and last name is less than 50

def user_profile_setname_test_2():
    user_setname = auth_login('abc@gmail.com','abcd123','ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')

def user_profile_setname_test_3():
    user_setname = auth_login('ab@gmail.com','ab456','mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')

#both are invalid
def user_profile_setname_test_4():
    user_setname = auth_login('a@gmail.com','abcd23','askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')

def user_profile_setname_test_5():
    user_setname = auth_login('123@gmail.com','heythere12345','rohan','luli')
    token = user_setname['token']
    # first and last names cant be null
    assert user_profile_setname('123@gmail.com','heythere12345','','') == True
    
