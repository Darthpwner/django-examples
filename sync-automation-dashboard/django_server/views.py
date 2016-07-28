from django.views import generic
from rest_framework import viewsets

from django_server import models
from django_server import serializers


# class HomeView(generic.ListView):
#     def get_queryset(self):
#         return models.Post.objects.all().order_by('-posted_date')

# home_view = HomeView.as_view()


# class CategoryPosts(generic.DetailView):
#     model = models.Category
#     template_name = 'django_server/post_list.html'

#     def get_context_data(self, **kwargs):
#         context = super(CategoryPosts, self).get_context_data(**kwargs)
#         context['post_list'] = self._get_posts()
#         return context

#     def _get_posts(self):
#         category = self.object
#         return (models.Post.objects.filter(category_id=category.id)
#                 .order_by('-posted_date'))

# category_posts = CategoryPosts.as_view()


# class PostView(generic.DetailView):
#     model = models.Post

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['is_python'] = self._get_is_python()
#         return context

#     def _get_is_python(self):
#         return ('python' in self.object.category.name.lower()
#                 or 'python' in self.object.title)

# post_view = PostView.as_view()


# class CategorySetView(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer

#     def get_queryset(self):
#         return queryset


# class PostSetView(viewsets.ReadOnlyModelViewSet):
#     model = models.Post
#     serializer_class = serializers.PostSerializer
#     filter_fields = ('category', )
#     queryset = models.Post.objects.all()

class SummaryView(generic.DetailView):
    model = models.Summary

summary_view = SummaryView.as_view()

class SummarySetView(viewsets.ReadOnlyModelViewSet):
    queryset = models.Summary.objects.all()
    serializer_class = serializers.SummarySerializer

