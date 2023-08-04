from django.contrib.auth import get_user_model

user_model = get_user_model()


def create_user(email, **kwargs):
    password = kwargs.pop("password", None)
    user = user_model.objects.create_user(email, password, **kwargs)

    # TODO send notification
    return user
