from agents import Agent, Runner
from connection import config

# Create a specialized banking agent.
banking_agent: Agent = Agent(
    name="BankAgent",
    instructions="""You are an AI assistant for a bank. Your purpose is to help customers with common banking inquiries.
    You can:
    - Check an account balance.
    - Provide information on recent transactions.
    - Explain different banking services (e.g., checking accounts, savings accounts, loans).
    - Answer general questions about banking hours and locations.

    Your responses should be polite, professional, and helpful. Always remind the user that for sensitive information, they should contact a human representative directly.
    """
)

# --- Example 1: Check account balance (simulated) ---
print("--- Example 1: Checking a balance ---")
balance_inquiry = "What is my current account balance?"
result_balance = Runner.run_sync(banking_agent, balance_inquiry, run_config=config)
print(result_balance.final_output)

# --- Example 2: Inquire about a transaction (simulated) ---
print("\n--- Example 2: Asking about a transaction ---")
transaction_inquiry = "Tell me about my most recent transaction."
result_transaction = Runner.run_sync(banking_agent, transaction_inquiry, run_config=config)
print(result_transaction.final_output)

# --- Example 3: Ask about banking services ---
print("\n--- Example 3: Getting information on services ---")
services_inquiry = "Can you explain the different types of loans you offer?"
result_services = Runner.run_sync(banking_agent, services_inquiry, run_config=config)
print(result_services.final_output)


