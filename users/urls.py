from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('account/', views.userAccount, name="account"),

    path('edit-account/', views.editAccount, name="edit-account"),

    path('create-skill', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>', views.deleteSkill, name="delete-skill"),
   
    path('inbox/', views.inbox, name="inbox"),
    path('personal-meeting-inbox/', views.personalMeetingInbox, name="personal-meeting-inbox"),

    path('message/<str:pk>/', views.viewMessage, name='message'),
    path('personal-meeting/<str:pk>/', views.viewPersonalMeeting, name='personal-meeting'),

    path('create-message/<str:pk>/', views.createMessage, name="create-message"),

    path('create-personal-meeting/<str:pk>/', views.createPersonalMeeting, name="create-personal-meeting"),

    path('attendance/', views.attendance, name="attendance"),
    path('attendance-in/', views.attendanceIn, name="attendance-in"),
    path('attendance-out/', views.attendanceOut, name="attendance-out"),
    path('work-log/', views.worklog, name="work-log"),
]
