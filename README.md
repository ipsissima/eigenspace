# EigenSpace Model: Code & Data Monorepo

This repository contains all code, data, and demonstration scripts for the EigenSpace Model framework, supporting the results in:

**Ballús Santacana, Andreu. "The EigenSpace Model: A Spectral-Categorical Framework for Semantic Processing in Brains and Language Models."**  
*(Manuscript under review; preprint link will be provided upon acceptance)*

---

## 🚦 Project Status

> **This repository accompanies a research paper that is currently under peer review. The associated manuscript is not yet public. Please do not cite this repository as a published work until a preprint or final publication becomes available. For early access or collaboration, contact the author.**

---

## Repository Structure

```
eigenspace/
├── toy_certificate_demo/
│   ├── make_toy_certificates.py      # Generate certificates for analytic functions
│   ├── toy_x.npy, toy_y.npy         # Synthetic data: x, y points for demo
│   ├── toy_cheb_coeffs.npy          # Chebyshev coefficients
│   ├── toy_certificate_errors.npy   # L2 errors vs N
│   ├── toy_error_decay.png          # Error decay plot
│   ├── toy_cheb_reconstruction.png  # Reconstruction plot
│   ├── toy_stats_summary.json       # Demo statistics
│   └── README_toy.md                # Demo instructions
│
├── tinystories_llm_certificates_repo/
│   ├── make_certificates.py         # PCA, certificate extraction for LLM data
│   ├── requirements.txt             # Python dependencies for LLM pipeline
│   ├── tinystories_texts.csv        # 100 TinyStories prompts
│   ├── tinystories_gpt2_activations.npy # 768-dim GPT-2 activations
│   ├── llm_pca_*.npy / .csv         # PCA data: components, explained var, projections, etc.
│   ├── llm_pc_scatter.png           # PC1 vs PC2 plot
│   ├── llm_principal_angles_deg.npy # Pairwise subspace angles
│   ├── stats_summary.json           # CCA / angle / runtime summary
│   └── README.md                    # LLM pipeline instructions
│
├── openneuro_certificates/
│   ├── extract_fmri_certificates.py # fMRI PCA/certificate extraction
│   ├── CHANGES                      # fMRI pipeline change log
│   ├── dataset_description.json     # Dataset metadata
│   ├── participants.xlsx            # Subject info
│   ├── sub-0*_fmri_matrix.npy       # PCA-ready fMRI matrices
│   ├── sub-0*_pca_*.npy/.png        # PCA components, variance, projections
│   ├── sub-0*_stats_summary.json    # Summary stats per subject
│   ├── fmri_group_stats_summary.*   # Group-level stats
│   └── README.md                    # fMRI instructions
```
---

## 🚀 Quickstart

1. **Clone and enter repo**

    ```bash
    git clone https://github.com/ipsissima/eigenspace.git
    cd eigenspace
    ```

2. **Set up Python environment**

    *We recommend Python 3.9+ and [virtualenv](https://virtualenv.pypa.io/en/latest/):*

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install dependencies**

    - For toy + fMRI demos:
      ```bash
      pip install numpy scipy matplotlib pandas scikit-learn
      ```
    - For LLM demo (GPT-2 / TinyStories):
      ```bash
      cd tinystories_llm_certificates_repo
      pip install -r requirements.txt
      cd ..
      ```

4. **Run the demos**

    - **Toy analytic demo**
      ```bash
      cd toy_certificate_demo
      python make_toy_certificates.py
      ```

    - **LLM / TinyStories**
      ```bash
      cd tinystories_llm_certificates_repo
      python make_certificates.py
      ```

    - **fMRI / OpenNeuro**
      ```bash
      cd openneuro_certificates
      python extract_fmri_certificates.py
      ```

---

## 📝 Citation

This repository accompanies a manuscript currently **under review**.  
**Please do not cite as a published work**. A preprint or DOI will be posted here as soon as available.

If you have questions or would like to use or extend this work, please contact:  
**Andreu Ballús Santacana**  
<andreu.ballus@uab.cat>

---

## 📄 License

All code and data in this repository are released under the [MIT License](LICENSE).

---

*For questions, issues, or collaboration requests, open an issue or contact the maintainer directly.*

