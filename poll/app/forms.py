from django import forms
from .models import Question, Choice, VoteForm
class VoteFrom(forms.ModelForm):
    class Meta:
        model = VoteForm
        fields = ['question','choice']

    def __init__(self, question_id):
        super(VoteFrom, self).__init__()
        self.fields['question'].queryset = Question.objects.filter(id=question_id)
        self.fields['choice'].queryset = Choice.objects.filter(question=question_id)