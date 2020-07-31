from allauth.account.forms import SignupForm, LoginForm, ResetPasswordForm

class PassportSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(PassportSignUpForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            input_type = field.widget.input_type
            if input_type not in ['checkbox']:
                field.widget.attrs.update({
                    'class': 'form-input'
                })            

class PassportLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(PassportLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            input_type = field.widget.input_type
            if input_type not in ['checkbox']:
                field.widget.attrs.update({
                    'class': 'form-input'
                })            

class ResetPasswordForm(ResetPasswordForm):

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            input_type = field.widget.input_type
            if input_type not in ['checkbox']:
                field.widget.attrs.update({
                    'class': 'form-input'
                })            
