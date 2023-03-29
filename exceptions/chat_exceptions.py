class ChatAPIError(Exception):
    """Base class for Chat API related errors"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class AuthenticationError(ChatAPIError):
    """Raised when API credentials are invalid (API Key)"""
    pass


class AuthorizationError(ChatAPIError):
    """Raised when the authentication credentials are valid, but the API key doesn't have sufficient permissions to perform the requested action."""
    pass


class RateLimitError(ChatAPIError):
    """Raised when the API rate limit has been exceeded."""
    pass


class ServerError(ChatAPIError):
    """Raised when the server encounters an error"""
    pass

