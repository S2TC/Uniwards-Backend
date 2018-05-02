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
             "token_verified": (200, "1"),
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
             "university_get_success": (200, "4"),
             "university_register_success": (200, "5"),
             "university_delete_success": (200, "6"),
             "university_update_success": (200, "7"),
             "coupon_get_failed": (200, "0"),
             "coupon_register_failed": (200, "1"),
             "coupon_delete_failed": (200, "2"),
             "coupon_update_failed": (200, "3"),
             "coupon_get_success": (200, "4"),
             "coupon_register_success": (200, "5"),
             "coupon_delete_success": (200, "6"),
             "coupon_update_success": (200, "7"),
             "reward_get_failed": (200, "0"),
             "reward_register_failed": (200, "1"),
             "reward_delete_failed": (200, "2"),
             "reward_update_failed": (200, "3"),
             "reward_get_success": (200, "4"),
             "reward_register_success": (200, "5"),
             "reward_delete_success": (200, "6"),
             "reward_update_success": (200, "7"),
             "point_get_failed": (200, "0"),
             "point_register_failed": (200, "1"),
             "point_delete_failed": (200, "2"),
             "point_update_failed": (200, "3"),
             "point_get_success": (200, "4"),
             "point_register_success": (200, "5"),
             "point_delete_success": (200, "6"),
             "point_update_success": (200, "7"),
             "vendor_get_failed": (200, "0"),
             "vendor_register_failed": (200, "1"),
             "vendor_delete_failed": (200, "2"),
             "vendor_update_failed": (200, "3"),
             "vendor_get_success": (200, "4"),
             "vendor_register_success": (200, "5"),
             "vendor_delete_success": (200, "6"),
             "vendor_update_success": (200, "7"),
             "redemption_get_failed": (200, "0"),
             "redemption_register_failed": (200, "1"),
             "redemption_delete_failed": (200, "2"),
             "redemption_update_failed": (200, "3"),
             "redemption_get_success": (200, "4"),
             "redemption_register_success": (200, "5"),
             "redemption_delete_success": (200, "6"),
             "redemption_update_success": (200, "7"),
             "enrolment_get_failed": (200, "0"),
             "enrolment_register_failed": (200, "1"),
             "enrolment_delete_failed": (200, "2"),
             "enrolment_update_failed": (200, "3"),
             "enrolment_get_success": (200, "4"),
             "enrolment_register_success": (200, "5"),
             "enrolment_delete_success": (200, "6"),
             "enrolment_update_success": (200, "7"),
             "uniclass_get_failed": (200, "0"),
             "uniclass_register_failed": (200, "1"),
             "uniclass_delete_failed": (200, "2"),
             "uniclass_update_failed": (200, "3"),
             "uniclass_get_success": (200, "4"),
             "uniclass_register_success": (200, "5"),
             "uniclass_delete_success": (200, "6"),
             "uniclass_update_success": (200, "7"),
             "student_get_failed": (200, "0"),
             "student_register_failed": (200, "1"),
             "student_delete_failed": (200, "2"),
             "student_update_failed": (200, "3"),
             "student_get_success": (200, "4"),
             "student_register_success": (200, "5"),
             "student_delete_success": (200, "6"),
             "student_update_success": (200, "7")
             }


#Return json containing response message + HTML response code
def GenerateResponse(response_type):
    return [jsonify(response_message=responses[response_type][1]), responses[response_type][0]]

#Return json containing response message & JWT + HTML response code
def GenerateStudentResponse(response_type, student):
    return [jsonify(response_message=responses[response_type][1], student=student), responses[response_type][0]]

def GenerateTokenResponse(response_type, raw_token, uni_id):
    return [jsonify(response_message=responses[response_type][1], user_token=raw_token, uni_id=uni_id), responses[response_type][0]]

def GenerateUniversitiesResponse(response_type, universities):
    return [jsonify(response_message=responses[response_type][1], universities=universities), responses[response_type][0]]

def GenerateUniversityResponse(response_type, university):
    return [jsonify(response_message=responses[response_type][1], university=university), responses[response_type][0]]

def GenerateCouponsResponse(response_type, coupons):
    return [jsonify(response_message=responses[response_type][1], coupons=coupons), responses[response_type][0]]

def GenerateCouponResponse(response_type, coupon):
    return [jsonify(response_message=responses[response_type][1], coupon=coupon), responses[response_type][0]]

def GenerateRewardsResponse(response_type, rewards):
    return [jsonify(response_message=responses[response_type][1], rewards=rewards), responses[response_type][0]]

def GenerateRewardResponse(response_type, reward):
    return [jsonify(response_message=responses[response_type][1], reward=reward), responses[response_type][0]]

def GeneratePointsResponse(response_type, points):
    return [jsonify(response_message=responses[response_type][1], points=points), responses[response_type][0]]

def GeneratePointResponse(response_type, point):
    return [jsonify(response_message=responses[response_type][1], point=point), responses[response_type][0]]

def GenerateVendorsResponse(response_type, vendors):
    return [jsonify(response_message=responses[response_type][1], vendors=vendors), responses[response_type][0]]

def GenerateVendorResponse(response_type, vendor):
    return [jsonify(response_message=responses[response_type][1], vendor=vendor), responses[response_type][0]]

def GenerateRedemptionsResponse(response_type, redemptions):
    return [jsonify(response_message=responses[response_type][1], redemptions=redemptions), responses[response_type][0]]

def GenerateRedemptionResponse(response_type, redemption):
    return [jsonify(response_message=responses[response_type][1], redemption=redemption), responses[response_type][0]]

def GenerateEnrolmentsResponse(response_type, enrolments):
    return [jsonify(response_message=responses[response_type][1], enrolments=enrolments), responses[response_type][0]]

def GenerateEnrolmentResponse(response_type, enrolment):
    return [jsonify(response_message=responses[response_type][1], enrolment=enrolment), responses[response_type][0]]

def GenerateUniclassesResponse(response_type, uniclasses):
    return [jsonify(response_message=responses[response_type][1], uniclasses=uniclasses), responses[response_type][0]]

def GenerateUniclassResponse(reponse_type, uniclass):
    return [jsonify(response_message=responses[response_type][1], uniclass=uniclass), responses[response_type][0]]
