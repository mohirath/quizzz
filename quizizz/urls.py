"""quizizz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.api import QuestionResource
from game.api import GameResource
from leaderboard.api import LeaderBoardResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(QuestionResource())

v2_api = Api(api_name='v2')
v2_api.register(QuestionResource())
v2_api.register(GameResource())

v3_api = Api(api_name='v3')
v3_api.register(QuestionResource())
v3_api.register(GameResource())
v3_api.register(LeaderBoardResource())

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(v1_api.urls)),
    path('api/', include(v2_api.urls)),
    path('api/', include(v3_api.urls)),
]