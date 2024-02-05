def banquet_logo_upload_to(instance, filename):
    client_name = (
        instance.client.name if instance.client else instance.name + "_has_not_menu"
    )
    return f"{client_name.replace(' ', '_').capitalize()}/logo/banquet_{filename}"


def subhall_photo_upload_to(instance, filename):
    client_name = (
        instance.banquet_card.client.name
        if instance.banquet_card and instance.banquet_card.client
        else "unknown"
    )
    return f"{client_name.replace(' ', '_').capitalize()}/banquet_photo/{filename}"
