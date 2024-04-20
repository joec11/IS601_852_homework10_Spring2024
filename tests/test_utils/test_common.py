import pytest
from datetime import timedelta
from fastapi import HTTPException
from app.utils.common import (
    create_access_token,
    validate_and_sanitize_url,
    verify_refresh_token,
    encode_url_to_filename,
    decode_filename_to_url,
)

# Mock settings object
class MockSettings:
    def __init__(self):
        self.admin_user = "admin"
        self.admin_password = "adminpassword"
        self.secret_key = "secret"
        self.algorithm = "HS256"

mock_settings = MockSettings()

# Test cases
def test_create_access_token():
    data = {"sub": "test_user"}
    expires_delta = timedelta(minutes=15)
    token = create_access_token(data, expires_delta)
    assert isinstance(token, str)

def test_validate_and_sanitize_url():
    valid_url = "https://example.com"
    invalid_url = "not_a_url"
    assert validate_and_sanitize_url(valid_url) == valid_url
    assert validate_and_sanitize_url(invalid_url) is None

def test_verify_refresh_token():
    valid_token = create_access_token({"sub": "test_user"}, timedelta(minutes=15))
    assert verify_refresh_token(valid_token) == {"username": "test_user"}

    invalid_token = "invalid_token"
    with pytest.raises(HTTPException):
        verify_refresh_token(invalid_token)

def test_encode_decode_url():
    url = "https://example.com"
    encoded_url = encode_url_to_filename(url)
    decoded_url = decode_filename_to_url(encoded_url)
    assert decoded_url == url
