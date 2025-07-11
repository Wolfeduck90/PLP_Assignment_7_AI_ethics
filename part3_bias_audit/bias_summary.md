# COMPAS Dataset Bias Audit Summary

## 📊 Key Findings

Using IBM’s AI Fairness 360 toolkit, the COMPAS dataset was analyzed to detect racial bias in recidivism risk scores.

- **Disparate Impact Ratio:** Found below the fairness threshold (<0.8), indicating disproportionate high-risk labeling for African-American individuals.
- **Mean Difference:** Highlighted unfair penalization patterns across racial groups.
- **Base Rate Visualization:** Showed significantly higher base rates for unprivileged groups.

## 🛠️ Remediation Strategies

1. **Preprocessing Fixes**
   - Reweighting or sampling to create balanced datasets.
2. **In-Training Fairness Enhancements**
   - Use algorithms like adversarial debiasing or reject option classification.
3. **Post-processing Adjustments**
   - Recalibrate risk scores to improve predictive parity and equal opportunity.

## 💡 Conclusion

AI systems in criminal justice must be rigorously audited for fairness to ensure ethical deployment. This analysis underlines the importance of transparent, inclusive data practices and continued monitoring.
