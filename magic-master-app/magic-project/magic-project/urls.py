"""
URL configuration for formula1_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from magic_app.views import Home, MagicalCreatureListView, WizardListView, EnchantedPlaceListView, MagicalEncounterListView, MagicalEventListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('creature_list/', MagicalCreatureListView.as_view(), name='creature-list'),
    path('wizard_list/', WizardListView.as_view(), name='wizard-list'),
    path('place_list/', EnchantedPlaceListView.as_view(), name='place-list'),
    path('encounter_list/', MagicalEncounterListView.as_view(), name='encounter-list'),
    path('event_list/', MagicalEventListView.as_view(), name='event-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
