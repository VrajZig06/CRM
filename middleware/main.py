from CRM.constants import JsonResponse,UNAUTHORIZED_ACCESS,JWT_SECRET,jwt,json,SOMETHING_WENT_WRONG,Users,INVALID_AUTHORIZATION_TOKEN

EXEMPT_PATHS = ['/api/v1/user/loginUser'] 

class VerifyAccessTokenMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwds):

        if request.path in EXEMPT_PATHS:
            return self.get_response(request)

        try:
            auth_header = request.headers.get('Authorization')
            if auth_header:
                token = auth_header.split(" ")[1]

                if Users.objects.filter(accessToken = token):

                    # extract data from Token.
                    payload = jwt.decode(token,JWT_SECRET,algorithms=["HS256"])
                    userId = payload.get('id')

                    request.userId = userId

                    return self.get_response(request)
                
                else:
                   return JsonResponse({
                        "Error" : INVALID_AUTHORIZATION_TOKEN
                    },status = 400)

                
            else:
                return JsonResponse({
                    "Error" : UNAUTHORIZED_ACCESS
                },status = 400)
    
        except Exception as e:
            return JsonResponse({
                "Error" : SOMETHING_WENT_WRONG
            },status = 400)

        

        
