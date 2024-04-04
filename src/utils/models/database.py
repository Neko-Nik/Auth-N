"""
Models for the database tables with their relationships
Contains the following models:
    - User
    - Role
    - Permission
    - UserRoles
    - RolePermissions
    - LoginAttempt
    - AuditLog
    - Session
    - JWTToken
    - APIKey
    - PasswordResetToken
    - IPRestriction
    - CSRFToken
    - OTPToken
    - Device
"""

from src.utils.base.libraries import (
    Column,
    Integer,
    String,
    DateTime,
    JSON,
    Boolean,
    ForeignKey,
    relationship,
    datetime,
    timezone,
    declarative_base
)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    password_salt = Column(String)
    email = Column(String, index=True)
    phone_number = Column(String)
    profile_picture_url = Column(String, default="")    # TODO: Add default profile picture URL
    last_login = Column(DateTime)
    is_active = Column(Boolean, default=True)
    is_locked = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)
    lockout_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, onupdate=datetime.now(timezone.utc))
    password_last_changed = Column(DateTime)
    failed_login_attempts = Column(Integer, default=0)

    roles = relationship("Role", secondary="user_roles", back_populates="users", primaryjoin="User.user_id == UserRoles.user_id", secondaryjoin="Role.role_id == UserRoles.role_id")
    login_attempts = relationship("LoginAttempt", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")
    sessions = relationship("Session", back_populates="user")
    jwt_tokens = relationship("JWTToken", back_populates="user")
    api_keys = relationship("APIKey", back_populates="user")
    password_reset_tokens = relationship("PasswordResetToken", back_populates="user")
    ip_restrictions = relationship("IPRestriction", back_populates="user")
    csrf_tokens = relationship("CSRFToken", back_populates="user")
    otp_tokens = relationship("OTPToken", back_populates="user")
    devices = relationship("Device", back_populates="user")


class Role(Base):
    __tablename__ = "roles"

    role_id = Column(String, primary_key=True)
    role_name = Column(String, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    users = relationship("User", secondary="user_roles", back_populates="roles", primaryjoin="Role.role_id == UserRoles.role_id", secondaryjoin="User.user_id == UserRoles.user_id")
    permissions = relationship("Permission", secondary="role_permissions")


class Permission(Base):
    __tablename__ = "permissions"

    permission_id = Column(String, primary_key=True)
    permission_name = Column(String, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    permission_data = Column(JSON)


class UserRoles(Base):
    __tablename__ = "user_roles"

    user_id = Column(String, ForeignKey("users.user_id"), primary_key=True)
    role_id = Column(String, ForeignKey("roles.role_id"), primary_key=True)
    assigned_by = Column(String, ForeignKey("users.user_id"))
    assigned_at = Column(DateTime, default=datetime.now(timezone.utc))


class RolePermissions(Base):
    __tablename__ = "role_permissions"

    role_id = Column(String, ForeignKey("roles.role_id"), primary_key=True)
    permission_id = Column(String, ForeignKey("permissions.permission_id"), primary_key=True)
    assigned_by = Column(String, ForeignKey("users.user_id"))
    assigned_at = Column(DateTime, default=datetime.now(timezone.utc))


class LoginAttempt(Base):
    __tablename__ = "login_attempts"

    attempt_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    attempt_time = Column(DateTime, default=datetime.now(timezone.utc))
    success = Column(Boolean)
    ip_address = Column(String)
    other_info = Column(JSON)

    user = relationship("User", back_populates="login_attempts")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    log_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    action_performed = Column(String)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))
    details = Column(JSON)

    user = relationship("User", back_populates="audit_logs")


class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    device_info = Column(String)
    login_time = Column(DateTime, default=datetime.now(timezone.utc))
    last_activity_time = Column(DateTime, default=datetime.now(timezone.utc))
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="sessions")


class JWTToken(Base):
    __tablename__ = "jwt_tokens"

    token_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    token = Column(String)
    expiration_time = Column(DateTime)

    user = relationship("User", back_populates="jwt_tokens")


class APIKey(Base):
    __tablename__ = "api_keys"

    key_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    key = Column(String)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    user = relationship("User", back_populates="api_keys")


class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    token_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    token = Column(String)
    expiration_time = Column(DateTime)

    user = relationship("User", back_populates="password_reset_tokens")


class IPRestriction(Base):
    __tablename__ = "ip_restrictions"

    restriction_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    ip_address = Column(String)
    restriction_type = Column(String)   #, default="blacklist", options=["blacklist", "whitelist"])
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    user = relationship("User", back_populates="ip_restrictions")


class CSRFToken(Base):
    __tablename__ = "csrf_tokens"

    token_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    token = Column(String)
    expiration_time = Column(DateTime)

    user = relationship("User", back_populates="csrf_tokens")


class OTPToken(Base):
    __tablename__ = "otp_tokens"

    token_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    token = Column(String)
    expiration_time = Column(DateTime)

    user = relationship("User", back_populates="otp_tokens")


class Device(Base):
    __tablename__ = "devices"

    device_id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.user_id"))
    device_info = Column(String)
    last_login = Column(DateTime)
    
    user = relationship("User", back_populates="devices")
