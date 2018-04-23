import ResponseHandle, SQLHandle

def GetRewardByID(reward_id):
    temp_reward = SQLHandle.reward.query.filter_by(reward_id=reward_id).first()
    if(temp_reward is not None):
        response = ResponseHandle.GenerateRewardResponse(temp_reward)
    else:
        response = ResponseHandle.GenerateResponse('reward_get_failed')
    return response


def GetRewards():
    temp_rewards = SQLHandle.reward.query.all()
    reward_list = SQLHandle.GetListOfRows(temp_rewards)
    if(reward_list is not None):
        if(len(reward_list) > 0):
            response = ResponseHandle.GenerateRewardsResponse(reward_list)
        else:
            response = ResponseHandle.GenerateResponse('reward_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('reward_get_failed')

    return response

def GetRewardsByTier(tier):
    temp_rewards = SQLHandle.reward.query.filter_by(tier=tier)
    reward_list = SQLHandle.GetListOfRows(temp_rewards)
    if(reward_list is not None):
        if(len(reward_list) > 0):
            response = ResponseHandle.GenerateRewardsResponse(reward_list)
        else:
            response = ResponseHandle.GenerateResponse('reward_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('reward_get_failed')

    return response


def RegisterReward(req_data):
    temp_reward = SQLHandle.reward(name=req_data['name'], value=req_data['value'],
                                           requirement=req_data['requirement'],
                                           type=req_data['point_cost'], tier=req_data['vendor_id'], desc=req_data['desc'])
    if(SQLHandle.InsertRowObject(temp_reward)):
        response = ResponseHandle.GenerateResponse('reward_register_success')
    else:
        response = ResponseHandle.GenerateResponse('reward_register_failed')
    return response


def UpdateReward(req_data):
    pass


def DeleteReward(req_data):
    pass