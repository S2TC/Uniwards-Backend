import ResponseHandle, SQLHandle

def GetUniclassByName(name):
    temp_uniclass = SQLHandle.uniclass.query.filter_by(name=name).first()
    if(temp_uniclass is not None):
        response = ResponseHandle.GenerateUniclassResponse("uniclass_get_success", temp_uniclass.todict())
    else:
        response = ResponseHandle.GenerateResponse('uniclass_get_failed')
    return response



def GetUniclasses():
    temp_uniclasses = SQLHandle.uniclass.query.all()
    uniclass_list = SQLHandle.GetListOfRows(temp_uniclasses)
    if (uniclass_list is not None):
        if(len(uniclass_list) > 0):
            response = ResponseHandle.GenerateUniclassesResponse("uniclass_get_success", uniclass_list)
        else:
            response = ResponseHandle.GenerateResponse('uniclass_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('uniclass_get_failed')

    return response


def GetUniclassesByTutorID(tutor_id):
    temp_uniclasses = SQLHandle.uniclass.query.filter_by(tutor_id=tutor_id)
    uniclass_list = SQLHandle.GetListOfRows(temp_uniclasses)
    if (uniclass_list is not None):
        if(len(uniclass_list) > 0):
            response = ResponseHandle.GenerateUniclassesResponse("uniclass_get_success", uniclass_list)
        else:
            response = ResponseHandle.GenerateResponse('uniclass_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('uniclass_get_failed')

    return response

def GetUniclassesByUniID(uni_id):
    temp_uniclasses = SQLHandle.uniclass.query.filter_by(id=uni_id)
    uniclass_list = SQLHandle.GetListOfRows(temp_uniclasses)
    if (uniclass_list is not None):
        if(len(uniclass_list) > 0):
            response = ResponseHandle.GenerateUniclassesResponse("uniclass_get_success", uniclass_list)
        else:
            response = ResponseHandle.GenerateResponse('uniclass_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('uniclass_get_failed')

    return response

def RegisterUniclass(req_data):
    temp_uniclass = SQLHandle.uniclass(name=req_data['name'], tutor_id=req_data['tutor_id'],
                                           id=req_data['id'])
    if(SQLHandle.InsertRowObject(temp_uniclass)):
        response = ResponseHandle.GenerateResponse('uniclass_register_success')
    else:
        response = ResponseHandle.GenerateResponse('uniclass_register_failed')
    return response


def UpdateUniclass(req_data):
    pass


def DeleteUniclass(req_data):
    pass