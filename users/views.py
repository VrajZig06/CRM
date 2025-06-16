from CRM.constants import *

def getUsers(request):
    if request.method == 'GET':

        if request.GET.get("page", 1):
            pageNumber = request.GET.get("page", 1)
            count = request.GET.get("count", 5)

        try:
            data = Users.objects.filter(isActive = True,isDeleted = False)
            paginator = Paginator(data, count)

            page_obj = paginator.get_page(pageNumber)
            users = []
            for i in page_obj:
                users.append({"id" : i.id,"username" : i.username,"email" : i.email,"companyName":i.company_name})
                
            return JsonResponse({
                    "status" : 200,
                    "data" : users,
                    "total_pages": paginator.num_pages,
                    "current_page": page_obj.number,
                    "has_next": page_obj.has_next(),
                    "has_previous": page_obj.has_previous()
                }, status=200)
        
        except Exception as e:
            return JsonResponse({
                 "message" : USER_ALREADY_EXISTS
            },status = 400)



@csrf_exempt
# Create your views here.
def createUser(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            if not data.get('username') or not data.get('password') or not data.get('email') or not data.get('company_name'):
                return JsonResponse({'Error': All_FIELDS_REQUIRED}, status=400)
            
            userExists = Users.objects.filter(username=data.get('username'),company_name=data.get('company_name'),isActive= True,isDeleted = False)

            new_user = Users(
                    username=data['username'],
                    password=make_password(data['password']),  # Hash password!
                    email=data['email'],
                    company_name=data['company_name']
                    ) if not userExists else JsonResponse({
                            "Error" : USER_ALREADY_EXISTS
                        },status = 400) 

            try:
                new_user.save()
                return JsonResponse({
                    'Message' : USER_CREATED_SUCCESSFULLY,
                    "Data" : model_to_dict(new_user)

                })
            except Exception as e:
                return JsonResponse({
                    "Error" :USER_ALREADY_EXISTS
                },status = 400) 

        except Exception as e:
             return JsonResponse({
                    "Error" : str(e)
                },status = 400)


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            if not request.body:
                return JsonResponse({
                    "Error" : PAYLOAD_REQUIRED
                })
            
            data = json.loads(request.body)

            email = data['email']
            password = data['password']

            if not email and not password and password is None:
                return JsonResponse({
                    "Error" : EMAIL_PASSWORD_REQUIRED
                },status = 400)
            
            
            isUserExist = Users.objects.filter(email=email,isDeleted=False ,isActive=True).first()
            print(isUserExist.id)
            if isUserExist:
                
                # Password Matching
                if check_password(password,str(isUserExist.password)):
                    
                    payload = {
                        "id" : str(isUserExist.id),
                        "username" : isUserExist.username,
                        "email" : isUserExist.email,
                        "lastLogin" : str(timezone.now())
                    }


                    try:
                        encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
                        isUserExist.accessToken = encoded_jwt
                        isUserExist.lastLogin = timezone.now()
                        isUserExist.save()

                        return JsonResponse({
                            "id" : isUserExist.id,
                            "username" : isUserExist.username,
                            "company_name" : isUserExist.company_name,
                            "AccessToken" : isUserExist.accessToken

                        },status = 200)
                    except Exception as e:
                        return JsonResponse({
                            "Error" :FAILED_ACCESS_TOKEN
                        },status = 400)
                
                else:
                    return JsonResponse({
                        "Error"  : "Password Incorrect."
                    },status = 400)
            else:
                return JsonResponse({
                    "Error" : USER_NOT_FOUND
                },status = 400)


        except Exception as e:
            return JsonResponse({
                "Error" : SOMETHING_WENT_WRONG
            },status = 400)