from django.db import models

#DATABASE MODEL FOR EMPLOYEE TABLE
class Employee(models.Model):
    employeeID = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    contact_number = models.IntegerField()
    gender = models.IntegerField()
    birthday = models.DateField()
    age = models.CharField(max_length=255)
    citizenship = models.CharField(max_length=20)
    height = models.DecimalField(max_digits=16, decimal_places=2)
    weight = models.DecimalField(max_digits=16, decimal_places=2)
    blood_type = models.IntegerField()
    status = models.IntegerField()
    image = models.ImageField('profilepic', blank=True)
    def __str__(self):
       return self.employeeID
    

#DATABASE MODEL FOR USER TABLE
class User(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.IntegerField()
    token = models.CharField(max_length=5000)
    def __str__(self):
       return self.username

#DATABASE MODEL FOR TRAINING TABLE
class Training(models.Model):
    training = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    time = models.CharField(max_length=100)
    timeDisplay = models.CharField(max_length=100)
    speaker = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    address = models.CharField(max_length=500,blank=True)
    def __str__(self):
       return self.training

#DATABASE MODEL FOR BUDGET TABLE
class Budget(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateField()
    amount = models.CharField(max_length=255)
    def __str__(self):
       return self.training

#DATABASE MODEL FOR TRAINEES TABLE
class Trainees(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    def __str__(self):
       return self.employee

#DATABASE MODEL FOR INDIVIDUAL POINTS TABLE
class IndividualPoints(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.TimeField()
    notpaid_billable = models.TimeField()
    extra_workload = models.TimeField()
    management = models.TimeField()
    training = models.TimeField()
    admin = models.TimeField()
    investment = models.TimeField()
    non_billable = models.TimeField()
    sales = models.TimeField()
    points = models.CharField(max_length=50)

    def __str__(self):
        return self.employee_id

#DATABASE MODEL FOR EMPLOYEE EVALUATION TABLE
class EmployeeEvaluation(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=50)
    certified_by = models.CharField(max_length=50)
    performance_rating = models.DecimalField(max_digits=16, decimal_places=2)
    def __str__(self):
       return self.employee_id

#DATABASE MODEL FOR DEPARTMENT TABLE
class Department(models.Model):
    department_name = models.CharField(max_length=50, unique=True)
    classification = models.CharField(max_length=50)
    def __str__(self):
       return self.department_name

#DATABASE MODEL FOR ROLES AND RESPONSIBILITIES TABLE
class RolesResponsibilities(models.Model):
    position = models.CharField(max_length=255, unique=True)
    responsibilities = models.CharField(max_length=5000)
    def __str__(self):
       return self.position

#DATABASE MODEL FOR SCHEDULE TABLE
class Schedule(models.Model):
    login = models.TimeField()
    breakout = models.TimeField()
    breakin = models.TimeField()
    logout = models.TimeField()
    def __int__(self):
       return self.login

#DATABASE MODEL FOR EMPLOYMENT DETAILS TABLE
class EmploymentDetails(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_employed = models.DateField()
    date_effective = models.DateField()
    roles_responsibilities_id = models.ForeignKey(RolesResponsibilities, on_delete=models.CASCADE)
    quota = models.DecimalField(max_digits=16, decimal_places=2)
    salary_base = models.DecimalField(max_digits=16, decimal_places=2)
    basic_rate = models.DecimalField(max_digits=16, decimal_places=2)
    incentive = models.DecimalField(max_digits=16, decimal_places=2)
    challenge_quota = models.DecimalField(max_digits=16, decimal_places=2, blank=True)
    designation = models.CharField(max_length=255)
    assignment = models.CharField(max_length=255)
    employee_type = models.IntegerField()
    employment_status = models.IntegerField()
    resignation_date = models.DateField(null=True)
    end_of_contract = models.DateField(null=True)
    remarks_for_resignation_termination = models.CharField(max_length=255, blank=True)
    flexi = models.IntegerField()
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)

#DATABASE MODEL FOR EMPLOYMENT DETAILS HISTORY
class EmploymentHistory(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    date_employed = models.DateField()
    date_effective = models.DateField()
    roles_responsibilities_id = models.ForeignKey(RolesResponsibilities, on_delete=models.CASCADE)
    quota = models.CharField(max_length=255)
    salary_base = models.DecimalField(max_digits=16, decimal_places=2)
    basic_rate = models.DecimalField(max_digits=16, decimal_places=2)
    incentive = models.DecimalField(max_digits=16, decimal_places=2)
    challenge_quota = models.CharField(max_length=255, blank=True)
    designation = models.CharField(max_length=255)
    assignment = models.CharField(max_length=255)
    employee_type = models.IntegerField()
    employment_status = models.IntegerField()
    resignation_date = models.DateField(null=True)
    end_of_contract = models.DateField(null=True)
    remarks_for_resignation_termination = models.CharField(max_length=255, blank=True)
    flexi = models.IntegerField()
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date_updated = models.DateField()

#DATABASE MODEL FOR SCHEDULE TABLE
class UserLogs(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

#DATABASE MODEL FOR ACCOUNT SETTINGS
class AccountSettings(models.Model):
    user_type = models.CharField(max_length=255)
    employeeProfile = models.BooleanField()
    individualPoints = models.BooleanField()
    trainingSeminar = models.BooleanField()
    positionResponsibilities = models.BooleanField()
    reports = models.BooleanField()
    adminSettings = models.BooleanField()
    departmentSettings = models.BooleanField()
    userSettings = models.BooleanField()
    userLogs = models.BooleanField()
