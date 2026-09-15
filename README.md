# DMart Financial Statement & Ratio Analysis

An end-to-end financial analysis project on **Avenue Supermarts Ltd. (NSE: DMART)**, covering FY2022–FY2026. The project has two parts: a Python tool that extracts financial statements for any NSE-listed company, and a formula-driven Excel model that turns DMart's data into a full ratio analysis with a written verdict.

## Why this project

Most student finance projects stop at "here are some ratios." This one is built to answer the question an actual analyst has to answer: **is the company getting healthier or weaker, and why?** That means:
- A one-paragraph analyst verdict, not just a table of numbers
- A DuPont ROE decomposition that cross-checks against the reported ROE, to prove the math is internally consistent
- Explicit "strengths vs. areas to watch," rather than one-sided commentary
- Honest limitations (e.g., no market-value ratios, since live share price data wasn't used)

## Project structure

```
├── main.py                  # Extracts financial statements for any NSE ticker via yfinance
├── requirements.txt
├── DMART_Financial_Statement_Ratio_Analysis.xlsx   # The analysis workbook
└── README.md
```

## How it works

1. **`main.py`** — Run it, enter any NSE ticker (e.g. `DMART`, `TCS`, `RELIANCE`), and it pulls the Income Statement, Balance Sheet, and Cash Flow Statement via the [yfinance](https://pypi.org/project/yfinance/) API and writes them to a formatted Excel workbook. This automates the manual copy-paste from sources like Screener.in.
2. **The analysis workbook** — DMart's data (sourced from Screener.in and its annual reports, FY22–FY26) was structured into a formula-linked model with:
   - **Cover** — project overview
   - **Summary** — executive verdict, FY26 snapshot, DuPont ROE bridge, strengths/watch-items
   - **Assumption** — every formula and assumption used, documented and sourced
   - **Ratio Analysis** — profitability, liquidity, leverage, efficiency ratios, plus a Baumol optimal cash balance model and DOL/DFL/DCL leverage analysis
   - **Analysis** — key observations with supporting charts
   - **Profit & Loss / Balance Sheet / Cashflow Statement** — the underlying 5-year financials

All ratios are live Excel formulas referencing the source statements — nothing is hardcoded, so the model recalculates if the underlying figures are updated.

## Key findings (FY26)

- Revenue more than doubled over FY22–FY26 (₹30,976 Cr → ₹68,821 Cr), but growth has decelerated (38% in FY23 → 16% in FY26)
- ROCE and ROE both peaked in FY23 (14.3% / 14.8%) and have since declined to 11.5% / 12.1%
- Leverage remains very low (Debt-to-Equity 0.10x, Interest Coverage 29.7x) — no signs of financial distress
- Liquidity has thinned materially (Current Ratio 3.7x → 2.0x; Cash Ratio 0.96x → 0.08x), alongside DMart's first use of short-term borrowings

Full detail and interpretation is in the workbook's **Summary** and **Analysis** sheets.

## Running the extraction tool

```bash
pip install -r requirements.txt
python main.py
```

You'll be prompted for a ticker symbol; the output Excel file is written to `output/<TICKER>_Financial_Statements.xlsx`.

## Limitations

- Market Value Ratios (P/E, P/B, EV/EBITDA) are excluded — this project does not incorporate live market price data
- This is a financial statement and ratio analysis exercise, not a valuation model or an investment recommendation
- `main.py` currently assumes NSE-listed companies (`.NS` suffix); other exchanges require passing the correct Yahoo Finance suffix manually

## Author

**Mihir** — CMA Intermediate student, ICMAI
