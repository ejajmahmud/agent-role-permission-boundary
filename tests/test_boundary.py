"""Tests for agent-role-permission-boundary."""
import unittest
from agent_role_permission_boundary.boundary import PermissionBoundary


class TestPermissionBoundary(unittest.TestCase):
    def setUp(self):
        self.boundary = PermissionBoundary()
        self.boundary.define_role("analyst", ["query_db", "fetch_stats"])
        self.boundary.assign_role("agent_1", "analyst")

    def test_allow_and_deny(self):
        self.assertTrue(self.boundary.check_permission("agent_1", "query_db"))
        self.assertFalse(self.boundary.check_permission("agent_1", "drop_db"))
        self.assertFalse(self.boundary.check_permission("unknown_agent", "query_db"))


if __name__ == "__main__":
    unittest.main()
