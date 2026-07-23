# 14. Event Engine

## 1. Purpose
This document outlines the architecture for generating random financial hazards (shocks) during the simulation. These events are crucial for teaching resilience and the value of emergency funds.

## 2. Scope
Defines the structure of static events pulled from the NCFE research (specifically the *BEAWARE Modus Operandi of Financial Fraudsters* book). Generative AI events are explicitly out of scope for the MVP.

## 3. Definitions
* **Event Dictionary:** A static JSON array or database table containing all possible events.
* **RNG:** Random Number Generator.

## 4. Event Dictionary Structure

Events are heavily categorized by archetype. A "Tractor Repair" event applies to a Farmer, while a "Laptop Repair" applies to a Student.

```json
[
  {
    "eventId": "EVT_001",
    "targetArchetype": ["ALL"],
    "title": "Medical Emergency",
    "description": "You suffered a minor fracture. Without comprehensive health insurance, you must pay out of pocket.",
    "financialImpact": {
      "cashDeduction": 15000
    },
    "probabilityWeight": 0.05
  },
  {
    "eventId": "EVT_002",
    "targetArchetype": ["NEW_ENTRANT", "STUDENT"],
    "title": "QR Code Phishing Scam",
    "description": "You scanned a fake QR code on a second-hand marketplace. Money was deducted from your account.",
    "financialImpact": {
      "cashDeduction": 5000
    },
    "probabilityWeight": 0.02
  }
]
```

## 5. Event Trigger Logic

During the Engine pipeline, the Event module rolls a pseudo-random number (0 to 1).
* **Step 1:** Check if `Roll < 0.10` (10% chance an event happens this month).
* **Step 2:** If true, filter the Event Dictionary to match the user's `Archetype`.
* **Step 3:** Select an event based on weighted probability.
* **Step 4:** Deduct the `cashDeduction` from the user's `Cash` balance. (If Cash goes below 0, it auto-converts to Credit Debt as per Business Rules).
* **Step 5:** Append the `eventId` and `title` to the `EventLog` payload so the UI can display a popup alert.

## 6. References
* `docs/research/Books/BEAWARE_Modus_Operandi_of_Financial_Fraudsters.md`
* [06_BUSINESS_RULES.md](06_BUSINESS_RULES.md)

## 7. Future Considerations
Post-MVP, this static dictionary will be replaced by an `AI Storyteller` that evaluates the user's current net worth and dynamically generates context-aware narrative events (e.g., triggering a housing market crash only if the user is over-leveraged in real estate).
