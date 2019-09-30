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
        print('valid email')
    else:
        raise Exception('Invalid email')
        
    if (len(password) < 5):
        raise Exception('Invalid password')
    else:
        p1 = token(email, password)
    return p1
    
    
<<<<<<< HEAD
def auth_logout(token):
    if (token.email == 


def auth_register(email, password, name_first, name_last):
    






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

=======
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
>>>>>>> d2958806598942a08e68bdf5857258c9fc6c4318
    
def test_3(): #this tests the email if statement (vaild) 
    result = auth_login('thisisatest.com@gamil', '54351222')
    #assert result.email == 'thisisatest.com@gamil' 
    assert result.password == '54351222'
    pass 


