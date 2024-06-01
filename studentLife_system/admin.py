from django.contrib import admin
from .models import studentInfo,RequestedGMC,Schedule,equipment, Program, Project, MOD

class StudentInfoAdmin(admin.ModelAdmin):
    
    list_display = ('studID', 'lastname', 'firstname', 'middlename', 'degree', 'yearlvl', 'sex', 'emailadd', 'contact')
    search_fields = ('studID', 'lastname', 'firstname', 'lrn')
    list_filter = ('degree', 'yearlvl', 'sex')

admin.site.register(studentInfo, StudentInfoAdmin)

class requestedgmcAdmin(admin.ModelAdmin):
    list_display = ('student', 'reason', 'or_num', 'request_date', 'processed')

admin.site.register(RequestedGMC, requestedgmcAdmin)


class scheduleAdmin(admin.ModelAdmin):
    list_display = ('sched_Id','title', 'description', 'start_datetime', 'end_datetime')

admin.site.register(Schedule, scheduleAdmin)

admin.site.register(equipment)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "caption", "date_time", "archive", "image_upload")


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "caption", "date_time", "archive", "image_upload")


class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "donated",
        "donation_type",
        "name",
        "gcash_number",
        "paymaya_number",
        "contact_number",
        "amount",
        "address_volunteer",
        "date_sched",
        "date_time",
    )


admin.site.register(Program, ProgramAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(MOD, DonationAdmin)
