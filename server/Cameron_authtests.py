import pytest  
from Error import AccessError 

def test_auth_register_valid_token():  
    register_details = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    token = register_details['token']
    assert validToken(token) == True
   
def test_auth_register_correctemail(): 
    with pytest.raises(ValueError):
        auth_register('hello.com', 'stronkpassword123', 'John', 'Super')
       
def test_auth_register_emailused():
    auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')
    with pytest.raises(ValueError):
        auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')
   
def test_auth_register_password_length():
    with pytest.raises(ValueError):
        auth_register('correctemail@gmail.com', '123', 'ShortN', 'Sweet')
       
def test_auth_register_first_name(): 
    with pytest.raises(ValueError):
        auth_register('doyourfingershurt@hotmail.com', '324sf223', 'sdfsvsdbgsdvsvbnsdvnsdovosdnvodsnvosdnvodsvnsdvnsdvfwj', 'LongAssFirstName')
    
def test_auth_register_last_name(): 
    with pytest.raises(ValueError):
        auth_register('donthateme@gmail.com', 'ihavegivenup232e', 'Joe', 'tehrhdbfsmohteojfblkdnfgojdvfjgbfgodbdljhpobfhfdjhpdrsdsvr') 
        
def test_auth_passwordrest_request_registered_user():
    token = auth_register('human@gmail.com', '12323452', 'legit', 'human')
    assert validToken(token) == True
    auth_passwordreset_request('human@gmail.com') 
    with pytest.raises(ValueError):
        auth_passwordreset_request('nonhumanperson@gmail.com')
        
def test_auth_passwordreset_reset_works(): 
    assert validCode(reset_code) == True 
    assert (len(new_password) >= 5)

def test_auth_passwordreset_reset_invalid_code(): 
    assert validCode(reset_code) == False
    with pytest.raises(ValueError)
        auth_passwordreset_reset(reset_code, new_password)

def test_auth_passwordreset_reset_invalid_password(): 
    assert (len(new_password) < 5) 
    with pytest.raises(ValueError)
        auth_passwordreset_reset(reset_code, new_password)

