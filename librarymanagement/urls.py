from django.contrib import admin
from django.urls import path, include
from library import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # 🔹 Admin Panel  
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    # 🔹 Home Page  
    path('', views.home_view, name='home'),

    # 🔹 Authentication  
    path('adminlogin/', LoginView.as_view(template_name='library/adminlogin.html'), name='adminlogin'),
    path('studentlogin/', LoginView.as_view(template_name='library/studentlogin.html'), name='studentlogin'),
    path('adminsignup/', views.adminsignup_view, name='adminsignup'),
    path('studentsignup/', views.studentsignup_view, name='studentsignup'),

    # 🔹 Logout Fix (Redirects to Home Page)  
    path('adminafterlogin/logout/', LogoutView.as_view(next_page='home'), name='logout'),

    # 🔹 Click Pages  
    path('adminclick/', views.adminclick_view, name='adminclick'),
    path('studentclick/', views.studentclick_view, name='studentclick'),

    # 🔹 After Login Redirects  
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('studentafterlogin/', views.studentafterlogin_view, name='studentafterlogin'),
    path('adminafterlogin/', views.adminafterlogin_view, name='adminafterlogin'),

    # 🔹 Book Management  
    path('addbook/', views.addbook_view, name='addbook'),
    path('bookadded/', views.bookadded_view, name='bookadded'),
    path('bookadded/viewbook/', views.view_books, name='view_books'),  # 🆕 Fix for 404 on book view
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

    # 🔹 Issued Books  
    path('issuebook/', views.issuebook_view, name='issuebook'),
    path('viewissuedbook/', views.viewissuedbook_view, name='viewissuedbook'),
    path('bookissued/', views.bookissued_view, name='bookissued'),
    path('delete_issued_book/<int:book_id>/', views.delete_issued_book, name='delete_issued_book'),

    # 🔹 Student Dashboard  
    path('studentafterlogin/viewissuedbookbystudent/', views.viewissuedbookbystudent_view, name='viewissuedbookbystudent'),
    path('studentafterlogin/view_available_books/', views.view_available_books, name='view_available_books'),
    path('studentafterlogin/view_to_read_list/', views.view_to_read_list, name='view_to_read_list'),

    # 🔹 View Available Books  
    path('view_available_books/', views.view_available_books, name='view_available_books'),

    # 🔹 Return Book  
    path('return_book/<int:book_id>/', views.return_book, name='return_book'),

    # 🔹 Student Management  
    path('viewstudent/', views.viewstudent_view, name='viewstudent'),

    # 🔹 To Read List (Fix for NoReverseMatch)  
    path('view_to_read_list/', views.view_to_read_list, name='view_to_read_list'),
    path('add_to_read_list/<int:book_id>/', views.add_to_read_list, name='add_to_read_list'),
    path('remove_from_read_list/<int:book_id>/', views.remove_from_read_list, name='remove_from_read_list'),

    # 🔹 Other Pages  
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('contactus/', views.contactus_view, name='contactus'),
]