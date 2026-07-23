# 13. Frontend Architecture

## 1. Purpose
This document outlines the architecture for the React.js Single Page Application (SPA), defining state management, routing, and component hierarchy.

## 2. Scope
Applies exclusively to the web-based user interface.

## 3. Tech Stack
*   **Framework:** React 18+
*   **Build Tool:** Vite
*   **Language:** TypeScript
*   **Styling:** TailwindCSS (for rapid, responsive prototyping)
*   **Data Visualization:** Recharts
*   **State Management:** React Context API + Custom Hooks (Redux is overkill for the MVP).

## 4. Folder Structure (src/)

```text
src/
 ├── components/     # Reusable UI (Buttons, Cards, Modals, Recharts wrappers)
 ├── pages/          # Route-level components (Login, Dashboard, EndReport)
 ├── hooks/          # Custom hooks (e.g., useSimulationState)
 ├── services/       # Axios API client functions (fetchState, advanceMonth)
 ├── context/        # AuthProvider (stores JWT and user info)
 ├── types/          # TypeScript interfaces matching backend models
 └── assets/         # Static images, icons
```

## 5. Component Hierarchy (The Dashboard)

```mermaid
graph TD
    Dashboard[Dashboard Page]
    Dashboard --> TopBar[TopNav (Shows Age, Month, Archetype)]
    Dashboard --> KPI[KPI Grid (Cash, Net Worth, Debt)]
    Dashboard --> Charts[History Chart (Recharts)]
    Dashboard --> Action[Decision Panel]
    
    Action --> Inputs[Input Sliders (Invest, Pay Debt)]
    Action --> Submit[Advance Month Button]
```

## 6. State Management Strategy
Because the backend `Engine` acts as the single source of truth, the frontend is effectively a "dumb" viewer.
* When the user clicks "Advance Month", the frontend sends the decisions to the API.
* The frontend waits for the API response (which contains the new State JSON).
* The frontend overwrites its local Context state with the new State JSON and triggers a re-render of the KPI Grid and Charts.

## 7. References
* [11_API_SPECIFICATION.md](11_API_SPECIFICATION.md)

## 8. Future Considerations
When Multiplayer is introduced, the frontend will need to migrate from standard Axios polling to a WebSocket connection (e.g., Socket.io) to receive real-time state updates when the *other* player makes a decision.
