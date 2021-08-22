import os

from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from courses.models import Course, Lesson


def remove_file_and_cleanup(filepath):
    """
    Helper to remove a media file;
    also removes the containing folder, if left empty
    """
    folder = os.path.dirname(filepath)
    # remove file
    if os.path.isfile(filepath):
        os.remove(filepath)
    # finally, remove folder if empty
    if os.path.isdir(folder) and len(os.listdir(folder)) <= 0:
        os.rmdir(folder)


# @receiver(models.signals.post_delete, sender=Lesson)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem when corresponding `MediaFile` object is deleted."""

    # Collect names of FileFields
    fieldnames = [
        f.name for f in instance._meta.get_fields() if isinstance(f, models.FileField)
    ]
    for fieldname in fieldnames:
        field = getattr(instance, fieldname)
        if bool(field):
            remove_file_and_cleanup(field.path)


post_delete.connect(auto_delete_file_on_delete, sender=Lesson)
post_delete.connect(auto_delete_file_on_delete, sender=Course)

# @receiver(models.signals.pre_save, sender=Lesson)


def auto_delete_file_on_change(sender, instance, **kwargs):
    """ Deletes file from filesystem when corresponding object is changed or removed.\
    """

    if not instance.pk or sender.objects.filter(pk=instance.pk).count() <= 0:
        return False

    fieldnames = [
        f.name for f in instance._meta.get_fields() if isinstance(f, models.FileField)
    ]
    for fieldname in fieldnames:
        try:
            old_field = getattr(sender.objects.get(pk=instance.pk), fieldname)
            old_filepath = old_field.path

            new_field = getattr(instance, fieldname)
            new_filepath = new_field.path if new_field else None

            # if ready to save a new file, delete the old one
            if old_filepath != new_filepath:
                remove_file_and_cleanup(old_filepath)
        except Exception:
            pass


pre_save.connect(auto_delete_file_on_change, sender=Lesson)
pre_save.connect(auto_delete_file_on_change, sender=Course)
