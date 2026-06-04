# MetaCRISPR Methodology

## Objective

The objective of MetaCRISPR is to generate and prioritize CRISPR guide RNAs (gRNAs) that maximize gene-editing efficiency while minimizing off-target effects.

The framework combines transformer-based sequence understanding, few-shot learning, physics-informed neural networks, and explainable AI to support intelligent guide RNA design.

---

## Workflow

The MetaCRISPR pipeline consists of six major stages:

1. DNA Sequence Processing
2. PAM Site Detection
3. Candidate gRNA Generation
4. Feature Extraction
5. Hybrid AI Scoring
6. Explainability and Ranking

---

## Stage 1: DNA Sequence Processing

Input DNA sequences undergo validation and preprocessing.

Processing steps include:

- Sequence cleaning
- Nucleotide validation
- Length verification
- Window generation

The validated sequence is prepared for PAM detection and candidate extraction.

---

## Stage 2: PAM Site Detection

Potential Protospacer Adjacent Motif (PAM) sites are identified across the input sequence.

For CRISPR-Cas9 systems, PAM sequences act as anchor points for guide RNA targeting.

Outputs:

- PAM coordinates
- Targetable genomic regions

---

## Stage 3: Candidate gRNA Generation

Candidate guide RNAs are generated from valid PAM regions.

Filtering criteria include:

- Sequence validity
- Length consistency
- Target compatibility

The resulting candidate pool is passed to downstream scoring modules.

---

## Stage 4: Feature Extraction

Multiple biological and thermodynamic features are computed.

Features include:

### GC Content

Measures nucleotide composition and sequence stability.

### Delta G (ΔG)

Approximates thermodynamic binding energy.

### Minimum Free Energy (MFE)

Estimates structural stability of the guide RNA.

### Sequence Context

Captures nucleotide relationships surrounding target sites.

---

## Stage 5: Hybrid AI Scoring Framework

MetaCRISPR combines multiple AI approaches.

### DNABERT-2

DNABERT-2 generates contextual genomic embeddings from DNA sequences.

Purpose:

- Sequence representation
- Biological pattern recognition
- Context-aware feature learning

---

### Prototypical Few-Shot Learning

Few-shot learning enables efficacy prediction using limited biological datasets.

Purpose:

- Generalization under low-data conditions
- Efficient adaptation to unseen targets

Outputs:

- Predicted guide RNA efficacy

---

### Physics-Informed Neural Network (PINN)

The PINN incorporates biological constraints directly into model training.

Inputs:

- Sequence embeddings
- Delta G
- MFE
- GC content

Outputs:

- Efficiency score
- Specificity score

Benefits:

- Improved biological consistency
- Reduced unrealistic predictions

---

## Stage 6: Explainability and Ranking

SHAP (SHapley Additive exPlanations) is used to interpret model predictions.

Purpose:

- Feature attribution
- Model transparency
- Biological insight generation

Final candidate ranking is performed using:

- Efficacy score
- Specificity score
- CFD score
- Thermodynamic features

The highest-ranked guide RNAs are selected for downstream validation.

---

## Evaluation Metrics

The framework evaluates candidate gRNAs using:

- Efficiency
- Specificity
- CFD (Cutting Frequency Determination)
- Delta G
- Minimum Free Energy
- GC Content

---

## Expected Outcome

MetaCRISPR produces a ranked set of guide RNAs that balance:

- High efficacy
- High specificity
- Low off-target risk
- Favorable thermodynamic properties
