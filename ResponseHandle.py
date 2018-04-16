"""
*   Module Name: ResponseHandle
*   Module Purpose: Define and generate responses for requests
"""
from flask import jsonify

responses = {"registration_successful": (201, "success"),
             "registration_failed": (201, "fail"),
             "registration_username_already_registered": (200, "username taken"),
             "registration_email_already_registered": (200, "email registered"),
             "registration_auth_required": (2200, "email auth req"),
             "registration_already_registered": (2200, "already registered"),
             "bad_token": (403, "bad token"),
             "expired_token": (403, "expired token"),
             "email_auth_verified": (200, "email_auth_verified"),
             "email_auth_failed": (400, "email_auth_failed"),
             "login_success": (200, "0"),
             "login_incorrect_password": (400, "1"),
             "login_nonexistant_user": (400, "2"),
             "login_wrong_username": (400, "3"),
             "login_unregistered": (400, "4")}


#Return json containing response message + HTML response code
def GenerateResponse(response_type):
    return [jsonify(response_message=responses[response_type][1]), responses[response_type][0]]

#Return json containing response message & JWT + HTML response code
def GenerateTokenResponse(response_type, raw_token):
    return [jsonify(response_message=responses[response_type][1], user_token=raw_token), responses[response_type][0]]