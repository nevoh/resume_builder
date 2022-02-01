from socket import fromshare
from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'
