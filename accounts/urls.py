from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('activate/<uidb64>/<token>/',views.activate,name="activate"),
    path('resetpassword_validate/<uidb64>/<token>/',views.resetpassword_validate,name="resetpassword_validate"),
    path('profile/',views.profile,name="profile"),
    path('signout/',views.signout,name="signout"),
    path('forgotPassword/',views.forgotPassword,name="forgotPassword"),
    path('resetPassword/',views.resetPassword,name="resetPassword"),
    path('edit_profile/',views.edit_profile,name="edit_profile"),
]
