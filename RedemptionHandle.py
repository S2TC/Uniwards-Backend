import ResponseHandle, SQLHandle
from dateutil import parser

def GetRedemptionByID(redemption_id):
    temp_redemption = SQLHandle.redemption.query.filter_by(id=redemption_id).first()
    if(temp_redemption is not None):
        response = ResponseHandle.GenerateRedemptionResponse("redemption_get_success", temp_redemption.todict())
    else:
        response = ResponseHandle.GenerateResponse('redemption_get_failed')
    return response

def GetRedemptionsByStudentID(student_id):
    temp_redemptions = SQLHandle.redemption.query.filter_by(student_id=student_id)
    redemption_list = SQLHandle.GetListOfRows(temp_redemptions)
    if (redemption_list is not None):
        if(len(redemption_list) > 0):
            response = ResponseHandle.GenerateRedemptionsResponse("redemption_get_success", redemption_list)
        else:
            response = ResponseHandle.GenerateResponse('redemption_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('redemption_get_failed')

    return response


def GetRedemptionsByCouponID(coupon_id):
    temp_redemptions = SQLHandle.redemption.query.filter_by(coupon_id=coupon_id)
    redemption_list = SQLHandle.GetListOfRows(temp_redemptions)
    if (redemption_list is not None):
        if(len(redemption_list) > 0):
            response = ResponseHandle.GenerateRedemptionsResponse("redemption_get_success", redemption_list)
        else:
            response = ResponseHandle.GenerateResponse('redemption_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('redemption_get_failed')

    return response


def GetRedemptions():
    temp_redemptions = SQLHandle.redemption.query.all()
    redemption_list = SQLHandle.GetListOfRows(temp_redemptions)
    if (redemption_list is not None):
        if(len(redemption_list) > 0):
            response = ResponseHandle.GenerateRedemptionsResponse("redemption_get_success", redemption_list)
        else:
            response = ResponseHandle.GenerateResponse('redemption_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('redemption_get_failed')

    return response


def CreateRedemption(req_data):
    parsed_date = parser.parse(req_data['date'])
    temp_redemption = SQLHandle.redemption(date=parsed_date, student_id=req_data['student_id'],
                                           coupon_id=req_data['coupon_id'])
    if(SQLHandle.InsertRowObject(temp_redemption)):
        response = ResponseHandle.GenerateResponse('redemption_register_success')
    else:
        response = ResponseHandle.GenerateResponse('redemption_register_failed')
    return response


def UpdateRedemption(req_data):
    pass


def DeleteRedemption(req_data):
    pass
