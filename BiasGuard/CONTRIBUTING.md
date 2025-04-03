# 🤝 Contributing to BiasGuard

Thank you for your interest in contributing to **BiasGuard** — the indispensable trust layer for responsible AI.

Whether you're a developer, legal expert, researcher, DEIA advocate, or concerned citizen, we welcome your ideas, code, and voice.

---

## 🧱 What You Can Contribute

| Role | Contribution Ideas |
|------|---------------------|
| 🛠 Developers | Write and test YAML rules for detecting bias, chaining, or lack of attribution |
| ⚖️ Legal / Policy Experts | Help translate laws (EEOC, GDPR, Title VI) into enforceable rule clauses |
| 🧠 Researchers | Prototype rules in academic or testing contexts |
| 🌱 Social Advocates | Suggest bias types or harm categories we may have missed |
| 📚 Translators | Help adapt rules for global/regional use cases |
| 🖋️ Writers | Improve documentation, onboarding, and rule clarity |

---

## 🧰 Getting Started

1. **Fork the repository**  
2. Create a new branch: `feature/my-new-rule`  
3. Add your rule under `/rules/` following our taxonomy  
4. Run `scripts/lint-rule.py` to validate  
5. Submit a Pull Request with a short description

Need help with YAML structure or clause mapping? See our docs under `/docs/` or join our next community call.

---

## 🧪 Rule Example (Basic YAML)

```yaml
id: warn/unattributed-output
description: Flags text generations that use content from external sources without attribution
applies_to: [text-generation]
severity: medium
references:
  - "GDPR Art. 5 – Transparency"
  - "Creative Commons 4.0"
