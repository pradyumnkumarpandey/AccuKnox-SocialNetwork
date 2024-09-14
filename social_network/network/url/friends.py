from django.urls import path  , include
from network.friends.views import SendFriendRequests, ViewPendingRequests, RejectFriendRequests, AcceptFriendRequests, ViewFriends
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('send_request',SendFriendRequests,basename="send_request")
router.register('pending_requests',ViewPendingRequests,basename="pending_requests")
router.register('reject_request',RejectFriendRequests,basename="reject_request")
router.register('accept_request',AcceptFriendRequests,basename="accept_request")
router.register('view_friends',ViewFriends,basename="view_friends")






urlpatterns = [
    path("", include(router.urls)),

]