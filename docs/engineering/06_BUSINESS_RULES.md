# 06. Business Rules

## 1. Purpose
This document codifies the strict mathematical and conditional logic that dictates how the `SimulationEngine` operates. These rules are sourced directly from the NCFE handbooks.

## 2. Scope
Applies exclusively to the backend `Engine` layer. These rules MUST have 100% test coverage.

## 3. Definitions
* **Tick:** The advancement of one Simulated Month.
* **EMI:** Equated Monthly Installment.
* **SIP:** Systematic Investment Plan.

## 4. The Rules

### 4.1 Time Rules
* **Rule TIME-01:** 1 User Action (Advance Month) = 1 Simulated Month.
* **Rule TIME-02:** 12 Simulated Months = 1 Simulated Year.

### 4.2 Salary & Income Rules
* **Rule INC-01:** Salary is credited at the beginning of the tick, before any expenses are deducted.
* **Rule INC-02:** Annual increments (e.g., 5% raise) are applied only on month 13, 25, 37, etc.

### 4.3 Expense & Budget Rules
* **Rule EXP-01:** Mandatory fixed expenses (Rent, Utilities) are deducted immediately after income is credited.
* **Rule EXP-02 (Auto-Debt):** If `Cash` falls below `0` after mandatory expenses, the negative balance is automatically converted into High-Interest Credit Card Debt (Liability).

### 4.4 Liability & Debt Rules
* **Rule LIA-01:** Standard EMIs (e.g., Student Loan) are deducted fixed amounts.
* **Rule LIA-02 (Credit Debt Compound):** Unpaid credit card balances compound at a fixed rate of 3% per month (equivalent to ~36% APR). The formula is: `NewBalance = OldBalance * 1.03`.

### 4.5 Asset & Investment Rules
* **Rule AST-01 (Fixed Deposits):** FDs grow at a guaranteed 7.2% annually, applied monthly as `0.6%`. `NewBalance = OldBalance * 1.006`.
* **Rule AST-02 (Equities):** Equities/SIPs grow based on a randomized monthly return ranging from `-5.0%` to `+6.0%`, mimicking high volatility but upward long-term trends.

### 4.6 Tax Rules (Simplified Indian Context)
* **Rule TAX-01:** Income tax is calculated and deducted annually (every 12th month) based on the total income accumulated over the past 12 months.
* **Rule TAX-02:** (Simplified Regime) 
  * 0 to ₹3 Lakhs: 0%
  * ₹3L to ₹6L: 5%
  * ₹6L to ₹9L: 10%
  * ₹9L+: 15%

### 4.7 Game Over Rules
* **Rule END-01 (Bankruptcy):** If `Cash` < 0 AND `Total Debt` > `Total Assets * 1.5`, the user is declared bankrupt. Simulation locked.
* **Rule END-02 (Retirement):** If `Simulated Age` reaches `60`, the simulation ends successfully.

## 5. References
* `docs/research/Books/`
* [07_SIMULATION_ENGINE.md](07_SIMULATION_ENGINE.md)

## 6. Future Considerations
Future phases may introduce complex tax deduction rules (Section 80C) and dynamic interest rates tied to a simulated Reserve Bank of India (RBI).
