import copy

def merge_and_clean(profile_list, post_list):
    profile_list_copy = copy.deepcopy(profile_list)
    fix_list = []
    for neg_followers in profile_list_copy:
        try:
            neg_followers['followers'] = int(neg_followers['followers'])
            if not neg_followers['followers'] < 0:
                fix_list.append(neg_followers)
        except:
            ValueError
            continue

    exist_users = []
    for users1 in fix_list:
        for users2 in post_list:
            if users1['user'] == users2['user']:
                exist_users.append(users1 | users2)

    return exist_users


def calculate_metrics(cleaned_data):
    total_scores = []
    final_list = []
    for items in cleaned_data:  
        score = (items['likes'] + items['comments']) / items['followers']
        total_scores.append({'user': items['user'], 'score' : round(score, 2)}) 


    for users in cleaned_data:
        for scores in total_scores:
            if users['user'] == scores['user']:
                 final_list.append(users | scores)

    return(final_list)


def generate_report(final_data):
    influencers = []
    high_rate = []
    best =[]
    for highest in final_data:
        influencers.append({'top influencer': highest['user'], 'average engagement' : highest['score']})
        high_rate.append(highest['score'])
    highest = max(high_rate)
    for users in influencers:
        if users['average engagement'] == highest:
            best.append(users)
    
    return best

