from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResourse(ModelResource):
    class Meta:  # собственный атрибут клclасса CategoryResourse
        queryset = Category.objects.all()
        resourse_name = 'categories'
        allowed_methods = ['get']  # это методы http для разных ресурсов


class CourseResourse(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resourse_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_at']
        authentication = CustomAuthentication()
        authorization = Authorization()

# эти методы для api запросов чтобы создать новые посты ?
    def hydrate(self, bundle):
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle
