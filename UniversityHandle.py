import ResponseHandle, SQLHandle

def GetUniversity(uni_code):
    new_university = SQLHandle.university.query.filter_by(uni_code=uni_code).first()
    response = ResponseHandle.GetUniversityResponse(new_university)
    return response

def GetUniversities():
    temp_universities = SQLHandle.university.query.all()
    university_list = [university.dict() for university in temp_universities)
    def todict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    response = ResponseHandle.GenerateUniversitiesResponse(university_list)
    print response
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


