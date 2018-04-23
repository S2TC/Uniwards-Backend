import ResponseHandle, SQLHandle

def GetVendorByID(vendor_id):
    temp_vendor = SQLHandle.vendor.query.filter_by(vendor_id=vendor_id).first()
    if(temp_vendor is not None):
        response = ResponseHandle.GenerateVendorResponse(temp_vendor)
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')
    return response



def GetVendors():
    temp_vendors = SQLHandle.vendor.query.all()
    vendor_list = SQLHandle.GetListOfRows(temp_vendors)
    if (vendor_list is not None):
        if(len(vendor_list) > 0):
            response = ResponseHandle.GenerateVendorsResponse(vendor_list)
        else:
            response = ResponseHandle.GenerateResponse('vendor_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')

    return response


def GetVendorsByType(type):
    temp_vendors = SQLHandle.vendor.query.filter_by(type=type)
    vendor_list = SQLHandle.GetListOfRows(temp_vendors)
    if (vendor_list is not None):
        if(len(vendor_list) > 0):
            response = ResponseHandle.GenerateVendorsResponse(vendor_list)
        else:
            response = ResponseHandle.GenerateResponse('vendor_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('vendor_get_failed')

    return response


def RegisterVendor(req_data):
    temp_vendor = SQLHandle.vendor(name=req_data['name'], mobile=req_data['mobile'],
                                           website=req_data['website'], type=req_data['type'],
                                           email=req_data['email'])
    if(SQLHandle.InsertRowObject(temp_vendor)):
        response = ResponseHandle.GenerateResponse('vendor_register_success')
    else:
        response = ResponseHandle.GenerateResponse('vendor_register_failed')
    return response


def UpdateVendor(req_data):
    pass


def DeleteVendor(req_data):
    pass
