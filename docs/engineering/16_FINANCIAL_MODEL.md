# 16. Financial Model

## 1. Purpose
This document isolates the mathematical logic and domain constraints for the financial calculations. It ensures that backend developers implement the mathematics uniformly and avoid floating-point inaccuracies.

## 2. Scope
Pertains specifically to the calculation of compounding growth, amortization, and net worth aggregation.

## 3. Definitions
* **Basis Points (BPS):** 1/100th of 1%. Used to prevent floating-point errors.
* **Integer Math:** All financial values must be stored in the smallest currency unit (Paise for INR, Cents for USD). `₹500` is stored as `50000`.

## 4. The Mathematical Models

### 4.1 Asset Compounding Model (Discrete Monthly)
The formula to calculate the new value of an asset subject to monthly interest:
$$ A_{t} = A_{t-1} \times (1 + r_m) $$
Where:
* $A_t$ = Asset value at current month.
* $A_{t-1}$ = Asset value from previous month.
* $r_m$ = Monthly interest rate (Annual Rate / 12).

**Implementation Note:** In code, use `Math.floor(balance * rateMultiplier)` to prevent fractional paise.

### 4.2 Debt Amortization Model
For fixed term loans, the standard EMI deduction is applied. However, for revolving credit (Credit Cards), the balance compounds:
$$ D_{t} = (D_{t-1} - P_t) \times (1 + c_m) $$
Where:
* $D_{t-1}$ = Previous debt balance.
* $P_t$ = Payment made by player this month.
* $c_m$ = High-interest monthly rate (e.g., 3%).

### 4.3 Net Worth Aggregation
$$ NW = Cash + \sum Assets - \sum Liabilities $$

## 5. System Guardrails
* **No Negative Assets:** An asset value cannot drop below 0.
* **No Negative Cash (Without Penalty):** The engine MUST catch `Cash < 0` during the deduction phase. It must immediately transfer the absolute value of the negative cash into the `creditCard` liability bucket, resetting `Cash` to `0`.

## 6. References
* [06_BUSINESS_RULES.md](06_BUSINESS_RULES.md)
* [07_SIMULATION_ENGINE.md](07_SIMULATION_ENGINE.md)

## 7. Future Considerations
Integration of complex derivative modeling (Options/Futures) or localized real estate depreciation is reserved for post-internship roadmap expansions.
