from exceptiongen import exception_generator as eg

OxfordException = eg('OxfordException')
InvalidAPIInfoError = eg('InvalidAPIInfoError', parent = OxfordException, message='The app_id/app_key is invalid. Please check the app_id/app_key.')
