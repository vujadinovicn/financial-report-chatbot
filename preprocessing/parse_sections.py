#ebay

def get_items_to_extract(company_name):
    if company_name == "EBAY INC":
        return {
            "item1": ("Item 1:", "Item 1A:"),
            "item1a": ("Item 1A:", "Item 1B:"),
            "item7": ("Item 7:", "Item 7A:"),
            "item7a": ("Item 7A:", "Item 8:")
        }

    if company_name == "BOEING CO" or company_name == "AIRBNB INC" or company_name == "CHEVRON CORP" \
        or company_name == "JOHNSON & JOHNSON INC" or company_name == "UBER TECHNOLOGIES INC" or company_name == "NVIDIA CORP":
            return {
                    "item1": ("Item 1. Business", "Item 1A. Risk Factors"),
                    "item1a": ("Item 1A. Risk Factors", "Item 1B. Unresolved Staff Comments"),
                    "item7": ("Item 1B. Unresolved Staff Comments", "Item 7. Manage"),
                    "item7a": ("Item 7A. Quantitative and Qualitative Disclosures About Market Risk", "Item 8. Financial Statements and Supplementary Data")
                }

    if company_name == "WALMART INC COM" or company_name == "PFIZER INC COM" or company_name == "ALPHABET INC":
        return {
                "item1": ("ITEM 1.", "ITEM 1A."),
                "item1a": ("ITEM 1A.", "ITEM 1B."),
                "item7": ("ITEM 7.", "ITEM 7A."),
                "item7a": ("ITEM 7A.", "ITEM 8.")
            }

    if company_name == "PEPSI CO":
        return {
                "item1": ("Item 1.  Business.", "Item 1A.  Risk Factors."),
                "item1a": ("Item 1A.  Risk Factors.", "Item 1B.  Unresolved Staff Comments."),
                "item7": ("Item 7.  Management's Discussion and Analysis of Financial Condition and Results of Operations.", "Item 7A.  Quantitative and Qualitative Disclosures About Market Risk."),
                "item7a": ("Item 7A.  Quantitative and Qualitative Disclosures about Market Risk.", "Item 8.  Financial Statements and Supplementary Data.")
            }

    if company_name == "NETFLIX INC COM" or company_name == "META PLATFORMS":
        return {
                "item1": ("Item 1.", "Item 1A."),
                "item1a": ("Item 1A.", "Item 1B."),
                "item7": ("Item 7.", "Item 7A."),
                "item7a": ("Item 7A.", "Item 8.")
            }

    if company_name == "COCA COLA CO":
        return {
                "item1": ("ITEM 1.  BUSINESS", "ITEM 1A.  RISK FACTORS"),
                "item1a": ("ITEM 1A.  RISK FACTORS", "ITEM 1B.  UNRESOLVED STAFF COMMENTS"),
                "item7": ("ITEM 7.  MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS", "ITEM 7A.  QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK"),
                "item7a": ("ITEM 7A.  QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "ITEM 8.  FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA")
            }

    if company_name == "WALMART INC COM":
        return {
                "item1": ("ITEM 1. Business.", "ITEM 1A. Risk Factors."),
                "item1a": ("ITEM 1A. Risk Factors.", "ITEM 1B. Unresolved Staff Comments."),
                "item7": ("ITEM 7. Management's Discussion and Analysis of Financial Condition and Results of Operations.", "ITEM 7A. Quantitative and Qualitative Disclosures about Market Risk."),
                "item7a": ("ITEM 7A. Quantitative and Qualitative Disclosures about Market Risk.", "ITEM 8. Financial Statements and Supplementary Data.")
            }

    if company_name == "AMERICAN EXPRESS CO COM":
        return {
                "item1": ("ITEM 1.    BUSINESS", "ITEM 1A.    RISK FACTORS"),
                "item1a": ("ITEM 1A.    RISK FACTORS", "ITEM 1B."),
                "item7": ("ITEM 7.    ", "ITEM 7A.    QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK"),
                "item7a": ("ITEM 7A.    QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK", "ITEM 8.    FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA")
            }