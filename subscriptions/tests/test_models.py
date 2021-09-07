from django.test import TestCase

from subscriptions.models import Subscribe


class SubscribeModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.subscribe_test = Subscribe.objects.create(
            email="testemail@gmail.com", status="subscribed"
        )

    def test_subscribe_model_instance(self):
        obj = Subscribe.objects.get(id=1)
        self.assertEqual(obj.email, "testemail@gmail.com")
