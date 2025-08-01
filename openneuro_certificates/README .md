
# OpenNeuro fMRI Certificate Extraction Supplement

This folder contains all files needed to reproduce the **empirical evaluation of spectral certificate extraction and subspace analysis** for fMRI data as described in the paper:

**"Let’s Open the Boxes: The EigenSpace Model of Semantic Processing Systems"**

---

## Folder Contents

### **Per-Subject Outputs (for sub-01, sub-02, sub-03):**
- `sub-XX_fmri_matrix.npy`  
  - Voxelwise fMRI activation matrix (`n_timepoints x n_voxels`) for subject XX.
- `sub-XX_pca_mean.npy`  
  - Mean signal vector used for centering.
- `sub-XX_pca_components.npy`  
  - Top 50 PCA spatial components (basis for certificate extraction).
- `sub-XX_pca_projections.npy`  
  - Subject timecourses projected onto PCA basis (`n_timepoints x 50`).
- `sub-XX_pca_explained_var.npy`  
  - Variance explained by each of the 50 PCs.
- `sub-XX_pca_cumulative_variance.png`  
  - Plot: Cumulative explained variance vs. number of PCs.
- `sub-XX_stats_summary.json`  
  - Certificate and subspace summary: n_samples, n_voxels, certificate size (N) for 90/95/99% variance, etc.

### **Group Outputs**
- `fmri_group_stats_summary.csv` / `fmri_group_stats_summary.json`  
  - Table and JSON of per-subject summary stats (for easy aggregation and plotting).

---

## How to Reproduce Results

**All results were generated using the script `extract_fmri_certificates.py`** (included in this folder).  
To replicate or extend these results:

1. Install dependencies:
    ```
    pip install numpy matplotlib scikit-learn nilearn nibabel pandas
    ```
2. Ensure your folder structure matches OpenNeuro BIDS conventions (sub-01/func/...).
3. Run the script on any subject(s). Outputs will match those in this folder.

**Analysis steps:**
- Each subject’s bold images were masked and vectorized using `nilearn`.
- Data were mean-centered, PCA applied, and the top 50 PCs retained.
- Certificate size (minimal N for 90/95/99% explained variance) and plots were generated per subject.
- Group summary statistics are provided for easy comparison and reporting.

---

## File Naming Conventions

- `sub-XX_*` → Files for subject XX (e.g., sub-01)
- `_pca_*`  → PCA-derived outputs (basis, projections, explained variance)
- `_stats_summary.json` → Summary stats for certificate size and explained variance
- `_cumulative_variance.png` → Plot of cumulative variance (as in main paper)

---

## Software and Data Versions

- **nilearn** version: 0.10+  
- **scikit-learn** version: 1.2+  
- **OpenNeuro dataset**: [Provide accession number or DOI here]
- **Python** version: 3.9–3.11 (Colab and local)

---

## Contact

Questions or reproducibility issues?  
Contact: [Your Name & Email]

---

## Citation

If using this data or pipeline, please cite:
- [Your paper’s citation or preprint]
- OpenNeuro dataset: [DOI/accession]

---
