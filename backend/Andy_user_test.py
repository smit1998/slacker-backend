import pytest
import backend.backend_functions as BF


# test user_profile function and return the valid user's information 
def test_user_profile_valid_user():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.user_profile(authRegisterDic['token'], authRegisterDic['u_id'])
    BF.resetUser_id(authRegisterDic['u_id'])
    assert result['email'] == '2199009762@qq.com'
    assert result['name_first'] == 'Andy'
    assert result['name_last'] == 'Wei'
    assert result['handle_str'] == 'TEAM WORK'
   
# when user_id is invalid
def test_user_profile_invalid_user_id():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    with pytest.raises(BF.ValueError):
        BF.user_profile(authRegisterDic['token'], 2)
      
