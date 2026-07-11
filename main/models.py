from django.db import models
# from django.contrib.auth.models import User

class Institution(models.Model):
    institution_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    institution_name = models.CharField(max_length=50)
    password = models.CharField()
    institution_abbreviation = models.CharField(max_length=50, unique=True, null=True, blank=True)


    def __str__(self):
        return self.institution_name
class Users(models.Model):
    ROLE_CHOICES = [
        ('class_head', 'Class Head'),
        ('subject_head', 'Subject Head'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.role} - {self.id}"

    

class Classes(models.Model):
    id = models.BigAutoField(primary_key=True)
    class_name = models.CharField(max_length=50)
    class_head = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField()
    class_abbreviation = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.class_abbreviation or self.class_name



class Subjects(models.Model):
    id = models.BigAutoField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    subject_head = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name




class Students(models.Model):
    id = models.BigAutoField(primary_key=True)
    roll_no = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True, null=True, blank=True)
    password = models.CharField()
    class_obj = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Parents(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    password = models.CharField()
    name = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True) 
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user'],
                name='unique_parent_user'
            )
        ]


class Attendance(models.Model):
    class StatusChoices(models.TextChoices):
        PRESENT = 'present', 'Present'
        ABSENT = 'absent', 'Absent'

    id = models.BigAutoField(primary_key=True)
    attendance_date = models.DateField()
    hour = models.PositiveSmallIntegerField()
    status = models.CharField(
        max_length=10, 
        choices=StatusChoices.choices,
        default=StatusChoices.PRESENT
    )
    student = models.ForeignKey('Students', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class StudentEvaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    study_time_rating = models.FloatField(null=True)
    sleep_time_rating = models.FloatField(null=True)
    class_participation_rating = models.FloatField(null=True)
    academic_activity_rating = models.FloatField(null=True)
    attendance_percentage = models.FloatField(null=True)
    marks_percentage = models.FloatField(null=True)

class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    sender = models.ForeignKey(Users, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name='received_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class Quizzes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    class_obj = models.ForeignKey(Classes, on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class QuizQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)
    correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

class QuizResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(QuizQuestions, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    student_response = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], null=True, blank=True)
    

class Announcements(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.TextField()
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

class AnnouncementRead(models.Model):
    """Track which students have read each announcement"""
    id = models.BigAutoField(primary_key=True)
    announcement = models.ForeignKey(Announcements, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    read_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('announcement', 'student')  # Prevent duplicate reads

class StudyMaterials(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_url = models.TextField(null=True, blank=True)
    announcement = models.TextField(null=True, blank=True)
    class_obj = models.ForeignKey(Classes, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('login', 'User Login'),
        ('logout', 'User Logout'),
    ]
    
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='audit_logs', null=True, blank=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='audit_logs', null=True, blank=True)
    action = models.CharField(max_length=50, choices=ACTION_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField(blank=True, null=True, help_text="Additional details about the action")
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    related_object_id = models.PositiveIntegerField(blank=True, null=True, help_text="ID of related object (e.g., prescription ID)")
    related_object_type = models.CharField(max_length=50, blank=True, null=True, help_text="Type of related object (e.g., Prescription, Appointment)")
    
    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['user', '-timestamp']),
            models.Index(fields=['action', '-timestamp']),
        ]
    
    def __str__(self):
        if self.institution:
             return f"{self.institution} - {self.get_action_display()} at {self.timestamp}"
        return f"{self.user} - {self.get_action_display()} at {self.timestamp}"
    
    def get_user_display_name(self):
        """Get display name for the user based on their role"""
        if self.institution:
            return self.institution.institution_name
        
        if self.user:
            return str(self.user)
            
        return "Unknown User"