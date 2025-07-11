# audit_code.py
# COMPAS Bias Analysis using AI Fairness 360

# Install dependencies (comment out if already installed)
# !pip install aif360

import pandas as pd
import matplotlib.pyplot as plt
from aif360.datasets import CompasDataset
from aif360.metrics import BinaryLabelDatasetMetric

# Load COMPAS dataset
dataset = CompasDataset()

# Define privileged and unprivileged groups
privileged = [{'race': 'Caucasian'}]
unprivileged = [{'race': 'African-American'}]

# Create metric object
metric = BinaryLabelDatasetMetric(dataset,
                                  privileged_groups=privileged,
                                  unprivileged_groups=unprivileged)

# Print bias metrics
print("Disparate Impact Ratio:", metric.disparate_impact())
print("Mean Difference:", metric.mean_difference())

# Visualization (Base Rates by Race)
fig, ax = plt.subplots()
ax.bar(['Caucasian', 'African-American'],
       [metric.base_rate(privileged=True), metric.base_rate(privileged=False)],
       color=['skyblue', 'salmon'])
ax.set_title('Base Rates by Race')
ax.set_ylabel('Rate')
plt.tight_layout()
plt.savefig('base_rate_visualization.png')
plt.show()
