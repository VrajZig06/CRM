from CRM.constants import path
from person.views import create_employee,get_employees,get_emp

urlpatterns = [
    path('getEmps/',get_employees),
    path('addEmp/',create_employee),
    path('getEmp/<empId>/',get_emp),

]
