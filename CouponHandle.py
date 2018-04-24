import ResponseHandle, SQLHandle

def GetCouponByID(coupon_id):
    temp_coupon = SQLHandle.coupon.query.filter_by(coupon_id=coupon_id).first()
    if(temp_coupon is not None):
        response = ResponseHandle.GenerateCouponResponse(temp_coupon)
    else:
        response = ResponseHandle.GenerateResponse('coupon_get_failed')
    return response


def GetCouponByVendor(vendor_id):
    temp_coupon = SQLHandle.coupon.query.filter_by(vendor_id=vendor_id).first()
    if(temp_coupon is not None):
        response = ResponseHandle.GenerateCouponResponse(temp_coupon)
    else:
        response = ResponseHandle.GenerateResponse('coupon_get_failed')

    return response


def GetCoupons():
    temp_coupons = SQLHandle.coupon.query.all()
    coupon_list = SQLHandle.GetListOfRows(temp_coupons)
    if (coupon_list is not None):
        if(len(coupon_list) > 0):
            #if(start < len(coupon_list) and end < len(coupon_list)):
            response = ResponseHandle.GenerateUCouponsResponse(coupon_list)
        else:
            response = ResponseHandle.GenerateResponse('coupon_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('coupon_get_failed')

    return response


def CreateCoupon(req_data):
    temp_coupon = SQLHandle.coupon(name=req_data['name'], code=req_data['code'],
                                           expiry=req_data['expiry'], desc=req_data['desc'],
                                           point_cost=req_data['point_cost'], vendor_id=req_data['vendor_id'])
    if(SQLHandle.InsertRowObject(temp_coupon)):
        response = ResponseHandle.GenerateResponse('coupon_register_success')
    else:
        response = ResponseHandle.GenerateResponse('coupon_register_failed')
    return response


def UpdateCoupon(req_data):
    pass


def DeleteCoupon(req_data):
    pass

