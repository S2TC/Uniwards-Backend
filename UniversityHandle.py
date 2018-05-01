import ResponseHandle, SQLHandle

def GetUniversity(uni_code):
    temp_university = SQLHandle.university.query.filter_by(uni_code=uni_code).first()
    if(temp_university is not None):
        response = ResponseHandle.GenerateUniversityResponse("university_get_success", temp_university.todict())
    else:
        response = ResponseHandle.GenerateResponse('university_get_failed')
    return response


def GetUniversities():
    temp_universities = SQLHandle.university.query.all()
    university_list = SQLHandle.GetListOfRows(temp_universities)
    if(university_list is not None):
        if(len(university_list) > 0):
            response = ResponseHandle.GenerateUniversitiesResponse("university_get_success", university_list)
        else:
            response = ResponseHandle.GenerateResponse('university_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('university_get_failed')

    return response


def RegisterUniversity(req_data):
    temp_university = SQLHandle.university(uni_code=req_data['uni_code'], name=req_data['name'], address=req_data['address'],
                                           mobile_no=req_data['mobile_no'])
    if(SQLHandle.InsertRowObject(temp_university)):
        response = ResponseHandle.GenerateResponse('university_register_success')
    else:
        response = ResponseHandle.GenerateResponse('university_register_failed')
    return response


def UpdateUniversity(req_data):
    pass


def DeleteUniversity(req_data):
    pass


