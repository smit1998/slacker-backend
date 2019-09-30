import pytest 
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'     

def auth_login(email, password):
    
    token = {}
    if(re.search(regex, email)):
        try:
            token["email"] = email
        except Exception:
            print("Got wrong e-mail")
    if(len(password) > 5):
        try:
            token["password"] = password
        except Exception:
            print("Got wrong password")
    return token
    

def auth_logout(token):
    
    if(re.search(regex, token["email"]) and len(token["password"]) > 5):
        del(token["email"])
        del(token["password"])
        return token 
    return token 
    
   
# when both of email and password are valid
def test_1():
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result == {"email": 'ankitrai326@gmail.com', "password": '224232r4'}
    
    result = {"email": 'ankitrai326@gmail.com', "password": '224232r4'}
    auth_logout(result)
    assert result == {}

# when the email is valid and password is invalid
def test_2(): 
    result = auth_login('ankitrai326@gmail.com', '2242')
    assert result == {"email": 'ankitrai326@gmail.com'}
    
    result = {"email": 'ankitrai326@gmail.com', "password": '2242'}
    auth_logout(result)
    assert result == {"email": 'ankitrai326@gmail.com', "password": '2242'}
    
# when the password is valid and email is invalid
def test_3(): 
    result = auth_login('1337memesgmail.com', '123243223') 
    assert result == {'password': '123243223'}
    
    result = {'email': '1337memesgmail.com', 'password': '123243223'}
    auth_logout(result)
    assert result == {'email': '1337memesgmail.com', 'password': '123243223'}
    
# when both of email and password are invalid
def test_4(): 
    result = auth_login('tisisatest.comgamil', '66666')
    assert result == {}   
    
    result = {'email': 'tisisatest.comgamil', 'password': '66666'}
    auth_logout(result)
    assert result == {'email': 'tisisatest.comgamil', 'password': '66666'}

