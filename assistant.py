from retriever import retrieve_rules
import json

def corep_assistant(question: str, scenario: dict):

    # Step 1: Retrieve regulatory rules
    retrieved_docs = retrieve_rules(question)

    rule_refs = []
    for doc in retrieved_docs:
        rule_refs.append(doc.page_content.strip())

    # Step 2: Interpret scenario (controlled logic for prototype)
    retained_earnings = scenario.get("retained_earnings")
    common_shares = scenario.get("common_shares")

    fields = []

    if common_shares is not None:
        fields.append({
            "row": "020",
            "label": "Common shares",
            "column": "010",
            "value": common_shares,
            "unit": "GBP",
            "justification": [
                "CRR Article 26(1)(a)",
                "CRR Article 28",
                "COREP C01 Row 020"
            ]
        })

    if retained_earnings is not None:
        fields.append({
            "row": "030",
            "label": "Retained earnings",
            "column": "010",
            "value": retained_earnings,
            "unit": "GBP",
            "justification": [
                "CRR Article 26(1)(c)",
                "COREP C01 Row 030"
            ]
        })

    # Step 3: Aggregate CET1
    total_cet1 = sum(
        f["value"] for f in fields if f["row"] in ["020", "030"]
    )

    fields.append({
        "row": "060",
        "label": "Total Common Equity Tier 1 capital",
        "column": "010",
        "value": total_cet1,
        "unit": "GBP",
        "justification": [
            "COREP C01 Row 060 (sum of CET1 components)"
        ]
    })

    # Final structured output
    output = {
        "template": "C_01.00",
        "fields": fields,
        "retrieved_rules_used": rule_refs
    }

    return output


# ---------------- DEMO RUN ----------------
if __name__ == "__main__":
    question = "How should retained earnings be reported in CET1?"
    scenario = {
        "common_shares": 120000000,
        "retained_earnings": 80000000,
        "interim_profits": 0
    }

    result = corep_assistant(question, scenario)
    print(json.dumps(result, indent=2))