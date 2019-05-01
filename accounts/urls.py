from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from .views import SignupView


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # CHANGE PASSWORD
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name = 'accounts/password_change_form.html',
        success_url = reverse_lazy('accounts:password_change_done')
    ),
         name = 'password_change'),

    path('change-password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name = 'accounts/password_change_done.html'),
         name = 'password_change_done'
    ),

    # RESET PASSWORD
    path('reset/',
         auth_views.PasswordResetView.as_view(
            template_name = 'accounts/password_reset.html',
            email_template_name = 'accounts/password_reset_email.html',
            subject_template_name = 'accounts/password_reset_subject.txt',
            success_url = reverse_lazy('accounts:password_reset_done')
         ),
         name = 'password_reset'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),
         name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name = 'accounts/password_reset_confirm.html',
            success_url = reverse_lazy('accounts:password_reset_complete')
         ),
         name = 'password_reset_confirm'),
    path('reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name = 'password_reset_complete'),
]