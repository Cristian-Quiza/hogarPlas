from django import forms
from .models import Users

class usersForm(forms.ModelForm):
    # Muestra los valores que estan en cada una de las tablas
    class Meta:
        model = Users
        fields = ('rol_id','first_names','last_names','type_id','num_document','address','phone','email',
                  'Password','Condition','Rol')
        labels = {
            'rol_id': 'Id Rol',
            'first_names': 'First Names',
            'last_names': 'Last Names',
            'type_id': 'Type id',
            'num_document': 'Number Document'
        }
        
    def __init__(self, *args, **kwargs):
        super(usersForm, self).__init__(*args, **kwargs)
        self.fields['Rol'].empty_label = "Select"
        self.fields['Condition'].required = False