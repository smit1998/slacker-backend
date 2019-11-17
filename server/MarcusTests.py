import pytest 
import re
import backend_functions as BF


# assumptions:
# 1. The list of owners are also in the list of members of a channel
# 2. All users can view the list of members in a public channel

def test_channels_create_valid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    BF.resetUser_id()
    assert result['channel_id'] == 1

def test_channels_create_invalid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    BF.resetUser_id()
    with pytest.raises(BF.ValueError):
        BF.channels_create(authRegisterDic['token'], 'good team we are good is right ???', True)

def test_channels_list_no_channel1():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']
    assert BF.channels_list(token1) == {'channels': []}

def test_channels_list_one_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']
    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    assert BF.channels_list(token1) == {'channels': [1, 'Channel 1']}

def test_channels_list_two_channels():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict1 = BF.channels_create(token1, 'Channel 1', False)
    channelID1 = channelsCreateDict1['channel_id']

    channelsCreateDict2 = BF.channels_create(token1, 'Channel 2', False)
    channelID2 = channelsCreateDict2['channel_id']

    assert BF.channels_list(token1) == {
        'channels': [1, 'Channel 1', 2, 'Channel 2']
    }

def test_channels_list_no_channel2():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    assert BF.channels_list(token2) == {'channels': []}

def test_channels_listall_no_channel1():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']
    assert BF.channels_listall(token1) == {'channels': []}

def test_channels_listall_one_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    assert BF.channels_listall(token1) == {'channels': [1, 'Channel 1']}

def test_channels_listall_two_channels():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict1 = BF.channels_create(token1, 'Channel 1', True)
    channelID1 = channelsCreateDict1['channel_id']

    channelsCreateDict2 = BF.channels_create(token1, 'Channel 2', True)
    channelID2 = channelsCreateDict2['channel_id']

    assert BF.channels_listall(token1) == {
        'channels': [1, 'Channel 1', 2, 'Channel 2']
    }

def test_channels_listall_not_in_the_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']
    
    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    assert BF.channels_list(token2) == {'channels': []}

def test_channels_create_valid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    
    assert BF.channel_details(token1, channelID) == {
        'name': 'Channel 1',
        'all_members': [{'name_first': 'real', 'name_last': 'bot', 'u_id': 1}],
        'owner_members': [{'name_first': 'real', 'name_last': 'bot', 'u_id': 1}]
    }

def test_channels_create_long_name():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    with pytest.raises(BF.ValueError):
        channelsCreateDict = BF.channels_create(token1, 'abcdefghijklmnopqrstuvwxyz', True)

def test_message_remove_valid():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")
    BF.message_remove(token1, messageDict['message_id'])    

def test_message_remove_message_doesnt_exist():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_remove(token1, messageDict['message_id'])
    with pytest.raises(BF.ValueError):
        BF.message_remove(token1, messageDict['message_id'])

def test_message_remove_no_permission():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.AccessError):
        BF.message_remove(token2, messageDict['message_id'])

def test_message_react_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_react(token1, random_message_id, 1)

def test_message_react_invalid_react():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    invalidReactID = -420
    with pytest.raises(BF.ValueError):
        BF.message_react(token1, messageDict['message_id'], invalidReactID)

def test_message_react_already_reacted():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_react(token1, messageDict['message_id'], 1)
    with pytest.raises(BF.ValueError):
        BF.message_react(token1, messageDict['message_id'], 1)

def test_message_unreact_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, random_message_id, 1)

def test_message_unreact_invalid_react():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    invalidReactID = -420
    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, messageDict['message_id'], invalidReactID)

def test_message_unreact_no_active_react():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.ValueError):
        BF.message_unreact(token1, messageDict['message_id'], 1)

def test_message_pin_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    random_message_id = 23

    with pytest.raises(BF.ValueError):
        BF.message_pin(token1, random_message_id)

def test_message_pin_not_admin():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.ValueError):
        BF.message_pin(token2, messageDict['message_id'])

def test_message_pin_already_pinned():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_pin(token1, messageDict['message_id'])
    with pytest.raises(BF.ValueError):
        BF.message_pin(token1, messageDict['message_id'])

def test_message_pin_not_member():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()

    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    authRegisterDict2 = BF.user_register('bot2@gmail.com', '1234567', 'real2', 'bot2')
    token2 = authRegisterDict2['token']

    assert token1 != token2

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    with pytest.raises(BF.AccessError):
        BF.message_pin(token2, messageDict['message_id'])
'''
def test_message_unpin_invalid_message():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    with pytest.raises(BF.ValueError):
        BF.message_unpin(token1, random_message_id)
def test_message_unpin_not_admin():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    BF.channel_join(token2, channelID)

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_pin(token1, messageDict['message_id'])
    with pytest.raises(BF.ValueError):
        BF.message_unpin(token2, messageDict['message_id'])

def test_message_unpin_already_unpinned():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_pin(token1, messageDict['message_id'])
    BF.message_unpin(token1, messageDict['message_id'])
    with pytest.raises(BF.ValueError):
        BF.message_unpin(token1, messageDict['message_id'])

def test_message_unpin_not_member():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    BF.resetUser_id()
    BF.resetChannel_id()
    BF.resetMessage_id()
    authRegisterDict1 = BF.user_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = BF.user_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = BF.channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    messageDict = BF.message_send(token1, channelID, "Hello World")

    BF.message_pin(token1, messageDict['message_id'])
    with pytest.raises(AccessError, match=r"*"):
        BF.message_unpin(token2, messageDict['message_id'])
'''