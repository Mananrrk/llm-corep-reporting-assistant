# LLM-Assisted PRA COREP Reporting Assistant (Prototype)

## Overview
This project is a proof-of-concept **LLM-assisted regulatory reporting assistant** designed to support UK banks preparing **PRA COREP regulatory returns**.

The prototype focuses on a **narrow, well-scoped subset of COREP**—specifically **Template C 01.00 (Own Funds – CET1)**—and demonstrates how natural-language questions and simple reporting scenarios can be translated into **structured, auditable COREP outputs** using regulatory text retrieval and rule-based reasoning.

---

## Problem Statement
Preparing COREP returns is labour-intensive and error-prone due to:
- Complex PRA Rulebook and COREP instructions
- Frequent regulatory updates
- Manual interpretation and mapping to template fields

This prototype demonstrates how an **LLM-assisted workflow** can:
- Retrieve relevant regulatory guidance
- Map it to COREP template structures
- Produce structured outputs with clear audit justification

---

## Scope (Prototype)
- **Template:** COREP C 01.00 – Own Funds  
- **Capital Type:** Common Equity Tier 1 (CET1)  
- **Jurisdiction:** UK PRA (CRR-based)  
- **Status:** Proof of Concept (PoC)

Out of scope:
- Full COREP coverage
- XBRL generation
- Production-grade validation

---


---

## How It Works

1. A user provides:
   - A natural-language reporting question
   - A simple reporting scenario (e.g. capital values)

2. Relevant PRA Rulebook and COREP instructions are retrieved.

3. The system maps scenario data to COREP C 01.00 rows:
   - Common shares
   - Retained earnings
   - Total CET1

4. A **structured JSON output** is generated with:
   - COREP row and column references
   - Monetary values
   - Rule-level justifications

---

## Example Output

The generated COREP JSON is saved to:

Example (excerpt):

```json
{
  "template": "C_01.00",
  "fields": [
    {
      "row": "030",
      "label": "Retained earnings",
      "column": "010",
      "value": 80000000,
      "unit": "GBP",
      "justification": [
        "CRR Article 26(1)(c)",
        "COREP C01 Row 030"
      ]
    }
  ]
}
```
## 👨‍💻 AUTHOR

**Manan Goyal**  
🎓 B.Tech CSE | Bennett University  
📧 Email: [mananmlzs@gmail.com](mailto:mananmlzs@gmail.com)  
📱 Phone: +91-7895297561  
🔗 [LinkedIn](https://www.linkedin.com/in/mananrrk/)  
💻 [GitHub](https://github.com/Mananrrk) 
