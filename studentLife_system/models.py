from django.db import models


class studentInfo(models.Model):
    studID = models.IntegerField(primary_key=True)
    lrn = models.CharField(max_length = 12)
    lastname = models.CharField(max_length = 100)
    firstname = models.CharField( max_length = 100)
    middlename = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 150)
    yearlvl = models.CharField(max_length = 10)
    sex = models.CharField(max_length = 10)
    emailadd = models.EmailField()
    contact = models.CharField(max_length = 11)

    def __str__(self):
        return f"{self.studID} {self.lastname} {self.firstname}"
    
    class Meta:
        ordering = ['lastname']  


class RequestedGMC(models.Model):
    student = models.ForeignKey(studentInfo, on_delete=models.CASCADE)
    reason = models.TextField()
    or_num = models.CharField(max_length=100, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)  
    
    def __str__(self):
        return f"GMC Request for {self.student} - {self.reason}"

class Schedule(models.Model):
    sched_Id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
   
    
    def __str__(self):
        return f"{self.sched_Id} {self.title}"


class equipment(models.Model):
    itemId = models.AutoField(primary_key=True)
    equipmentName = models.CharField(max_length=255)
    equipmentSN = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.equipmentName} {self.equipmentSN}"


class Program(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    image_upload = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=1000)
    date_time = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    image_upload = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title


class MOD(models.Model):
    donated = models.CharField(max_length=255)
    name = models.CharField(max_length=150)

    donation_type = models.CharField(max_length=10)
    gcash_number = models.CharField(max_length=11)
    paymaya_number = models.CharField(max_length=11)

    amount = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    address_volunteer = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=11)
    date_sched = models.CharField(max_length=20)

    def __str__(self):
        return self.name
