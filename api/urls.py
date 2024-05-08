from django.urls import include, path
from api.models import CourseResourse, CategoryResourse
from tastypie.api import Api


api = Api(api_name='v1')
api.register(CourseResourse())
api.register(CategoryResourse())

# api/v1/courseresourse/       GET,POST
# api/v1/courseresourse/1/     GET,DELETE
# api/v1/categoryresourse/     GET
# api/v1/categoryresourse/1/   GET

# For post delete and header
# Key: Authorization
# Value :  ApiKey  umar:qwerty123456

urlpatterns = [
    path('', include(api.urls), name='index')
    # path('api/', include(course_resourse.urls)),
    # path('api/', include(category_resourse.urls)),

]
