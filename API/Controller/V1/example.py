# import traceback
# from Services.V1.db import db
# from Services.V1.models import otp_coll, user_coll, login_trace_collection, user_subscription_collection
# from Middleware.authenticate import *
# import datetime
# from Utils.V1.mail import sendOTPEmail,sendSignupEmail,sendForgotPasswordEmail
# from Utils.V1.object import signUpUserObject, loginTraceObject, otpDataObject, loginResponseObject
# from Utils.V1.otp import isVerified
# from Utils.V1.response import successResponse, errorResponse
# from Constant.http import *
# from Utils.logger import logger
#
#
#
# def userSignup(request_body):
#     '''
#     verify request_body data and add user to db
#
#     :param request_body:
#     :return success response:
#     '''
#     try:
#         # find user
#         username = db.find_one(user_coll, {'username': request_body.username}, {'username': 1, '_id': 0})
#         # username exist
#         if username:
#             logger.error(HEM_USERNAME_EXISTS)
#             return errorResponse(HC_UNAUTHORISED, HEM_USERNAME_EXISTS)
#         if len(request_body.username) < 3:
#             logger.error(HEM_USERNAME_LENGTH)
#             return errorResponse(HC_UNAUTHORISED,HEM_USERNAME_LENGTH)
#
#         if not verifyUsername(request_body.username):
#             logger.error(HEM_USERNAME_ALPHANUMERIC)
#             return errorResponse(HC_UNAUTHORISED, HEM_USERNAME_ALPHANUMERIC)
#
#         email_exist = db.find_one(user_coll, {'email':{"$regex": request_body.email, "$options": "i"} }, {'email': 1, '_id': 0})
#         # email exist
#         if email_exist:
#             logger.error(HEM_EMAIL_EXISTS)
#             return errorResponse(HC_UNAUTHORISED, HEM_EMAIL_EXISTS)
#
#         # creating user object
#         user = signUpUserObject(request_body)
#         # add phone_no if exist
#         if request_body.phone_no:
#             # check phone_no length
#             if len(request_body.phone_no) != 10:
#                 logger.error(HEM_PHONE_NO_LENGTH)
#                 return errorResponse(HC_UNAUTHORISED, HEM_PHONE_NO_LENGTH)
#             user.update({"phone_no": request_body.phone_no})
#         # check password length
#         if len(request_body.password) < 8:
#             logger.error(HEM_PASSWORD_LENGTH)
#             return errorResponse(HC_UNAUTHORISED, HEM_PASSWORD_LENGTH)
#
#         otp_data = db.find_one(otp_coll, {'email': {"$regex": request_body.email, "$options": "i"}}, {'_id': 0})
#
#         if not otp_data:
#             logger.error(HEM_VERIFY_EMAIL)
#             return errorResponse(HC_UNAUTHORISED, HEM_VERIFY_EMAIL)
#
#         # otp does not match
#         if not isVerified(request_body.email, request_body.otp, "signup",otp_data):
#             logger.error(HEM_INVALID_OTP)
#             return errorResponse(HC_UNAUTHORISED, HEM_INVALID_OTP)
#
#         # add user
#         db.insert_one(user_coll, user)
#         sendSignupEmail(request_body.email, request_body.username)
#         return successResponse(HC_CREATED, HEM_CREATED)
#
#     except Exception as e:
#         logger.error(f"error while executing Signup API: {e}")
#         return errorResponse(HC_INTERNAL_SERVER_ERROR, HEM_SERVER_ERROR)
#
#
# def userLogin(request,request_body):
#     '''
#     verify request_body details from db, calls market_data_api
#
#     :param request:
#     :param request_body:
#     :return token:
#     '''
#     try:
#         # find user in DB
#         user = db.find_one(user_coll, {'username': request_body.username.lower()}) or db.find_one(user_coll,{'email': {"$regex": request_body.username, "$options": "i"} })
#         # user not found
#         if not user:
#             logger.error(HEM_USER_NOT_FOUND, extra={"client_host": request.client.host})
#             return errorResponse(HC_NOT_FOUND, HEM_USER_NOT_FOUND)
#         # user found
#         if user:
#             # password not matched
#             if not verify_pwd(request_body.password, user['password']):
#                 logger.error(HEM_CREDENTIAL, extra={"client_host": request.client.host})
#                 return errorResponse(HC_UNAUTHORISED, HEM_CREDENTIAL)
#
#             # generate token
#             access_token = create_access_token(data={"user": user['username']})
#             logger.info(f"Access token generated for user:{user['username']}", extra={"client_host": request.client.host})
#
#             # # Generate Login Trace DB object
#             # login_trace = loginTraceObject(user['_id'], request, request_body)
#             # # Insert Login Trace object
#             # db.insert_one(login_trace_collection, login_trace)
#
#             logger.info(f"Login trace detail added for user:{user['username']}",
#                         extra={"client_host": request.client.host})
#             # Generate response object
#             response_data = loginResponseObject(access_token,  user, request_body)
#             # send response
#             return successResponse(HC_OK, HEM_LOGIN_SUCCESS, response_data)
#     except Exception as e:
#         logger.error(f"error while executing Login API: {e}",extra={"client_host": request.client.host})
#         return errorResponse(HC_INTERNAL_SERVER_ERROR, HEM_SERVER_ERROR)