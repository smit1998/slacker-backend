data = {
    'user_info': [
    {
        'u_id':'', 
        'email':'',
        'password':'',
        'name_first':'',
        'name_last':'',
        'token':'',
        'handle_str':'',
        'profile_img_url':'',
        'permission_id':'',  # 1: Slackr Owner, 2: Slackr Admin, 3: Member (Default)
        'reset_code':''
    }],

    'channel_info': [
    {
        'name':'',
        'channel_id':'',
        'owner_members':[{''}],
        'all_members':[{''}],
        'is_public':''
    }],

    'message_info': [
    {
        'message_id':'',
        'message':'',
        'react_id':'', # 0: No react, 1: Reacted
        'is_pinned':'', # 0: Not pinned, 1: Pinned
        'sender':'', # The person that sends the message
        'channel_id':'', # The channel that the message is in
        'time_created':''
    }]
}