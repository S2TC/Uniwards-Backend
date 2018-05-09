from flask import Flask, request
from ConfigHandle import Config
import SQLHandle, RegistrationHandle, LoginHandle, ResponseHandle, UniversityHandle, CouponHandle, RewardHandle
import PointHandle, RedemptionHandle, VendorHandle, EnrolmentHandle, UniclassHandle, StudentHandle
from LogHandle import Logger, LogLevel

app = Flask(__name__)
log_inst = Logger("Uniwards-Backend.txt")

@app.route('/api')
def hello_world():
    #AlwaysRun()
    return 'Hello World!'


'''----------REGISTRATION, LOGIN, AUTHENTICATION----------'''


#Authenticate email token to complete user registration
@app.route('/api/auth_user/<auth_token>')
def AuthUser(auth_token):
    if(RegistrationHandle.VerifyStudentEmailAuth(auth_token)):
        log_inst.Log("Verified email for: %s" % (RegistrationHandle.DecryptEmailAuth(auth_token)), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('email_auth_verified')
    else:
        log_inst.Log("Failed to verify email for: %s" % (RegistrationHandle.DecryptEmailAuth(auth_token)), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('email_auth_failed')

    return response[0], response[1]


@app.route('/api/validate_token/<token>/<username>')
def ValidateToken(token, username):
    response = LoginHandle.TokenValidation(token, username)
    print response
    return response[0], response[1]


#User Registration endpoint
@app.route('/api/registeruser', methods = ['POST'])
def RegisterUser():
    response = LoginHandle.TokenVerification(request.headers['Token'])
    print response
    if(response is not 'Valid' and response is not 'Expired'):
        log_inst.Log("Registering student: %s" % (request.form['username']), LogLevel.DEBUG)
        response = RegistrationHandle.RegisterUser(request.form)
    else:
        log_inst.Log("Student already registered: %s" % (request.form['username']), LogLevel.DEBUG)
        response = ResponseHandle.GenerateResponse('register_already_registered')

    return response[0], response[1]


#Student Login endpoint
@app.route('/api/login', methods = ['POST'])
def StudentLogin():
    log_inst.Log("Student attempting to login: %s" % (request.form['username']), LogLevel.DEBUG)
    response = LoginHandle.Login(request.form)
    if(response[0] == 'login_success'):
        log_inst.Log("Student login success: %s" % (request.form['username']), LogLevel.DEBUG)
    return response[0], response[1]


@app.route('/api/validate_studentpasscode/<passcode>')
def ValidateStudentPasscode(passcode):
    response = StudentHandle.ValidateStudentPasscode(request.headers['Token'], passcode)
    print response
    return response[0], response[1]


@app.route('/api/validate_vendorpasscode/<passcode>/<vendor_id>')
def ValidateVendorPasscode(passcode, vendor_id):
    response = VendorHandle.ValidateVendorPasscode(passcode, vendor_id)
    print response
    return response[0], response[1]

'''-------------------------------------------------------'''


'''------------------General GET Requests-----------------'''


@app.route('/api/getuniversity/<uni_code>')
def GetUniversity(uni_code):
    response = UniversityHandle.GetUniversity(uni_code)
    return response[0], response[1]


@app.route('/api/getuniversities')
def GetUniversities():
    response = UniversityHandle.GetUniversities()
    return response[0], response[1]

@app.route('/api/getcoupons')
def GetCoupons():
    response = CouponHandle.GetCoupons()
    return response[0], response[1]

@app.route('/api/getcouponbyid/<coupon_id>')
def GetCouponByID(coupon_id):
    response = CouponHandle.GetCouponByID(coupon_id)
    return response[0], response[1]

@app.route('/api/getcouponsbytier/<tier>')
def GetCouponsByTier(tier):
    response = CouponHandle.GetCouponsByTier(tier)
    return response[0], response[1]

@app.route('/api/getcouponbyvendor/<vendor_id>')
def GetCouponByVendor(vendor_id):
    response = CouponHandle.GetCouponByVendor(vendor_id)
    return response[0], response[1]

@app.route('/api/getrewardbyid/<reward_id>')
def GetRewardByID(reward_id):
    response = RewardHandle.GetRewardByID(reward_id)
    return response[0], response[1]

@app.route('/api/getrewardsbytier/<tier>')
def GetRewardsByTier(tier):
    response = RewardHandle.GetRewardsByTier(tier)
    return response[0], response[1]

@app.route('/api/getrewards')
def GetRewards():
    response = RewardHandle.GetRewards()
    return response[0], response[1]

@app.route('/api/getpointsbystudentid/<student_id>')
def GetPointsByStudentID(student_id):
    response = PointHandle.GetPointsByStudentID(student_id)
    return response[0], response[1]

@app.route('/api/getpointsbytutorid/<tutor_id>')
def GetPointsByTutorID(tutor_id):
    response = PointHandle.GetPointsByTutorID(tutor_id)
    return response[0], response[1]

@app.route('/api/getpointsbyrewardid/<reward_id>')
def GetPointsByRewardID(reward_id):
    response = PointHandle.GetPointsByRewardID(reward_id)
    return response[0], response[1]

@app.route('/api/getvendorbyid/<vendor_id>')
def GetVendorByID(vendor_id):
    response = VendorHandle.GetVendorByID(vendor_id)
    return response[0], response[1]

@app.route('/api/getvendorsbytype/<type>')
def GetVendorsByType(type):
    response = VendorHandle.GetVendorsByType(type)
    return response[0], response[1]

@app.route('/api/getvendors')
def GetVendors():
    response = VendorHandle.GetVendors()
    return response[0], response[1]

@app.route('/api/getredemptionbyid/<redemption_id>')
def GetRedemptionByID(redemption_id):
    response = RedemptionHandle.GetRedemptionByID(redemption_id)
    return response[0], response[1]

@app.route('/api/getredemptionsbystudentid/<student_id>')
def GetRedemptionsByStudentID(student_id):
    response = RedemptionHandle.GetRedemptionsByStudentID(student_id)
    return response[0], response[1]

@app.route('/api/getredemptionsbycouponid/<coupon_id>')
def GetRedemptionsByCouponID(coupon_id):
    response = RedemptionHandle.GetRedemptionsByCouponID(coupon_id)
    return response[0], response[1]

@app.route('/api/getredemptions')
def GetRedemptions():
    response = RedemptionHandle.GetRedemptions()
    return response[0], response[1]

@app.route('/api/getenrolmentsbystudentid/<student_id>')
def GetEnrolmentsByStudentID(student_id):
    response = EnrolmentHandle.GetEnrolmentsByStudentID(student_id)
    return response[0], response[1]

@app.route('/api/getenrolmentsbyclassid/<class_id>')
def GetEnrolmentByClassID(class_id):
    response = EnrolmentHandle.GetEnrolmentsByClassID(class_id)
    return response[0], response[1]

@app.route('/api/getenrolments')
def GetEnrolments():
    response = EnrolmentHandle.GetEnrolments()
    return response[0], response[1]

@app.route('/api/getuniclassbyname/<name>')
def GetUniclassesByName(name):
    response = UniclassHandle.GetUniclassByName(name)
    return response[0], response[1]

@app.route('/api/getuniclassesbytutorid/<tutor_id>')
def GetUniclassesByTutorID(tutor_id):
    response = UniclassHandle.GetUniclassesByTutorID(tutor_id)
    return response[0], response[1]

@app.route('/api/getuniclassesbyuniid/<uni_id>')
def GetUniclassesByUniID(uni_id):
    response = UniclassHandle.GetUniclassesByUniID(uni_id)
    return response[0], response[1]

@app.route('/api/getuniclasses')
def GetUniclasses():
    response = UniclassHandle.GetUniclasses()
    return response[0], response[1]

@app.route('/api/getstudent')
def GetStudent():
    response = StudentHandle.GetStudent(request.headers['Token'])
    return response[0], response[1]

'''-------------------------------------------------------'''


'''------------------General POST Requests-----------------'''

@app.route('/api/registeruniversity', methods = ['POST'])
def CreateUniversity():
    response = UniversityHandle.RegisterUniversity(request.form)
    return response[0], response[1]

@app.route('/api/newcoupon', methods = ['POST'])
def CreateCoupon():
    response = CouponHandle.CreateCoupon(request.form)
    return response[0], response[1]

@app.route('/api/newreward', methods = ['POST'])
def CreateReward():
    response = RewardHandle.CreateReward(request.form)
    return response[0], response[1]

@app.route('/api/newpoint', methods = ['POST'])
def CreatePoint():
    response = PointHandle.CreatePoint(request.form)
    return response[0], response[1]

@app.route('/api/newvendor', methods = ['POST'])
def CreateVendor():
    response = VendorHandle.RegisterVendor(request.form)
    return response[0], response[1]

@app.route('/api/newredemption', methods = ['POST'])
def CreateRedemption():
    response = RedemptionHandle.CreateRedemption(request.form)
    return response[0], response[1]

@app.route('/api/newenrolment', methods = ['POST'])
def CreateEnrolment():
    response = EnrolmentHandle.CreateEnrolment(request.form)
    return response[0], response[1]

@app.route('/api/newuniclass', methods = ['POST'])
def CreateUniclass():
    response = UniclassHandle.RegisterUniclass(request.form)
    return response[0], response[1]

@app.route('/api/deleteenrolment', methods = ['POST'])
def DeleteEnrolment():
    response = EnrolmentHandle.DeleteEnrolment(request.form)
    return response[0], response[1]
'''-------------------------------------------------------'''


def TestFunc():
    uni = SQLHandle.university(1, "test", "test", "1234")
    SQLHandle.InsertRowObject(uni)
    uni2 = SQLHandle.university.query.all()
    print(uni2[0].mobile_no)
    pass

def DebugDB():
    #RegistrationHandle.SendAuthEmail('test@uniwards.xyz', '123')
    pass


def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        log_inst.Log(line)

if __name__ == '__main__':
    config = Config()
    SQLHandle.CreateTables()
    DebugDB()
    app.run(host='0.0.0.0')
