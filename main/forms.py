from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Institution, Classes, Subjects, Students
from django.core.validators import RegexValidator
import re

class InstitutionRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'input-field'
        }),
        max_length=191,
        help_text="Required: 6+ chars, 1 uppercase, 1 digit, 1 special char."
    )

    class Meta:
        model = Institution
        fields = ['institution_name', 'email', 'institution_abbreviation', 'password']
        
        # Adding class names and placeholders to match your UI
        widgets = {
            'institution_name': forms.TextInput(attrs={
                'placeholder': 'Global University of Excellence',
                'class': 'input-field'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'admin@edu.com',
                'class': 'input-field'
            }),
            'institution_abbreviation': forms.TextInput(attrs={
                'placeholder': 'e.g. MIT, Stanford',
                'class': 'input-field'
            }),
        }
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # You can add custom password validation here if needed

        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[0-9]', password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise forms.ValidationError("Password must contain at least one special character.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        return password

    def save(self, commit=True):
        institution = super().save(commit=False)
            # Here you can hash the password before saving if needed
        if commit:
            institution.save()
        return institution
    
    
# Form for user login (authentication)
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4',
            'placeholder': 'Email Address'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-400 rounded-lg p-2 w-full mb-4',
            'placeholder': 'Password'
        })
    )


class ClassHeadLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your email',
            'id': 'email',
        }),
        label='Email Address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your password',
            'id': 'password',
        }),
        label='Password'
    )

class SubjectHeadLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your email',
            'id': 'email',
        }),
        label='Email Address'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your password',
            'id': 'password',
        }),
        label='Password'
    )

class StudentLoginForm(forms.Form):
    roll_no = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your Roll No.',
            'id': 'roll_no',
        }),
        label="Roll No."
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter your password',
            'id': 'password',
        }),
        label="Password"
    )

class ParentLoginForm(forms.Form):
    roll_no = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
            'placeholder': 'Enter Student Roll No.',
            'id': 'roll_no',
        }),
        label="Roll No."
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'block w-full px-4 py-3 rounded-lg border border-gray-400',
        'placeholder': 'Enter your password',
        'id': 'password'
    }))


#######################################################################################################################


class AddClassForm(forms.ModelForm):
    class_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Class Name',
            'id': 'class_name',
        })
    )
    class_head = forms.CharField(  # Keeping class_head as a text field
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Class Head Name',
            'id': 'class_head',
        })
    )
    class_abbreviation = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'e.g. CS, MECH, MBA',
            'id': 'class_abbreviation',
        }),
        required=False,
        help_text="Short code for roll number generation."
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Email',
            'id': 'email',
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Password',
            'id': 'password',
            'onfocus': 'this.type="text"',
            'onblur': 'this.type="password"'
        })
    )

    class Meta:
        model = Classes
        fields = ['class_name', 'class_abbreviation', 'class_head', 'email', 'password']



# class AddSubjectForm(forms.ModelForm):
#     class Meta:
#         model = Subjects
#         fields = ['subject_name', 'subject_head', 'email', 'password', 'class_id']

#     subject_name = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
#             'placeholder': 'Enter Subject Name',
#             'autocomplete': 'off'
#         })
#     )

#     subject_head = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
#             'placeholder': 'Enter Subject Head',
#             'autocomplete': 'off'
#         })
#     )

#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={
#             'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
#             'placeholder': 'Enter Email',
#             'autocomplete': 'email'
#         })
#     )

#     password = forms.CharField(
#         max_length=100,
#         widget=forms.PasswordInput(attrs={
#             'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none password-field',
#             'placeholder': 'Enter Password',
#             'autocomplete': 'new-password'
#         })
#     )

#     # Lazy load class choices to prevent unnecessary DB queries on form initialization
#     class_id = forms.ModelChoiceField(
#         queryset=Classes.objects.none(),  # Initially empty, populated in __init__
#         empty_label="Select Class",
#         widget=forms.Select(attrs={
#             'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none'
#         })
#     )

#     def __init__(self, *args, **kwargs):
#         super(AddSubjectForm, self).__init__(*args, **kwargs)
#         self.fields['class_id'].queryset = Classes.objects.all()
class AddSubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['subject_name', 'subject_head', 'email', 'password', 'class_obj']

    subject_name = forms.CharField(
        max_length=191,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Subject Name',
            'autocomplete': 'off'
        })
    )

    subject_head = forms.CharField(
        max_length=191,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Subject Head',
            'autocomplete': 'off'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none',
            'placeholder': 'Enter Email',
            'autocomplete': 'email'
        })
    )

    password = forms.CharField(
        max_length=191,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none password-field',
            'placeholder': 'Enter Password',
            'autocomplete': 'new-password'
        })
    )

    class_obj = forms.ModelChoiceField(
        queryset=Classes.objects.none(),  # Initially empty, populated in __init__
        empty_label="Select Class",
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-[#4f0074] focus:outline-none'
        })
    )

    def __init__(self, *args, **kwargs):
        institution_id = kwargs.pop('institution_id', None)
        super(AddSubjectForm, self).__init__(*args, **kwargs)
        
        # --- This is the magic part ---
        # We override the method only for this specific instance of the field
        self.fields['class_obj'].label_from_instance = lambda obj: obj.class_abbreviation or obj.class_name
        # ------------------------------
        
        if institution_id:
            self.fields['class_obj'].queryset = Classes.objects.filter(institution_id=institution_id)

class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'roll_no', 'password', 'class_obj']

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'django-input',
            'placeholder': 'Enter Student Name',
            'autocomplete': 'off',
            'id': 'student_name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'django-input',
            'placeholder': 'Enter Student Email',
            'autocomplete': 'email',
            'id': 'email'
        })
    )

    parent_email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'django-input',
            'placeholder': 'Enter Parent Email',
            'autocomplete': 'email',
            'id': 'parent_email'
        })
    )

    roll_no = forms.CharField(
        max_length=20,
        validators=[RegexValidator(r'^[a-zA-Z0-9\-]+$', message="Only letters, numbers, and hyphens allowed.")],
        widget=forms.TextInput(attrs={
            'class': 'django-input',
            'placeholder': 'Enter Roll Number',
            'id': 'roll_no'})
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'django-input',
            'placeholder': 'Enter Password',
            'autocomplete': 'new-password',
            'id': 'password'
        })
    )

    # Lazy load class choices to prevent unnecessary DB queries on form initialization
    class_obj = forms.ModelChoiceField(
        queryset=Classes.objects.none(),  # Initially empty, populated in __init__
        empty_label="Select Class",
        widget=forms.Select(attrs={
            'class': 'django-input',
            'id': 'class_id' # Keep ID as class_id for JS compatibility
        })
    )

    def __init__(self, *args, **kwargs):
        institution_id = kwargs.pop('institution_id', None)
        super(AddStudentForm, self).__init__(*args, **kwargs)

        # --- This is the magic part ---
        # We override the method only for this specific instance of the field
        self.fields['class_obj'].label_from_instance = lambda obj: obj.class_abbreviation
        # ------------------------------

        if institution_id:
            qs = Classes.objects.filter(institution_id=institution_id).distinct()
            self.fields['class_obj'].queryset = qs
        else:
            self.fields['class_obj'].queryset = Classes.objects.all()



class ClassUploadForm(forms.Form):
    file = forms.FileField()


class SubjectUploadForm(forms.Form):
    file = forms.FileField()


class StudentUploadForm(forms.Form):
    file = forms.FileField()
