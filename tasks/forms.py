from django import forms
from django.forms import ModelForm
from crispy_forms.layout import Layout, Fieldset, Row, Column, Submit, Div, ButtonHolder, Field
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton, InlineField, InlineCheckboxes
from .models import Task
from datetime import datetime
from django.urls import reverse_lazy


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'category', 'deadline']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = 'create_task'
        self.helper.field_template = 'bootstrap5/layout/inline_field.html'
        # self.helper.form_class = "form-inline"
        self.helper.layout = Layout(
                Div(
            Div('name', css_class="col"),
            Div('deadline', css_class="col-sm"),
            Div('category', css_class="col-sm"),
            ButtonHolder(Submit( 'Save', 'Add task', css_class='btn-primary my-2')),
            css_class="row"))
            
        self.fields['deadline'] = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'min': datetime.now().date()}))

class EditTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('edit_task', args=[self.instance.id])
        self.helper.form_show_labels = False
        self.helper.form_id = 'update-task'
        # self.helper.form_tag = False #don't wrap in form tag
        self.helper.layout = Layout(
                Div(
            Div('name', css_class="col"),
            Div(ButtonHolder(Submit('Update', 'Update', css_class='btn-primary')), css_class="col"),
            css_class="row"),
        )
        
class TaskCompleteForm(ModelForm):
    class Meta:
        model = Task
        fields = ('completed', )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_style = 'inline'
        self.helper.form_action = reverse_lazy('complete_task', args=[self.instance.id])