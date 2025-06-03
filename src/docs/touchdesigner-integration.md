# 🎮 TouchDesigner Integration Guide

## Overview
The Sacred Geometry Context Tree TouchDesigner integration enables real-time 3D visualization of workspace hierarchies using sacred geometry principles including the golden ratio, Fibonacci sequences, and pentagonal positioning.

## Key Features

### 🌐 Real-Time Data Streaming
- **OSC Server** (Port 7000): Low-latency control signals for live interaction
- **TCP Server** (Port 7001): High-bandwidth data stream for complex visualizations
- **30 FPS** real-time updates with sacred geometry calculations

### 🎨 Sacred Geometry Visualization
- **Pentagonal Positioning**: 3D node placement using 5-dimensional sacred geometry
- **Golden Ratio Scaling**: Visual harmony through φ=1.618 proportions
- **Fibonacci Spirals**: Organic connection patterns and animation timing
- **Harmonic Colors**: Color calculation based on harmonic signatures

### 🔮 Sacred Patterns
- **Fibonacci Spiral**: Organic growth visualization
- **Golden Ratio Grid**: Harmonious spatial organization
- **Pentagonal Web**: 5-dimensional connection networks
- **Harmonic Resonance**: Frequency-based visual effects
- **Sacred Polyhedra**: Dodecahedron and icosahedron patterns

## Quick Start

### 1. Standalone Demo
```bash
cd /workspaces/sacred-geometry-context-tree/src/integrations
python touchdesigner_integration.py
```

### 2. Integration with Context Tree
```python
from touchdesigner_integration import TouchDesignerIntegration
from sacred_geometry_context_tree import SacredGeometryContextTree

# Load context tree
context_tree = SacredGeometryContextTree()
context_tree.load_from_json("your_context_tree.json")

# Initialize TouchDesigner integration
td_integration = TouchDesignerIntegration(context_tree)

# Start real-time streaming
td_integration.start_real_time_streaming(fps=30)
```

## TouchDesigner Setup

### Data Input Components

#### TCP Data Stream (Port 7001)
```
TCP In DAT
├── Network Address: 127.0.0.1
├── Network Port: 7001
├── Protocol: TCP
└── Output: JSON frame data with nodes and patterns
```

#### OSC Control Signals (Port 7000)
```
OSC In CHOP
├── Network Address: 127.0.0.1
├── Network Port: 7000
├── Channels: /sacred/time, /sacred/golden_ratio, /sacred/harmonic, /sacred/node_count
└── Output: Real-time control values
```

### Data Processing
```
Convert DAT → JSON Parser
├── Input: TCP In DAT
├── Convert Format: JSON
└── Output: Structured node and pattern data

Table DAT → Node Data
├── Input: JSON Parser.nodes
├── Columns: position_x, position_y, position_z, color_r, color_g, color_b, scale
└── Output: Per-node visualization parameters
```

### Visualization Components

#### Node Geometry
```
Sphere SOP → Base Geometry
├── Divisions: 12
├── Type: Primitive
└── Output: Base node shape

Copy SOP → Node Instancer
├── Source: Sphere SOP
├── Template: Table DAT (node positions)
├── Transform: position_x, position_y, position_z
└── Output: Positioned nodes in 3D space
```

#### Sacred Geometry Background
```
Circle SOP → Fibonacci Spiral
├── Divisions: 89 (Fibonacci number)
├── Arc Angles: 360 * 1.618 (golden ratio)
└── Animation: Harmonic rotation

Grid SOP → Golden Ratio Grid
├── Size X: 16.18
├── Size Y: 10.0
├── Rows: 13 (Fibonacci)
├── Columns: 21 (Fibonacci)
└── Proportions: Golden ratio based
```

### Materials and Shading

#### Sacred Material
```
Phong MAT
├── Diffuse Color: Harmonic signature based
├── Specular: 0.618 (golden ratio)
├── Roughness: 0.382 (golden ratio complement)
└── Metallic: Golden ratio modulated
```

## Data Format

### Node Data Structure
```json
{
  "node_id": "unique_identifier",
  "name": "Node Display Name",
  "position_x": 3.14,
  "position_y": 1.59,
  "position_z": 2.65,
  "scale": 0.85,
  "rotation": 233.4,
  "color_r": 0.618,
  "color_g": 0.382,
  "color_b": 0.236,
  "alpha": 0.9,
  "harmonic_frequency": 4.32,
  "fibonacci_index": 5,
  "golden_ratio_phase": 0.618,
  "animation_speed": 1.2,
  "connection_strength": 0.75
}
```

### Pattern Data Structure
```json
{
  "pattern_id": "fibonacci_spiral_001",
  "pattern_type": "fibonacci_spiral",
  "center_x": 0.0,
  "center_y": 0.0,
  "scale": 1.0,
  "rotation_speed": 16.18,
  "color_palette": [[1.0, 0.618, 0.0], [0.618, 0.382, 0.0]],
  "animation_phase": 2.618,
  "harmonic_resonance": 0.85,
  "active": true
}
```

## Sacred Geometry Principles

### Golden Ratio (φ = 1.618)
- **Positioning**: Node placement using golden ratio spirals
- **Scaling**: Visual elements sized with golden ratio proportions
- **Timing**: Animation speeds based on golden ratio multiples
- **Colors**: Hue and saturation calculated using φ

### Fibonacci Sequences
- **Spiral Paths**: Connection lines follow Fibonacci spiral patterns
- **Animation Timing**: Frame timing based on Fibonacci numbers
- **Index Mapping**: Node indices mapped to Fibonacci sequence positions
- **Scaling Factors**: Size variations using Fibonacci ratios

### Pentagonal Geometry
- **5D Positioning**: Nodes positioned using pentagonal angles (72°)
- **Sacred Angles**: 5-fold symmetry in pattern generation
- **Harmonic Resonance**: 5-based frequency calculations
- **Connection Networks**: Pentagonal relationship mapping

## Performance Optimization

### Frame Rate Management
- **Target FPS**: 30 FPS for smooth real-time visualization
- **Dynamic Quality**: Automatic LOD based on node count
- **Efficient Updates**: Only changed data transmitted
- **Memory Management**: Automatic cleanup of disconnected clients

### Network Optimization
- **TCP Streaming**: High-bandwidth complete frame data
- **OSC Controls**: Low-latency critical values only
- **JSON Compression**: Minimal data structure overhead
- **Connection Pooling**: Reuse network connections

## Advanced Usage

### Custom Pattern Generation
```python
def create_custom_pattern(center_x, center_y, scale):
    return SacredGeometryPattern(
        pattern_id="custom_001",
        pattern_type="custom_spiral",
        center_x=center_x,
        center_y=center_y,
        scale=scale,
        rotation_speed=fibonacci_number * golden_ratio,
        color_palette=custom_sacred_colors,
        animation_phase=time * phi,
        harmonic_resonance=sin(time * pi * phi),
        active=True
    )

# Register custom pattern
td_integration.pattern_generators["custom_spiral"] = create_custom_pattern
```

### Interactive Control
```python
# Real-time parameter adjustment
td_integration.animation_speed = 2.0  # Double speed
td_integration.golden_ratio = 1.618033988749  # High precision φ

# Selective pattern activation
patterns = td_integration.generate_sacred_patterns()
for pattern in patterns:
    if pattern.pattern_type == "fibonacci_spiral":
        pattern.active = user_preference
```

## Troubleshooting

### Common Issues

#### Network Connection Problems
```bash
# Check port availability
netstat -an | grep 7000
netstat -an | grep 7001

# Firewall configuration
sudo ufw allow 7000
sudo ufw allow 7001
```

#### TouchDesigner Setup Issues
1. **TCP In DAT not receiving data**: Check IP address and port configuration
2. **OSC In CHOP empty**: Verify OSC message format and addressing
3. **JSON parsing errors**: Validate data structure in Convert DAT
4. **Performance issues**: Reduce FPS or node count for lower-end systems

### Debug Mode
```python
# Enable verbose logging
td_integration.debug_mode = True
td_integration.start_real_time_streaming(fps=10)  # Lower FPS for debugging
```

## Integration Examples

### Basic Workspace Visualization
```python
# Simple workspace tree visualization
context_tree = SacredGeometryContextTree()
context_tree.analyze_workspace("/path/to/workspace")

td_integration = TouchDesignerIntegration(context_tree)
td_integration.start_real_time_streaming()
```

### Multi-Project Dashboard
```python
# Multiple workspace comparison
workspaces = ["/project1", "/project2", "/project3"]
combined_nodes = []

for workspace in workspaces:
    tree = SacredGeometryContextTree()
    tree.analyze_workspace(workspace)
    combined_nodes.extend(tree.get_nodes_as_dict())

td_integration = TouchDesignerIntegration()
td_nodes = td_integration.convert_context_tree_to_touchdesigner(combined_nodes)
```

## Sacred Geometry Mathematics

### Golden Ratio Calculations
```python
φ = (1 + √5) / 2 ≈ 1.618033988749
φ² = φ + 1 ≈ 2.618033988749
1/φ = φ - 1 ≈ 0.618033988749
```

### Fibonacci Spiral Formula
```python
# Polar coordinates
r(θ) = a * φ^(2θ/π)
# Where θ = angle, a = scaling factor, φ = golden ratio
```

### Pentagonal Angles
```python
# Regular pentagon interior angle
interior_angle = 108°
# Pentagon vertex angle
vertex_angle = 72°
# Sacred pentagon ratio
pentagon_ratio = φ² = 2.618
```

This integration transforms abstract workspace data into living, breathing sacred geometry visualizations that reveal the hidden mathematical harmony within code structures.
