from . import views
from django.urls import path
urlpatterns = [
    path('LocTagPage',views.LocTagPage),
    path('PartTagPage',views.PartTagPage),
    path('home',views.HomePage),
    path('newlt',views.NewLocTag),
    path('newpt',views.NewPartTag),
    path('addlt',views.addLocTag),
    path('addpt',views.addPartTag),
    path('DelLocTag',views.DelLocTag),
    path('DelPartTag',views.DelPartTag),
    path('EditUserTags',views.EditUserTags),
    path('EditLocTags',views.EditLocTags),
    path('ModifyUser',views.ModifyUser),
    path('ModifyLoc',views.ModifyLoc),
    path('DeleteTag',views.DeleteTag),
    path('DeleteLocTag',views.DeleteLocTag),
    path('AddUserTag',views.AddUserTag),
    path('AddLocTag',views.AddLocTag),
    path('AddUTag',views.AddUTag),
    path('AddLTag',views.AddLTag),
    path('SearchPage',views.SearchPage),
    path('EventStep1',views.EventStep1),
    path('EventBooking1',views.EventBooking1),
    path('EventStep2',views.EventStep2),
    path('EventBooking2',views.EventBooking2),
    path('EventStep3',views.EventStep3),
    path('EventStep4',views.EventStep4),
    path('EventStep5',views.EventStep5),
    path('plist',views.plist),
    path('people',views.people)
]
