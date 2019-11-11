for channel in data['channels']:
        for user in channel['owner_members']:
            if user == token:
                channel['owner_members'].remove(user)
                if p_id == 'admin_members':
                    channel['admin_members'].append(user)
                else:
                    channel['all_members'].append(user)
        for user in channel['admin_members']:
            if user == token and p_id != 'admin_members':
                channel['admin_members'].remove(user)
                if p_id == 'owner_members':
                    channel['owner_mambers'].append(user)
                else:
                    channel['all_members'].append(user)