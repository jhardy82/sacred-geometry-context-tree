/**
 * Sacred Geometry Engine for Context Tree Visualization
 * Implements golden ratio, Fibonacci, and pentagonal sacred geometry patterns
 */

class SacredGeometryEngine {
    constructor(canvas) {
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.width = canvas.width;
        this.height = canvas.height;

        // Sacred geometry constants
        this.PHI = 1.618033988749;
        this.FIBONACCI = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
        this.PENTAGON_ANGLE = (2 * Math.PI) / 5;

        // Visualization state
        this.nodes = new Map();
        this.selectedNode = null;
        this.animationFrame = null;
        this.zoom = 1.0;
        this.panX = 0;
        this.panY = 0;

        // Colors based on sacred geometry
        this.colors = {
            background: '#0a0a1a',
            node: '#4a90e2',
            nodeHover: '#7b68ee',
            nodeSelected: '#ffd700',
            connection: 'rgba(74, 144, 226, 0.3)',
            goldenPath: '#ffd700',
            fibonacciSpiral: '#ff6b6b',
            pentagonalGrid: 'rgba(123, 104, 238, 0.2)'
        };

        this.setupEventListeners();
        this.startAnimation();
    }

    setupEventListeners() {
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('wheel', (e) => this.handleWheel(e));

        window.addEventListener('resize', () => this.handleResize());
    }

    handleResize() {
        this.width = this.canvas.width = this.canvas.parentElement.clientWidth;
        this.height = this.canvas.height = this.canvas.parentElement.clientHeight;
        this.render();
    }

    handleClick(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = (event.clientX - rect.left - this.panX) / this.zoom;
        const y = (event.clientY - rect.top - this.panY) / this.zoom;

        // Find clicked node
        for (const [nodeId, node] of this.nodes) {
            const distance = Math.sqrt(
                Math.pow(x - node.x, 2) + Math.pow(y - node.y, 2)
            );

            if (distance <= node.radius) {
                this.selectNode(nodeId);
                return;
            }
        }

        this.selectedNode = null;
        this.render();
    }

    handleMouseMove(event) {
        // Update hover state for nodes
        const rect = this.canvas.getBoundingClientRect();
        const x = (event.clientX - rect.left - this.panX) / this.zoom;
        const y = (event.clientY - rect.top - this.panY) / this.zoom;

        let hoverNode = null;
        for (const [nodeId, node] of this.nodes) {
            const distance = Math.sqrt(
                Math.pow(x - node.x, 2) + Math.pow(y - node.y, 2)
            );

            if (distance <= node.radius) {
                hoverNode = nodeId;
                break;
            }
        }

        this.canvas.style.cursor = hoverNode ? 'pointer' : 'default';
    }

    handleWheel(event) {
        event.preventDefault();
        const zoomFactor = event.deltaY > 0 ? 0.9 : 1.1;
        this.zoom = Math.max(0.1, Math.min(3.0, this.zoom * zoomFactor));
        this.render();
    }

    selectNode(nodeId) {
        this.selectedNode = nodeId;
        this.render();

        // Notify external systems
        if (window.onNodeSelected) {
            window.onNodeSelected(nodeId);
        }
    }

    addNode(nodeId, data) {
        const position = this.calculateSacredPosition(nodeId, data);

        this.nodes.set(nodeId, {
            id: nodeId,
            x: position.x,
            y: position.y,
            radius: this.calculateNodeRadius(data),
            harmonicSignature: data.harmonicSignature || 0,
            goldenPosition: data.goldenPosition || [0, 0],
            connections: data.connections || [],
            dimensions: data.dimensions || {},
            ...data
        });

        this.render();
    }

    calculateSacredPosition(nodeId, data) {
        const centerX = this.width / 2;
        const centerY = this.height / 2;

        // Use golden ratio and Fibonacci for positioning
        const phi = this.PHI;
        const fibIndex = this.getFibonacciIndex(nodeId);
        const angle = (fibIndex * this.PENTAGON_ANGLE) % (2 * Math.PI);

        // Calculate distance using golden ratio
        const baseRadius = Math.min(this.width, this.height) * 0.3;
        const distance = baseRadius * Math.pow(phi, (fibIndex % 5) / 5);

        return {
            x: centerX + Math.cos(angle) * distance,
            y: centerY + Math.sin(angle) * distance
        };
    }

    getFibonacciIndex(nodeId) {
        // Convert node ID to consistent Fibonacci index
        let hash = 0;
        for (let i = 0; i < nodeId.length; i++) {
            hash = ((hash << 5) - hash + nodeId.charCodeAt(i)) & 0xffffffff;
        }
        return Math.abs(hash) % this.FIBONACCI.length;
    }

    calculateNodeRadius(data) {
        // Base radius using golden ratio
        const baseRadius = 15;
        const qualityMultiplier = (data.qualitative?.completeness_score || 0.5);
        return baseRadius * this.PHI * qualityMultiplier;
    }

    startAnimation() {
        const animate = () => {
            this.update();
            this.render();
            this.animationFrame = requestAnimationFrame(animate);
        };
        animate();
    }

    update() {
        // Update animations (pulsing nodes, rotating connections, etc.)
        const time = Date.now() * 0.001;

        for (const [nodeId, node] of this.nodes) {
            // Harmonic pulsing based on sacred geometry
            node.pulse = Math.sin(time * this.PHI + node.harmonicSignature) * 0.1 + 1;
        }
    }

    render() {
        // Clear canvas
        this.ctx.fillStyle = this.colors.background;
        this.ctx.fillRect(0, 0, this.width, this.height);

        // Apply zoom and pan
        this.ctx.save();
        this.ctx.translate(this.panX, this.panY);
        this.ctx.scale(this.zoom, this.zoom);

        // Draw sacred geometry background
        this.drawSacredBackground();

        // Draw connections first (behind nodes)
        this.drawConnections();

        // Draw nodes
        this.drawNodes();

        // Draw golden ratio spiral if selected node
        if (this.selectedNode) {
            this.drawGoldenSpiral();
        }

        this.ctx.restore();
    }

    drawSacredBackground() {
        // Draw pentagonal grid
        this.ctx.strokeStyle = this.colors.pentagonalGrid;
        this.ctx.lineWidth = 1;

        const centerX = this.width / 2;
        const centerY = this.height / 2;
        const radius = Math.min(this.width, this.height) * 0.4;

        // Draw concentric pentagons
        for (let r = radius * 0.2; r <= radius; r += radius * 0.2) {
            this.drawPentagon(centerX, centerY, r);
        }

        // Draw radial lines
        for (let i = 0; i < 5; i++) {
            const angle = i * this.PENTAGON_ANGLE;
            this.ctx.beginPath();
            this.ctx.moveTo(centerX, centerY);
            this.ctx.lineTo(
                centerX + Math.cos(angle) * radius,
                centerY + Math.sin(angle) * radius
            );
            this.ctx.stroke();
        }
    }

    drawPentagon(x, y, radius) {
        this.ctx.beginPath();
        for (let i = 0; i < 5; i++) {
            const angle = i * this.PENTAGON_ANGLE - Math.PI / 2;
            const px = x + Math.cos(angle) * radius;
            const py = y + Math.sin(angle) * radius;
            
            if (i === 0) {
                this.ctx.moveTo(px, py);
            } else {
                this.ctx.lineTo(px, py);
            }
        }
        this.ctx.closePath();
        this.ctx.stroke();
    }

    drawConnections() {
        for (const [nodeId, node] of this.nodes) {
            for (const connectionId of node.connections) {
                const targetNode = this.nodes.get(connectionId);
                if (targetNode) {
                    this.ctx.strokeStyle = this.colors.connection;
                    this.ctx.lineWidth = 2;
                    this.ctx.beginPath();
                    this.ctx.moveTo(node.x, node.y);
                    this.ctx.lineTo(targetNode.x, targetNode.y);
                    this.ctx.stroke();
                }
            }
        }
    }

    drawNodes() {
        for (const [nodeId, node] of this.nodes) {
            // Determine node color
            let color = this.colors.node;
            if (nodeId === this.selectedNode) {
                color = this.colors.nodeSelected;
            }

            // Draw node with pulsing effect
            const radius = node.radius * node.pulse;
            
            // Outer glow
            this.ctx.save();
            this.ctx.shadowColor = color;
            this.ctx.shadowBlur = 10;
            this.ctx.beginPath();
            this.ctx.arc(node.x, node.y, radius, 0, 2 * Math.PI);
            this.ctx.fillStyle = color;
            this.ctx.fill();
            this.ctx.restore();

            // Inner core
            this.ctx.beginPath();
            this.ctx.arc(node.x, node.y, radius * 0.6, 0, 2 * Math.PI);
            this.ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
            this.ctx.fill();

            // Node label
            this.ctx.fillStyle = '#ffffff';
            this.ctx.font = '12px Segoe UI';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(nodeId.substring(0, 8), node.x, node.y - radius - 5);
        }
    }

    drawGoldenSpiral() {
        const selectedNode = this.nodes.get(this.selectedNode);
        if (!selectedNode) return;

        this.ctx.strokeStyle = this.colors.goldenPath;
        this.ctx.lineWidth = 3;
        this.ctx.setLineDash([5, 5]);

        // Draw golden ratio spiral from selected node
        const spiralSteps = 50;
        let angle = 0;
        let radius = 10;

        this.ctx.beginPath();
        this.ctx.moveTo(selectedNode.x, selectedNode.y);

        for (let i = 0; i < spiralSteps; i++) {
            angle += 0.1;
            radius *= Math.pow(this.PHI, 0.1);
            
            const x = selectedNode.x + Math.cos(angle) * radius;
            const y = selectedNode.y + Math.sin(angle) * radius;
            
            this.ctx.lineTo(x, y);
        }

        this.ctx.stroke();
        this.ctx.setLineDash([]);
    }

    loadContextTree(treeData) {
        // Load context tree data and create visual nodes
        this.nodes.clear();

        for (const [nodeId, nodeData] of Object.entries(treeData.nodes)) {
            this.addNode(nodeId, {
                harmonicSignature: nodeData.harmonic_signature || 0,
                goldenPosition: nodeData.golden_ratio_position || [0, 0],
                connections: nodeData.relational?.child_contexts || [],
                dimensions: {
                    terrestrial: nodeData.terrestrial,
                    temporal: nodeData.temporal,
                    relational: nodeData.relational,
                    qualitative: nodeData.qualitative,
                    operational: nodeData.operational
                }
            });
        }

        this.render();
    }

    exportVisualization() {
        // Export current visualization as image
        const link = document.createElement('a');
        link.download = 'sacred-geometry-context-tree.png';
        link.href = this.canvas.toDataURL();
        link.click();
    }

    clearSelection() {
        this.selectedNode = null;
        this.render();
    }

    resetView() {
        this.zoom = 1.0;
        this.panX = 0;
        this.panY = 0;
        this.render();
    }
}

// Global functions for the HTML interface
function clearSelection() {
    if (window.sacredEngine) {
        window.sacredEngine.clearSelection();
    }
}

function resetView() {
    if (window.sacredEngine) {
        window.sacredEngine.resetView();
    }
}
