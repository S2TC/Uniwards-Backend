"""
*   Module Name: ResponseHandle
*   Module Purpose: Define and generate responses for requests
"""
from flask import jsonify


responses = {"register_success": (200, "0"),
             "register_failed": (201, "1"),
             "register_username_taken": (200, "2"),
             "registe_email_taken": (200, "3"),
             "register_auth_required": (200, "4"),
             "register_already_registered": (200, "already registered"),
             "token_valid": (200, "0"),
             "token_verfied": (200, "1"),
             "token_bad": (200, "2"),
             "token_expired": (200, "3"),
             "email_auth_verified": (200, "email_auth_verified"),
             "email_auth_failed": (200, "email_auth_failed"),
             "login_success": (200, "0"),
             "login_incorrect_password": (200, "1"),
             "login_nonexistant_user": (200, "2"),
             "login_wrong_username": (200, "3"),
             "login_unregistered": (200, "4"),
             "university_get_failed": (200, "0"),
             "university_register_failed": (200, "1"),
             "university_delete_failed": (200, "2"),
             "university_update_failed": (200, "3"),
             "university_register_success": (200, "4"),
             "university_delete_success": (200, "5"),
             "university_update_success": (200, "6")}


#Return json containing response message + HTML response code
def GenerateResponse(response_type):
    return [jsonify(response_message=responses[response_type][1]), responses[response_type][0]]

#Return json containing response message & JWT + HTML response code
def GenerateTokenResponse(response_type, raw_token):
    return [jsonify(response_message=responses[response_type][1], user_token=raw_token), responses[response_type][0]]

def GenerateUniversitiesResponse(universities):
    return [jsonify(universities=universities), 200]

def GenerateUniversityResponse(university):
    return [jsonify(university=university), 200]
