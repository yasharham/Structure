# from typing import Union
from fastapi import APIRouter,Header,Request
# from Services.V1 import schemas
# from API.Controller.V1.example import *
#

router = APIRouter()
#
@router.post("/v1/user/signup", tags=['User'])
def signup():
    return "SAd"

#
# @router.post("/v1/user/login",tags=['User'])
# def login(request:Request, request_body: schemas.requestSchemaname):
#     return userLogin(request,request_body)
#
#
# @router.post('/v1/user/updatepassword', tags=['User'])
# def updatepassword(request_body: schemas.UpdatePassword, authToken: Union[str, None] = Header(default=None)):
#     return updatePassword(request_body,authToken)




