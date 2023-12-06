
from rest_framework import serializers

from .models import *


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
  department = serializers.CharField(write_only=True)
  password = serializers.CharField(write_only=True)
  confirm_password = serializers.CharField(write_only=True)
 
  class Meta:
    model = CustomUser
    fields = ["id", "first_name", "last_name", "email", "role", "department", "password", "confirm_password"]
    
  def validate_department(self, value):
    if not Department.objects.filter(department_name=value).exists():
      raise serializers.ValidationError("Department does not exist!")
    return Department.objects.get(department_name=value)
    
  def create(self, **validated_data):
    return CustomUser.objects.create(validated_data)
      
  def save(self):
    user = CustomUser(
      first_name=self.validated_data["first_name"],
      last_name=self.validated_data["last_name"],
      email=self.validated_data["email"],
      role=self.validated_data["role"],
      department=self.validated_data["department"]
    )
    
    password = self.validated_data["password"]
    confirm_password = self.validated_data["confirm_password"]
    
    if password != confirm_password:
      raise serializers.ValidationError("Passwords must match!")
    else:
      user.set_password(password)
      user.save()
      return user


# Serializers for each model in the app models.py, meant to transform python objects into JSON formatted dictionaries and vice-versa
class CustomUserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(write_only=True)
  password = serializers.CharField(write_only=True)
  
  class Meta:
    model = CustomUser
    fields = ['email', 'password']
    
  def validate(self, attrs):
    email = attrs.get("email")
    password = attrs.get("password")
    
    try:
      user = CustomUser.objects.filter(email=email).first()
    except CustomUser.DoesNotExist:
      raise serializers.ValidationError(f"No user with email {email} exists!")
    
    if not user.check_password(password):
      raise serializers.ValidationError("Password not correct.")
    
    return attrs
    

class FacultySerializer(serializers.ModelSerializer):

  class Meta:
    model = Faculty
    fields = ('__all__')
    
class RASerializer(serializers.ModelSerializer):
  class Meta:
    model = RA
    fields = ('__all__')
    

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Projects
    fields = ('__all__')
    

class MilestoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Milestones
    fields = ('__all__')
    

class ProjectMilestoneSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProjectMilestones
    fields = ('__all__')
    
    
class ProjectCreationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Projects
        fields = ["id", "title", "start_date", "end_date", "description"]
        
    def create_project(self, **validated_data):
        return Projects.objects.create(validated_data)
    
    
    def save(self):
        
        milestone = Milestones(
            milestone=self.validated_data["milestone"]
        )
        milestone.save()
                
        project = Projects(
            title=self.validated_data["title"],
            start_date=self.validated_data["start_date"],
            end_date=self.validated_data["end_date"],
            description=self.validated_data["description"]
        )
        project.save()
        
        projectMilestone = ProjectMilestones(
            milestone_complete="No",
            milestone_id=milestone,
            project_id=project
        )
        projectMilestone.save()
        
        return project
    

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = ('__all__')
    

class InterestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Interest
    fields = ('__all__')
    

class FacultyInterestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Faculty_Interest
    fields = ('__all__')
    

class RAInterestSerializer(serializers.ModelSerializer):
  class Meta:
    model = RA_Interest
    fields = ('__all__')
    

class RAProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = RA_Project
    fields = ('__all__')
    

class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skills
    fields = ('__all__')
    

class ProjectSkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project_Skills
    fields = ('__all__')
    
class RASkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = RA_Skills
    fields = ('__all__')
    