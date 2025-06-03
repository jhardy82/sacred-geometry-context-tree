/**
 * Context Tree API for Sacred Geometry Visualization
 * Provides data loading and management for the visualization engine
 */

class ContextTreeAPI {
    constructor() {
        this.baseUrl = '/api/context-tree';
        this.currentTree = null;
        this.subscribers = [];
    }

    /**
     * Load context tree data from backend or local file
     */
    async loadContextTree(workspacePath = '/workspaces') {
        try {
            // Try to load from backend API first
            const response = await fetch(`${this.baseUrl}/load?workspace=${encodeURIComponent(workspacePath)}`);
            
            if (response.ok) {
                this.currentTree = await response.json();
            } else {
                // Fallback to sample data if backend not available
                this.currentTree = this.generateSampleTree();
            }

            this.notifySubscribers('tree_loaded', this.currentTree);
            return this.currentTree;
        } catch (error) {
            console.warn('Backend not available, using sample data:', error);
            this.currentTree = this.generateSampleTree();
            this.notifySubscribers('tree_loaded', this.currentTree);
            return this.currentTree;
        }
    }

    /**
     * Generate sample tree data for demonstration
     */
    generateSampleTree() {
        const PHI = 1.618033988749;
        const nodes = {};

        // Create sample nodes with sacred geometry properties
        const sampleNodes = [
            'workspace_root',
            'src',
            'core',
            'analysis',
            'navigation',
            'gui',
            'visualization',
            'tests',
            'examples',
            'docs'
        ];

        sampleNodes.forEach((nodeId, index) => {
            const harmonicSignature = (index + 1) * PHI;
            const goldenPosition = [
                Math.cos(index * 2 * Math.PI / 5) * PHI,
                Math.sin(index * 2 * Math.PI / 5) * PHI
            ];

            nodes[nodeId] = {
                harmonic_signature: harmonicSignature,
                golden_ratio_position: goldenPosition,
                terrestrial: {
                    file_path: `/${nodeId}`,
                    size: Math.floor(Math.random() * 1000) + 100
                },
                temporal: {
                    version: "1.0.0",
                    lifecycle_stage: index < 5 ? "active" : "development",
                    last_modified: new Date().toISOString()
                },
                relational: {
                    parent_contexts: index > 0 ? [sampleNodes[Math.floor(index / 2)]] : [],
                    child_contexts: sampleNodes.filter((_, i) => Math.floor(i / 2) === index),
                    peer_contexts: []
                },
                qualitative: {
                    completeness_score: 0.3 + (index / sampleNodes.length) * 0.7,
                    validation_status: Math.random() > 0.5 ? "validated" : "pending",
                    quality_metrics: {
                        complexity: Math.random(),
                        maintainability: Math.random(),
                        testability: Math.random()
                    }
                },
                operational: {
                    current_status: ["active", "idle", "processing", "error"][Math.floor(Math.random() * 4)],
                    resource_usage: Math.random(),
                    performance_metrics: {
                        response_time: Math.random() * 100,
                        throughput: Math.random() * 1000
                    }
                }
            };
        });

        return {
            workspace_path: '/workspaces/sacred-geometry-context-tree',
            created_at: new Date().toISOString(),
            sacred_geometry_metadata: {
                phi: PHI,
                fibonacci_sequence: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
                pentagonal_harmony: PHI * PHI
            },
            nodes: nodes
        };
    }

    /**
     * Navigate to a specific node
     */
    async navigateTo(nodeId, navigationType = 'harmonic') {
        if (!this.currentTree || !this.currentTree.nodes[nodeId]) {
            throw new Error(`Node ${nodeId} not found`);
        }

        const targetNode = this.currentTree.nodes[nodeId];
        this.notifySubscribers('navigation', { nodeId, targetNode, navigationType });

        return targetNode;
    }

    /**
     * Search nodes by criteria
     */
    searchNodes(query, dimension = null) {
        if (!this.currentTree) {
            return [];
        }

        const results = [];
        const queryLower = query.toLowerCase();

        for (const [nodeId, nodeData] of Object.entries(this.currentTree.nodes)) {
            let match = false;

            // Search in node ID
            if (nodeId.toLowerCase().includes(queryLower)) {
                match = true;
            }

            // Search in specific dimension if specified
            if (dimension && nodeData[dimension]) {
                const dimensionData = JSON.stringify(nodeData[dimension]).toLowerCase();
                if (dimensionData.includes(queryLower)) {
                    match = true;
                }
            }

            // Search in all dimensions if no specific dimension
            if (!dimension) {
                const allData = JSON.stringify(nodeData).toLowerCase();
                if (allData.includes(queryLower)) {
                    match = true;
                }
            }

            if (match) {
                results.push({
                    nodeId,
                    nodeData,
                    relevanceScore: this.calculateRelevanceScore(nodeData, query)
                });
            }
        }

        // Sort by relevance
        results.sort((a, b) => b.relevanceScore - a.relevanceScore);

        this.notifySubscribers('search_results', { query, dimension, results });
        return results;
    }

    /**
     * Calculate relevance score for search results
     */
    calculateRelevanceScore(nodeData, query) {
        const PHI = 1.618033988749;
        let score = 0;

        // Base score from harmonic signature
        score += nodeData.harmonic_signature / 100;

        // Quality score influence
        score += nodeData.qualitative.completeness_score * PHI;

        // Operational status influence
        if (nodeData.operational.current_status === 'active') {
            score += PHI;
        }

        return score;
    }

    /**
     * Get Fibonacci neighbors of a node
     */
    getFibonacciNeighbors(nodeId, depth = 1) {
        if (!this.currentTree || !this.currentTree.nodes[nodeId]) {
            return [];
        }

        const fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
        const targetDistance = fibonacci[Math.min(depth, fibonacci.length - 1)];
        
        const sourceNode = this.currentTree.nodes[nodeId];
        const neighbors = [];

        for (const [otherNodeId, otherNode] of Object.entries(this.currentTree.nodes)) {
            if (otherNodeId === nodeId) continue;

            // Calculate sacred geometry distance
            const distance = this.calculateSacredDistance(sourceNode, otherNode);
            
            if (Math.abs(distance - targetDistance) < 0.5) {
                neighbors.push({
                    nodeId: otherNodeId,
                    nodeData: otherNode,
                    distance: distance
                });
            }
        }

        return neighbors;
    }

    /**
     * Calculate sacred geometry distance between nodes
     */
    calculateSacredDistance(node1, node2) {
        const [x1, y1] = node1.golden_ratio_position;
        const [x2, y2] = node2.golden_ratio_position;
        
        return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    }

    /**
     * Export tree data
     */
    exportTree(format = 'json') {
        if (!this.currentTree) {
            throw new Error('No tree data to export');
        }

        switch (format) {
            case 'json':
                return JSON.stringify(this.currentTree, null, 2);
            case 'csv':
                return this.exportToCSV();
            case 'xml':
                return this.exportToXML();
            default:
                throw new Error(`Unsupported export format: ${format}`);
        }
    }

    /**
     * Export to CSV format
     */
    exportToCSV() {
        const headers = [
            'Node ID',
            'File Path',
            'Harmonic Signature',
            'Completeness Score',
            'Status',
            'Golden Position X',
            'Golden Position Y'
        ];

        const rows = [headers.join(',')];

        for (const [nodeId, nodeData] of Object.entries(this.currentTree.nodes)) {
            const row = [
                nodeId,
                nodeData.terrestrial.file_path || '',
                nodeData.harmonic_signature,
                nodeData.qualitative.completeness_score,
                nodeData.operational.current_status,
                nodeData.golden_ratio_position[0],
                nodeData.golden_ratio_position[1]
            ];
            rows.push(row.join(','));
        }

        return rows.join('\n');
    }

    /**
     * Export to XML format
     */
    exportToXML() {
        let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
        xml += '<sacred-geometry-context-tree>\n';
        xml += `  <metadata>\n`;
        xml += `    <workspace-path>${this.currentTree.workspace_path}</workspace-path>\n`;
        xml += `    <created-at>${this.currentTree.created_at}</created-at>\n`;
        xml += `  </metadata>\n`;
        xml += '  <nodes>\n';

        for (const [nodeId, nodeData] of Object.entries(this.currentTree.nodes)) {
            xml += `    <node id="${nodeId}">\n`;
            xml += `      <harmonic-signature>${nodeData.harmonic_signature}</harmonic-signature>\n`;
            xml += `      <golden-position x="${nodeData.golden_ratio_position[0]}" y="${nodeData.golden_ratio_position[1]}" />\n`;
            xml += `      <status>${nodeData.operational.current_status}</status>\n`;
            xml += `    </node>\n`;
        }

        xml += '  </nodes>\n';
        xml += '</sacred-geometry-context-tree>';

        return xml;
    }

    /**
     * Subscribe to API events
     */
    subscribe(callback) {
        this.subscribers.push(callback);
    }

    /**
     * Unsubscribe from API events
     */
    unsubscribe(callback) {
        const index = this.subscribers.indexOf(callback);
        if (index > -1) {
            this.subscribers.splice(index, 1);
        }
    }

    /**
     * Notify all subscribers of events
     */
    notifySubscribers(eventType, data) {
        this.subscribers.forEach(callback => {
            try {
                callback(eventType, data);
            } catch (error) {
                console.error('Error in subscriber callback:', error);
            }
        });
    }
}

// Create global API instance
window.contextTreeAPI = new ContextTreeAPI();
