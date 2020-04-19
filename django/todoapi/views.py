# For getting the username from the JWT token.
from rest_framework_jwt.utils import jwt_decode_handler
from .utils import get_auth0_user_id_from_request



# Lists and Creates entries of Task.
class TaskList(generics.ListCreateAPIView):
    """
    Lists and creates tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        auth0_user_id = get_auth0_user_id_from_request(self.request)
        # Set the user to the one in the token.
        serializer.save(created_by=auth0_user_id)

    def get_queryset(self):
        """
        This view should return a list of all Tasks
        for the currently authenticated user.
        """
        token = self.request.META.get('HTTP_AUTHORIZATION', '').split()[1]
        payload = jwt_decode_handler(token)
        auth0_user_id = payload.get('sub')
        return Task.objects.filter(created_by=auth0_user_id)