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
             "university_register_success": (200, "4"),
             "university_delete_success": (200, "5"),
             "university_update_success": (200, "6"),
             "coupon_get_failed": (200, "0"),
             "coupon_register_failed": (200, "1"),
             "coupon_delete_failed": (200, "2"),
             "coupon_update_failed": (200, "3"),
             "coupon_register_success": (200, "4"),
             "coupon_delete_success": (200, "5"),
             "coupon_update_success": (200, "6"),
             "reward_get_failed": (200, "0"),
             "reward_register_failed": (200, "1"),
             "reward_delete_failed": (200, "2"),
             "reward_update_failed": (200, "3"),
             "reward_register_success": (200, "4"),
             "reward_delete_success": (200, "5"),
             "reward_update_success": (200, "6"),
             "point_get_failed": (200, "0"),
             "point_register_failed": (200, "1"),
             "point_delete_failed": (200, "2"),
             "point_update_failed": (200, "3"),
             "point_register_success": (200, "4"),
             "point_delete_success": (200, "5"),
             "point_update_success": (200, "6"),
             "vendor_get_failed": (200, "0"),
             "vendor_register_failed": (200, "1"),
             "vendor_delete_failed": (200, "2"),
             "vendor_update_failed": (200, "3"),
             "vendor_register_success": (200, "4"),
             "vendor_delete_success": (200, "5"),
             "vendor_update_success": (200, "6"),
             "redemption_get_failed": (200, "0"),
             "redemption_register_failed": (200, "1"),
             "redemption_delete_failed": (200, "2"),
             "redemption_update_failed": (200, "3"),
             "redemption_register_success": (200, "4"),
             "redemption_delete_success": (200, "5"),
             "redemption_update_success": (200, "6"),
             "enrollment_get_failed": (200, "0"),
             "enrollment_register_failed": (200, "1"),
             "enrollment_delete_failed": (200, "2"),
             "enrollment_update_failed": (200, "3"),
             "enrollment_register_success": (200, "4"),
             "enrollment_delete_success": (200, "5"),
             "enrollment_update_success": (200, "6")}


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

def GenerateCouponsResponse(coupons):
    return [jsonify(coupons=coupons), 200]

def GenerateCouponResponse(coupon):
    return [jsonify(coupon=coupon), 200]

def GenerateRewardsResponse(rewards):
    return [jsonify(rewards=rewards), 200]

def GenerateRewardResponse(reward):
    return [jsonify(reward=reward), 200]

def GeneratePointsResponse(points):
    return [jsonify(coupons=points), 200]

def GeneratePointResponse(point):
    return [jsonify(point=point), 200]

def GenerateVendorsResponse(vendors):
    return [jsonify(vendors=vendors), 200]

def GenerateVendorResponse(vendor):
    return [jsonify(vendor=vendor), 200]

def GenerateRedemptionsResponse(redemption):
    return [jsonify(redemption=redemption), 200]

def GenerateRedemptionResponse(redemption):
    return [jsonify(Redemption=redemption), 200]

def GenerateEnrolmentsResponse(enrolments):
    return [jsonify(enrolments=enrolments), 200]

def GenerateEnrolmentResponse(enrolments):
    return [jsonify(enrolments=enrolments), 200]
