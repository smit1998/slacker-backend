Comp1531 project planning markdown
    The following plan has been discussed by our team on how to approach the project requirements and time deadlines have been marked accordingly.

Written format:
    
    -Functions to be done in week 4:-
        Auth_login
        Auth_logout
        Auth_register
        Auth_passwordreset_request
        Auth_passwordreset_reset
        User_profile
        User_profile_setname
        user_profile_setemail
        User_profile_sethandle
        User_profiles_uploadphoto
    -Functions to be done in week 5:-
        Channel_messages
        Channel_details
        Channel_invite
        Channel_leave
        Channel_join
        Channel_addowner
        Channel_removeowner
        Channels_list
        Channels_listall
        Channels_create
        Message_sendlater
        Message_send
        Message_remove
        Message_edit
    -Functions to do in week 6:-
        Standup_start
        Standup_send
        Search
        Admin_userpermission_change
        Message_react
        Message_unreact
        Message_pin
        message_unpin

    -Function testing and bug resolving during week 7.
    -Weekly meetings to discuss the code and the progress of the prooject.
    -Constant discussion of project progress on discord.
    
    We decided on this order of function implementation based on the importance of each category of functions.
    Since channel creation requires a user token, authentication forms the basis for the development of other functions.
    When creating Channels tokens need to be given to be able to check things like who is the owner of the channel.
    Hence they should be developed after user as messages can only be utilised within channels.
    Other miscellaneous functions such as ‘Search’ can be developed later as we deem them to be less significant in comparison to other core features.
    As there are around five functions under each category, we estimate that the time required for each category will be roughly equal.
    But acknowledge that during the initial build more time should be allocated to the channels and authentication.
    Each week there will be two team meetings, one code meeting and the other developer meetings,
    in the developer meetings we will talk about what we are up to, what needs to be done
    and if there are any user requirement updates. For code meetings, we will conduct code review to improve efficiency and optimize each others work.
    This code review session will mostly happen over codeshare where we will demonstrate the features that we are working on,
    during these sessions we will explain what our features do,
    discuss if extra time is required and to make sure everyone is on the same page. 

Diagram Format:
        Authentication functions ->UserProflie functions->Message functions->remaining functions

