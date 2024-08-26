from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='posts'),
   path('<int:pk>', PostDetail.as_view(), name='post'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_confirm_delete.html'),
]