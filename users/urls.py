
from CRM.constants import *
from users.views import *

urlpatterns = [
    path('allUsers/',getUsers),
    path('create-user/',createUser),
    path('loginUser',user_login)
]
