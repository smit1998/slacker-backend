#smit
1. The given email and password should be correct for user_profile_setname
    and user must be registered first.
2. The new email can not be null and can not be same as the current email for user_setemail
user first and last names are less than 50.
#andy
3. So in the function channel_create(), can we let one user to create more than one channel ?
4. So in the function message_sendlater(), the date should be like the time when another         channel 
   should be received messages, or should be the time channel send the message to another channel
5. When it comes to private or public, so if the name of channel would be private, is it 
    meaning that the name would only be private to the people who are not in this channel, or
    it is also private to the people who are in the channel
6. Authorized user can send a message to a channel, even though this user still not in this      channel
7. Only authorized user who was in this channel can send the message to the channel
#cameron
8. I assume that when a person leaves a channel they are not a member anymore so if the          channel is private they have to be added back and inviting someone makes them a memeber 
9. Auth_addowner / remove owner assume only someone that is currently an owner has this power
10. Assume the owner/admin to the slack is the developer and the channel owner is just people     that run the channel 
11. If someone is made an admin, assume that they can join in channels that are private when      they have not been invited to them 
#marcus
12.The list of owners should also in the list of members of a channel.
13. A 'Like' react has a 'reactID' equal to 1.
14. An unreact has a 'reactID' equal to 0.
15. Only owners and admins can pin messages in their respective channels.
16. All users can view the list of members in a public channel.
17. Only members of a private channel and view the list of members in that channel.
