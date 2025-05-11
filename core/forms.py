from django import forms
from .models import GuestUser

class GuestUserForm(forms.ModelForm):
    class Meta:
        model = GuestUser
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name to start'
            })
        }
        
class ChallengeSubmissionForm(forms.Form):
    # We will add fields dynamically in __init__

    def __init__(self, *args, **kwargs):
        # Expect 'num_blanks' to be passed in when creating the form instance
        num_blanks = kwargs.pop('num_blanks', 0)
        super().__init__(*args, **kwargs)

        # Dynamically create a CharField for each blank
        for i in range(num_blanks):
            self.fields[f'answer_{i}'] = forms.CharField(
                label=f'Blank #{i+1}',
                required=True,
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': f'Your code for blank {i+1}'})
                # You might use forms.Textarea for multi-line answers if needed
            )

    def get_ordered_answers(self) -> list[str]:
        """Helper method to extract answers in the correct order."""
        answers = []
        i = 0
        # Loop through field names like answer_0, answer_1, ...
        while True:
            field_name = f'answer_{i}'
            if field_name in self.cleaned_data:
                answers.append(self.cleaned_data[field_name])
                i += 1
            else:
                break # Stop when we run out of answer fields
        return answers