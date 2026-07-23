# 17. Time Model

## 1. Purpose
This document defines how time is represented, tracked, and abstracted within the simulator.

## 2. Scope
Time modeling applies to the user's age, the tick progression, and the maturity of certain financial instruments.

## 3. Definitions
* **Simulation Epoch:** Month 1 (The starting month of the simulation).
* **Tick:** 1 Month of simulated time.

## 4. The Time Abstraction

To ensure users experience the consequences of long-term compounding, the game operates on a vastly accelerated timeline:

*   **Real World:** 1 Week (Assuming standard open-source async play sessions).
*   **Game World:** 1 Month.

However, from an *engineering* standpoint, time is simply an integer `currentMonth` that increments by `1` during every API call to `/advance-month`.

## 5. Time-Triggered Mechanisms

Several business rules are tied directly to the `currentMonth` integer using modulo arithmetic:

### 5.1 Annual Events (Modulo 12)
Every time `currentMonth % 12 === 0`, the Engine must trigger:
1.  **Income Tax Calculation:** Deduct tax based on the accumulated income of the past 12 months.
2.  **Salary Increment:** Increase the base monthly salary by a fixed percentage (e.g., 5%).
3.  **Age Increment:** Increase the `simulatedAgeYears` by 1.

### 5.2 Retirement (Hard Stop)
The simulation enforces a hard stop when `simulatedAgeYears` reaches `60`.
At this point, the `/advance-month` API will reject requests, returning a status of `RETIRED`. The frontend will lock the decision inputs and display the final End-of-Life report.

## 6. References
* [06_BUSINESS_RULES.md](06_BUSINESS_RULES.md)
* [07_SIMULATION_ENGINE.md](07_SIMULATION_ENGINE.md)

## 7. Future Considerations
If macro-economic cycles (Boom/Bust) are introduced, they will require a Global Time Model, mapping specific server days to specific economic conditions, rather than having time exist only relative to the individual player's tick count.
