def classify_intent(sentence):
    # Convert to lowercase so "Block" and "block" both work
    sentence = sentence.lower()
    
    # CARD_BLOCK keywords
    if "block" in sentence or "harayo" in sentence or "choryo" in sentence:
        return "CARD_BLOCK"
    
    # BALANCE_INQUIRY keywords
    elif "paisa" in sentence or "balance" in sentence or "kati cha" in sentence:
        return "BALANCE_INQUIRY"
    
    # FUND_TRANSFER keywords
    elif "transfer" in sentence or "pathau" in sentence or "patha" in sentence:
        return "FUND_TRANSFER"
    
    # VIEW_STATEMENT keywords
    elif "statement" in sentence or "history" in sentence or "transaction" in sentence:
        return "VIEW_STATEMENT"
    
    # CUSTOMER_SUPPORT keywords
    elif "help" in sentence or "problem" in sentence or "support" in sentence or "issue" in sentence:
        return "CUSTOMER_SUPPORT"
    
    # If nothing matches
    else:
        return "UNKNOWN"


# Test it
sentences = [
    "Mero card block garnu cha",
    "Mero balance kati cha?",
    "5000 rupees transfer garnu cha",
    "Last month ko statement chahiyo",
    "Help chahiyo mero account ma problem cha",
    "Kasto mausam cha aaja",   # unrelated
]

for s in sentences:
    result = classify_intent(s)
    print(f"Input:  {s}")
    print(f"Intent: {result}")
    print("-" * 40)