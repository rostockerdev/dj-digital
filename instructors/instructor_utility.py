def unique_username_generator(model_instance, first_name, last_name, username):
    """
    :param model_instance
    :param first_name
    :param last_name
    :param username
    :return

    """
    # model_class = model_instance.__class__
    if first_name == "" or first_name is None:
        first_name = ""
    if last_name == "" or last_name is None:
        last_name = ""
    username = f"{first_name} {last_name}"
    return username
