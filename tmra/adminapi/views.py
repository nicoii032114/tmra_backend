from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, User, Training, Budget, Trainees, IndividualPoints, EmployeeEvaluation, Department, RolesResponsibilities, Schedule,EmploymentDetails
from .serializers import EmployeeSerializers, UserSerializers, TrainingSerializers, BudgetSerializers, TraineesSerializers, IndividualPointsSerializers, EmployeeEvaluationSerializers, DepartmentSerializers, RolesResponsibilitiesSerializers, ScheduleSerializers, EmploymentDetailsSerializers

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers

class BudgetView(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializers

class TraineesView(viewsets.ModelViewSet):
    queryset = Trainees.objects.all()
    serializer_class = TraineesSerializers

class IndividualPointsView(viewsets.ModelViewSet):
    queryset = IndividualPoints.objects.all()
    serializer_class = IndividualPointsSerializers

class EmployeeEvaluationView(viewsets.ModelViewSet):
    queryset = EmployeeEvaluation.objects.all()
    serializer_class = EmployeeEvaluationSerializers

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

class RolesResponsibilitiesView(viewsets.ModelViewSet):
    queryset = RolesResponsibilities.objects.all()
    serializer_class = RolesResponsibilitiesSerializers

class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers

class EmploymentDetailsView(viewsets.ModelViewSet):
    queryset = EmploymentDetails.objects.all()
    serializer_class = EmploymentDetailsSerializers