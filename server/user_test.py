import pytest

# test user_profile(....) function and return the valid user's information 
def test_user_profile1():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    basic_info = user_profile('easy easy easy', 23)
    # what's the handle_str ? ? ? ?
    assert basic_info == {'email': 'andyWei326@gmail.com', 'name_first': 'Andy', 'name_last': 'Wei', 'handle_str': 'change'}
    
# when user is invalid, valueError would happen
def test_user_profile2():
    result = auth_login('andyWei326@gmail.com', '224232r4')
    assert result['token'] == 'easy easy easy'
    assert result['u_id'] == 23
    with pytest.raises(ValueError):
        user_profile('easy easy easy', 34)
       

    
