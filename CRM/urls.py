from CRM.constants import BASE_URL,path,include,admin

urlpatterns = [
    path(BASE_URL + 'admin/', admin.site.urls),
    path(BASE_URL + 'employee/',include('person.urls')),
    path(BASE_URL + "user/",include('users.urls')),
]
