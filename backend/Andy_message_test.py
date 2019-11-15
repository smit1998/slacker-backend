import pytest
import backend_functions as BF


# when message is more than 1000 characters, just ValueError 
def test_message_send_many_characters():
    BF.data['user_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'isufhuierghvuwreidbvgiuedvgbreiwudvbciwrghv8734gvefuydbvuysvgbisudghvbufydbvuysbvjsfvbjsfvbjsfhvbsdjvbusfvbiudfbviudbviudvbiudbviudbvufdbvuhdiuyvbh8er7hc47byvfuysvbsiudveriusvberiudfbvndfiuybvdfiubvndiufybnvdfiuvnfdiuyvbnufidbvuedsfhgiesrhg98vndzoisfjwkpofskkver90sghfjvopaeDhvbniusdsifhnvwiusrkjdgniruedkfghviosrdghveriudfdghvnirudfgbvnvdiufxcjvndifudgkjvndtxifukbjvndtifdkjgnvdfikjxgnv fgukfjghmiukjfdgbv nuifjdfgjkbnidufkjbcnvifjkcbn ijkfbnvjkdfxkcnbvgjkfbcnvjk dgfmncb jgkffcbn vjkdfmcbn jxc,m xmnvc kdjfxcvnisfudkjkfjncifuxkcxvjndfjikcvkxnxfkjcvnmkfjxcvmkfxjcvndfjxkcvnmfsjxkcxvnjckxvmnfxkjcvmnfxjkcbnvkjxvcbmnvkjxvcbnjkcbvndgjkfcvbndfjkhbiufvdhiugjve98geouei09eroitlyugf9j;iowkaszorygHJfcpavluoetkl4rhs;zedbgunlivcekrdhfxzgjvo;ikrlgfjxdgvn kudfgisdklzxldjcbnzv okjvbsroghjeuroshjj803w4hgrjfwoirshgdfoiwrsgdjhfoivedthgvoielhdngvoierhgoivehrnfiouvnersoidvneoirsfbnvoirfnbvoirlfnvioersfhgnvoiernvoiedfnbvioe tdlkfbnvoibenbdvbioesrvnisneoinbveoisfnbvoielrsnfvoieskfndgvoielnsfdvpoengdoiversndoignerwspodzgklbnvwposfklhjbnmcpwosedl;xfghcnmvpowrdklfxbnmviogklfdngmvbiodfklxdgnvboi dgflxkdgnvbodifklxdngbiodfkxnbmopivdlkfxbnvopivdfklxcbnvoilskfnvdoisfkvnmiorsfkdjgviorsfhbnioedlfkxbnmoidlgknmbiopflkgcmnoilfkgdnboidgkjniobfgchnbtdghcnrtfgchnfgchtrtdthdthdthfbbdtfhbetdfhgbetdfhgbetdfhgtedhrtdhftdfhrtdhfryfghbdgfxhgtdfhrtdghtdgchrftghcrtdfhgdfgdfxgdxfgdtfxgetdfgdfgdrfgiorsjdgiorejsdg98uer98sdgj9erijg09erjg98jve98rfgjerfjgoierjfdgoivdjrfoidgjvriodfdgjvoirsdjfg98btsriuzdg0bjvoirshbnvmoiskdfxnbvmoifkxndgoivdkfndvoifkdngvviofkxncbiu jsfbnxcbvoijdgnfcvxoi kgnfiobkdnbikdnbijkdfnobknfboidfgbvrfcgvdfg'
    with pytest.raises(BF.ValueError):
        BF.message_send(authRegisterDic['token'], result['channel_id'], message)

# user sends message to the channel
def test_message_send_message_to_channel():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'how are you' 
    result = BF.message_send(authRegisterDic['token'], result['channel_id'], message)
    BF.resetMessage_id(result['message_id'])
    assert result['message_id'] == 1

# test message_sendlater channel_id is invalid
def test_message_sendlater():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    message = 'how are you' 
    with pytest.raises(BF.ValueError):
        BF.sendlater_message(authRegisterDic['token'], 1, message, 4596999)
 
# time sent is a time in the past
def test_message_sendlater():
    BF.data['user_info'] = []
    BF.data['channel_info'] = []
    BF.data['message_info'] = []
    authRegisterDic = BF.user_register('2199009762@qq.com', '1234567', 'Andy', 'Wei')
    result = BF.channels_create(authRegisterDic['token'], 'good team', True)
    message = 'how are you' 
    with pytest.raises(BF.ValueError):
        BF.sendlater_message(authRegisterDic['token'], result['channel_id'], message, 1242523)
        

