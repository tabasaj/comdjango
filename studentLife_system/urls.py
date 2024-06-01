from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("requestgmc", views.requestgmc, name="requestgmc"),
    path("equipmenttracker", views.equipmentTracker, name="equipmentTracker"),
    path(
        "equipmenttrackerAdmin/",
        views.equipmentTrackerAdmin,
        name="equipmentTrackerAdmin",
    ),
    path("adminmain", views.adminhome, name="adminmain"),
    path("requested-gmc", views.adminRequestedGmc, name="adminRequestedGmc"),
    path("gmc-form", views.gmcform, name="gmcform"),
    path("generate-gmc/<int:request_id>/", views.generateGmc, name="generateGmc"),
    path("monthlyCalendar", views.monthlyCalendar, name="monthlyCalendar"),
    path(
        "monthlyCalendarAdmin", views.monthlyCalendarAdmin, name="monthlyCalendarAdmin"
    ),
    path("save-schedule/", views.save_schedule, name="save_schedule"),
    path(
        "delete-schedule/<int:schedule_id>/",
        views.delete_schedule,
        name="delete_schedule",
    ),
    path("addEquipment/", views.addEquipment, name="addEquipment"),
    
    
    
    #COMMUNITY INVOLVEMENT
    path("programs/", views.programs, name="programs"),
    path("projects/", views.projects, name="projects"),
    path("reports/", views.reports, name="reports"),
    # Forms
    path("program-form/", views.program_form, name="program-form"),
    path("project-form/", views.project_form, name="project-form"),
    # Add Program
    path("program-form/add_program/", views.add_program, name="add_program"),
    path("program-form/add_project/", views.add_project, name="add_project"),
    # Mode
    path("projects/gcash-mode", views.gcash_mode, name="gcash-mode"),
    path("projects/paymaya-mode", views.paymaya_mode, name="paymaya-mode"),
    path("projects/volunteer-mode", views.volunteer_mode, name="volunteer-mode"),
    
    path("reports/", views.reports, name="reports"),
]
