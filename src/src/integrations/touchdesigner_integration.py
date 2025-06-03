#!/usr/bin/env python3
"""
🎮 TouchDesigner Integration Module for Sacred Geometry Context Tree
===================================================================

Purpose:
- Export context tree data for real-time visual generation in TouchDesigner
- Create OSC, TCP, and JSON data streams for live visualization
- Generate TouchDesigner-compatible data formats with sacred geometry properties
- Enable real-time workspace visualization and interaction

Sacred Geometry Integration:
- Real-time pentagonal positioning calculations
- Live golden ratio and Fibonacci sequence updates
- Harmonic resonance visualization data
- Sacred pattern generators for visual effects

Author: GitHub Copilot (Avanade Modern Workplace Engineering)
"""

import json
import math
import socket
import threading
import time
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, asdict
import struct


@dataclass
class TouchDesignerNode:
    """TouchDesigner-compatible node representation with real-time properties."""

    node_id: str
    name: str
    position_x: float
    position_y: float
    position_z: float
    scale: float
    rotation: float
    color_r: float
    color_g: float
    color_b: float
    alpha: float
    harmonic_frequency: float
    fibonacci_index: int
    golden_ratio_phase: float
    animation_speed: float
    connection_strength: float
    metadata: Dict[str, Any]


@dataclass
class SacredGeometryPattern:
    """Real-time sacred geometry pattern for TouchDesigner visualization."""

    pattern_id: str
    pattern_type: str  # "fibonacci_spiral", "golden_ratio_grid", "pentagonal_web", etc.
    center_x: float
    center_y: float
    scale: float
    rotation_speed: float
    color_palette: List[Tuple[float, float, float]]
    animation_phase: float
    harmonic_resonance: float
    active: bool


class OSCServer:
    """
    🌐 OSC (Open Sound Control) Server for real-time TouchDesigner communication

    Sends sacred geometry data and context tree updates via OSC protocol
    for seamless integration with TouchDesigner's OSC In CHOP.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 7000):
        self.host = host
        self.port = port
        self.running = False
        self.socket = None

    def start(self):
        """Start OSC server for sending data to TouchDesigner."""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.running = True
            print(f"🌐 OSC Server started on {self.host}:{self.port}")
        except Exception as e:
            print(f"❌ Failed to start OSC server: {e}")

    def stop(self):
        """Stop OSC server."""
        self.running = False
        if self.socket:
            self.socket.close()
        print("🔴 OSC Server stopped")

    def send_message(self, address: str, values: List[Any]):
        """Send OSC message to TouchDesigner."""
        if not self.running or not self.socket:
            return

        try:
            # Simple OSC message format
            message = self._create_osc_message(address, values)
            self.socket.sendto(message, (self.host, self.port))
        except Exception as e:
            print(f"❌ OSC send error: {e}")

    def _create_osc_message(self, address: str, values: List[Any]) -> bytes:
        """Create OSC message in binary format."""
        # Simplified OSC message creation
        # In production, use proper OSC library like python-osc
        message_parts = [address.encode("utf-8")]

        for value in values:
            if isinstance(value, float):
                message_parts.append(struct.pack(">f", value))
            elif isinstance(value, int):
                message_parts.append(struct.pack(">i", value))
            elif isinstance(value, str):
                message_parts.append(value.encode("utf-8"))

        return b"".join(message_parts)


class TCPServer:
    """
    🔌 TCP Server for high-bandwidth data streaming to TouchDesigner

    Provides continuous data streams for complex visualizations
    requiring high-frequency updates.
    """

    def __init__(self, host: str = "127.0.0.1", port: int = 7001):
        self.host = host
        self.port = port
        self.running = False
        self.server_socket = None
        self.clients = []

    def start(self):
        """Start TCP server for data streaming."""
        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            self.running = True

            # Start accepting connections in separate thread
            threading.Thread(target=self._accept_connections, daemon=True).start()
            print(f"🔌 TCP Server started on {self.host}:{self.port}")
        except Exception as e:
            print(f"❌ Failed to start TCP server: {e}")

    def stop(self):
        """Stop TCP server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        for client in self.clients:
            client.close()
        self.clients.clear()
        print("🔴 TCP Server stopped")

    def _accept_connections(self):
        """Accept incoming TouchDesigner connections."""
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                print(f"📱 TouchDesigner client connected: {address}")
            except:
                break

    def broadcast_data(self, data: Dict[str, Any]):
        """Broadcast data to all connected TouchDesigner clients."""
        if not self.clients:
            return

        try:
            message = json.dumps(data).encode("utf-8") + b"\n"

            # Send to all clients
            disconnected_clients = []
            for client in self.clients:
                try:
                    client.send(message)
                except:
                    disconnected_clients.append(client)

            # Remove disconnected clients
            for client in disconnected_clients:
                self.clients.remove(client)
                client.close()

        except Exception as e:
            print(f"❌ TCP broadcast error: {e}")


class TouchDesignerIntegration:
    """
    🎨 Sacred Geometry TouchDesigner Integration

    Converts context tree data into real-time visual elements
    for TouchDesigner with sacred geometry properties.
    """

    def __init__(self, context_tree=None):
        self.context_tree = context_tree
        self.golden_ratio = 1.618033988749
        self.fibonacci_sequence = self._generate_fibonacci(20)

        # Real-time servers
        self.osc_server = OSCServer()
        self.tcp_server = TCPServer()

        # Animation state
        self.animation_time = 0.0
        self.animation_speed = 1.0
        self.streaming = False

        # Sacred geometry generators
        self.pattern_generators = {
            "fibonacci_spiral": self._generate_fibonacci_spiral,
            "golden_ratio_grid": self._generate_golden_ratio_grid,
            "pentagonal_web": self._generate_pentagonal_web,
            "harmonic_resonance": self._generate_harmonic_resonance,
            "sacred_polyhedra": self._generate_sacred_polyhedra,
        }

        # Color palettes based on sacred geometry
        self.sacred_palettes = {
            "golden": [(1.0, 0.618, 0.0), (0.618, 0.382, 0.0), (0.382, 0.236, 0.0)],
            "fibonacci": [
                (0.0, 0.618, 1.0),
                (0.382, 0.618, 0.618),
                (0.618, 0.382, 0.618),
            ],
            "pentagonal": [
                (0.618, 0.0, 0.618),
                (0.382, 0.618, 0.382),
                (1.0, 0.618, 0.618),
            ],
            "harmonic": [(0.5, 0.809, 0.618), (0.309, 0.5, 0.809), (0.809, 0.309, 0.5)],
        }

    def _generate_fibonacci(self, n: int) -> List[int]:
        """Generate first n Fibonacci numbers."""
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        elif n == 2:
            return [1, 1]

        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib

    def _calculate_pentagonal_position(
        self, index: int, total_count: int, radius: float = 1.0
    ) -> Tuple[float, float, float]:
        """Calculate 3D position using pentagonal sacred geometry."""
        # Base pentagonal angle
        angle = (index / total_count) * 2 * math.pi

        # Golden ratio spiral height
        height = (index / total_count - 0.5) * 2 * radius * self.golden_ratio

        # Pentagonal positioning with golden ratio radius scaling
        fib_index = index % len(self.fibonacci_sequence)
        radius_scale = self.fibonacci_sequence[fib_index] / max(self.fibonacci_sequence)

        x = radius * radius_scale * math.cos(angle)
        y = radius * radius_scale * math.sin(angle)
        z = height

        return (x, y, z)

    def _calculate_harmonic_color(
        self, harmonic_signature: float
    ) -> Tuple[float, float, float]:
        """Calculate color based on harmonic signature using sacred geometry."""
        # Map harmonic signature to golden ratio color space
        hue = (harmonic_signature * self.golden_ratio) % 1.0
        saturation = 0.618 + 0.382 * math.sin(harmonic_signature * math.pi)
        brightness = 0.618 + 0.382 * math.cos(harmonic_signature * math.pi * 2)

        # Convert HSB to RGB using sacred proportions
        c = brightness * saturation
        x = c * (1 - abs((hue * 6) % 2 - 1))
        m = brightness - c

        if 0 <= hue < 1 / 6:
            r, g, b = c, x, 0
        elif 1 / 6 <= hue < 2 / 6:
            r, g, b = x, c, 0
        elif 2 / 6 <= hue < 3 / 6:
            r, g, b = 0, c, x
        elif 3 / 6 <= hue < 4 / 6:
            r, g, b = 0, x, c
        elif 4 / 6 <= hue < 5 / 6:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x

        return (r + m, g + m, b + m)

    def convert_context_tree_to_touchdesigner(
        self, nodes_data: List[Dict] = None
    ) -> List[TouchDesignerNode]:
        """
        🌟 Convert context tree to TouchDesigner-compatible nodes

        Creates 3D positioned nodes with sacred geometry properties
        for real-time visualization.
        """
        td_nodes = []

        # Use provided nodes_data or fallback to demo data
        if nodes_data:
            all_nodes = nodes_data
        elif self.context_tree and hasattr(self.context_tree, "nodes"):
            all_nodes = list(self.context_tree.nodes.values())
        else:
            # Demo data for testing without context tree
            all_nodes = [
                {
                    "node_id": f"demo_{i}",
                    "name": f"Demo Node {i}",
                    "harmonic_signature": i * 0.1618,
                    "metadata": {"path": f"/demo/{i}", "type": "demo"},
                    "dimensions": [1, 1, 1],
                }
                for i in range(10)
            ]

        total_count = len(all_nodes)

        for i, node in enumerate(all_nodes):
            # Handle both object and dict node formats
            if isinstance(node, dict):
                node_id = node.get("node_id", f"node_{i}")
                name = node.get("name", f"Node {i}")
                harmonic_signature = node.get("harmonic_signature", i * 0.1618)
                metadata = node.get("metadata", {})
                dimensions = node.get("dimensions", [1, 1, 1])
            else:
                node_id = getattr(node, "node_id", f"node_{i}")
                name = getattr(node, "name", f"Node {i}")
                harmonic_signature = getattr(node, "harmonic_signature", i * 0.1618)
                metadata = getattr(node, "metadata", {})
                dimensions = getattr(node, "dimensions", [1, 1, 1])

            # Calculate 3D position using pentagonal sacred geometry
            x, y, z = self._calculate_pentagonal_position(i, total_count, radius=5.0)

            # Calculate visual properties based on sacred geometry
            fibonacci_index = i % len(self.fibonacci_sequence)
            golden_ratio_phase = (i * self.golden_ratio) % 1.0

            # Harmonic color calculation
            color_r, color_g, color_b = self._calculate_harmonic_color(
                harmonic_signature
            )

            # Scale based on harmonic signature
            scale = 0.5 + (harmonic_signature * 0.5)

            # Animation properties
            animation_speed = 0.5 + (harmonic_signature * 1.5)
            rotation = golden_ratio_phase * 360.0

            # Connection strength (for drawing lines between related nodes)
            connection_strength = min(harmonic_signature, 1.0)

            td_node = TouchDesignerNode(
                node_id=node_id,
                name=name,
                position_x=x,
                position_y=y,
                position_z=z,
                scale=scale,
                rotation=rotation,
                color_r=color_r,
                color_g=color_g,
                color_b=color_b,
                alpha=0.8 + (harmonic_signature * 0.2),
                harmonic_frequency=harmonic_signature
                * 10.0,  # For audio-reactive effects
                fibonacci_index=fibonacci_index,
                golden_ratio_phase=golden_ratio_phase,
                animation_speed=animation_speed,
                connection_strength=connection_strength,
                metadata={
                    "dimensions": dimensions,
                    "original_path": metadata.get("path", ""),
                    "file_type": metadata.get("type", "unknown"),
                    "sacred_geometry": True,
                },
            )

            td_nodes.append(td_node)

        return td_nodes

    def _generate_fibonacci_spiral(
        self, center_x: float, center_y: float, scale: float
    ) -> SacredGeometryPattern:
        """Generate real-time Fibonacci spiral pattern."""
        return SacredGeometryPattern(
            pattern_id="fibonacci_spiral_001",
            pattern_type="fibonacci_spiral",
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            rotation_speed=self.golden_ratio * 10.0,
            color_palette=self.sacred_palettes["fibonacci"],
            animation_phase=self.animation_time * self.golden_ratio,
            harmonic_resonance=math.sin(
                self.animation_time * math.pi / self.golden_ratio
            ),
            active=True,
        )

    def _generate_golden_ratio_grid(
        self, center_x: float, center_y: float, scale: float
    ) -> SacredGeometryPattern:
        """Generate golden ratio grid pattern."""
        return SacredGeometryPattern(
            pattern_id="golden_grid_001",
            pattern_type="golden_ratio_grid",
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            rotation_speed=5.0,
            color_palette=self.sacred_palettes["golden"],
            animation_phase=self.animation_time,
            harmonic_resonance=math.cos(
                self.animation_time * math.pi * 2 / self.golden_ratio
            ),
            active=True,
        )

    def _generate_pentagonal_web(
        self, center_x: float, center_y: float, scale: float
    ) -> SacredGeometryPattern:
        """Generate pentagonal connection web."""
        return SacredGeometryPattern(
            pattern_id="pentagonal_web_001",
            pattern_type="pentagonal_web",
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            rotation_speed=15.0,
            color_palette=self.sacred_palettes["pentagonal"],
            animation_phase=self.animation_time * 0.618,
            harmonic_resonance=math.sin(self.animation_time * math.pi * 5),
            active=True,
        )

    def _generate_harmonic_resonance(
        self, center_x: float, center_y: float, scale: float
    ) -> SacredGeometryPattern:
        """Generate harmonic resonance visualization."""
        return SacredGeometryPattern(
            pattern_id="harmonic_resonance_001",
            pattern_type="harmonic_resonance",
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            rotation_speed=self.golden_ratio * 7.0,
            color_palette=self.sacred_palettes["harmonic"],
            animation_phase=self.animation_time * math.pi,
            harmonic_resonance=math.sin(
                self.animation_time * math.pi * self.golden_ratio
            ),
            active=True,
        )

    def _generate_sacred_polyhedra(
        self, center_x: float, center_y: float, scale: float
    ) -> SacredGeometryPattern:
        """Generate sacred polyhedra (dodecahedron, icosahedron) patterns."""
        return SacredGeometryPattern(
            pattern_id="sacred_polyhedra_001",
            pattern_type="sacred_polyhedra",
            center_x=center_x,
            center_y=center_y,
            scale=scale,
            rotation_speed=3.0,
            color_palette=self.sacred_palettes["golden"],
            animation_phase=self.animation_time / self.golden_ratio,
            harmonic_resonance=math.cos(self.animation_time * math.pi / 3),
            active=True,
        )

    def generate_sacred_patterns(self) -> List[SacredGeometryPattern]:
        """Generate all sacred geometry patterns for TouchDesigner."""
        patterns = []

        # Create patterns at different scales and positions
        pattern_configs = [
            {"center": (0, 0), "scale": 1.0},
            {"center": (3, 3), "scale": 0.618},
            {"center": (-3, -3), "scale": 0.382},
            {"center": (5, -2), "scale": 1.618},
            {"center": (-2, 5), "scale": 0.236},
        ]

        for config in pattern_configs:
            for pattern_name, generator in self.pattern_generators.items():
                pattern = generator(
                    config["center"][0], config["center"][1], config["scale"]
                )
                patterns.append(pattern)

        return patterns

    def start_real_time_streaming(self, fps: int = 30):
        """
        🚀 Start real-time data streaming to TouchDesigner

        Begins continuous updates of context tree and sacred geometry data
        for live visualization.
        """
        if self.streaming:
            print("⚠️ Streaming already active")
            return

        # Start servers
        self.osc_server.start()
        self.tcp_server.start()

        self.streaming = True
        self.animation_time = 0.0

        # Start streaming thread
        threading.Thread(target=self._streaming_loop, args=(fps,), daemon=True).start()
        print(f"🚀 Real-time streaming started at {fps} FPS")

    def stop_real_time_streaming(self):
        """Stop real-time streaming."""
        self.streaming = False
        self.osc_server.stop()
        self.tcp_server.stop()
        print("🔴 Real-time streaming stopped")

    def _streaming_loop(self, fps: int):
        """Main streaming loop for real-time updates."""
        frame_time = 1.0 / fps

        while self.streaming:
            start_time = time.time()

            # Update animation time
            self.animation_time += frame_time * self.animation_speed

            # Generate current frame data
            td_nodes = self.convert_context_tree_to_touchdesigner()
            sacred_patterns = self.generate_sacred_patterns()

            # Create complete frame data
            frame_data = {
                "timestamp": time.time(),
                "animation_time": self.animation_time,
                "golden_ratio": self.golden_ratio,
                "fibonacci_sequence": self.fibonacci_sequence[:10],
                "nodes": [asdict(node) for node in td_nodes],
                "patterns": [asdict(pattern) for pattern in sacred_patterns],
                "sacred_geometry_state": {
                    "active_patterns": len(sacred_patterns),
                    "total_nodes": len(td_nodes),
                    "harmonic_resonance": math.sin(
                        self.animation_time * math.pi * self.golden_ratio
                    ),
                    "fibonacci_phase": (self.animation_time * self.golden_ratio) % 1.0,
                },
            }

            # Send via TCP (high bandwidth)
            self.tcp_server.broadcast_data(frame_data)

            # Send key values via OSC (low latency)
            self.osc_server.send_message("/sacred/time", [self.animation_time])
            self.osc_server.send_message("/sacred/golden_ratio", [self.golden_ratio])
            self.osc_server.send_message(
                "/sacred/harmonic",
                [frame_data["sacred_geometry_state"]["harmonic_resonance"]],
            )
            self.osc_server.send_message("/sacred/node_count", [len(td_nodes)])

            # Frame rate control
            elapsed = time.time() - start_time
            sleep_time = max(0, frame_time - elapsed)
            time.sleep(sleep_time)

    def export_touchdesigner_project_template(self, output_path: str) -> str:
        """
        📁 Export TouchDesigner project template (.toe file data)

        Creates template configuration for importing sacred geometry context tree
        visualization into TouchDesigner.
        """
        # TouchDesigner project template configuration
        template_config = {
            "project_info": {
                "name": "Sacred Geometry Context Tree Visualizer",
                "description": "Real-time visualization of workspace context tree using sacred geometry principles",
                "version": "1.0.0",
                "created_by": "Sacred Geometry Context Tree System",
                "created_at": datetime.now().isoformat(),
            },
            "network_configuration": {
                "tcp_input": {
                    "type": "TCP In DAT",
                    "host": "127.0.0.1",
                    "port": 7001,
                    "description": "High-bandwidth data stream for complex visualizations",
                },
                "osc_input": {
                    "type": "OSC In CHOP",
                    "host": "127.0.0.1",
                    "port": 7000,
                    "description": "Low-latency control signals for real-time interaction",
                },
            },
            "data_processing": {
                "json_parser": {
                    "type": "Convert DAT",
                    "input": "tcp_input",
                    "convert_format": "JSON",
                    "description": "Parse incoming JSON data from context tree",
                },
                "node_data_table": {
                    "type": "Table DAT",
                    "input": "json_parser",
                    "description": "Context tree nodes with sacred geometry properties",
                },
                "pattern_data_table": {
                    "type": "Table DAT",
                    "input": "json_parser",
                    "description": "Sacred geometry patterns for background visualization",
                },
            },
            "visualization_components": {
                "node_geometry": {
                    "type": "Sphere SOP",
                    "description": "Base geometry for context nodes",
                    "parameters": {
                        "divisions": 12,
                        "type": "Primitive",
                        "scale": "from_data_table",
                    },
                },
                "node_instancer": {
                    "type": "Copy SOP",
                    "input": "node_geometry",
                    "template_points": "node_data_table",
                    "description": "Instance nodes at sacred geometry positions",
                },
                "connection_lines": {
                    "type": "Line SOP",
                    "description": "Connect related nodes with golden ratio curves",
                    "parameters": {"curve_type": "golden_ratio_spiral"},
                },
                "fibonacci_spiral": {
                    "type": "Circle SOP",
                    "description": "Background Fibonacci spiral",
                    "parameters": {
                        "divisions": 89,  # Fibonacci number
                        "arc_angles": 360 * 1.618,
                    },
                },
                "golden_ratio_grid": {
                    "type": "Grid SOP",
                    "description": "Golden ratio proportioned grid",
                    "parameters": {
                        "size_x": 16.18,
                        "size_y": 10.0,
                        "rows": 13,  # Fibonacci number
                        "columns": 21,  # Fibonacci number
                    },
                },
            },
            "materials_and_shading": {
                "sacred_material": {
                    "type": "Phong MAT",
                    "description": "Material with harmonic color calculations",
                    "parameters": {
                        "diffuse_color": "harmonic_signature_based",
                        "specular": 0.618,
                        "roughness": 0.382,
                        "metallic": "golden_ratio_modulated",
                    },
                },
                "pattern_material": {
                    "type": "PBR MAT",
                    "description": "Material for sacred geometry patterns",
                    "parameters": {
                        "base_color": "sacred_palette",
                        "emission": "harmonic_resonance_driven",
                        "alpha": "fibonacci_modulated",
                    },
                },
            },
            "animation_and_interaction": {
                "harmonic_animation": {
                    "type": "Transform TOP",
                    "description": "Sacred geometry-based transformations",
                    "parameters": {
                        "rotation_speed": "golden_ratio * 10",
                        "scale_animation": "fibonacci_sequence_based",
                    },
                },
                "user_interaction": {
                    "type": "Mouse In CHOP",
                    "description": "Interactive navigation through context tree",
                    "parameters": {"navigation_mode": "sacred_geometry_guided"},
                },
            },
            "output_configuration": {
                "main_output": {
                    "type": "Out TOP",
                    "resolution": "1920x1080",
                    "description": "Main visualization output",
                },
                "data_export": {
                    "type": "TCP Out DAT",
                    "description": "Export interaction data back to context tree system",
                },
            },
            "parameter_bindings": {
                "node_positions": {
                    "source": "node_data_table",
                    "columns": ["position_x", "position_y", "position_z"],
                    "target": "node_instancer.translate",
                },
                "node_colors": {
                    "source": "node_data_table",
                    "columns": ["color_r", "color_g", "color_b"],
                    "target": "sacred_material.diffusecolor",
                },
                "node_scales": {
                    "source": "node_data_table",
                    "columns": ["scale"],
                    "target": "node_instancer.scale",
                },
                "harmonic_frequencies": {
                    "source": "node_data_table",
                    "columns": ["harmonic_frequency"],
                    "target": "harmonic_animation.speed",
                },
                "animation_time": {
                    "source": "osc_input./sacred/time",
                    "target": "harmonic_animation.time",
                },
                "golden_ratio": {
                    "source": "osc_input./sacred/golden_ratio",
                    "target": "golden_ratio_grid.golden_ratio_param",
                },
            },
            "setup_instructions": [
                "1. Create new TouchDesigner project",
                "2. Import this configuration as reference",
                "3. Set up TCP In DAT on port 7001 for data stream",
                "4. Set up OSC In CHOP on port 7000 for control signals",
                "5. Connect data parsing and visualization components",
                "6. Run Sacred Geometry Context Tree with real-time streaming",
                "7. Enjoy the sacred geometry visualization!",
            ],
        }

        # Export template
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(template_config, f, indent=2, ensure_ascii=False)

        return output_path

    def export_static_data(
        self, output_path: str, nodes_data: List[Dict] = None
    ) -> str:
        """Export static context tree data for TouchDesigner import."""
        td_nodes = self.convert_context_tree_to_touchdesigner(nodes_data)
        patterns = self.generate_sacred_patterns()

        export_data = {
            "export_info": {
                "type": "Sacred Geometry Context Tree Static Export",
                "created_at": datetime.now().isoformat(),
                "total_nodes": len(td_nodes),
                "total_patterns": len(patterns),
            },
            "nodes": [asdict(node) for node in td_nodes],
            "patterns": [asdict(pattern) for pattern in patterns],
            "sacred_geometry_constants": {
                "golden_ratio": self.golden_ratio,
                "fibonacci_sequence": self.fibonacci_sequence,
                "color_palettes": self.sacred_palettes,
            },
        }

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        return output_path


def main():
    """🎮 Demo: TouchDesigner integration with real-time streaming"""
    print("🎮 Sacred Geometry Context Tree → TouchDesigner Integration")
    print("=" * 60)

    # Initialize TouchDesigner integration (works standalone)
    touchdesigner = TouchDesignerIntegration()

    print("📊 Demo mode: Using generated demo nodes")
    print()

    # Convert to TouchDesigner format
    print("🎨 Converting context tree to TouchDesigner format...")
    td_nodes = touchdesigner.convert_context_tree_to_touchdesigner()
    sacred_patterns = touchdesigner.generate_sacred_patterns()

    print(f"✅ Created {len(td_nodes)} TouchDesigner nodes")
    print(f"✅ Generated {len(sacred_patterns)} sacred geometry patterns")
    print()

    # Export static data
    output_dir = "/tmp/touchdesigner_exports"
    os.makedirs(output_dir, exist_ok=True)

    static_path = f"{output_dir}/sacred_context_tree_static.json"
    template_path = f"{output_dir}/touchdesigner_project_template.json"

    touchdesigner.export_static_data(static_path)
    touchdesigner.export_touchdesigner_project_template(template_path)

    print(f"📁 Exported static data: {static_path}")
    print(f"🎮 Exported project template: {template_path}")
    print()

    # Demo real-time streaming (for 10 seconds)
    print("🚀 Starting real-time streaming demo...")
    print("   - OSC server on port 7000 (control signals)")
    print("   - TCP server on port 7001 (data stream)")
    print("   - Running for 10 seconds...")

    touchdesigner.start_real_time_streaming(fps=30)

    # Run for demo period
    time.sleep(10)

    touchdesigner.stop_real_time_streaming()

    print()
    print("🌟 TouchDesigner integration complete!")
    print()
    print("📋 Next Steps:")
    print("   1. Open TouchDesigner")
    print("   2. Create TCP In DAT (port 7001) for data stream")
    print("   3. Create OSC In CHOP (port 7000) for control signals")
    print("   4. Use project template as reference for setup")
    print("   5. Run this script again to start real-time streaming")
    print("   6. Enjoy sacred geometry visualization!")


if __name__ == "__main__":
    main()
