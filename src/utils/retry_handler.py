"""
Retry handling utilities for API calls and error recovery.
"""

import time
import logging
from typing import Callable, Any, Optional, Union
from functools import wraps


class RetryHandler:
    """Utility class for handling retries with exponential backoff."""
    
    def __init__(
        self,
        max_attempts: int = 3,
        base_delay: float = 1.0,
        max_delay: float = 60.0,
        exponential_base: float = 2.0
    ):
        """
        Initialize retry handler.
        
        Args:
            max_attempts: Maximum number of retry attempts
            base_delay: Initial delay between retries in seconds
            max_delay: Maximum delay between retries in seconds
            exponential_base: Base for exponential backoff calculation
        """
        self.max_attempts = max_attempts
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        
        # Setup logging
        self.logger = logging.getLogger(__name__)
    
    def calculate_delay(self, attempt: int) -> float:
        """Calculate delay for the given attempt number."""
        delay = self.base_delay * (self.exponential_base ** attempt)
        return min(delay, self.max_delay)
    
    def retry_on_exception(
        self,
        exceptions: Union[Exception, tuple] = Exception,
        should_retry_func: Optional[Callable[[Exception], bool]] = None
    ):
        """
        Decorator for retrying function calls on specified exceptions.
        
        Args:
            exceptions: Exception types to retry on
            should_retry_func: Optional function to determine if retry should happen
        """
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(*args, **kwargs) -> Any:
                last_exception = None
                
                for attempt in range(self.max_attempts):
                    try:
                        return func(*args, **kwargs)
                        
                    except exceptions as e:
                        last_exception = e
                        
                        # Check if we should retry this specific exception
                        if should_retry_func and not should_retry_func(e):
                            self.logger.warning(f"Not retrying due to should_retry_func: {str(e)}")
                            raise e
                        
                        # Don't retry on the last attempt
                        if attempt == self.max_attempts - 1:
                            self.logger.error(f"Max retries ({self.max_attempts}) exceeded for {func.__name__}")
                            raise e
                        
                        # Calculate delay and wait
                        delay = self.calculate_delay(attempt)
                        self.logger.warning(
                            f"Attempt {attempt + 1}/{self.max_attempts} failed for {func.__name__}: {str(e)}. "
                            f"Retrying in {delay:.1f} seconds..."
                        )
                        time.sleep(delay)
                
                # This should never be reached, but just in case
                if last_exception:
                    raise last_exception
                    
            return wrapper
        return decorator


def is_retryable_api_error(exception: Exception) -> bool:
    """
    Determine if an API error should be retried.
    
    Args:
        exception: The exception to check
        
    Returns:
        True if the error should be retried, False otherwise
    """
    error_message = str(exception).lower()
    
    # Retryable conditions
    retryable_patterns = [
        "rate limit",
        "timeout",
        "temporary",
        "service unavailable",
        "internal server error",
        "connection error",
        "network error",
        "502",
        "503",
        "504"
    ]
    
    # Non-retryable conditions
    non_retryable_patterns = [
        "invalid api key",
        "authentication",
        "unauthorized",
        "forbidden",
        "not found",
        "400",
        "401",
        "403",
        "404"
    ]
    
    # Check for non-retryable errors first
    for pattern in non_retryable_patterns:
        if pattern in error_message:
            return False
    
    # Check for retryable errors
    for pattern in retryable_patterns:
        if pattern in error_message:
            return True
    
    # Default to retrying unknown errors (conservative approach)
    return True


# Pre-configured retry handlers for common use cases
def retry_api_call(max_attempts: int = 3, base_delay: float = 1.0):
    """Decorator for retrying API calls with smart error detection."""
    handler = RetryHandler(max_attempts=max_attempts, base_delay=base_delay)
    return handler.retry_on_exception(
        exceptions=Exception,
        should_retry_func=is_retryable_api_error
    )


def retry_with_backoff(max_attempts: int = 3, base_delay: float = 1.0):
    """Decorator for basic retry with exponential backoff."""
    handler = RetryHandler(max_attempts=max_attempts, base_delay=base_delay)
    return handler.retry_on_exception(exceptions=Exception)


# Standalone retry function for use without decorators
def execute_with_retry(
    func: Callable,
    max_attempts: int = 3,
    base_delay: float = 1.0,
    should_retry_func: Optional[Callable[[Exception], bool]] = None,
    *args,
    **kwargs
) -> Any:
    """
    Execute a function with retry logic.
    
    Args:
        func: Function to execute
        max_attempts: Maximum retry attempts
        base_delay: Initial delay between retries
        should_retry_func: Optional function to determine retry eligibility
        *args, **kwargs: Arguments to pass to the function
        
    Returns:
        Function result
        
    Raises:
        Last encountered exception if all retries fail
    """
    handler = RetryHandler(max_attempts=max_attempts, base_delay=base_delay)
    
    @handler.retry_on_exception(
        exceptions=Exception,
        should_retry_func=should_retry_func
    )
    def wrapper():
        return func(*args, **kwargs)
    
    return wrapper()