import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.utils import shuffle
from scipy.linalg import subspace_angles
import matplotlib.pyplot as plt
import json

# Load data
activations = np.load('tinystories_gpt2_activations.npy')
texts = pd.read_csv('tinystories_texts.csv')
activations_centered = activations - activations.mean(axis=0)

# PCA
pca = PCA(n_components=50)
X_pca = pca.fit_transform(activations_centered)
explained_var = pca.explained_variance_ratio_
cumulative_explained = np.cumsum(explained_var)

# Save certificate files
np.save('llm_pca_components.npy', pca.components_)
np.save('llm_pca_mean.npy', activations.mean(axis=0))
np.save('llm_pca_projections.npy', X_pca)
np.save('llm_pca_explained_var.npy', explained_var)
pd.DataFrame({'num_pc': range(1, 51), 'cumulative_var': cumulative_explained[:50]}).to_csv('llm_pca_cumulative_variance.csv', index=False)

# Principal angles between half splits (stability)
inds = np.arange(activations_centered.shape[0])
inds_shuffled = shuffle(inds, random_state=42)
inds1 = inds_shuffled[:50]
inds2 = inds_shuffled[50:]
X1 = activations_centered[inds1]
X2 = activations_centered[inds2]
pca1 = PCA(n_components=9).fit(X1)
pca2 = PCA(n_components=9).fit(X2)
angles = subspace_angles(pca1.components_.T, pca2.components_.T)
angles_deg = np.degrees(angles)
np.save('llm_principal_angles_deg.npy', angles_deg)

# Plot scatter of PC1 vs PC2
plt.figure(figsize=(6,6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.7)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('TinyStories LLM Activations: First 2 PCs')
plt.grid()
plt.tight_layout()
plt.savefig('llm_pc_scatter.png')
plt.close()

# Save statistical summary as JSON
stats = {
    "num_samples": activations.shape[0],
    "activation_dim": activations.shape[1],
    "N_90_var": int(np.argmax(cumulative_explained >= 0.90) + 1),
    "N_95_var": int(np.argmax(cumulative_explained >= 0.95) + 1),
    "N_99_var": int(np.argmax(cumulative_explained >= 0.99) + 1),
    "first_10_cumulative_var": cumulative_explained[:10].tolist(),
    "principal_angles_deg": angles_deg.tolist(),
    "min_pc_angle_deg": float(np.min(angles_deg)),
    "max_pc_angle_deg": float(np.max(angles_deg)),
    "mean_pc_angle_deg": float(np.mean(angles_deg))
}
with open('stats_summary.json', 'w') as f:
    json.dump(stats, f, indent=2)

print("All files generated! See README for usage and explanation.")
