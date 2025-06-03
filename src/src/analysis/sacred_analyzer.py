#!/usr/bin/env python3
"""
🔬 Advanced Sacred Geometry Analysis Engine

Provides deeper insights into context tree patterns using
advanced sacred geometry principles for pattern discovery,
harmonic clustering, and sacred pathway identification.
"""

import math
from typing import Dict, List, Any, Optional
from sacred_geometry_context_tree import SacredGeometryContextTree, SacredContextNode


class AdvancedSacredGeometryAnalyzer:
    """
    🔬 Advanced Sacred Geometry Analysis Engine

    Provides deeper insights into context tree patterns using
    advanced sacred geometry principles.
    """

    def __init__(self, context_tree: SacredGeometryContextTree):
        self.context_tree = context_tree
        self.golden_ratio = 1.618033988749
        self.phi_squared = self.golden_ratio**2
        self.fibonacci_sequence = self._generate_fibonacci(50)

        # Advanced sacred geometry constants
        self.sacred_constants = {
            "phi": self.golden_ratio,
            "phi_squared": self.phi_squared,
            "pi": math.pi,
            "euler": math.e,
            "sqrt_5": math.sqrt(5),
            "pentagonal_angle": 72.0,  # degrees
            "golden_angle": 137.508,  # degrees (360 / phi^2)
            "silver_ratio": 1 + math.sqrt(2),
            "bronze_ratio": (3 + math.sqrt(13)) / 2,
        }

    def _generate_fibonacci(self, n: int) -> List[int]:
        """Generate extended Fibonacci sequence."""
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

    def analyze_harmonic_clusters(self) -> List[Dict[str, Any]]:
        """
        🎵 Identify harmonic clusters in the context tree

        Groups nodes by harmonic signature similarity using golden ratio analysis.
        """
        clusters = []
        all_nodes = list(self.context_tree.nodes.values())

        # Sort nodes by harmonic signature
        sorted_nodes = sorted(all_nodes, key=lambda n: n.harmonic_signature)

        # Create clusters using golden ratio intervals
        cluster_threshold = 1.0 / self.golden_ratio  # ~0.618
        current_cluster = []

        for i, node in enumerate(sorted_nodes):
            if not current_cluster:
                current_cluster.append(node)
            else:
                # Check if node fits in current cluster
                signature_diff = abs(
                    node.harmonic_signature - current_cluster[-1].harmonic_signature
                )
                if signature_diff <= cluster_threshold:
                    current_cluster.append(node)
                else:
                    # Finalize current cluster and start new one
                    if len(current_cluster) >= 2:  # Only keep meaningful clusters
                        cluster_analysis = self._analyze_cluster(current_cluster)
                        clusters.append(cluster_analysis)
                    current_cluster = [node]

        # Don't forget the last cluster
        if len(current_cluster) >= 2:
            cluster_analysis = self._analyze_cluster(current_cluster)
            clusters.append(cluster_analysis)

        return clusters

    def _analyze_cluster(self, nodes: List[SacredContextNode]) -> Dict[str, Any]:
        """Analyze a harmonic cluster for sacred geometry properties."""
        signatures = [n.harmonic_signature for n in nodes]

        cluster_analysis = {
            "cluster_id": f"cluster_{len(nodes)}_{min(signatures):.3f}",
            "node_count": len(nodes),
            "harmonic_range": [min(signatures), max(signatures)],
            "mean_harmonic": sum(signatures) / len(signatures),
            "golden_ratio_coherence": self._calculate_golden_ratio_coherence(
                signatures
            ),
            "fibonacci_alignment": self._calculate_fibonacci_alignment(len(nodes)),
            "node_ids": [n.node_id for n in nodes],
            "dimensional_patterns": self._analyze_dimensional_patterns(nodes),
            "sacred_geometry_score": 0.0,
        }

        # Calculate overall sacred geometry score
        cluster_analysis["sacred_geometry_score"] = (
            cluster_analysis["golden_ratio_coherence"] * 0.4
            + cluster_analysis["fibonacci_alignment"] * 0.3
            + len(cluster_analysis["dimensional_patterns"]) / 5.0 * 0.3
        )

        return cluster_analysis

    def _calculate_golden_ratio_coherence(self, signatures: List[float]) -> float:
        """Calculate how well signatures align with golden ratio intervals."""
        if len(signatures) < 2:
            return 0.0

        coherence_scores = []
        for i in range(len(signatures) - 1):
            ratio = signatures[i + 1] / signatures[i] if signatures[i] != 0 else 0
            # How close is this ratio to golden ratio or its inverse?
            golden_distance = min(
                abs(ratio - self.golden_ratio),
                abs(ratio - (1 / self.golden_ratio)),
                abs(ratio - self.phi_squared),
                abs(ratio - (1 / self.phi_squared)),
            )
            coherence = max(0, 1 - golden_distance)
            coherence_scores.append(coherence)

        return sum(coherence_scores) / len(coherence_scores)

    def _calculate_fibonacci_alignment(self, count: int) -> float:
        """Calculate how well the count aligns with Fibonacci numbers."""
        # Find closest Fibonacci number
        closest_fib = min(self.fibonacci_sequence, key=lambda x: abs(x - count))
        alignment = 1.0 / (1.0 + abs(count - closest_fib))
        return alignment

    def _analyze_dimensional_patterns(
        self, nodes: List[SacredContextNode]
    ) -> List[str]:
        """Identify common dimensional patterns in cluster."""
        patterns = []

        # Check for dimensional consistency across sacred dimensions
        dimension_weights = {}
        for node in nodes:
            dimension_weights.setdefault("terrestrial", []).append(
                node.terrestrial.weight
            )
            dimension_weights.setdefault("temporal", []).append(node.temporal.weight)
            dimension_weights.setdefault("relational", []).append(
                node.relational.weight
            )
            dimension_weights.setdefault("qualitative", []).append(
                node.qualitative.weight
            )
            dimension_weights.setdefault("operational", []).append(
                node.operational.weight
            )

        active_dimensions = sum(
            1 for weights in dimension_weights.values() if any(w > 0 for w in weights)
        )

        if active_dimensions >= 3:
            patterns.append("dimensional_consistency")

        if active_dimensions == 5:
            patterns.append("pentagonal_completeness")

        # Check for golden ratio relationships in dimension weights
        for dim, weights in dimension_weights.items():
            if self._has_golden_ratio_progression(weights):
                patterns.append(f"golden_ratio_{dim}")

        return patterns

    def _has_golden_ratio_progression(self, values: List[float]) -> bool:
        """Check if numeric values show golden ratio progression patterns."""
        if len(values) < 3:
            return False

        # Filter out zero values
        non_zero_values = [v for v in values if v > 0]
        if len(non_zero_values) < 2:
            return False

        # Check if values follow golden ratio progression
        for i in range(len(non_zero_values) - 1):
            ratio = non_zero_values[i + 1] / non_zero_values[i]
            if (
                abs(ratio - self.golden_ratio) < 0.2
                or abs(ratio - (1 / self.golden_ratio)) < 0.2
            ):
                return True

        return False

    def discover_sacred_pathways(self) -> List[Dict[str, Any]]:
        """
        🛤️ Discover optimal pathways through context tree using sacred geometry

        Identifies navigation paths that follow golden ratio and Fibonacci principles.
        """
        pathways = []
        all_nodes = list(self.context_tree.nodes.values())

        # Find high-harmonic nodes as pathway anchors
        anchor_nodes = sorted(
            all_nodes, key=lambda n: n.harmonic_signature, reverse=True
        )[
            :13
        ]  # Fibonacci number

        for i, start_node in enumerate(anchor_nodes[:8]):  # Fibonacci number
            pathway = self._trace_sacred_pathway(start_node, anchor_nodes)
            if len(pathway["nodes"]) >= 3:  # Minimum meaningful pathway
                pathways.append(pathway)

        return pathways

    def _trace_sacred_pathway(
        self, start_node: SacredContextNode, anchor_nodes: List[SacredContextNode]
    ) -> Dict[str, Any]:
        """Trace a pathway following sacred geometry principles."""
        pathway_nodes = [start_node]
        current_node = start_node

        # Trace pathway using golden ratio progression
        for step in range(7):  # Maximum pathway length (sacred number)
            next_node = self._find_next_sacred_node(
                current_node, anchor_nodes, pathway_nodes
            )
            if next_node:
                pathway_nodes.append(next_node)
                current_node = next_node
            else:
                break

        # Analyze pathway properties
        pathway = {
            "pathway_id": f"sacred_path_{start_node.node_id}",
            "start_node": start_node.node_id,
            "end_node": pathway_nodes[-1].node_id,
            "nodes": [n.node_id for n in pathway_nodes],
            "length": len(pathway_nodes),
            "total_harmonic": sum(n.harmonic_signature for n in pathway_nodes),
            "golden_ratio_flow": self._calculate_pathway_flow(pathway_nodes),
            "fibonacci_alignment": self._calculate_fibonacci_alignment(
                len(pathway_nodes)
            ),
            "sacred_geometry_score": 0.0,
        }

        # Calculate overall sacred geometry score for pathway
        pathway["sacred_geometry_score"] = (
            pathway["golden_ratio_flow"] * 0.5
            + pathway["fibonacci_alignment"] * 0.3
            + (pathway["total_harmonic"] / len(pathway_nodes)) * 0.2
        )

        return pathway

    def _find_next_sacred_node(
        self,
        current_node: SacredContextNode,
        candidates: List[SacredContextNode],
        used_nodes: List[SacredContextNode],
    ) -> Optional[SacredContextNode]:
        """Find next node in pathway using sacred geometry criteria."""
        best_node = None
        best_score = 0.0

        for candidate in candidates:
            if candidate in used_nodes:
                continue

            # Calculate sacred geometry score for this transition
            harmonic_ratio = (
                candidate.harmonic_signature / current_node.harmonic_signature
                if current_node.harmonic_signature > 0
                else 1
            )

            # Prefer golden ratio relationships
            golden_score = max(
                0,
                1
                - min(
                    abs(harmonic_ratio - self.golden_ratio),
                    abs(harmonic_ratio - (1 / self.golden_ratio)),
                ),
            )

            # Prefer increasing harmonic progression
            progression_score = (
                1.0
                if candidate.harmonic_signature > current_node.harmonic_signature
                else 0.5
            )

            # Dimensional similarity bonus
            similarity_score = self._calculate_dimensional_similarity(
                current_node, candidate
            )

            total_score = (
                golden_score * 0.4 + progression_score * 0.3 + similarity_score * 0.3
            )

            if total_score > best_score:
                best_score = total_score
                best_node = candidate

        return best_node if best_score > 0.3 else None  # Minimum quality threshold

    def _calculate_pathway_flow(self, nodes: List[SacredContextNode]) -> float:
        """Calculate how well pathway follows golden ratio flow."""
        if len(nodes) < 2:
            return 0.0

        flow_scores = []
        for i in range(len(nodes) - 1):
            current_sig = nodes[i].harmonic_signature
            next_sig = nodes[i + 1].harmonic_signature

            if current_sig > 0:
                ratio = next_sig / current_sig
                # How close to golden ratio?
                golden_distance = min(
                    abs(ratio - self.golden_ratio), abs(ratio - (1 / self.golden_ratio))
                )
                flow_score = max(0, 1 - golden_distance)
                flow_scores.append(flow_score)

        return sum(flow_scores) / len(flow_scores) if flow_scores else 0.0

    def _calculate_dimensional_similarity(
        self, node1: SacredContextNode, node2: SacredContextNode
    ) -> float:
        """Calculate dimensional similarity between two nodes."""
        # Calculate similarity across all five sacred dimensions
        dimension_similarities = []

        dimensions = [
            "terrestrial",
            "temporal",
            "relational",
            "qualitative",
            "operational",
        ]

        for dim in dimensions:
            weight1 = getattr(node1, dim).weight
            weight2 = getattr(node2, dim).weight

            # Calculate relative similarity (accounting for zero values)
            if weight1 == 0 and weight2 == 0:
                similarity = 1.0  # Both are zero - perfect similarity
            elif weight1 == 0 or weight2 == 0:
                similarity = 0.0  # One is zero, one isn't - no similarity
            else:
                # Calculate proportional similarity
                ratio = min(weight1, weight2) / max(weight1, weight2)
                similarity = ratio

            dimension_similarities.append(similarity)

        return sum(dimension_similarities) / len(dimension_similarities)

    def generate_comprehensive_analysis(self) -> Dict[str, Any]:
        """Generate comprehensive sacred geometry analysis of the context tree."""
        harmonic_clusters = self.analyze_harmonic_clusters()
        sacred_pathways = self.discover_sacred_pathways()

        return {
            "analysis_timestamp": "2025-01-28T00:00:00Z",
            "context_tree_stats": {
                "total_nodes": len(self.context_tree.nodes),
                "workspace_path": self.context_tree.workspace_path,
                "phi_value": self.golden_ratio,
                "fibonacci_depth": len(self.fibonacci_sequence),
            },
            "harmonic_cluster_analysis": {
                "total_clusters": len(harmonic_clusters),
                "clusters": harmonic_clusters,
                "cluster_quality_distribution": {
                    "high_quality": len(
                        [
                            c
                            for c in harmonic_clusters
                            if c["sacred_geometry_score"] > 0.7
                        ]
                    ),
                    "medium_quality": len(
                        [
                            c
                            for c in harmonic_clusters
                            if 0.4 <= c["sacred_geometry_score"] <= 0.7
                        ]
                    ),
                    "low_quality": len(
                        [
                            c
                            for c in harmonic_clusters
                            if c["sacred_geometry_score"] < 0.4
                        ]
                    ),
                },
            },
            "sacred_pathway_analysis": {
                "total_pathways": len(sacred_pathways),
                "pathways": sacred_pathways,
                "pathway_quality_distribution": {
                    "excellent": len(
                        [p for p in sacred_pathways if p["sacred_geometry_score"] > 0.8]
                    ),
                    "good": len(
                        [
                            p
                            for p in sacred_pathways
                            if 0.6 <= p["sacred_geometry_score"] <= 0.8
                        ]
                    ),
                    "moderate": len(
                        [p for p in sacred_pathways if p["sacred_geometry_score"] < 0.6]
                    ),
                },
            },
            "sacred_geometry_recommendations": {
                "optimal_navigation_nodes": [
                    p["nodes"][:3]
                    for p in sacred_pathways
                    if p["sacred_geometry_score"] > 0.7
                ][:5],
                "harmonic_focus_clusters": [
                    c["node_ids"]
                    for c in harmonic_clusters
                    if c["sacred_geometry_score"] > 0.6
                ][:3],
                "fibonacci_expansion_candidates": [
                    c["node_ids"][0]
                    for c in harmonic_clusters
                    if c["fibonacci_alignment"] > 0.8
                    and len(c["node_ids"]) in self.fibonacci_sequence[:8]
                ],
            },
        }
