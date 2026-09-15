import yfinance as yf
import pandas as pd
import os


def get_financial_statements(ticker_symbol):
    # Add .NS for NSE companies as yfinance uses this suffix for Indian stocks
    ticker = ticker_symbol.upper().strip()

    if not ticker.endswith(".NS"):
        ticker = ticker + ".NS"

    print(f"\nFetching financial statements for {ticker}...")

    # Create yfinance ticker object
    company = yf.Ticker(ticker)

    # Get financial statements
    income_statement = company.financials
    balance_sheet = company.balance_sheet
    cash_flow = company.cashflow

    # Check if data was received
    if income_statement.empty and balance_sheet.empty and cash_flow.empty:
        print("No financial data found.")
        print("Please check whether the ticker symbol is correct.")
        return

    # Remove .NS from filename
    company_name = ticker.replace(".NS", "")

    # Create Excel filename
    file_name = f"{company_name} Financial Statements.xlsx"

    # Create Excel workbook
    with pd.ExcelWriter(file_name, engine="openpyxl") as writer:

        # Income Statement
        if not income_statement.empty:
            income_statement.to_excel(
                writer,
                sheet_name="Income Statement"
            )

        # Balance Sheet
        if not balance_sheet.empty:
            balance_sheet.to_excel(
                writer,
                sheet_name="Balance Sheet"
            )

        # Cash Flow Statement
        if not cash_flow.empty:
            cash_flow.to_excel(
                writer,
                sheet_name="Cash Flow Statement"
            )

    print(f"\nFinancial statements successfully extracted!")
    print(f"Excel file created: {os.path.abspath(file_name)}")



# Main program 


print("========================================")
print(" NSE COMPANY FINANCIAL STATEMENT TOOL")
print("========================================")

ticker_symbol = input(
    "\nEnter NSE ticker symbol (Example: DMART, TCS, RELIANCE): "
)

get_financial_statements(ticker_symbol)