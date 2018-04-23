import ResponseHandle, SQLHandle

def GetUniversity(uni_code):
    temp_university = SQLHandle.university.query.filter_by(uni_code=uni_code).first()
    response = ResponseHandle.GetUniversityResponse(temp_university)
    return response

def GetUniversities():
    temp_universities = SQLHandle.university.query.all()
    response = ResponseHandle.GenerateUniversitiesResponse(temp_universities)
    return response

def RegisterUniversity(req_data):
    temp_university = SQLHandle.university(uni_code=req_data['uni_code'], name=req_data['name'], address=req_data['address'],
                                           mobile_no=req_data['mobile_no'])
    response = ResponseHandle.GenerateResponse('university_register_success')
    return response

def UpdateUniversity(req_data):
    pass

def DeleteUniversity(req_data):
    pass


