
API_VERSION = "v1"
API_VERSION_URL = "api/"+API_VERSION+"/"
NAME_REGULAR_EXPRESSION = "^[a-zA-Z0-9.!@#%&*()_ ]*$"
NUMBER_ONLY = "^[0-9]*$"
REGEX_VALID = {
    'password': '^[a-zA-Z0-9]+$'
}

CHARACTER_SIZE = {
    'first_name_max': 50,
    'last_name_max': 50,
    'phone_max': 10,
    'phone_min': 10,
    'pass_min': 8,
    'pass_max': 20,
    'company_name': 100,
    'employee_size_min': 1,
    'employee_size_max': 99999,
}


EMAIL_REGEX = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
