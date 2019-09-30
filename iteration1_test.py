import pytest 
import re

class token:
    def __init__(self, email, password):
        self.email = email
        self.password = password 

# What's the functionality of regex
regex = 'sfjkngklsmbv@sf'   
        
def auth_login(email, password):
    
    if(re.search(regex, email)):
        raise Exception('Invalide email')
    else:
        if (len(password) < 5):
            raise Exception('Invalide password')
        else:
            p1 = token(email, password)
    return p1
    
    
def auth_logout(token):
    if (token.email == 


def auth_register(email, password, name_first, name_last):
    

kjew




def test_1():
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result.email == 'ankitrai326@gmail.com'
    assert result.password == '224232r4'
    auth_logout(result)

'''def test_2():
    result = auth_login('219900Andy.Wei', 'er22r2222')
    assert result.email == 'Invalid email'
    assert result.password == 'er22r2222'
'''

'''def test_3():
    result = auth_login('200023Andy@.com', '1234')
    assert result.email == '200023Andy@.com'
    assert result.password == 'Invalid password'

    
    
