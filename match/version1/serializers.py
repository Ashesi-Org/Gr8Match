from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "first_name", "last_name", "email", "role", "department", "last_login", ]


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("Invalid password provided")

        return value

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Confirm password and new password do not match")

        if attrs["old_password"] == attrs["new_password"]:
            raise serializers.ValidationError("Old password cannot be used as new password")

        # validate_password(attrs["new_password"], user=self.context["request"].user)
        return attrs

    def update(self, instance):
        user = self.context["request"].user

        instance.set_password(self.validated_data["new_password"])
        instance.save()
        return instance


class UploadPhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField(write_only=True, required=True)

    def validate_file_extension(image):
        if not image.name.lower().endswith(".png"):
            raise ValidationError("Only PNG files allowed")
        return image

    def update(self, instance):
        user = self.context["request"].user
        uploaded_image = self.request.FILES["photo"]
        filename = uploaded_image.name

        instance.image = filename
        instance.save()
        return instance


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


class ProjectApplicationSerializer(serializers.Serializer):

    def save(self, ra_id, project_id):
        ra_project = RA_Project(
            status="Pending",
            project_id=project_id,
            rA_id=ra_id
        )

        ra_project.save()
        return ra_project


class ProjectMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMilestones
        fields = ('__all__')


class ProjectCreationSerializer(serializers.ModelSerializer):
    skills = serializers.ListField(write_only=True)

    class Meta:
        model = Projects
        fields = ["owner", "title", "start_date", "end_date", "description", "department", "skills"]

    def create(self, validated_data):
        # Store skills in context
        self.context["skills"] = validated_data.pop("skills")

        project = Projects.objects.create(**validated_data)

        # Access skills from context and create ProjectSkills objects
        for skill_name in self.context["skills"]:
            try:
                skill = Skills.objects.get(skill_name=skill_name)
                Project_Skills.objects.create(project=project, skills=skill)
            except Skills.DoesNotExist:
                pass

        return project


class TaskCreationSerializer(serializers.ModelSerializer):
    # project_id = serializers.IntegerField()
    # milestone_id = serializers.IntegerField()

    class Meta:
        model = ProjectMilestoneTask
        fields = ["task", ]

    def save(self, project_milestone):
        task = ProjectMilestoneTask(
            project_milestone=project_milestone,
            task=self.validated_data["task"],
            completed=False
        )

        task.save()

        return task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMilestoneTask
        fields = ('__all__')


class MatchingSerializer(serializers.Serializer):
    faculty_id = serializers.IntegerField()
    project_id = serializers.IntegerField()


class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = ('__all__')


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
