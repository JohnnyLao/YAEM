def client_logo_upload_to(instance, filename):
    return f"{instance.name.replace(' ', '_').capitalize()}/logo/{filename}"


def dish_image_upload_to(instance, filename):
    return f"{instance.client.name.replace(' ', '_').capitalize()}/dishes/{instance.food_type.name}/{instance.name}_{filename}"
