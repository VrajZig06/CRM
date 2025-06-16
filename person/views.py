from CRM.constants import *

def get_employees(request):
    if request.method == "GET":

        if request.GET.get("page", 1):
            pageNumber = request.GET.get("page", 1)
            count = request.GET.get("count", 5)

        try:
            allEmployees = Employee.objects.filter(isActive=True,isDeleted=False)

            paginator = Paginator(allEmployees, count)

            page_obj = paginator.get_page(pageNumber)

            list = []
            
            for emp in page_obj:

                    employee = {
                        "id" : emp.id,
                        "first_name" : emp.first_name,
                        "last_name" : emp.last_name,
                        "email" : emp.email,
                        "phone" : emp.phone,
                        "salary" : emp.salary,
                        "role" : emp.role
                    }

                    list.append(employee)

            
            return JsonResponse({
                "status" : 200,
                "data" : list,
                "total_pages": paginator.num_pages,
                "current_page": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            
            },status= 200)
        except Exception as e:
            return JsonResponse({
                "Error" : SOMETHING_WENT_WRONG,
            },status = 400)

@csrf_exempt
def create_employee(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)
            userid = request.userId

            if not data.get('first_name') or not data.get('last_name') or not data.get('email') or not data.get('phone') or not data.get('salary') or not data.get('role') :
                return JsonResponse({'error': All_FIELDS_REQUIRED}, status=400)
            
            if(userid):
                try:
                    user = Users.objects.get(id=userid)
                except Users.DoesNotExist:
                    return JsonResponse({'error': COMPANY_OWNER_NOT_EXISTS}, status=404)

                if Employee.objects.filter(email=data['email'],isActive=True,isDeleted= False).exists():
                    return JsonResponse({'error': USER_WITH_SAME_EMAIL_EXISTS}, status=400)

                if user:
                    employee = Employee(
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        email=data['email'],
                        phone=data['phone'],
                        salary=data['salary'],
                        role=data['role'],
                        userid=user
                    )

                    try:
                        employee.save()
                    except IntegrityError as e:
                        return JsonResponse({
                            "error": DB_INTEGRITY_ERROR,
                            "details": str(e)
                        }, status=400)
                            
                    return JsonResponse({
                        "message": EMPLOYEE_CREATED,
                        "employee": model_to_dict(employee)
                    }, status=201)
                
                return 1

        except Exception as e : 
            return JsonResponse({
                "message" : SOMETHING_WENT_WRONG,
                "details" : str(e)
            },status = 400)

@csrf_exempt
def get_emp(request,empId):

    if not empId:
        return JsonResponse({
            "Error" : EMPLOYEE_ID_REQUIRED
            },status = 400)
    
    try:
        emp = Employee.objects.get(id=empId,isActive=True,isDeleted = False)
        
    except Employee.DoesNotExist:
        return JsonResponse({
            "Error" : EMPLOYEE_NOT_FOUND
        },status = 400)


    if request.method == "GET":

            empDetails = {
                "id" : str(emp.id),
                "first_name" : emp.first_name,
                "last_name" : emp.last_name,
                "email" : emp.email,
                "phone" : emp.phone,
                "salary" : emp.salary,
                "role" : emp.role
            }
            
            return JsonResponse({
                "data" : empDetails,                   
            },status = 200)
    
    elif request.method == "PATCH":

        try:
            data = json.loads(request.body)

            emp.first_name = data.get("first_name", emp.first_name)
            emp.last_name = data.get("last_name", emp.last_name)
            emp.email = data.get("email", emp.email)
            emp.phone = data.get("phone", emp.phone)
            emp.salary = data.get("salary", emp.salary)
            emp.role = data.get("role", emp.role)

            try:
                emp.save()
                return JsonResponse({
                    "data" : EMPLOYEE_UPDATED
                },status = 200)
            except Exception as e:
                return JsonResponse({
                    "Error" : SOMETHING_WENT_WRONG,
                    "details" : str(e)
                },status = 400)

        except Exception as e:
            return JsonResponse({
                "Error" : SOMETHING_WENT_WRONG
            })
        
    elif request.method == "DELETE":
        try:
            emp.isActive,emp.isDeleted = False,True
            
            emp.save()

            return JsonResponse({
                "Data" : EMPLOYEE_DELETED
            },status = 200)
        except Exception as e:
            return JsonResponse({
                "Error" : SOMETHING_WENT_WRONG
            },status = 400)


