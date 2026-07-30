"""Test database models."""

import pytest
from app.models.user import User


class TestUserModel:
    """Test suite for the User model."""

    def test_user_creation(self):
        """Test that a User can be created with required fields."""
        user = User(username="admin", email="admin@cyberill.sec")
        assert user.username == "admin"
        assert user.email == "admin@cyberill.sec"
        assert user.is_active is True
        assert user.id is not None  # UUID auto-generated

    def test_user_repr(self):
        """Test User string representation."""
        user = User(username="analyst", email="analyst@cyberill.sec")
        assert "analyst" in repr(user)
        assert "analyst@cyberill.sec" in repr(user)

    def test_user_default_active(self):
        """Test that users are active by default."""
        user = User(username="readonly", email="ro@cyberill.sec")
        assert user.is_active is True

    def test_user_inactive(self):
        """Test that a user can be set inactive."""
        user = User(username="disabled", email="disabled@cyberill.sec", is_active=False)
        assert user.is_active is False

    def test_user_unique_id(self):
        """Test that each user gets a unique UUID."""
        user1 = User(username="u1", email="u1@test.com")
        user2 = User(username="u2", email="u2@test.com")
        assert user1.id != user2.id

    def test_user_timestamps(self):
        """Test that TimestampMixin is applied."""
        from app.models.base import TimestampMixin
        assert isinstance(User(), TimestampMixin)
