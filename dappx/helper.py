def get_json_format(userform, profileform):
    first_name = userform.cleaned_data.get('first_name')
    last_name = userform.cleaned_data.get('last_name')
    name = first_name + " " + last_name
    cnic = profileform.cleaned_data.get('id')
    gender = profileform.cleaned_data.get('gender')
