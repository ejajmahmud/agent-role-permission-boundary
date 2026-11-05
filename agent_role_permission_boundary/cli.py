"""CLI for agent-role-permission-boundary."""
import sys
import argparse
from .boundary import PermissionBoundary


def main():
    parser = argparse.ArgumentParser(description="Agent Role Permission Boundary")
    parser.add_argument("--demo", action="store_true", help="Run RBAC permission check demonstration")
    args = parser.parse_args()

    boundary = PermissionBoundary()
    if args.demo:
        boundary.define_role("viewer", ["read_file", "search_docs", "list_dir"])
        boundary.define_role("admin", ["*"])

        boundary.assign_role("agent_alice", "viewer")
        boundary.assign_role("agent_bob", "admin")

        print("Alice invoke read_file:", boundary.check_permission("agent_alice", "read_file"))
        print("Alice invoke delete_file:", boundary.check_permission("agent_alice", "delete_file"))
        print("Bob invoke delete_file:", boundary.check_permission("agent_bob", "delete_file"))
        print("Audit Log:", boundary.get_audit_log())
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
