from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from api.serializers import PrettyJSONSerializer
from apiplayground.models import Feedback


class FeedbackResource(ModelResource):

    class Meta:
        resource_name = "feedbacks"
        queryset = Feedback.objects.all()
        authorization = Authorization()
        serializer = PrettyJSONSerializer()
        always_return_data = True