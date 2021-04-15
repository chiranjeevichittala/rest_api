from rest_framework import routers
from core.views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'universities', UniversityViewSet)

urlpatterns = router.urls

# http://127.0.0.1:8000/api/students
# http://127.0.0.1:8000/api/universities