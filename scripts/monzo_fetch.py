#!/usr/bin/env python3
"""
Monzo Transaction Fetcher - Money v1 MVP
Securely fetches daily transactions from Monzo API and stores them locally.

Security Notes:
- Never hard-code access tokens
- Use environment variables for sensitive data
- Run locally; never expose secrets in notebooks or web

Requirements: pip install requests pandas python-dotenv

Usage:
1. Set environment variable: export MONZO_ACCESS_TOKEN=your_token_here
   Or use the env_manager.py script: python scripts/env_manager.py --set MONZO_ACCESS_TOKEN your_token
2. Run: python scripts/monzo_fetch.py
3. Data saved to /data/transactions.csv
"""

import requests
import pandas as pd
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Security: Get token from environment, never hard-code
MONZO_TOKEN = os.getenv('MONZO_ACCESS_TOKEN')
if not MONZO_TOKEN:
    print("ERROR: MONZO_ACCESS_TOKEN environment variable not set.")
    print("Get your token from: https://developers.monzo.com/")
    exit(1)

# API headers with secure token
headers = {
    'Authorization': f'Bearer {MONZO_TOKEN}'
}

def fetch_accounts():
    """Fetch user accounts from Monzo API."""
    url = 'https://api.monzo.com/accounts'
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Handle API errors
    return response.json()['accounts']

def fetch_transactions(account_id):
    """Fetch transactions for a specific account."""
    url = f'https://api.monzo.com/transactions?account_id={account_id}'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['transactions']

def categorize_transaction(description):
    """
    Basic categorization based on transaction description.
    Beginner-friendly: simple keyword matching.
    """
    desc_lower = description.lower()

    # Housing & bills
    if any(word in desc_lower for word in ['rent', 'mortgage', 'utility', 'electric', 'gas', 'water', 'internet']):
        return 'housing'

    # Food & dining
    elif any(word in desc_lower for word in ['food', 'restaurant', 'grocery', 'cafe', 'coffee', 'meal']):
        return 'food'

    # Transportation
    elif any(word in desc_lower for word in ['uber', 'taxi', 'bus', 'train', 'fuel', 'parking']):
        return 'transport'

    # Entertainment & fun
    elif any(word in desc_lower for word in ['cinema', 'game', 'spotify', 'netflix', 'entertainment', 'fun']):
        return 'entertainment'

    # Shopping
    elif any(word in desc_lower for word in ['amazon', 'shopping', 'store', 'clothes', 'book']):
        return 'shopping'

    # Health
    elif any(word in desc_lower for word in ['pharmacy', 'doctor', 'health', 'gym']):
        return 'health'

    # Income
    elif any(word in desc_lower for word in ['salary', 'income', 'deposit', 'transfer in']):
        return 'income'

    else:
        return 'other'

def main():
    """Main function to fetch and process transactions."""
    try:
        # Fetch accounts
        accounts = fetch_accounts()
        if not accounts:
            print("No accounts found.")
            return

        # Use the first account (typically current account)
        account_id = accounts[0]['id']
        print(f"Fetching transactions for account: {accounts[0]['description']}")

        # Fetch transactions
        transactions = fetch_transactions(account_id)

        if not transactions:
            print("No transactions found.")
            return

        # Convert to DataFrame
        df = pd.DataFrame(transactions)

        # Add fetch timestamp
        df['fetched_at'] = datetime.now()

        # Add categorization
        df['category'] = df['description'].apply(categorize_transaction)

        # Ensure data directory exists
        data_dir = '/data'
        os.makedirs(data_dir, exist_ok=True)

        # Append to CSV (create if doesn't exist)
        csv_path = os.path.join(data_dir, 'transactions.csv')

        if os.path.exists(csv_path):
            # Read existing data and append
            existing_df = pd.read_csv(csv_path)
            combined_df = pd.concat([existing_df, df], ignore_index=True)
            # Remove duplicates based on transaction id
            combined_df = combined_df.drop_duplicates(subset=['id'], keep='last')
            combined_df.to_csv(csv_path, index=False)
            print(f"Appended {len(df)} transactions. Total: {len(combined_df)}")
        else:
            # Create new file
            df.to_csv(csv_path, index=False)
            print(f"Created new CSV with {len(df)} transactions")

        print(f"Data saved to {csv_path}")

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()