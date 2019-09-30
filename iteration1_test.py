import pytest 
import re

class token:
    def __init__(self, email, password):
        self.email = email
        self.password = password 
         
    
        
def auth_login(email, password):
    # What's the functionality of regex
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        print('valid email')
    else:
        raise Exception('Invalid email')
        
    if (len(password) < 5):
        raise Exception('Invalid password')
    else:
        p1 = token(email, password)
    return p1
    
    
def test_1(): #this tests if the code works 
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result.email == 'ankitrai326@gmail.com'
    assert result.password == '224232r4'
    pass 
    
def test_2(): # this tests the password if statement < 5
    result = auth_login('1337memes@gmail.com', '123') 
    assert result.email == '1337memes@gmail.com' 
    #assert result.password == '123' 
    pass
    
def test_3(): #this tests the email if statement (vaild) 
    result = auth_login('thisisatest.com@gamil', '54351222')
    #assert result.email == 'thisisatest.com@gamil' 
    assert result.password == '54351222'
    pass 

