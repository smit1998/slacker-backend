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
        raise Exception('Invalide email')
    else:
        if (len(password) < 5):
            raise Exception('Invalide password')
        else:
            p1 = token(email, password)
    return p1
    
    
def test_1():
    result = auth_login('ankitrai326@gmail.com', '224232r4')
    assert result.email == 'ankitrai326@gmail.com'
    assert result.password == '224232r4'
    
    
    
