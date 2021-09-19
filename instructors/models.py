from django.conf import settings
from django.db import models
from django.db.models import Avg, Func
from django.db.models.signals import pre_save
from django.urls import reverse

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from phonenumber_field.modelfields import PhoneNumberField

from instructors.instructor_utility import unique_username_generator


class Round(Func):
    function = "ROUND"


class Instructor(models.Model):
    username = models.CharField("Instructor Name", max_length=64, blank=True, null=True)
    first_name = models.CharField("First Name", max_length=24, blank=True, null=True)
    last_name = models.CharField("Last Name", max_length=24, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    dofb = models.DateField("Date of Birth", blank=True, null=True)
    biography = models.TextField("Biography", blank=True, null=True)
    mobile_no = PhoneNumberField()
    pro_pic = ProcessedImageField(
        upload_to="instructor_pic/",
        default="avatar.jpg",
        processors=[ResizeToFill(180, 180)],
        format="JPEG",
        options={"quality": 60},
    )

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse(
            "instructors:instructor-detail", kwargs={"instructor_name": self.username}
        )

    @property
    def ratings(self):
        return self.rating_set.all().order_by("-pub_date")[:3]

    @property
    def rating_average(self):
        return self.rating_set.aggregate(rating_avg=Round(Avg("rating")))


def instructor_username_save(sender, instance, *args, **kwargs):
    if not instance.username:
        instance.username = unique_username_generator(
            instance, instance.first_name, instance.last_name, instance.username
        )


pre_save.connect(instructor_username_save, sender=Instructor)


class Rating(models.Model):
    RATING_CHOICES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name="Published Date", auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField("Review", blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

    def __str__(self):
        return self.review
