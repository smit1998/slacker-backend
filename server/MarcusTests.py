import pytest 
import re

from Error import AccessError

# assumptions:
# 1. The list of owners are also in the list of members of a channel
# 2. A 'Like' react has a 'reactID' equal to 1
# 3. Only owners and admins can pin messages in their respective channels
# 4. All users can view the list of members in a public channel

def test_channels_list_no_channel1():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']
    assert channels_list(token1) == {}

def test_channels_list_one_channel():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    assert channels_list(token1) == {'channelID': channelID, 'name': 'Channel 1'}

def test_channels_list_two_channels():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict1 = channels_create(token1, 'Channel 1', False)
    channelID1 = channelsCreateDict1['channel_id']

    channelsCreateDict2 = channels_create(token1, 'Channel 2', False)
    channelID2 = channelsCreateDict2['channel_id']

    assert channels_list(token1) == {
        'channelID': channelID1, 'name': 'Channel 1', 'channelID': channelID2, 'name': 'Channel 2'
    }

def test_channels_list_no_channel2():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    assert channels_list(token2) == {}

def test_channels_listall_no_channel1():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']
    assert channels_listall(token1) == {}

def test_channels_listall_one_channel():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    assert channels_listall(token1) == {'channelID': channelID, 'name': 'Channel 1'}

def test_channels_listall_two_channels():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict1 = channels_create(token1, 'Channel 1', True)
    channelID1 = channelsCreateDict1['channel_id']

    channelsCreateDict2 = channels_create(token1, 'channel 2', True)
    channelID2 = channelsCreateDict2['channel_id']

    assert channels_listall(token1) == {
        'channelID': channelID1, 'name': 'Channel 1', 'channelID': channelID2, 'name': 'Channel 2'
    }

def test_channels_listall_not_in_the_channel():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']
    
    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    assert channels_list(token2) == {'channelID': channelID, 'name': 'Channel 1'}

def test_channels_create_valid():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    
    assert channel_details(token1, channelID) == {'Channel 1', 'real', 'real'}

def test_channels_create_long_name()
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    with pytest.raises(ValueError):
        channelsCreateDict = channels_create(token1, 'abcdefghijklmnopqrstuvwxyz', True)

def test_message_remove_valid():
    authRegisterDict = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")

def test_message_remove_message_doesnt_exist():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    message_remove(token1, messageID)
    with pytest.raises(AccessError, match=r"*"):
        message_remove(token1, messageID)

def test_message_remove_no_permission():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    with pytest.raises(AccessError, match=r"*"):
        message_remove(token2, messageID)

def test_message_react_invalid_message():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    reactID = 1
    with pytest.raises(ValueError):
        message_react(token1, random_message_id, reactID)

def test_message_react_invalid_react():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    invalidReactID = -420
    with pytest.raises(ValueError):
        message_react(token1, messageID, invalidReactID)

def test_message_react_already_reacted():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    reactID = 1
    message_react(token1, messageID, reactID)
    with pytest.raises(ValueError):
        message_react(token1, messageID, reactID)

def test_message_unreact_invalid_message():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    unreactID = 0
    with pytest.raises(ValueError):
        message_unreact(token1, random_message_id, unreactID)

def test_message_unreact_invalid_react():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    invalidReactID = -420
    with pytest.raises(ValueError):
        message_unreact(token1, messageID, invalidReactID)

def test_message_unreact_no_active_react():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    unreactID = 0
    with pytest.raises(ValueError):
        message_unreact(token1, messageID, unreactID)

def test_message_pin_invalid_message():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    with pytest.raises(ValueError):
        message_pin(token1, random_message_id)

def test_message_pin_not_admin():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    with pytest.raises(ValueError):
        message_pin(token2, messageID)

def test_message_pin_already_pinned():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    message_pin(token1, messageID)
    with pytest.raises(ValueError):
        message_pin(token1, messageID)

def test_message_pin_not_member():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    with pytest.raises(AccessError, match=r"*"):
        message_pin(token2, messageID)

def test_message_unpin_invalid_message():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    with pytest.raises(ValueError):
        message_unpin(token1, random_message_id)
def test_message_unpin_not_admin():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']
    channel_join(token2, channelID)

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    message_pin(token1, messageID)
    with pytest.raises(ValueError):
        message_unpin(token2, messageID)

def test_message_unpin_already_unpinned():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', True)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    message_pin(token1, messageID)
    message_unpin(token1, messageID)
    with pytest.raises(ValueError):
        message_unpin(token1, messageID)

def test_message_unpin_not_member():
    authRegisterDict1 = auth_register('bot@gmail.com', '123456', 'real', 'bot')
    token1 = authRegisterDict1['token']
    authRegisterDict2 = auth_register('bot2@gmail.com', '123456', 'real', 'bot2')
    token2 = authRegisterDict2['token']

    channelsCreateDict = channels_create(token1, 'Channel 1', False)
    channelID = channelsCreateDict['channel_id']

    message_send(token1, channelID, "Hello World")
    channels_messages_dict = channels_messages(token1, channelID, 0)
    messageID = channels_messages_dict['message_id']

    message_pin(token1, messageID)
    with pytest.raises(AccessError, match=r"*"):
        message_unpin(token2, messageID)