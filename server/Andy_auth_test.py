import pytest
import dummy_error import AccessError

# when both of email and password are valid, return the valid token
def test_auth_login_both_valid01():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23

# when the email is valid and password is invalid, print error message
def test_auth_login_password_invalid():
    with pytest.raises(ValueError):
        auth_login('andyWei326@gmail.com', '2242')
        
# when the password is valid and email is invalid, print error message
def test_auth_login_email_invalid(): 
    with pytest.raises(ValueError):
        auth_login('1337memesgmail.com', '123243223') 
    
# when both of email and password are invalid, print error message
def test_auth_login_both_invalid(): 
    with pytest.raises(ValueError):
        auth_login('tisisatest.comgamil', '66666') 

# when both of email and password are valid, return the valid token
def test_auth_login_both_valid02():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66

# invalidating the authorized user 
def test_auth_logout_invalidate_user():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    auth_logout('easy easy easy')
    assert result == {}

# the token is invalide, nothing should be changed
def test_auth_logout_token_invalid01():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    auth_logout('really funny_123')
    assert result == {"u_id": 23, "token": 'easy easy easy'}

# the token is invalide, nothing should be changed
def test_auth_logout_token_invalid02():
    result = auth_login('2199009762@qq.com', '123456q789')
    assert result['token'] == 'right user'
    assert result['u_id'] == 66
    auth_logout('what should i do')
    assert result == {'u_id': 66, 'token': 'right user'}
        
