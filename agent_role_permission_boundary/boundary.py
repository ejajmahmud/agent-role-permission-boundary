"""Role-based access control (RBAC) boundary for agents and tools."""
from typing import Dict, List, Set, Any, Optional


class PermissionBoundary:
    def __init__(self):
        self._role_permissions: Dict[str, Set[str]] = {}
        self._agent_roles: Dict[str, str] = {}
        self._audit_log: List[Dict[str, Any]] = []

    def define_role(self, role: str, allowed_tools: List[str]):
        self._role_permissions[role] = set(allowed_tools)

    def assign_role(self, agent_id: str, role: str):
        if role not in self._role_permissions:
            raise ValueError(f"Role '{role}' is not defined")
        self._agent_roles[agent_id] = role

    def check_permission(self, agent_id: str, tool_name: str) -> bool:
        role = self._agent_roles.get(agent_id, "guest")
        allowed = self._role_permissions.get(role, set())

        is_allowed = (tool_name in allowed) or ("*" in allowed)

        self._audit_log.append({
            "agent_id": agent_id,
            "role": role,
            "tool": tool_name,
            "allowed": is_allowed
        })
        return is_allowed

    def get_audit_log(self) -> List[Dict[str, Any]]:
        return self._audit_log
