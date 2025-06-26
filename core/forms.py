from django import forms
from .models import GuestUser

class GuestUserForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    magic_word = forms.CharField(max_length=100, label="Your Secret Magic Word")
        
class ChallengeSubmissionForm(forms.Form):

    def __init__(self, *args, **kwargs):
        num_blanks = kwargs.pop('num_blanks', 0)
        super().__init__(*args, **kwargs)
        for i in range(num_blanks):
            self.fields[f'answer_{i}'] = forms.CharField(
                label=f'Blank #{i+1}',
                required=True,
                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': f'Your code for blank {i+1}'})
            )

    def get_ordered_answers(self) -> list[str]:
        """Helper method to extract answers in the correct order."""
        answers = []
        i = 0
        while True:
            field_name = f'answer_{i}'
            if field_name in self.cleaned_data:
                answers.append(self.cleaned_data[field_name])
                i += 1
            else:
                break
        return answers