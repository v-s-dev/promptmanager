# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/categories', views.get_categories),
    path('api/subcategories/<int:category_id>', views.get_subcategories),
    path('api/prompts/<int:subcategory_id>', views.get_prompts),
    path('api/prompt/<int:prompt_id>', views.get_prompt),

    path('api/categories/create', views.create_category),
    path('api/subcategories', views.create_subcategory),
    path('api/prompts/save', views.save_prompt),
    path('api/prompt', views.delete_prompt),
]
