import pytest
<<<<<<< HEAD
from Andy_first_iteration_stub import *
=======
from Andy_backend_functions import *
>>>>>>> Andy

# test user_profile function and return the valid user's information 
def test_user_profile_valid_user():
    data['user_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = user_profile(authRegisterDic['token'], authRegisterDic['u_id'])
    resetUser_id(authRegisterDic['u_id'])
    assert result['email'] == '2199009762@qq.com'
    assert result['name_first'] == 'Andy'
    assert result['name_last'] == 'Wei'
    assert result['handle_str'] == 'TEAM WORK'
   
# when user_id is invalid
def test_user_profile_invalid_user_id():
    data['user_info'] = []
    authRegisterDic = user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    with pytest.raises(ValueError):
        user_profile(authRegisterDic['token'], 2)
      
