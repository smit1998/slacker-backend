import pytest 
import re

#user first and last names are less than 50

def user_profile_setname_test_1():
    user_setname = auth_register('abcd@gmail.com','idontkonwpass','smit','dobaria')
    token = user_setname['token']
# updating user first name and last name
    user_profile_setname('abcd@gmail.com','idontknowpass','cameron','burrell')
    assert check_names('abcd@gmail.com','idnotknowpass') == ('cameron','burrell')

#user first name is more than 50 words and last name is less than 50

def user_profile_setname_test_2():
    user_setname = auth_register('abc@gmail.com','abcd123','ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','ansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','dobaria')

def user_profile_setname_test_3():
    user_setname = auth_register('ab@gmail.com','ab456','mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','mike','nasdfkbjdakjdfakjlbfalsbfbasfbalsfjlasbfbjsadflafdsafsfasdfasfaafa')

#both are invalid
def user_profile_setname_test_4():
    user_setname = auth_register('abc@gmail.com','abcd123','askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')
    token = user_setname['token']

    with pytest.raises(ValueError):
        user_profile_setname('token','askjjbvdansjdhaahahahahahahahahahahabdvdsvsgsdgsdgsdbxchgsdbseghdsbsdgsdbdsgsdbsdsd','saljdchalsvchvakchvaskcvkasvcksvckvckavkcvadskhcvakhscvkhavckhgackavkcacvasvgc')
