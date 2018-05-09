import ResponseHandle, SQLHandle
from datetime import datetime
def GetPointsByStudentID(student_id):
    temp_points = SQLHandle.point.query.filter_by(student_id=student_id)
    point_list = SQLHandle.GetListOfRows(temp_points)
    if(len(point_list) > 0):
        response = ResponseHandle.GeneratePointsResponse("point_get_success", point_list)
    else:
        response = ResponseHandle.GenerateResponse('point_get_failed')

    return response

def GetPointsByTutorID(tutor_id):
    temp_points = SQLHandle.point.query.filter_by(tutor_id=tutor_id)
    point_list = SQLHandle.GetListOfRows(temp_points)
    if (point_list is not None):
        if(len(point_list) > 0):
            response = ResponseHandle.GeneratePointsResponse("point_get_success", point_list)
        else:
            response = ResponseHandle.GenerateResponse('point_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('point_get_failed')

    return response


def GetPointsByRewardID(reward_id):
    temp_points = SQLHandle.point.query.filter_by(reward_id=reward_id)
    point_list = SQLHandle.GetListOfRows(temp_points)
    if(point_list is not None):
        if(len(point_list) > 0):
            response = ResponseHandle.GeneratePointsResponse("point_get_success", point_list)
        else:
            response = ResponseHandle.GenerateResponse('point_get_failed')
    else:
        response = ResponseHandle.GenerateResponse('point_get_failed')

    return response


def CreatePoint(req_data):
    #parsed_date = datetime.strptime(req_data['date'], "%m/%d/%Y").strftime('%m/%d/%Y')
    temp_point = SQLHandle.point(student_id=req_data['student_id'], reward_id=req_data['reward_id'],
                                           tutor_id=req_data['tutor_id'], date=req_data['date'])
    if(SQLHandle.InsertRowObject(temp_point)):
        student = SQLHandle.student.query.filter_by(student_id=req_data['student_id'])
        StudentHandle.SetTotalPoints(student)
        SQLHandle.CommitSession()
        response = ResponseHandle.GenerateResponse('point_register_success')
    else:
        response = ResponseHandle.GenerateResponse('point_register_failed')
    return response


def UpdatePoint(req_data):
    pass


def DeletePoint(req_data):
    pass