from django_registration.forms import RegistrationForm
# RegistrationFormTermsOfService, RegistrationFormUniqueEmail

from movienight_auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class MovieNightRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User

    def __init__(self, *args, **kwargs):
        super(MovieNightRegistrationForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))