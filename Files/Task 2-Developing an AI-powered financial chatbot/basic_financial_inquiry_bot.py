def financial_chatbot(query):
    responses = {
        "net income": "The net income for the fiscal year 2021 was $5 billion, a 10% increase from 2020.",
        "revenue growth": "The revenue grew by 8% from 2020 to 2021, reaching $22 billion."
    }
    return responses.get(query.lower(), "I'm not sure how to answer that. Can you try a different question?")