from rest_framework import routers
from studentregistration.viewsets import StudentViewSet, StaffViewSet, CourseViewSet, UnitViewSet


router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('staff', StaffViewSet)
router.register('courses', CourseViewSet)
router.register('units', UnitViewSet)


urlpatterns = router.urls
