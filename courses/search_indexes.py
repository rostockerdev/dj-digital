from haystack import indexes

from courses.models import Course


class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(
        document=True,
        use_template=True,
        template_name="search/indexes/courses/course_text.txt",
    )
    title = indexes.CharField(model_attr="title")
    slug = indexes.CharField(model_attr="slug")
    description = indexes.CharField(model_attr="description")
    start_date = indexes.DateTimeField(model_attr="start_date")
    allowed_membership = indexes.MultiValueField()
    instructors = indexes.MultiValueField()
    thumbnail = indexes.CharField(model_attr="thumbnail")

    content_auto = indexes.EdgeNgramField(model_attr="title")

    def get_model(self):
        return Course

    def prepare_allowed_membership(self, object):
        return [
            membership.membership_type for membership in object.allowed_membership.all()
        ]

    def prepare_instructors(self, object):
        return [instructor.username for instructor in object.instructors.all()]

    def prepare_thumbnail(self, object):
        return object.thumbnail.url

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
