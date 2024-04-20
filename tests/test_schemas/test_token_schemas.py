import pytest
from pydantic import ValidationError
from app.schemas.token_schemas import Token, TokenData, RefreshTokenRequest

# Example token data
token_data = {
    "access_token": "jhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}

# Test Token model
def test_token_model():
    try:
        token = Token(**token_data)
        assert token.access_token == token_data["access_token"]
        assert token.token_type == token_data["token_type"]
    except ValidationError as e:
        pytest.fail(f"Token validation failed: {e}")

# Test TokenData model
def test_token_data_model():
    try:
        token_data_obj = TokenData(**token_data)
        assert token_data_obj.username is None
    except ValidationError as e:
        pytest.fail(f"TokenData validation failed: {e}")

# Test RefreshTokenRequest model
def test_refresh_token_request_model():
    refresh_token_data = {"refresh_token": token_data["access_token"]}
    try:
        refresh_token_request = RefreshTokenRequest(**refresh_token_data)
        assert refresh_token_request.refresh_token == refresh_token_data["refresh_token"]
    except ValidationError as e:
        pytest.fail(f"RefreshTokenRequest validation failed: {e}")
