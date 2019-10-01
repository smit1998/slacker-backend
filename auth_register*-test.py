'''
import pytest 
import re

def auth_register(email,password,name_first,name_last): 
    
    





    #dictionarys = have no sence of order a clump of key value pairs (store data that 
    #makes sense to look up (kind of like structs)
    #userData = { 
     #'name' : 'sally', 
     #'age' : 18, 
     #'height' : '186cm',
   # }
    #userData['height'] = '187cm'
    #print(userData) 

#this tests if the email is already used by another user

        
        
        
'''        
        
        
        
        
        
  
def test_auth_register1(): 
    result = auth_register('memes@gmail.com', 'dankpassword121', 'Cameron', 'Burrell')
    token = 'this works' 
    assert result == {'token' : 'this works'} 
    
    pass

def test_auth_register2(): 
    result = auth_register('hello.com', 'stronkpassword123', 'John', 'Super')
    with.pytest.raises(ValueError):
        print ("Email entered is not a valid email")   
    
    pass 
    
def test_auth_register3():
    result = auth_register('ankitrai326@gmail.com', '224232r4', 'Andy', 'Wei')
    with.pytest.raises(ValueError):
        print('Email address is already being used by others') 
    
    pass 
    
def test_auth_register4():
    result = auth_register('correctemail@gmail.com', '123', 'ShortN', 'Sweet')
    with.pytest.raises(ValueError):
        print ("Password entered is not a valid password")  
    
    pass 

def test_auth_register5(): 
    result = auth_register('doyourfingershurt@hotmail.com', '324sf223', 'sdfsvsdbgsdvsvbnsdvnsdovosdnvodsnvosdnvodsvnsdvnsdvfwj', 'LongAssFirstName') 
    with.pytest.raises(ValueError):
        print ("name_first is more than 50 characters")  
    
    pass

def test_auth_register6(): 
    result = auth_register('donthateme@gmail.com', 'ihavegivenup232e', 'Joe', 'tehrhdbfsmohteojfblkdnfgojdvfjgbfgodbdljhpobfhfdjhpdrsdsvr')
    with.pytest.raises(ValueError):
        print ("name_last is more than 50 characters")  
        
    pass
