#!/usr/bin/env python3
"""
Sacred Geometry Context Navigator
Provides practical navigation interface for the Sacred Geometry Context Tree.

This module creates an intuitive command-line interface for navigating contexts
using sacred geometry principles, designed for our 2-person collaboration.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import List, Optional

# Add the core module to path
sys.path.append(str(Path(__file__).parent.parent / "core"))

from sacred_geometry_context_tree import (
    SacredContextTree,
    SacredContextNode,
    SacredDimension,
    NavigationType,
    create_workspace_context_tree,
    SacredGeometryConstants,
)


class SacredNavigator:
    """Interactive navigator for Sacred Geometry Context Tree."""

    def __init__(self, workspace_path: str = "/workspaces"):
        self.workspace_path = workspace_path
        self.tree_file = Path(workspace_path) / "temp" / "sacred_context_tree.json"
        self.tree: Optional[SacredContextTree] = None
        self.current_node: Optional[str] = None

        # Ensure temp directory exists
        self.tree_file.parent.mkdir(exist_ok=True)

        self.load_or_create_tree()

    def is_interactive(self) -> bool:
        """Check if we're running in an interactive terminal."""
        return (
            hasattr(sys.stdin, "isatty")
            and sys.stdin.isatty()
            and hasattr(sys.stdout, "isatty")
            and sys.stdout.isatty()
        )

    def demonstrate_navigation(self) -> None:
        """Run a non-interactive demonstration of the context tree."""
        print("\n🌟 Sacred Geometry Context Navigator - Demo Mode")
        print("=" * 60)

        # Show current context
        print("\n1️⃣ Showing current context:")
        self.show_current_context()

        # Show connections
        print("\n2️⃣ Showing available connections:")
        self.list_connections("children")

        # Try to navigate to docs
        print("\n3️⃣ Attempting navigation to 'src':")
        if self.navigate_to("src"):
            self.show_current_context()

        # Show Fibonacci neighbors
        print("\n4️⃣ Showing Fibonacci neighbors:")
        self.show_fibonacci_neighbors(1)

        # Search demonstration
        print("\n5️⃣ Searching for 'CONTEXT' in terrestrial dimension:")
        matches = self.search_by_dimension(SacredDimension.TERRESTRIAL, "CONTEXT")
        if matches:
            print(f"🔍 Found {len(matches)} matches:")
            for match in matches[:5]:
                node = self.tree.nodes.get(match)
                path = node.terrestrial.file_path if node else match
                print(f"   • {match} → {path}")
        else:
            print("🔍 No matches found")

        # Show sacred geometry properties
        print("\n6️⃣ Sacred Geometry Analysis:")
        self.analyze_sacred_patterns()

        print("\n✅ Demo completed! Context tree is working properly.")
        print(f"📊 Tree contains {len(self.tree.nodes)} nodes")
        print(f"💾 Saved to: {self.tree_file}")

    def analyze_sacred_patterns(self) -> None:
        """Analyze and display sacred geometry patterns in the tree."""
        if not self.tree.nodes:
            print("❌ No nodes to analyze")
            return

        print("🔮 Sacred Geometry Pattern Analysis:")

        # Calculate average harmonic signature
        signatures = [node.harmonic_signature for node in self.tree.nodes.values()]
        avg_signature = sum(signatures) / len(signatures)
        print(f"   📊 Average Harmonic Signature: {avg_signature:.3f}")

        # Find nodes closest to golden ratio
        phi = SacredGeometryConstants.PHI
        closest_to_phi = min(signatures, key=lambda x: abs(x - phi))
        print(f"   🌟 Closest to Golden Ratio (φ={phi:.3f}): {closest_to_phi:.3f}")

        # Count nodes by operational status
        status_counts = {}
        for node in self.tree.nodes.values():
            status = node.operational.current_status
            status_counts[status] = status_counts.get(status, 0) + 1

        print("   📈 Operational Status Distribution:")
        for status, count in status_counts.items():
            print(f"      {status}: {count} nodes")

        # Show Fibonacci sequence representation
        fib_nums = SacredGeometryConstants.FIBONACCI[:6]  # First 6 Fibonacci numbers
        print(f"   🌀 Fibonacci Sequence: {fib_nums}")
        print(f"   📐 Golden Ratio (φ): {phi:.6f}")

    def run(self) -> None:
        """Main entry point with automatic mode detection."""
        try:
            if self.is_interactive():
                print("🌟 Interactive terminal detected - starting interactive mode...")
                self.interactive_mode()
            else:
                print(
                    "🌟 Non-interactive environment detected - running demonstration..."
                )
                self.demonstrate_navigation()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
        except Exception as e:
            print(f"❌ Error: {e}")
            print("💡 Try running directly in terminal for interactive mode")

    def load_or_create_tree(self) -> None:
        """Load existing tree or create new one."""
        try:
            if self.tree_file.exists():
                print(f"🌟 Loading existing sacred geometry context tree...")
                self.tree = SacredContextTree(self.workspace_path)
                self.tree.load_from_file(str(self.tree_file))
                print(f"✅ Loaded tree with {len(self.tree.nodes)} nodes")
            else:
                print(f"🌱 Creating new sacred geometry context tree...")
                self.tree = create_workspace_context_tree(self.workspace_path)
                self.tree.save_to_file(str(self.tree_file))
                print(f"✅ Created tree with {len(self.tree.nodes)} nodes")

            # Start at workspace root
            self.current_node = "workspace_root"

        except Exception as e:
            print(f"❌ Error initializing context tree: {e}")
            self.tree = SacredContextTree(self.workspace_path)

    def show_current_context(self) -> None:
        """Display current context information."""
        if not self.current_node or self.current_node not in self.tree.nodes:
            print("❌ No current context")
            return

        node = self.tree.nodes[self.current_node]

        print("\n" + "=" * 60)
        print(f"🌟 CURRENT CONTEXT: {self.current_node}")
        print("=" * 60)

        # Show dimensional contexts
        print(f"🌍 Terrestrial: {node.terrestrial.file_path or 'Unknown'}")
        print(f"⏰ Temporal: {node.temporal.version} ({node.temporal.lifecycle_stage})")
        print(
            f"🔗 Relational: {len(node.relational.parent_contexts)} parents, {len(node.relational.child_contexts)} children"
        )
        print(
            f"⭐ Qualitative: {node.qualitative.completeness_score:.1%} complete, {node.qualitative.validation_status}"
        )
        print(f"⚡ Operational: {node.operational.current_status}")

        # Show sacred geometry properties
        print(f"\n🔮 Sacred Geometry:")
        print(f"   Harmonic Signature: {node.harmonic_signature:.3f}")
        print(
            f"   Golden Ratio Position: ({node.golden_ratio_position[0]:.3f}, {node.golden_ratio_position[1]:.3f})"
        )

        print("\n" + "=" * 60)

    def list_connections(self, connection_type: str = "all") -> None:
        """List available connections from current node."""
        if not self.current_node or self.current_node not in self.tree.nodes:
            print("❌ No current context")
            return

        node = self.tree.nodes[self.current_node]

        if connection_type in ["all", "children"]:
            print(f"\n🌱 Children ({len(node.relational.child_contexts)}):")
            for i, child in enumerate(node.relational.child_contexts[:10], 1):
                if child in self.tree.nodes:
                    child_node = self.tree.nodes[child]
                    path = child_node.terrestrial.file_path or child
                    print(f"   {i}. {child} → {path}")

        if connection_type in ["all", "parents"]:
            print(f"\n🌳 Parents ({len(node.relational.parent_contexts)}):")
            for i, parent in enumerate(node.relational.parent_contexts[:10], 1):
                if parent in self.tree.nodes:
                    parent_node = self.tree.nodes[parent]
                    path = parent_node.terrestrial.file_path or parent
                    print(f"   {i}. {parent} → {path}")

        if connection_type in ["all", "peers"]:
            print(f"\n🤝 Peers ({len(node.relational.peer_contexts)}):")
            for i, peer in enumerate(node.relational.peer_contexts[:10], 1):
                if peer in self.tree.nodes:
                    peer_node = self.tree.nodes[peer]
                    path = peer_node.terrestrial.file_path or peer
                    print(f"   {i}. {peer} → {path}")

    def navigate_to(
        self, target: str, navigation_type: NavigationType = NavigationType.HARMONIC
    ) -> bool:
        """Navigate to a target node."""
        if not self.current_node:
            print("❌ No current context")
            return False

        # Find target node
        target_node = None
        for node_id in self.tree.nodes:
            if (
                node_id == target
                or node_id.lower() == target.lower()
                or target.lower() in node_id.lower()
            ):
                target_node = node_id
                break

        if not target_node:
            print(f"❌ Target '{target}' not found")
            return False

        if navigation_type == NavigationType.HARMONIC:
            path = self.tree.find_harmonic_path(self.current_node, target_node)
        else:
            # For now, use direct navigation for other types
            path = (
                [self.current_node, target_node]
                if target_node in self.tree.adjacency_matrix.get(self.current_node, {})
                else []
            )

        if path:
            print(f"\n🌟 Navigating via {navigation_type.value} path:")
            for i, node_id in enumerate(path):
                node = self.tree.nodes.get(node_id)
                path_info = node.terrestrial.file_path if node else node_id
                symbol = "🎯" if i == len(path) - 1 else "→"
                print(f"   {i+1}. {symbol} {node_id} ({path_info})")

            self.current_node = target_node
            return True
        else:
            print(f"❌ No path found to '{target}'")
            return False

    def search_by_dimension(self, dimension: SacredDimension, query: str) -> List[str]:
        """Search nodes by dimensional criteria."""
        matches = []

        for node_id, node in self.tree.nodes.items():
            context = getattr(node, dimension.value)

            # Search in various context fields
            search_text = ""
            if hasattr(context, "value") and context.value:
                search_text += str(context.value).lower()
            if hasattr(context, "file_path") and context.file_path:
                search_text += str(context.file_path).lower()
            if hasattr(context, "current_status"):
                search_text += str(context.current_status).lower()

            if query.lower() in search_text:
                matches.append(node_id)

        return matches

    def show_fibonacci_neighbors(self, depth: int = 1) -> None:
        """Show neighbors at Fibonacci distances."""
        if not self.current_node:
            print("❌ No current context")
            return

        neighbors = self.tree.get_fibonacci_neighbors(self.current_node, depth)
        fib_distance = SacredGeometryConstants.FIBONACCI[
            min(depth, len(SacredGeometryConstants.FIBONACCI) - 1)
        ]

        print(f"\n🌀 Fibonacci Neighbors (distance {fib_distance}):")
        for i, neighbor in enumerate(neighbors[:10], 1):
            node = self.tree.nodes.get(neighbor)
            path = node.terrestrial.file_path if node else neighbor
            print(f"   {i}. {neighbor} → {path}")

    def interactive_mode(self) -> None:
        """Start interactive navigation mode."""
        print("\n🌟 Welcome to Sacred Geometry Context Navigator")
        print("   Golden Ratio Navigation for Enterprise Workspaces")
        print("\nCommands:")
        print("  show - Show current context")
        print("  list [children|parents|peers] - List connections")
        print("  nav <target> - Navigate to target")
        print("  search <dimension> <query> - Search by dimension")
        print("  fib [depth] - Show Fibonacci neighbors")
        print("  save - Save context tree")
        print("  help - Show this help")
        print("  quit - Exit navigator")

        self.show_current_context()

        while True:
            try:
                command = input(f"\n🌟 [{self.current_node}] > ").strip()

                if not command:
                    continue
                elif command == "quit":
                    break
                elif command == "show":
                    self.show_current_context()
                elif command.startswith("list"):
                    parts = command.split()
                    connection_type = parts[1] if len(parts) > 1 else "all"
                    self.list_connections(connection_type)
                elif command.startswith("nav "):
                    target = command[4:].strip()
                    self.navigate_to(target)
                elif command.startswith("search "):
                    parts = command[7:].split(maxsplit=1)
                    if len(parts) == 2:
                        try:
                            dimension = SacredDimension(parts[0])
                            query = parts[1]
                            matches = self.search_by_dimension(dimension, query)
                            print(f"\n🔍 Found {len(matches)} matches:")
                            for match in matches[:10]:
                                node = self.tree.nodes.get(match)
                                path = node.terrestrial.file_path if node else match
                                print(f"   • {match} → {path}")
                        except ValueError:
                            print(
                                f"❌ Invalid dimension. Use: {', '.join([d.value for d in SacredDimension])}"
                            )
                    else:
                        print("❌ Usage: search <dimension> <query>")
                elif command.startswith("fib"):
                    parts = command.split()
                    depth = (
                        int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
                    )
                    self.show_fibonacci_neighbors(depth)
                elif command == "save":
                    self.tree.save_to_file(str(self.tree_file))
                    print(f"✅ Saved context tree to {self.tree_file}")
                elif command == "help":
                    print("\nCommands:")
                    print("  show - Show current context")
                    print("  list [children|parents|peers] - List connections")
                    print("  nav <target> - Navigate to target")
                    print("  search <dimension> <query> - Search by dimension")
                    print("  fib [depth] - Show Fibonacci neighbors")
                    print("  save - Save context tree")
                    print("  help - Show this help")
                    print("  quit - Exit navigator")
                else:
                    print(f"❌ Unknown command: {command}")

            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")

        # Save on exit
        self.tree.save_to_file(str(self.tree_file))
        print(f"✅ Context tree saved to {self.tree_file}")


def main():
    """Main entry point for the navigator."""
    parser = argparse.ArgumentParser(description="Sacred Geometry Context Navigator")
    parser.add_argument(
        "--workspace",
        default="/workspaces",
        help="Workspace path (default: /workspaces)",
    )
    parser.add_argument("--command", help="Single command to execute")
    parser.add_argument("--target", help="Target for navigation command")
    parser.add_argument(
        "--force-interactive",
        action="store_true",
        help="Force interactive mode even in non-interactive environment",
    )
    parser.add_argument("--demo", action="store_true", help="Run demonstration mode")

    args = parser.parse_args()

    navigator = SacredNavigator(args.workspace)

    if args.demo:
        # Force demo mode
        navigator.demonstrate_navigation()
    elif args.command:
        # Execute single command
        if args.command == "show":
            navigator.show_current_context()
        elif args.command == "list":
            navigator.list_connections()
        elif args.command == "nav" and args.target:
            navigator.navigate_to(args.target)
        elif args.command == "create":
            print(f"✅ Created context tree with {len(navigator.tree.nodes)} nodes")
        elif args.command == "demo":
            navigator.demonstrate_navigation()
        else:
            print(f"❌ Unknown command or missing target: {args.command}")
    elif args.force_interactive:
        # Force interactive mode
        navigator.interactive_mode()
    else:
        # Auto-detect mode
        navigator.run()


if __name__ == "__main__":
    main()
