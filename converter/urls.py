from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('convert/', views.convert_pdf_to_word, name='convert'),
    path('download/<int:file_id>/', views.download_word_file, name='download'),
]