import pytest
import backend.backend_functions as BF

# when both of email and password are valid, return the valid token
def test_auth_register_both_valid01():
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    assert authRegisterDic['token'] == BF.generateToken(1)
    assert authRegisterDic['u_id'] == 1
    
# when the email is valid and password is inva lid, print error message
def test_auth_register_password_invalid():
    with pytest.raises(BF.ValueError):
        BF.user_register('andyWei326@gmail.com', '2242', 'Andy', 'Wei')
        
# when the password is valid and email is invalid, print error message
def test_auth_register_email_invalid(): 
    with pytest.raises(BF.ValueError):
        BF.user_register('1337memesgmail.com', '123243223', 'Andy', 'Wei') 
    
# when both of email and password are invalid, print error message
def test_auth_register_both_invalid(): 
    with pytest.raises(BF.ValueError):
        BF.user_register('tisisatest.comgamil', '66666', 'Andy', 'Wei') 

# when both of email and password are valid
def test_auth_login_both_valid01():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.user_login('2199009762@qq.com', '1234567')
    assert result['token'] == authRegisterDic['token']
    assert result['u_id'] == authRegisterDic['u_id']

# when the email is valid and password is invalid, print error message
def test_auth_login_password_invalid():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    with pytest.raises(BF.ValueError):
        BF.user_login('2199009762@qq.com', '2242')
      
# when the password is valid and email is invalid, print error message
def test_auth_login_email_invalid(): 
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    with pytest.raises(BF.ValueError):
        BF.user_login('1337memesgmail.com', '1234567') 
   
# when email you typed is not belonging to user
def test_auth_login_email_is_not_user_invalid(): 
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    with pytest.raises(BF.ValueError):
        BF.user_login('yesyesyes@unsw.edu.au', '123456')
        
# invalidating the authorized user, return True
def test_auth_logout_validate_user():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    return_flag = BF.user_logout(authRegisterDic['token'])
    assert return_flag['is_success'] == True
   
# the token is invalide, return False
def test_auth_logout_token_invalid01():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    authRegisterDic_02 = BF.user_register('AndyWei@unsw.edu.au', '6666666', 'Andrew', 'Wei')
    if(authRegisterDic['u_id'] == 1):
        return_flag = BF.user_logout(authRegisterDic_02['token'])
        assert return_flag['is_success'] == False
    
