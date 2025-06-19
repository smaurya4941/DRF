from rest_framework.throttling import UserRateThrottle
#TO set user rate limit for various actions 


class CustomUserRateThrottle(UserRateThrottle):
    """
    Custom user rate throttle that allows for different rate limits based on the action.
    """
    
    scope='custom'