"""Custom exceptions for MetMetric Communications API"""

class MetMetricError(Exception):
    """Base exception for MetMetric API errors"""
    pass

class AuthenticationError(MetMetricError):
    """Raised when authentication fails"""
    pass

class APIError(MetMetricError):
    """Raised when API request fails"""
    pass