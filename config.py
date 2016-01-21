WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# These are the settings that the Flast-WTF extension needs.
# L01: Activates the cross-site forgery prevention.
# L02: This is only needed if the CRSF is enabled.
#	|--It is used to create a cryptogryphic token that is used to validate a form.