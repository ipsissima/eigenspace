
# extract_fmri_certificates.py
# Usage: python extract_fmri_certificates.py --folder PATH --subjects sub-01 sub-02 sub-03
import os
import numpy as np
import matplotlib.pyplot as plt
import json
from sklearn.decomposition import PCA
from nilearn import image, masking
import argparse
import pandas as pd

def run_certificate_pipeline(folder, subjects):
    summary_list = []
    for sub in subjects:
        print(f"Processing {sub}...")
        func_dir = os.path.join(folder, sub, 'func')
        func_files = sorted([f for f in os.listdir(func_dir) if f.endswith('.nii.gz')])
        if not func_files:
            print(f"No functional images found for {sub} in {func_dir}. Skipping.")
            continue
        func_path = os.path.join(func_dir, func_files[0])
        img = image.load_img(func_path)
        mask = masking.compute_epi_mask(img)
        fmri_matrix = masking.apply_mask(img, mask)
        np.save(os.path.join(folder, f"{sub}_fmri_matrix.npy"), fmri_matrix)

        # Center and PCA
        fmri_mean = fmri_matrix.mean(axis=0)
        fmri_centered = fmri_matrix - fmri_mean
        pca = PCA(n_components=50)
        fmri_pca = pca.fit_transform(fmri_centered)
        explained_var = pca.explained_variance_ratio_
        cumvar = np.cumsum(explained_var)

        # Save outputs
        np.save(os.path.join(folder, f"{sub}_pca_components.npy"), pca.components_)
        np.save(os.path.join(folder, f"{sub}_pca_mean.npy"), fmri_mean)
        np.save(os.path.join(folder, f"{sub}_pca_projections.npy"), fmri_pca)
        np.save(os.path.join(folder, f"{sub}_pca_explained_var.npy"), explained_var)

        # Plot cumulative variance
        plt.plot(np.arange(1,51), cumvar[:50], 'o-')
        plt.axhline(0.90, color='r', ls='--', label='90% variance')
        plt.xlabel('# PCs')
        plt.ylabel('Cumulative variance')
        plt.title(f'{sub} fMRI PCA Cumulative Variance')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(folder, f"{sub}_pca_cumulative_variance.png"))
        plt.close()

        # Save per-subject stats
        summary = {
            "subject": sub,
            "num_samples": int(fmri_matrix.shape[0]),
            "num_voxels": int(fmri_matrix.shape[1]),
            "N_90_var": int(np.argmax(cumvar >= 0.90) + 1),
            "N_95_var": int(np.argmax(cumvar >= 0.95) + 1),
            "N_99_var": int(np.argmax(cumvar >= 0.99) + 1),
            "cumvar_first_10": [float(x) for x in cumvar[:10]]
        }
        summary_list.append(summary)
        with open(os.path.join(folder, f"{sub}_stats_summary.json"), 'w') as f:
            json.dump(summary, f, indent=2)

    # Group summary
    if summary_list:
        df = pd.DataFrame(summary_list)
        df.to_csv(os.path.join(folder, "fmri_group_stats_summary.csv"), index=False)
        with open(os.path.join(folder, "fmri_group_stats_summary.json"), 'w') as f:
            json.dump(summary_list, f, indent=2)
    print("All subject results and group summary saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=str, required=True, help="Path to OpenNeuro BIDS folder")
    parser.add_argument('--subjects', nargs='+', required=True, help="List of subject IDs (e.g., sub-01 sub-02)")
    args = parser.parse_args()
    run_certificate_pipeline(args.folder, args.subjects)
