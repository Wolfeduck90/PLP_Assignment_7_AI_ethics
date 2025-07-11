# Part 2: Case Study Analysis (40%)

---

## ⚙️ Case Study 1: Biased Hiring Tool (Amazon)

### 🎯 Identifying the Source of Bias
- Training data favored male applicants due to historical hiring trends.
- Gendered language and feature selection penalized female-associated terms.
- No fairness constraints in the model design.

### ✅ Proposed Fixes
1. Rebalance the training data with diverse candidate profiles.
2. Introduce fairness-aware algorithms to reduce bias during model training.
3. Audit feature importance and remove indirect gender indicators.

### 📊 Fairness Evaluation Metrics
- **Demographic Parity** – Equal selection rates across gender groups.
- **Equal Opportunity** – Comparison of true positive rates between male and female candidates.
- **Disparate Impact Ratio** – Should fall between 0.8 and 1.25 to be considered fair.

---

## 🚓 Case Study 2: Facial Recognition in Policing

### ⚠️ Ethical Risks
- Wrongful arrests from misidentification.
- Invasion of privacy via mass surveillance.
- Reinforcement of societal bias against minority groups.
- Erosion of public trust in law enforcement and AI.

### 📜 Recommended Deployment Policies
1. **Bias Audits:** Conduct third-party evaluations regularly.
2. **Human Oversight:** Require manual verification before action.
3. **Transparency Reports:** Disclose model performance and errors.
4. **Public Consultation:** Engage communities before system deployment.
5. **Restricted Usage:** Limit application to cases with high societal benefit, like finding missing persons.

---
