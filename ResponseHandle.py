"""
*   Module Name: ResponseHandle
*   Module Purpose: Define and generate responses for requests
"""
from flask import jsonify

responses = {"registration_successful": (201, "success"),
             "registration_failed": (201, "fail"),
             "registration_username_already_registered": (200, "username taken"),
             "registration_email_already_registered": (200, "email registered"),
             "registration_auth_required": (2200, "test"),
             "bad_token": (403, "test"),
             "login_wrong_username": (400, "test"),
             "login_wrong_password": (400, "test"),
             "login_unregistered": (400, "test")}


def GenerateResponse(response_type):
    return [jsonify(response_message=responses[response_type][1]), responses[response_type][0]]

def PrintResponses():
    print(responses)
    print("ResponseType: %s - ResponseCode:%s - ResponseMessage:%s" % ("bad_token", responses["bad_token"][0], responses["bad_token"][1]))