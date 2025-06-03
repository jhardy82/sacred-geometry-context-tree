/**
 * Main application controller for Sacred Geometry Context Tree visualization
 * Coordinates between the visualization engine and the context tree API
 */

class SacredContextTreeApp {
    constructor() {
        this.engine = null;
        this.api = window.contextTreeAPI;
        this.currentNode = null;
        
        this.initializeApp();
    }

    async initializeApp() {
        try {
            // Initialize canvas and engine
            const canvas = document.getElementById('contextCanvas');
            this.resizeCanvas(canvas);
            
            this.engine = new SacredGeometryEngine(canvas);
            window.sacredEngine = this.engine; // Make globally accessible

            // Set up API event listeners
            this.api.subscribe((eventType, data) => this.handleAPIEvent(eventType, data));

            // Set up UI event listeners
            this.setupUIEventListeners();

            // Load initial context tree
            await this.loadContextTree();

            // Hide loading indicator
            document.getElementById('loading').style.display = 'none';

        } catch (error) {
            console.error('Failed to initialize application:', error);
            this.showError('Failed to initialize Sacred Geometry Context Tree');
        }
    }

    resizeCanvas(canvas) {
        const container = canvas.parentElement;
        canvas.width = container.clientWidth;
        canvas.height = container.clientHeight;
    }

    setupUIEventListeners() {
        // Search input
        const searchInput = document.getElementById('search-input');
        searchInput.addEventListener('input', (e) => this.handleSearch(e.target.value));
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleNavigateToSearch(e.target.value);
            }
        });

        // Navigation type selector
        const navSelect = document.getElementById('navigationSelect');
        navSelect.addEventListener('change', (e) => this.handleNavigationTypeChange(e.target.value));

        // Control buttons
        document.getElementById('refreshBtn').addEventListener('click', () => this.refreshTree());
        document.getElementById('exportBtn').addEventListener('click', () => this.exportVisualization());

        // Window resize
        window.addEventListener('resize', () => this.handleResize());

        // Node selection callback
        window.onNodeSelected = (nodeId) => this.handleNodeSelection(nodeId);
    }

    async loadContextTree(workspacePath = '/workspaces/sacred-geometry-context-tree') {
        try {
            this.updateStatus('Loading context tree...');
            
            const treeData = await this.api.loadContextTree(workspacePath);
            this.engine.loadContextTree(treeData);
            
            this.updateNodeCount(Object.keys(treeData.nodes).length);
            this.updateStatus('Sacred geometry patterns calculated');
            
            // Set initial node if available
            if (treeData.nodes['workspace_root']) {
                this.handleNodeSelection('workspace_root');
            }

        } catch (error) {
            console.error('Failed to load context tree:', error);
            this.showError('Failed to load context tree data');
        }
    }

    handleAPIEvent(eventType, data) {
        switch (eventType) {
            case 'tree_loaded':
                console.log('Context tree loaded:', data);
                break;
            case 'navigation':
                this.updateCurrentNode(data.nodeId, data.targetNode);
                break;
            case 'search_results':
                this.displaySearchResults(data.results);
                break;
            default:
                console.log('API event:', eventType, data);
        }
    }

    handleNodeSelection(nodeId) {
        this.currentNode = nodeId;
        
        // Update UI to show selected node info
        if (this.api.currentTree && this.api.currentTree.nodes[nodeId]) {
            const nodeData = this.api.currentTree.nodes[nodeId];
            this.updateNodeInfo(nodeId, nodeData);
        }

        // Update status
        this.updateStatus(`Selected: ${nodeId}`);
    }

    updateNodeInfo(nodeId, nodeData) {
        // Update current context display
        document.getElementById('current-context').textContent = nodeId;

        // Update dimension bars
        this.updateDimensionBar('terrestrial-fill', this.calculateDimensionScore(nodeData.terrestrial));
        this.updateDimensionBar('temporal-fill', this.calculateDimensionScore(nodeData.temporal));
        this.updateDimensionBar('relational-fill', this.calculateDimensionScore(nodeData.relational));
        this.updateDimensionBar('qualitative-fill', nodeData.qualitative.completeness_score * 100);
        this.updateDimensionBar('operational-fill', this.calculateOperationalScore(nodeData.operational));

        // Update sacred geometry metrics
        document.getElementById('harmonic-signature').textContent = nodeData.harmonic_signature.toFixed(3);
        document.getElementById('golden-position').textContent = 
            `(${nodeData.golden_ratio_position[0].toFixed(3)}, ${nodeData.golden_ratio_position[1].toFixed(3)})`;
        
        // Calculate Fibonacci depth
        const fibDepth = this.calculateFibonacciDepth(nodeData.harmonic_signature);
        document.getElementById('fibonacci-depth').textContent = fibDepth;
        
        // Update pentagonal harmony
        const harmony = nodeData.harmonic_signature > 2.618 ? 'φ²' : 'φ';
        document.getElementById('pentagonal-harmony').textContent = harmony;
    }

    updateDimensionBar(elementId, percentage) {
        const element = document.getElementById(elementId);
        if (element) {
            element.style.width = `${Math.max(0, Math.min(100, percentage))}%`;
        }
    }

    calculateDimensionScore(dimensionData) {
        // Calculate a score based on dimension data completeness and quality
        let score = 0;
        const fields = Object.keys(dimensionData);
        
        fields.forEach(field => {
            if (dimensionData[field] !== null && dimensionData[field] !== undefined) {
                score += 20; // Each field contributes 20%
            }
        });

        return Math.min(100, score);
    }

    calculateOperationalScore(operationalData) {
        const statusScores = {
            'active': 90,
            'processing': 70,
            'idle': 50,
            'error': 10
        };
        
        return statusScores[operationalData.current_status] || 30;
    }

    calculateFibonacciDepth(harmonicSignature) {
        const fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55];
        
        for (let i = 0; i < fibonacci.length; i++) {
            if (harmonicSignature < fibonacci[i]) {
                return i;
            }
        }
        
        return fibonacci.length;
    }

    handleSearch(query) {
        if (query.length < 2) {
            return;
        }

        const results = this.api.searchNodes(query);
        this.displaySearchResults(results);
    }

    handleNavigateToSearch(query) {
        if (!query) return;

        const results = this.api.searchNodes(query);
        if (results.length > 0) {
            const topResult = results[0];
            this.api.navigateTo(topResult.nodeId).then(() => {
                this.engine.selectNode(topResult.nodeId);
            });
        }
    }

    displaySearchResults(results) {
        // Could display in a dropdown or sidebar panel
        console.log('Search results:', results);
    }

    handleNavigationTypeChange(navigationType) {
        console.log('Navigation type changed to:', navigationType);
        // Store preference for future navigation actions
        this.navigationMode = navigationType;
    }

    async refreshTree() {
        this.updateStatus('Refreshing context tree...');
        await this.loadContextTree();
    }

    exportVisualization() {
        // Export both the visualization and data
        this.engine.exportVisualization();
        
        // Also offer data export
        const treeJSON = this.api.exportTree('json');
        const blob = new Blob([treeJSON], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        
        const link = document.createElement('a');
        link.href = url;
        link.download = 'sacred-geometry-context-tree-data.json';
        link.click();
        
        URL.revokeObjectURL(url);
    }

    handleResize() {
        const canvas = document.getElementById('contextCanvas');
        this.resizeCanvas(canvas);
        this.engine.handleResize();
    }

    updateStatus(message) {
        document.getElementById('statusMessage').textContent = message;
    }

    updateNodeCount(count) {
        document.getElementById('nodeCountDisplay').textContent = `${count} nodes in sacred geometry tree`;
    }

    showError(message) {
        this.updateStatus(`❌ ${message}`);
        console.error(message);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.sacredContextTreeApp = new SacredContextTreeApp();
});
