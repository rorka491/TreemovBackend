from dataclasses import dataclass
from shared.enums.auth import UserRole
from shared.enums.profile import ProfileRole

@dataclass(frozen=True)
class AuthContext:
    user_id: str
    user_role: UserRole
    profile_roles: tuple[ProfileRole, ...]
    profile_exists: bool






