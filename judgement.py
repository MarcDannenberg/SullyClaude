from typing import Dict, List, Any, Optional, Union

class JudgmentProtocol:

    def _check_value_pluralism(self, claim: str) -> Dict[str, Any]:
            """Ethical check: Evaluates recognition of multiple value perspectives."""
            # Check for pluralistic language
            pluralism_markers = ["different perspectives", "various values", "multiple viewpoints", "diversity of", "depends on context"]
            has_pluralism_markers = any(marker in claim.lower() for marker in pluralism_markers)
            
            if has_pluralism_markers:
                return {"check": "value_pluralism", "score": 0.9, "reason": "Explicitly acknowledges value pluralism."}
                
            # Check for universalist language
            universalist_markers = ["universal", "absolute", "for all", "objective", "regardless of"]
            has_universalist_markers = any(marker in claim.lower() for marker in universalist_markers)
            
            if has_universalist_markers:
                return {"check": "value_pluralism", "score": 0.3, "reason": "Indicates universalist value framework."}
                
            return {"check": "value_pluralism", "score": 0.6, "reason": "Neutral on value pluralism."}

    def _check_justice_considerations(self, claim: str) -> Dict[str, Any]:
        """Ethical check: Evaluates consideration of justice and fairness."""
        # Check for justice language
        justice_markers = ["justice", "fairness", "rights", "equality", "equity", "discrimination", "oppression"]
        has_justice_markers = any(marker in claim.lower() for marker in justice_markers)
        
        if has_justice_markers:
            return {"check": "justice_considerations", "score": 0.9, "reason": "Explicitly addresses justice concerns."}
            
        # Check for power language
        power_markers = ["power", "privilege", "disadvantage", "marginalized", "vulnerable", "access"]
        has_power_markers = any(marker in claim.lower() for marker in power_markers)
        
        if has_power_markers:
            return {"check": "justice_considerations", "score": 0.8, "reason": "Addresses power dynamics."}
            
        return {"check": "justice_considerations", "score": 0.5, "reason": "Limited explicit justice considerations."}

    def _check_experiential_richness(self, claim: str) -> Dict[str, Any]:
        """Aesthetic check: Evaluates richness of experiential content."""
        # Check for sensory language
        sensory_markers = ["see", "hear", "feel", "touch", "taste", "smell", "sense", "experience"]
        sensory_count = sum(1 for marker in sensory_markers if marker in claim.lower())
        
        if sensory_count >= 2:
            return {"check": "experiential_richness", "score": 0.9, "reason": "Rich sensory language."}
        elif sensory_count == 1:
            return {"check": "experiential_richness", "score": 0.7, "reason": "Contains some sensory language."}
            
        # Check for emotional language
        emotion_markers = ["joy", "sorrow", "anger", "fear", "wonder", "awe", "delight", "melancholy"]
        has_emotion_markers = any(marker in claim.lower() for marker in emotion_markers)
        
        if has_emotion_markers:
            return {"check": "experiential_richness", "score": 0.8, "reason": "Contains emotional richness."}
            
        return {"check": "experiential_richness", "score": 0.4, "reason": "Limited experiential content."}

    def _check_form_content_coherence(self, claim: str) -> Dict[str, Any]:
        """Aesthetic check: Evaluates alignment of form and content."""
        # Check for explicit aesthetic language
        aesthetic_markers = ["beauty", "aesthetic", "form", "style", "expression", "artistic", "creative"]
        has_aesthetic_markers = any(marker in claim.lower() for marker in aesthetic_markers)
        
        if has_aesthetic_markers:
            # Check for form-content language
            form_content_markers = ["reflects", "expresses", "embodies", "represents", "manifests"]
            has_form_content = any(marker in claim.lower() for marker in form_content_markers)
            
            if has_form_content:
                return {"check": "form_content_coherence", "score": 0.9, "reason": "Explicit form-content relationship."}
            else:
                return {"check": "form_content_coherence", "score": 0.7, "reason": "Contains aesthetic language."}
                
        # Check for structural elements in the claim itself
        has_structural_elements = False
        
        # Look for patterns, parallelism, or other structural features
        words = claim.split()
        if len(words) > 10:
            # Check for parallelism (repeated syntactic structures)
            # This is a simplified check for demonstration
            phrases = claim.split(",")
            if len(phrases) >= 3:
                has_structural_elements = True
                
        if has_structural_elements:
            return {"check": "form_content_coherence", "score": 0.8, "reason": "Contains structural coherence."}
            
        return {"check": "form_content_coherence", "score": 0.5, "reason": "Neutral form-content relationship."}

    def _check_aesthetic_significance(self, claim: str) -> Dict[str, Any]:
        """Aesthetic check: Evaluates aesthetic significance of the claim."""
        # Check for significance language
        significance_markers = ["significant", "important", "meaningful", "profound", "reveals", "illuminates"]
        has_significance_markers = any(marker in claim.lower() for marker in significance_markers)
        
        if has_significance_markers:
            # Check for aesthetic domain
            aesthetic_domain_markers = ["art", "beauty", "literature", "music", "poetry", "creative", "imagination"]
            has_aesthetic_domain = any(marker in claim.lower() for marker in aesthetic_domain_markers)
            
            if has_aesthetic_domain:
                return {"check": "aesthetic_significance", "score": 0.9, "reason": "Claims aesthetic significance."}
            else:
                return {"check": "aesthetic_significance", "score": 0.6, "reason": "Claims significance in non-aesthetic domain."}
                
        return {"check": "aesthetic_significance", "score": 0.5, "reason": "Limited claims to aesthetic significance."}

    def _check_implementability(self, claim: str) -> Dict[str, Any]:
        """Practical check: Evaluates whether a claim can be implemented."""
        # Check for practical language
        practical_markers = ["implement", "apply", "use", "practice", "action", "do", "perform"]
        has_practical_markers = any(marker in claim.lower() for marker in practical_markers)
        
        if has_practical_markers:
            return {"check": "implementability", "score": 0.8, "reason": "Contains practical implementation language."}
            
        # Check for abstract vs. concrete language
        abstract_markers = ["theoretical", "abstract", "conceptual", "philosophical", "ideal"]
        has_abstract_markers = any(marker in claim.lower() for marker in abstract_markers)
        
        if has_abstract_markers:
            return {"check": "implementability", "score": 0.3, "reason": "Primarily abstract/theoretical."}
            
        # Check for specific steps or methods
        method_markers = ["method", "step", "procedure", "process", "technique", "approach"]
        has_method_markers = any(marker in claim.lower() for marker in method_markers)
        
        if has_method_markers:
            return {"check": "implementability", "score": 0.9, "reason": "Describes specific methods or procedures."}
            
        return {"check": "implementability", "score": 0.5, "reason": "Unclear implementability."}

    def _check_resource_feasibility(self, claim: str) -> Dict[str, Any]:
        """Practical check: Evaluates resource requirements and feasibility."""
        # Check for resource language
        resource_markers = ["resources", "cost", "time", "effort", "investment", "requires", "needs"]
        has_resource_markers = any(marker in claim.lower() for marker in resource_markers)
        
        if has_resource_markers:
            # Check for feasibility qualifiers
            feasibility_markers = ["feasible", "practical", "realistic", "achievable", "doable"]
            has_feasibility_markers = any(marker in claim.lower() for marker in feasibility_markers)
            
            if has_feasibility_markers:
                return {"check": "resource_feasibility", "score": 0.9, "reason": "Explicitly addresses feasibility."}
            else:
                return {"check": "resource_feasibility", "score": 0.7, "reason": "Mentions resources without clear feasibility."}
                
        # Check for idealistic language
        idealistic_markers = ["ideal", "perfect", "optimal", "ultimate", "best possible"]
        has_idealistic_markers = any(marker in claim.lower() for marker in idealistic_markers)
        
        if has_idealistic_markers:
            return {"check": "resource_feasibility", "score": 0.4, "reason": "Contains idealistic language."}
            
        return {"check": "resource_feasibility", "score": 0.6, "reason": "Neutral on resource feasibility."}

    def _check_scalability(self, claim: str) -> Dict[str, Any]:
        """Practical check: Evaluates whether a claim can scale to different contexts."""
        # Check for scalability language
        scalability_markers = ["scale", "expand", "grow", "widespread", "broad application", "generalize"]
        has_scalability_markers = any(marker in claim.lower() for marker in scalability_markers)
        
        if has_scalability_markers:
            return {"check": "scalability", "score": 0.9, "reason": "Explicitly addresses scalability."}
            
        # Check for scope language
        scope_markers = ["specific", "particular", "limited", "narrow", "certain cases", "this context"]
        has_scope_markers = any(marker in claim.lower() for marker in scope_markers)
        
        if has_scope_markers:
            return {"check": "scalability", "score": 0.3, "reason": "Indicates limited scope."}
            
        # Check for universal language
        universal_markers = ["all", "every", "universal", "always", "regardless", "in any case"]
        has_universal_markers = any(marker in claim.lower().split() for marker in universal_markers)
        
        if has_universal_markers:
            return {"check": "scalability", "score": 0.7, "reason": "Implies broad applicability."}
            
        return {"check": "scalability", "score": 0.5, "reason": "Unclear scalability."}


# if __name__ == "__main__":
# # Example usage when run directly
#     judgment = JudgmentProtocol()

# # Test with various claims
# test_claims = [
#     "All knowledge is ultimately subjective, as it is filtered through human perception.",
#     "The universe is deterministic, with every event following necessarily from prior causes.",
#     "Democracy is the best form of government because it respects individual autonomy.",
#     "Beauty exists objectively in the harmony and proportion of forms.",
#     "The most practical approach to climate change involves technological innovation and market incentives."
# ]

# print("=== Basic Judgment Examples ===")
# for claim in test_claims:
#     result = judgment.evaluate(claim, detailed_output=False)
#     print(f"\nClaim: {claim}")
#     print(f"Judgment: {result}")
    
# # Test different cognitive frameworks
# print("\n=== Cognitive Framework Examples ===")
# frameworks = list(judgment.cognitive_frameworks.keys())
# for i, framework in enumerate(frameworks):
#     if i < len(test_claims):
#         result = judgment.evaluate(test_claims[i], framework=framework, detailed_output=False)
#         print(f"\nClaim evaluated with {framework} framework:")
#         print(f"Claim: {test_claims[i]}")
#         print(f"Judgment: {result}")
        
# # Test multi-perspective evaluation
# print("\n=== Multi-Perspective Evaluation ===")
# multi_result = judgment.multi_perspective_evaluation(test_claims[0])
# print(f"Claim: {test_claims[0]}")
# print(f"Consensus Level: {multi_result['consensus_level']} ({multi_result['consensus_score']:.2f})")
# print(f"Average Score: {multi_result['average_score']:.2f}")
# print("Framework Verdicts:")
# for framework, eval_info in multi_result["framework_evaluations"].items():
#     print(f"  - {framework}: {eval_info['verdict']} ({eval_info['score']:.2f})")