from rest_framework.routers import SimpleRouter
from quick_hr.api.api import BroadCastView

router = SimpleRouter()
router.register("broadcasts", BroadCastView, basename="broadcasts")
