# MetaCRISPR Architecture

## System Overview

MetaCRISPR is a hybrid AI framework designed to generate, evaluate, and rank CRISPR guide RNAs (gRNAs) using a combination of transformer-based genomic embeddings, few-shot learning, physics-informed neural networks, and explainable AI.

The system processes raw DNA sequences and produces ranked candidate gRNAs optimized for efficacy, specificity, and thermodynamic stability.

---

## High-Level Pipeline

```text
DNA Sequence
      ↓
Preprocessing & Validation
      ↓
PAM Site Detection
      ↓
gRNA Candidate Generation
      ↓
Feature Extraction
      ↓
DNABERT-2 Embeddings
      ↓
Few-Shot Learning Model
      ↓
Physics-Informed Neural Network
      ↓
Scoring & Ranking
      ↓
SHAP Explainability
      ↓
Top Candidate gRNAs
```

---

## Module Descriptions

### 1. DNA Preprocessing Module

Responsibilities:

- Validate DNA sequences
- Clean invalid nucleotides
- Generate candidate windows
- Prepare sequences for downstream processing

Outputs:

- Validated DNA sequence
- PAM candidate regions

---

### 2. PAM Detection Module

Responsibilities:

- Identify CRISPR-Cas9 compatible PAM sites
- Extract targetable genomic regions

Outputs:

- PAM coordinates
- Candidate target regions

---

### 3. gRNA Generation Module

Responsibilities:

- Generate candidate guide RNAs
- Filter invalid candidates
- Standardize sequence length

Outputs:

- Candidate gRNA pool

---

### 4. DNABERT-2 Embedding Module

Responsibilities:

- Encode genomic sequences into contextual embeddings
- Capture biological sequence relationships

Outputs:

- Learned sequence representations

---

### 5. Few-Shot Learning Module

Responsibilities:

- Predict guide RNA efficacy using limited labeled samples
- Improve generalization under scarce biological datasets

Outputs:

- Efficacy predictions

---

### 6. Physics-Informed Neural Network (PINN)

Responsibilities:

- Incorporate biological constraints
- Integrate thermodynamic features
- Improve biological plausibility

Features:

- Delta G
- Minimum Free Energy (MFE)
- GC Content

Outputs:

- Efficiency scores
- Specificity scores

---

### 7. Explainability Module

Responsibilities:

- Generate SHAP explanations
- Identify influential sequence regions
- Improve model transparency

Outputs:

- Feature importance visualizations
- Nucleotide contribution analysis

---

### 8. Candidate Ranking Module

Responsibilities:

- Aggregate model predictions
- Rank candidate gRNAs
- Select elite candidates

Outputs:

- Top-ranked gRNA candidates
