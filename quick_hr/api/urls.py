from rest_framework.routers import SimpleRouter
from quick_hr.api.api import BroadCastView, HolidayView

router = SimpleRouter()
router.register("broadcasts", BroadCastView, basename="broadcasts")
router.register("holidays", HolidayView, basename="holidays")
