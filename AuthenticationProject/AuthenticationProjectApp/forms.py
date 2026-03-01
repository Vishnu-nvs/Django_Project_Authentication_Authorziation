from django.contrib.auth.forms import UserCreationForm


class NoHelpUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # disable help text for all fields
        for field in self.fields.values():
            field.help_text = ''
