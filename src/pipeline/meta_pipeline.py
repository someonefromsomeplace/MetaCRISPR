from typing import List, Dict
import numpy as np

class MetaCRISPRPipeline:
    """
    Core orchestrator for MetaCRISPR system.

    This pipeline connects:
    - DNA preprocessing
    - PAM detection
    - gRNA generation (DNABERT-2)
    - Few-shot efficacy prediction
    - PINN-based specificity scoring
    - SHAP explainability
    """

    def __init__(self):
        # Modules will be plugged in later
        self.dna_processor = None
        self.pam_detector = None
        self.generator = None
        self.efficacy_model = None
        self.specificity_model = None
        self.explainer = None

    def load_modules(
        self,
        dna_processor,
        pam_detector,
        generator,
        efficacy_model,
        specificity_model,
        explainer
    ):
        """Inject all system components"""
        self.dna_processor = dna_processor
        self.pam_detector = pam_detector
        self.generator = generator
        self.efficacy_model = efficacy_model
        self.specificity_model = specificity_model
        self.explainer = explainer

    def run(self, dna_sequence: str, top_k: int = 10) -> Dict:
        """
        End-to-end CRISPR guide RNA generation pipeline.
        """

        # 1. Preprocessing
        processed = self.dna_processor.process(dna_sequence)

        # 2. PAM detection
        pam_sites = self.pam_detector.detect(processed)

        # 3. Candidate generation
        candidates = self.generator.generate(processed, pam_sites)

        # 4. Efficacy prediction (Few-shot / DNABERT-2)
        for c in candidates:
            c["efficacy"] = self.efficacy_model.predict(c["sequence"])

        # 5. Specificity prediction (PINN)
        for c in candidates:
            spec_out = self.specificity_model.predict(c["sequence"], processed)
            c.update(spec_out)

        # 6. Ranking (multi-objective scoring)
        candidates = self.rank_candidates(candidates)

        # 7. Explainability (SHAP)
        explanations = self.explainer.explain(candidates[:top_k])

        return {
            "top_candidates": candidates[:top_k],
            "explanations": explanations
        }

    def rank_candidates(self, candidates: List[Dict]) -> List[Dict]:
        """
        Multi-objective ranking function:
        efficacy ↑, specificity ↑, CFD ↓, stability ↑
        """

        def score(c):
            return (
                0.4 * c.get("efficacy", 0) +
                0.3 * c.get("specificity", 0) -
                0.2 * c.get("cfd", 0) +
                0.1 * c.get("gc", 0)
            )

        return sorted(candidates, key=score, reverse=True)
