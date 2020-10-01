"""
validation error messages
"""
# Define valid character limit & min & max validation
CHAR_LIMIT_SIZE = {
    'max_description': 500,
    'zip_code_min': 4,
    'zip_code_max': 16,
}

# Define Validation message for all request submission
VALIDATION = {
    'email': {
        "blank": "Email is required",
        "invalid": "Your e-mail address is invalid. Please try again.",
        "min_length": "Email should be of minimum 5 characters",
        "max_length": "Email should be of maximum 254 characters"
    },
    'password': {
        "blank": "Password is required",
        "min_length": "Password should be of minimum 8 characters",
        "max_length": "Password should be of maximum 20 characters",
        "pattern": "Please enter valid alphanumeric password."
    },
    'old_password': {
        "blank": "Current password is required",
        "min_length": "Current password should be of minimum 8 characters",
        "max_length": "Current password should be of maximum 20 characters",
        "pattern": "Please enter valid alphanumeric current password."
    },
    'login_password': {
        "blank": "Password is required",
        "min_length": "Invalid login credentials",
        "max_length": "Invalid login credentials"
    },
    'zip_code': {
        "blank": "Please enter zip codee",
        "min_length": "Zip code should be minimum "+str(CHAR_LIMIT_SIZE['zip_code_min']) + " characters",
        "max_length": "Zip code should be maximum "+str(CHAR_LIMIT_SIZE['zip_code_max']) + " characters",
    },
    'first_name': {
        "blank": "Please enter first name",
        "max_length": "First name should be of maximum 50 characters",
        "special_char_error": "Special characters are not allowed in first name."
    },
    'last_name': {
        "blank": "Please enter last name",
        "max_length": "last name should be of maximum 50 characters",
        "special_char_error": "Special characters are not allowed in last name."
    },
    'phone': {
        "blank": "Phone is required",
        "invalid": "Your phone number is invalid. Please try again.",
        "min_length": "Phone should be of minimum 10 digits",
        "max_length": "Phone should be of maximum 10 digits"
    },
    'address': {
        "blank": "Address is required",
        "invalid": "Please enter a address"
    },
}