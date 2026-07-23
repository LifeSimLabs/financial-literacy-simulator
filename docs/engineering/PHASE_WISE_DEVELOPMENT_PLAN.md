# Financial Literacy Simulator: Phase-Wise Development Plan

> **Note to the Engineering Team:** This is a living execution document. It defines *how* we build the simulator, step by step. Do not rewrite architecture here; follow the established `docs/architecture/MASTER_PLAN.md` as the source of truth for *what* we are building.

---

# Section 1: Product Vision

## Product Vision
To eradicate financial illiteracy by providing a safe, hyper-realistic, and deeply engaging simulated environment where individuals can experience the lifelong consequences of their financial decisions without real-world risk.

## Mission
To transform complex, intimidating financial concepts (compound interest, tax slabs, debt traps, and fraud) into intuitive, experiential learning loops accessible to anyone with a smartphone or web browser.

## Goals
- **Educational:** Increase the user's practical understanding of Indian personal finance by 50% (measured via pre/post assessments).
- **Behavioral:** Instill long-term habits of emergency fund creation and disciplined SIP investing.
- **Technical:** Deliver a robust, deterministically tested mathematical engine that accurately mirrors real-world economic realities.

## Target Audience
- **Primary:** High school and college students (16-24 years) entering the workforce.
- **Secondary:** Young professionals (25-35 years) struggling with debt management and early-career financial planning.
- **Archetypes:** 'Student', 'New Entrant', 'Farmer' (as defined in NCFE research).

## Target Platforms
Both platforms are treated as first-class citizens:
- **Web Application:** A responsive Single Page Application (SPA) providing a comprehensive desktop-grade dashboard and marketing landing pages.
- **Mobile Application:** A native (or cross-platform) mobile experience focusing on daily engagement, push notifications, and quick on-the-go decisions.

## Success Metrics
- **Acquisition:** 10,000 registered users in the first 3 months post-launch.
- **Activation:** 60% of registered users complete the onboarding and simulate their first 5 game years.
- **Retention:** 20% Day-30 retention (significantly outperforming traditional EdTech).
- **Impact:** 80% of users report feeling "more confident" about managing real-world money.

## Business Goals
- Prove the concept and validate the educational effectiveness during the initial MVP phase.
- Secure seed funding based on engagement metrics to build the full Multiplayer/AI ecosystem.
- Eventually explore B2B partnerships with universities and banks for white-labeled financial literacy modules.

## Core Features
- Deterministic 600-month (50-year) financial simulation engine.
- Dynamic income, tax (Indian slabs), and debt amortization calculations.
- Random "Hazard" events based on real-world NCFE data (e.g., medical emergencies, QR code scams).
- Historical net worth and cash-flow tracking via interactive charts.

## MVP Scope (Internship Deliverable)
- Single-player experience.
- Web application only (responsive for mobile browsers).
- Core math engine, basic static events, and 3-tier tax slabs.
- *Preserved from existing MVP constraints:* Must be a stable, stateful, time-based web app. All AI and multiplayer deferred.

## Future Scope (Startup Vision)
- Multiplayer Co-Op (Household management).
- Generative AI Financial Coach (LLM integration).
- Native Mobile App (iOS/Android).
- Dynamic Macro-Economy (inflation, market crashes).
- Global Asset Marketplace (simulated real estate, peer-to-peer trading).

---

# Section 2: Platform Strategy

## Overview
To maximize reach and educational impact, the Financial Literacy Simulator adopts a multi-platform strategy. While the core mathematical engine (backend) is shared, the client-side experience is tailored to specific platforms. 

## Web Application (Primary Platform for MVP)
The web application serves two distinct purposes:
- **Marketing & Landing Pages:** Public-facing SEO-optimized pages designed to acquire users, explain the value proposition, and host the pitch deck/startup resources.
- **Simulation Dashboard (SPA):** The core authenticated experience. Optimized for longer, focused play sessions on desktop or tablet devices where users can analyze complex charts and data tables comfortably.
- **Progressive Web App (PWA):** As a future enhancement, the web app will be configured as a PWA, allowing users to "install" it on their desktop or Android devices for offline cache support.

## Mobile Application (Target for Seed Phase)
The mobile application is critical for establishing daily behavioral habits (e.g., checking emergency funds, responding to notifications).
- **Core Experience:** A focused, vertical layout prioritizing quick actions (e.g., swiping to pay a bill, tapping to view a simplified net-worth KPI). 
- **Push Notifications:** The primary driver for retention. The app will simulate real-time financial events (e.g., "Your credit card bill is due in 3 days!").
- **Biometric Security:** Leveraging FaceID/TouchID to reinforce the "real banking app" simulation.

## Admin Dashboard (Future Capability)
A restricted internal portal used by the founding team (and eventually B2B partners/teachers) to:
- Monitor aggregate user performance (e.g., "70% of players go bankrupt by month 40").
- Manage the Event Dictionary (injecting new fraud scenarios based on real-world news).
- Manage user accounts and support tickets.

## Platform Responsibilities
- **Backend (API):** The single source of truth. Handles all math, state transitions, and database queries. Completely platform-agnostic.
- **Web Client:** Handles detailed reporting, complex data visualization, and user acquisition (SEO).
- **Mobile Client:** Handles daily engagement, push notifications, and simplified decision-making.

## Shared vs. Specific Features

### Shared Features (Both Web and Mobile)
- Authentication (Login / Signup).
- Core Simulation Loop (Advancing months, making investments, paying debt).
- Leaderboards and Achievements.
- User Profile and Settings.

### Web-Specific Features
- Deep-dive Analytics (Multi-axis charts for 50-year projections).
- Admin Dashboard access.
- Marketing Landing Pages.

### Mobile-Specific Features
- Native Push Notifications.
- Biometric Login.
- "Swipe-to-invest" micro-interactions.
- Haptic feedback during major financial events (e.g., heavy vibration during a "Market Crash" or "Fraud" event).

---

# Section 3: Technology Strategy

## Overview
The technology stack is selected to optimize for developer velocity, strict type safety, and scalability. We are adopting a **TypeScript-first monorepo** approach. Sharing the same language across the frontend, mobile app, and backend reduces context switching and allows us to share interface definitions (e.g., the `PlayerState` JSON schema).

## Frontend (Web & Mobile)
- **Web Framework:** React 18+ (via Vite). Selected over Next.js because the core dashboard is a highly interactive, stateful SPA that does not require Server-Side Rendering (SSR) for SEO. 
- **Marketing Site:** A separate lightweight Next.js or Astro app strictly for SEO and fast page loads, distinct from the React SPA.
- **Mobile Framework:** React Native (Expo). Allows us to reuse up to 70% of the React web components and business logic while delivering native iOS/Android builds.
- **Styling:** Tailwind CSS. Enables rapid prototyping and maintains a strict, consistent design system across both web and mobile (via NativeWind).
- **State Management:** Zustand. Much lighter and less boilerplate-heavy than Redux, perfect for syncing the global simulation state.

## Backend
- **Framework:** Node.js with Express.js. 
- **Language:** TypeScript (Strict Mode).
- **Validation:** Zod. Crucial for validating incoming JSON payloads against our expected schemas before they touch the math engine.
- **Architecture:** Modular Monolith. The system is split logically into domains (Auth, Simulation, Users) but deployed as a single service for simplicity.

## Database & Storage
- **Primary Database:** Amazon DynamoDB. A highly scalable NoSQL database. We will use a Single-Table Design pattern to store Users, Profiles, and Historical Game States together to ensure single-digit millisecond latency.
- **Caching / Locking (Future):** Redis. Will be introduced when Multiplayer is built to handle distributed state locking (e.g., ensuring Player A and Player B both submit decisions before advancing the month).
- **Storage:** Amazon S3. Used for storing user avatars and hosting the static frontend assets.

## Infrastructure & DevOps
- **Authentication:** JWT (JSON Web Tokens) with short-lived access tokens and HttpOnly refresh tokens.
- **Push Notifications:** Expo Push Notifications service (simplifies APNs/FCM integration).
- **Analytics:** PostHog. Selected for its ability to track detailed product usage funnels and feature flags natively.
- **Monitoring & Logging:** Sentry (for real-time error tracking and crash reports on mobile/web) and AWS CloudWatch (backend logs).
- **CI/CD:** GitHub Actions. Automated workflows to run ESLint, Jest tests, and trigger deployments on merge to `main`.
- **Deployment:** AWS AppRunner (for the Node.js backend container) and AWS CloudFront/S3 (for the static React frontend).
- **Version Control:** Git (GitHub).
- **Design Tools:** Figma (UI/UX) and Mermaid (Architecture Diagrams).

---

# Section 4: Authentication & Security

## Overview
Because the Financial Literacy Simulator collects highly sensitive simulated financial behaviors, security must be bank-grade. We will implement a custom JWT-based authentication system rather than relying on heavy third-party providers (like Auth0) to keep costs near zero during the startup phase.

## Authentication Flows

### 1. Registration (Signup)
- **Email/Password:** Standard registration. Requires a strong password (minimum 8 characters, 1 uppercase, 1 number, 1 special character).
- **Email Verification:** Upon signup, a 6-digit OTP is sent via email (using AWS SES or SendGrid). The user account remains in a `PENDING_VERIFICATION` state until the OTP is submitted.
- **Google Authentication:** OAuth 2.0 integration for 1-click signups.

### 2. Login
- **Email/Password Login:** Requires email and password.
- **Remember Me:** If checked, a long-lived Refresh Token (30 days) is stored securely.
- **Apple Authentication (Future):** Required by Apple App Store guidelines if Google Auth is offered on iOS.

### 3. Session Management (JWT Strategy)
- **Access Token:** Short-lived JWT (15 minutes). Sent in the `Authorization: Bearer <token>` header. Contains `userId` and `role`.
- **Refresh Token:** Long-lived JWT (7-30 days). Stored in an `HttpOnly`, `Secure`, `SameSite=Strict` cookie on the web, and in SecureStorage on mobile.
- **Logout:** Clears the cookie and blacklists the current Refresh Token in DynamoDB.
- **Logout From All Devices:** Iterates through the user's active sessions in the database and invalidates all refresh tokens.

### 4. Account Recovery
- **Forgot Password:** User enters email. An email template with a secure, single-use, time-bound (15 mins) reset link is sent.
- **Reset Password:** User clicks the link, enters a new password. Previous active sessions are immediately invalidated.

## Security Architecture

### Data Protection
- **Password Hashing:** Passwords must be hashed using **Argon2** (preferred over Bcrypt for resistance to GPU cracking).
- **Password Salting:** A unique, cryptographically secure salt is generated per user and combined with the Argon2 hash.

### API Protection
- **CORS:** Strictly configured to only allow requests from the exact frontend origin (`https://simulator.example.com`).
- **CSRF Protection:** Handled inherently by keeping the Access Token in memory and only using the HttpOnly cookie for the `/refresh` endpoint.
- **Rate Limiting:** IP-based rate limiting (e.g., 5 login attempts per minute) via an Express middleware (e.g., `express-rate-limit`) to prevent brute force attacks.
- **CAPTCHA:** Google reCAPTCHA v3 will be implemented on the Signup and Forgot Password routes to prevent bot spam.

### Account Lifecycle
- **Deactivate Account:** Soft delete. The `User` record in DynamoDB is marked `isActive: false`. The user can log back in to reactivate.
- **Delete Account (GDPR/CCPA Compliance):** Hard delete. A background worker permanently scrubs the `User`, `Profile`, and all associated `History` records.

### Compliance & Tracking
- **Security Logs:** Failed login attempts and password changes are logged to AWS CloudWatch with the timestamp and IP address.
- **Device Tracking:** (Future) When a new device logs in, an email alert ("New Login from Mac OS") is triggered.
- **Legal Policies:** Enforced checkboxes during signup for Privacy Policy, Terms of Service, and Cookie Policy.

---

# Section 5: Onboarding Experience

## Overview
The onboarding flow is the most critical funnel in the application. It bridges the gap between account creation and the first simulation tick. It must collect enough data to generate an accurate starting `PlayerState` while keeping friction low enough to prevent drop-off.

## The Onboarding Funnel (Step-by-Step)

### Step 1: Welcome & Consent
- **Screen:** Warm welcome message explaining the value of the simulator.
- **Action:** User must explicitly agree to the Privacy Policy and Terms of Service (checkboxes).
- **Validation:** Next button disabled until checkboxes are ticked.

### Step 2: Basic Profile & Avatar
- **Screen:** "Let's set up your identity."
- **Inputs:** 
  - Display Name.
  - Avatar Selection (Choose from a grid of 6 preset vectors or upload a photo).
  - Language Preference (English / Hindi).

### Step 3: Financial Archetype Selection
- **Screen:** "Who are you in the simulation?"
- **Logic:** Instead of asking for exact income (which users might be hesitant to share), users select an Archetype based on NCFE data.
- **Options:**
  - *The Student:* High education debt, zero income.
  - *The New Entrant:* Moderate income, zero savings, high lifestyle spending.
  - *The Farmer / Gig Worker:* Variable income, high vulnerability to economic shocks.
- **Action:** Selecting an archetype automatically populates the starting `Cash`, `Assets`, and `Liabilities` in the background.

### Step 4: Real-World Calibration (Optional / Skippable)
- **Screen:** "Customize your starting scenario."
- **Inputs:** (Sliders)
  - Current Age (Default based on Archetype).
  - Risk Appetite (Conservative, Moderate, Aggressive).
  - Primary Financial Goal (Buy a House, Retire Early, Clear Debt).
- **Skip Rule:** "Skip this and use defaults."

### Step 5: Notification Preferences (Crucial for Mobile)
- **Screen:** "Don't miss important financial events."
- **Action:** Prompt for Push Notification permissions. 
- **Context:** Explain *why* (e.g., "We will only notify you when your simulated bills are due or a market event occurs").

### Step 6: Interactive Tutorial (The First Month)
- **Screen:** A guided overlay (joyride) on top of the main dashboard.
- **Action:** The system forces the user to make their very first decision (e.g., "Allocate 10% of your starting cash to this Fixed Deposit").
- **Completion:** Once the user clicks "Advance Month" for the first time, onboarding is officially marked as complete.

## Technical Implementation Details
- **State Machine:** The onboarding flow will be managed by a client-side state machine (e.g., XState or a complex `useReducer`) to handle back/forward navigation without losing input data.
- **Database Mapping:** The final payload from Step 6 is sent to `POST /api/users/onboard`, which initializes the `USER#PROFILE` and the month 1 `USER#STATE` records in DynamoDB.

---

# Section 6: Information Architecture

## Overview
The Information Architecture (IA) defines the complete hierarchy and routing structure of the application across both web and mobile. It is intentionally shallow (maximum 3 clicks to reach any core feature) to ensure high engagement.

## 1. Public Pages (Unauthenticated)
These pages are entirely static, optimized for SEO, and serve as the marketing/acquisition funnel.
- `/` (Landing Page)
- `/about` (Mission & Vision)
- `/faq` (Frequently Asked Questions)
- `/contact` (Support / Inquiries)
- `/privacy` (Privacy Policy)
- `/terms` (Terms of Service)
- `/cookie-policy` (Cookie Policy)

## 2. Authentication Pages (Unauthenticated)
- `/auth/login` (Email/Password & Google OAuth)
- `/auth/signup` (Registration Form)
- `/auth/verify-email` (OTP Entry)
- `/auth/forgot-password` (Request Reset Link)
- `/auth/reset-password` (Set New Password via Token)

## 3. Onboarding Funnel (Authenticated)
- `/onboarding` (Handles the 6-step wizard detailed in Section 5)

## 4. Core Simulation Pages (Authenticated)
These routes form the heart of the MVP. They require a valid JWT.
- `/dashboard` (The primary game loop: Net Worth, Cash flow, 'Advance Month' button)
  - `/dashboard/income` (Salary, Bonuses, Side Hustles)
  - `/dashboard/expenses` (Fixed Bills, Discretionary Spend)
- `/investments` (Asset allocation)
  - `/investments/fixed-deposits`
  - `/investments/mutual-funds` (SIPs)
  - `/investments/stocks`
- `/debt` (Liability management)
  - `/debt/credit-cards`
  - `/debt/education-loan`
  - `/debt/home-loan`
- `/insurance` (Risk mitigation)
  - `/insurance/health`
  - `/insurance/term-life`
- `/reports` (Historical analytics)
  - `/reports/net-worth-history`
  - `/reports/tax-summary`

## 5. User Management & Social (Authenticated)
- `/profile` (Avatar, Details)
- `/settings` (Notification toggles, Currency display, Danger Zone)
- `/leaderboard` (Global ranking based on Net Worth at Age 60)
- `/achievements` (Unlocked badges, e.g., "First 1 Lakh Saved")

## 6. Admin Pages (Future Scope - Role = ADMIN)
- `/admin/dashboard` (Platform KPIs)
- `/admin/users` (User management, Ban/Deactivate)
- `/admin/events` (CRUD interface for random hazards)

## URL Structure Principles
- **RESTful Routing:** URLs clearly indicate the resource being accessed.
- **Deep Linking:** Mobile app push notifications will map 1:1 with these routes (e.g., `simulator://debt/credit-cards` opens the exact debt screen).

---

# Section 7: Screen Inventory

## Overview
This section details the functional requirements for the highest-priority screens. It defines exactly what UI components are needed, what backend APIs power them, and how they handle edge cases.

## 1. Dashboard (The Main Hub)
- **Purpose:** The primary interface for the game loop. Gives an at-a-glance view of financial health before the user clicks "Advance Month".
- **Users:** Authenticated Users.
- **Components:** 
  - Net Worth KPI Card (Large, animated ticker).
  - Cash Balance Card.
  - "Advance Month" primary action button (Sticky on mobile, Floating on web).
  - Quick-action widgets (Pay Bills, View Pending Events).
  - Mini-chart showing 6-month Net Worth trend.
- **Backend APIs:** `GET /api/simulation/state` (Fetches the current month's data).
- **Permissions:** Valid JWT required.
- **Empty States:** N/A (Pre-populated during onboarding).
- **Loading States:** Skeleton loaders for KPI cards.
- **Errors:** If state fails to fetch, show an error boundary with a "Reload Simulator" button.

## 2. Investments Screen
- **Purpose:** Allows the user to allocate their cash into various asset classes.
- **Users:** Authenticated Users.
- **Components:**
  - Tab navigation (Fixed Deposits, Mutual Funds, Stocks).
  - Asset List Cards (showing Current Value vs Invested Amount).
  - "Invest" / "Withdraw" modal dialogs with numeric input sliders.
- **Backend APIs:** 
  - `GET /api/simulation/investments`
  - `POST /api/simulation/investments/allocate`
- **Validation:** User cannot invest more cash than they currently hold (`amount <= currentCash`).
- **Responsive Behaviour:** On web, the modal is a center dialog. On mobile, it slides up as a Bottom Sheet for better thumb reachability.

## 3. Debt Management Screen
- **Purpose:** Tracks liabilities and allows users to pay down debt or take new loans.
- **Components:**
  - Debt utilization progress bar (Red/Yellow/Green based on health).
  - List of active loans showing Principal, Interest Rate, and EMI.
  - "Pay Extra" button to reduce principal.
- **Backend APIs:**
  - `GET /api/simulation/debt`
  - `POST /api/simulation/debt/repay`
- **Empty States:** "You are completely debt-free! Great job." with an illustration.

## 4. Random Event Dialog (Interrupt)
- **Purpose:** Forces the user to make a decision based on a random life event (e.g., Medical Emergency).
- **Components:**
  - Full-screen modal (Cannot be dismissed by clicking outside).
  - Illustration depicting the event.
  - Impact description (e.g., "Pay ₹50,000 now").
  - Decision buttons (e.g., "Use Cash", "Take Loan", "Claim Insurance").
- **Backend APIs:** `POST /api/simulation/events/resolve`
- **Validation:** The simulator cannot advance to the next month until this event is resolved.

## 5. End of Game Summary (Age 60)
- **Purpose:** The final report card when the user hits retirement age.
- **Components:**
  - Confetti animation.
  - Final Net Worth.
  - "Financial Grade" (A, B, C, F) based on benchmarking against NCFE averages.
  - "Play Again" button.
- **Backend APIs:** `GET /api/simulation/summary`
- **Accessibility:** Ensure the final grade uses high-contrast colors and semantic text (not just color) to denote pass/fail.

---

# Section 8: Layout System

## Overview
Because the simulator is highly data-heavy, the layout must intelligently adapt between Web (where screen real estate allows complex charts) and Mobile (where vertical scrolling and thumb-reachability are paramount).

## 1. Web Layout (Desktop / Tablet)
- **Architecture:** Persistent Left Sidebar + Top Header + Main Content Area.
- **Sidebar:** 
  - Fixed width (e.g., `250px`).
  - Contains primary navigation (Dashboard, Investments, Debt, Insurance).
  - Highlights the current active route.
- **Top Header:** 
  - Height (e.g., `64px`).
  - Contains Global Search (to quickly find specific assets or terms), Notification Bell, and User Profile Dropdown.
- **Main Content Area:** 
  - Centered with a maximum width (`max-w-7xl`) for ultra-wide monitors to prevent text stretching.
  - Utilizes CSS Grid for complex layouts (e.g., `grid-cols-3` where cards span multiple columns).

## 2. Mobile Layout (iOS / Android)
- **Architecture:** Top App Bar + Main Content Area + Persistent Bottom Navigation.
- **Bottom Navigation:**
  - Replaces the Web Sidebar.
  - Contains max 4 icons: Home (Dashboard), Invest, Debt, Profile.
- **Top App Bar:**
  - Contains the Notification Bell and a Hamburger menu for secondary routes (Settings, Leaderboard).
- **Floating Action Button (FAB):**
  - The "Advance Month" button is a highly prominent FAB anchored to the bottom right. This ensures the primary game loop action is always a thumb-tap away.

## 3. Global UI Containers

### Cards
- Used to encapsulate distinct pieces of information (e.g., a specific Loan or a Net Worth summary).
- Must have consistent padding (`p-4` or `p-6`), rounded corners (`rounded-xl`), and subtle shadows (`shadow-sm`) to elevate them from the background.

### Tables vs. Lists
- **Web:** Uses standard Data Tables for historical transactions.
- **Mobile:** Tables are anti-patterns on mobile. They will be transformed into vertical, touch-friendly "Card Lists" where each row becomes a stacked card.

### Dialogs & Bottom Sheets
- **Web:** Interactions requiring focus (e.g., buying a stock) open in a centered Modal Dialog with a darkened backdrop.
- **Mobile:** The exact same interaction opens in a Bottom Sheet that slides up, making it easier to reach the inputs with one hand.

## 4. Notifications (Global State)
- **Toast Notifications:** Ephemeral, auto-dismissing popups (e.g., "Successfully invested ₹5000 in SIP") appearing at the bottom-center of the screen.
- **Interrupts:** Full-screen overlays for critical game events (e.g., "You have been fired!") that require immediate user acknowledgement.

---

# Section 9: Design System

## Overview
To maintain a high-quality, startup-grade aesthetic across Web and Mobile, we will build a centralized Design System. This ensures that every developer uses the exact same colors, typography, and spacing without writing custom CSS.

## 1. Typography
We use a modern, highly legible sans-serif font optimized for reading numerical data.
- **Primary Font:** `Inter` (or `Roboto` on Android).
- **Headings (H1-H4):** Heavy font weights (700-800), tight letter spacing.
- **Body Text:** Regular weight (400), relaxed line height (1.5) for readability.
- **Monospace:** `JetBrains Mono` or `Fira Code` specifically for tabular financial data (ensures numbers align vertically).

## 2. Color Palette (Semantic Tokens)
Hardcoded hex values are forbidden in components. We rely strictly on semantic tokens.
- **Primary Brand:** `slate-900` (Dark, trustworthy, 'banking' feel).
- **Accent:** `indigo-600` (Used for primary CTA buttons and active states).
- **Success (Green):** `emerald-500` (Used for Income, Profit, Portfolio Growth).
- **Danger (Red):** `rose-500` (Used for Expenses, Debt, Market Crashes).
- **Warning (Yellow):** `amber-500` (Used for low Emergency Funds, pending alerts).
- **Backgrounds:** `gray-50` for light mode, `gray-900` for dark mode.

## 3. Spacing & Grid
- **Spacing Scale:** Standard 4px baseline grid (e.g., `p-1` = 4px, `p-4` = 16px).
- **Border Radius:** Generous rounding to feel modern and friendly (`rounded-xl` for cards, `rounded-full` for buttons).

## 4. Core Components
All components must be built as reusable, stateless React components before being used in features.
- **Buttons:** 
  - *Primary:* Solid accent background, white text.
  - *Secondary:* Outline only, transparent background.
  - *Ghost:* No border, no background, accent text on hover.
  - *State:* All buttons must have explicit `:hover`, `:active`, and `:disabled` states.
- **Forms & Inputs:**
  - Standardized label sizing, placeholder text color, and focus rings (`ring-2 ring-indigo-500`).
  - Strict error states (red borders and micro-copy below the input).
- **Charts:**
  - Consistent tooltips and axis styling across Recharts/Victory.

## 5. Animations & Micro-Interactions
To make the application feel "alive", we will implement:
- **Number Tickers:** When Net Worth changes, the number counts up/down rapidly rather than snapping instantly (via `react-spring` or `framer-motion`).
- **Page Transitions:** Subtle fade-in/slide-up when navigating between routes.
- **Haptic Feedback:** On mobile, completing an action (like paying a bill) triggers a slight vibration.

## 6. Accessibility & Theming
- **Dark Mode:** Supported out-of-the-box. All Tailwind classes must include dark variants (e.g., `bg-white dark:bg-gray-800`).
- **Contrast:** All text must pass WCAG AA contrast ratios.
- **Screen Readers:** Generous use of `aria-labels`, especially on icon-only buttons.

---

# Section 10: Application Flows

## Overview
This section models how the user moves between the screens defined in Section 7. Mapping these flows explicitly ensures that there are no dead-ends and that the user's journey is always purposeful.

## 1. Authentication Flow
- **Entry:** User navigates to `/auth/login` or `/auth/signup`.
- **Condition (Signup):** User fills form -> Clicks Submit -> Redirected to `/auth/verify-email` -> Enters OTP -> Account Created.
- **Condition (Login):** User enters credentials -> Clicks Login -> JWT validation success.
- **Decision Node:** 
  - If `isFirstLogin == true` -> Redirect to `/onboarding`.
  - If `isFirstLogin == false` -> Redirect to `/dashboard`.

## 2. Onboarding Flow
- **Entry:** Redirect from Authentication Flow.
- **Path:** Welcome (Step 1) -> Profile (Step 2) -> Archetype Selection (Step 3) -> Calibration (Step 4, optional) -> Notifications (Step 5) -> Tutorial (Step 6).
- **Exit:** Tutorial complete -> Backend creates Month 1 state -> Redirect to `/dashboard`.
- **Constraint:** User cannot bypass `/onboarding` by manually typing `/dashboard` in the URL if `isFirstLogin == true`. The router will force a redirect back to onboarding.

## 3. Core Simulation Flow (The Main Game Loop)
- **Entry:** User is on `/dashboard`.
- **Action (Review):** User reviews income, expenses, and current net worth.
- **Action (Interact):** User navigates to `/investments` to buy stocks, or `/debt` to pay an EMI.
- **Action (Advance):** User clicks "Advance Month".
- **Decision Node (Backend Logic):**
  - Backend calculates new balances, interest, and taxes.
  - Backend rolls RNG (Random Number Generator) for events.
  - *If Event triggers:* Dashboard is blocked. Random Event Dialog appears. User must resolve it.
  - *If No Event triggers:* Month increments by 1. Dashboard re-renders with updated data.
- **Exit:** User repeats this loop until Month reaches 600 (Age 60).

## 4. End-of-Game Flow
- **Entry:** User clicks "Advance Month" at Month 599.
- **Path:** Simulator advances to Month 600 -> Backend flags `isGameComplete = true` -> Frontend automatically redirects to `/reports/summary`.
- **Action:** User reviews their lifetime financial grade and stats.
- **Exit:** User clicks "Play Again" -> Backend archives the current game -> Resets user to a new Month 1 state -> Redirect to `/dashboard`.

## 5. Security Flows
- **Logout Flow:** User clicks "Logout" -> Client deletes JWT from memory -> API call to `/auth/logout` clears HttpOnly cookie -> Redirect to `/auth/login`.
- **Session Timeout Flow:** User's Refresh Token expires -> API returns `401 Unauthorized` -> Axios Interceptor catches the 401 -> Automatically redirects to `/auth/login` with a query parameter `?reason=timeout` (displays toast: "Session expired. Please log in again.").

---

# Section 11: Feature Breakdown

## Overview
This section deconstructs the product into distinct features, prioritizing what must be built now (MVP) versus what is deferred to the startup phase (Future).

## 1. Core Simulation Engine (The Math)
- **Purpose:** Calculates the exact state of the user's finances for a given month.
- **Business Value:** Without this, there is no product. It is the single source of truth.
- **Dependencies:** None. Built as pure TypeScript functions.
- **Complexity:** High (requires accurate Indian tax slab logic and compound interest).
- **Status:** **MVP (P0)**

## 2. Event Dispatcher (Hazards)
- **Purpose:** Randomly triggers life events (e.g., Job Loss, Scams) based on statistical probabilities.
- **Business Value:** Creates the emotional engagement and "gamification" of the simulator.
- **Dependencies:** Core Simulation Engine.
- **Complexity:** Medium (requires balancing probabilities so the game isn't too punishing).
- **Status:** **MVP (P0)**

## 3. Web Dashboard (SPA)
- **Purpose:** Allows users to view their state and make financial decisions.
- **Business Value:** The primary user interface for the internship evaluation.
- **Dependencies:** Backend REST API.
- **Complexity:** High (requires complex state management and Recharts).
- **Status:** **MVP (P0)**

## 4. Push Notifications System
- **Purpose:** Alerts users to pending simulated bills to build daily habits.
- **Business Value:** The primary driver for Day-30 retention.
- **Dependencies:** Mobile App, Expo Push Server.
- **Complexity:** Medium (requires scheduling cron jobs on the backend).
- **Status:** **Future (P1)**

## 5. Multiplayer (Household Mode)
- **Purpose:** Allows two users to link their accounts and make joint financial decisions.
- **Business Value:** Introduces social virality and models realistic family dynamics.
- **Dependencies:** WebSockets, Redis (for distributed locks).
- **Complexity:** Extremely High (state sync across multiple clients is notoriously difficult).
- **Status:** **Future (P2)**

## 6. Generative AI Financial Coach
- **Purpose:** An LLM chatbot that explains *why* the user's Net Worth dropped, without giving explicit financial advice.
- **Business Value:** Replaces static tooltips with personalized, contextual education.
- **Dependencies:** OpenAI API / LangChain, RAG architecture.
- **Complexity:** High (requires strict prompt engineering to prevent hallucinations and legal liability).
- **Status:** **Future (P2)**

## 7. Global Asset Marketplace
- **Purpose:** Real-time simulated stock market where user decisions influence asset prices.
- **Business Value:** Teaches supply/demand and market volatility.
- **Dependencies:** Multiplayer Architecture.
- **Complexity:** High.
- **Status:** **Future (P3)**



# Section 12: Development Roadmap

## Overview
The following phases constitute the step-by-step execution plan for the engineering team. Phases 0-7 focus entirely on delivering the Minimum Viable Product (MVP) required to complete the internship, while Phase 8 represents the post-internship startup roadmap.

## Phase 0: Foundation & Engineering Setup

## Why
Before writing any feature code, the team must have a standardized, reproducible development environment. Inconsistent environments lead to "it works on my machine" bugs, which will derail our internship timeline. 

## Objectives
- Establish the Monorepo folder structure.
- Configure local development tooling (Docker, LocalStack).
- Enforce code quality via automated linting and formatting.
- Establish the CI/CD pipeline for automated testing.

## Scope
This phase covers zero product features. It is strictly limited to repository initialization, tool configuration, and process documentation.

## Deliverables
- `package.json` configurations for both `/client` and `/server`.
- `docker-compose.yml` for LocalStack (DynamoDB).
- GitHub Actions workflow file (`.github/workflows/ci.yml`).
- ESLint and Prettier configuration files.
- `README.md` and `CONTRIBUTING.md` setup instructions.

## Dependencies
- Approval of this execution plan.
- Creation of the GitHub Repository.

## Backend
- Initialize Node.js + Express + TypeScript in the `/server` directory.
- Configure `tsconfig.json` for strict type-checking.
- Setup `jest` for backend unit testing.

## Frontend
- Initialize React + Vite + TypeScript in the `/client` directory.
- Configure TailwindCSS.
- Setup `vitest` for frontend testing.

## Database
- Configure LocalStack in `docker-compose.yml` to simulate DynamoDB locally.
- Write a simple initialization script to create the `fls-main-table` in LocalStack on container startup.

## UI / UX
- *Not applicable for this phase.*

## Risks
- **Technical Risk:** Docker/LocalStack issues on Windows machines (if any interns use Windows).
  - *Mitigation:* Document WSL2 setup steps meticulously in `CONTRIBUTING.md`.
- **Schedule Risk:** Spending too much time debating ESLint rules.
  - *Mitigation:* Use standard industry presets (e.g., `eslint-config-prettier`) and move on.

## Testing
- Verify that `npm run test` executes successfully in both client and server directories.
- Verify that GitHub Actions successfully runs the test suite on a test PR.

## Definition of Done
- Any developer on the team can clone the repo, run `docker-compose up`, and `npm start` without any errors.
- CI/CD pipeline is active and blocking merges on lint/test failures.

## Milestone
**Milestone 1:** Project Foundation Complete.

### Team Allocation

Backend
- Initialize Node/Express/TS scaffolding.
- Configure Docker and LocalStack.

Frontend
- Initialize React/Vite scaffolding.
- Configure TailwindCSS and ESLint.

UI/UX
- *No tasks assigned.*

Documentation
- Write `CONTRIBUTING.md` with local setup instructions.

Testing
- Configure GitHub Actions CI workflow.

Estimated Duration: 3 Days
Completion Criteria: Successful CI pipeline run on `main`.

---

# Phase 1: UI / UX Foundation

## Why
A simulator lives or dies by its interface. Before any backend logic is hooked up, the frontend must have a cohesive design system. Building the UI components early ensures that when the backend APIs are ready, the frontend developers only need to map data rather than design layouts from scratch.

## Objectives
- Establish the visual language (Design System, Typography, Colors).
- Build the core reusable React Component Library.
- Map out the Information Architecture and Screen Inventory.
- Develop static wireframes for the main Dashboard.

## Scope
This phase focuses entirely on the visual presentation and frontend component structure. No backend APIs will be built or connected during this phase.

## Deliverables
- Tailwind CSS configuration (`tailwind.config.js`) matching the color palette.
- Reusable UI Components: Buttons, Modals, Forms, Sliders, Cards.
- Static prototype of the main Financial Dashboard.
- Defined User Journey maps for Onboarding and Monthly Decisions.

## Dependencies
- Phase 0 (Foundation Setup) must be complete.

## Backend
- *Not applicable for this phase.*

## Frontend
- Create the `/components` directory structure.
- Build the atomic UI components (Buttons, Inputs, Typography).
- Build the composite components (Decision Panel, KPI Cards).
- Ensure all components are fully responsive (Mobile First).

## Database
- *Not applicable for this phase.*

## UI / UX
- **Design Philosophy:** Clean, modern, "FinTech" aesthetic. Avoid overly playful/childish game UI; it must look like a serious financial tool to build trust.
- **Color Palette:** 
  - Primary: Deep Trust Blue.
  - Success/Assets: Forest Green.
  - Danger/Debt: Alert Red.
  - Background: Off-white/Light Gray to reduce eye strain during long sessions.
- **Accessibility:** Ensure high contrast ratios for text and colorblind-safe palettes for charts.

## Risks
- **Design Paralysis:** Spending too much time debating button border-radius rather than building.
  - *Mitigation:* Use an existing headless UI library (e.g., Radix UI, shadcn/ui) as a base.
- **Scope Creep:** Designing screens that are not required for the MVP.
  - *Mitigation:* Strictly adhere to the core MVP Screen Inventory list.

## Testing
- Visual regression testing (or manual UI review) across Mobile, Tablet, and Desktop breakpoints.
- Ensure all interactive elements have focus states for keyboard navigation.

## Definition of Done
- All primary UI components are built and viewable in a sandbox (e.g., a static `/styleguide` route).
- A static version of the main Dashboard is built and fully responsive.

## Milestone
**Milestone 2:** UI/UX Foundation Complete.

### Team Allocation

Backend
- *No tasks assigned.*

Frontend
- Configure Tailwind theme.
- Build React Component Library (Buttons, Cards, Sliders).
- Build Static Dashboard Layout.

UI/UX
- Define Color Palette and Typography.
- Create Wireframes (Figma/Excalidraw).
- Map User Journey (Onboarding -> Gameplay -> Game Over).

Documentation
- Document the Component Library usage in `/client/README.md`.

Testing
- Verify responsive breakpoints manually.

Estimated Duration: 4 Days
Completion Criteria: Static dashboard approved by the Product Manager.

---

# Phase 2: Simulation Core

## Why
The Simulation Core is the absolute brain of this project. If the financial math is incorrect, the educational value is zero. By building the core engine as a pure, isolated module before hooking it up to a database or HTTP server, we guarantee that the math is 100% testable and completely agnostic of the infrastructure.

## Objectives
- Build the pure mathematical engine (`SimulationEngine`).
- Define the exact JSON schema for `PlayerState` and `Decisions`.
- Implement the exact business rules extracted from the NCFE research (Taxes, SIPs, EMIs).
- Create a deterministic Random Event Generator for life hazards.

## Scope
This phase focuses exclusively on the backend `engine/` directory. There is NO database integration and NO network request handling. It is purely data-in, data-out logic.

## Deliverables
- `PlayerState` and `Decision` TypeScript interfaces.
- `loop.ts`: The main monthly progression function.
- `math.ts`: Compound interest and tax utility functions.
- `events.ts`: The static hazard event dictionary and probability roller.
- 100% Jest Unit Test coverage on all engine files.

## Dependencies
- NCFE Research documents mapping tax brackets and fraud scenarios.

## Backend
- Write pure TypeScript functions that accept an `OldState` and `Decisions`, and return a `NewState`.
- Implement integer math (all currency handled in paise/cents) to avoid floating-point rounding errors.
- Implement constraint checks (e.g., triggering auto-debt if Cash drops below zero).

## Frontend
- *Not applicable for this phase.*

## Database
- *Not applicable for this phase.*

## UI / UX
- *Not applicable for this phase.*

## Risks
- **Technical Risk:** Floating-point math errors compounding over 600 simulated months.
  - *Mitigation:* Strictly enforce integer-only math for all currency fields.
- **Logic Risk:** Incorrect implementation of Indian Tax Slabs.
  - *Mitigation:* Hardcode a simplified, 3-tier tax slab logic and cover every boundary condition with unit tests.

## Testing
- **Unit Testing:** This phase requires extreme test-driven development (TDD). 
- Write tests that simulate 50 years (600 months) of compound interest to verify the math holds up without crashing or drifting.
- Write tests forcing negative cash balances to ensure the Auto-Debt business rule triggers correctly.

## Definition of Done
- The `SimulationEngine` can take a starting state and process 600 months of decisions correctly.
- Jest test suite reports 100% coverage on the `engine/` directory.

## Milestone
**Milestone 3:** Simulation Core Complete.

### Team Allocation

Backend
- Define TS Interfaces (`PlayerState`, `Events`).
- Implement `math.ts` (Compound Interest, Taxes, Amortization).
- Implement `events.ts` (RNG Hazard Logic).
- Implement `loop.ts` (The master state transition function).

Frontend
- *No tasks assigned.*

UI/UX
- *No tasks assigned.*

Documentation
- Document the exact formulas used in `SIMULATION_RULES.md`.

Testing
- Write Jest Unit tests for every mathematical boundary condition.

Estimated Duration: 5 Days
Completion Criteria: `npm run test` passes with 100% coverage on the engine module.

---

# Phase 3: Backend Development

## Why
With the `SimulationEngine` proven and tested, the system needs an API layer to expose this logic to the internet and a persistence layer to save user progress. This phase builds the REST API and the database connections that will eventually power the frontend dashboard.

## Objectives
- Build the Express.js server and REST API endpoints.
- Implement JWT-based Authentication.
- Integrate Amazon DynamoDB (via LocalStack) using Single-Table Design.
- Connect the `SimulationEngine` to the API layer using Services and Controllers.

## Scope
This phase covers the entire Node.js/Express infrastructure. It stops at the API boundary; no frontend integration occurs here.

## Deliverables
- `auth` controller (`/register`, `/login`).
- `simulation` controller (`/state`, `/advance-month`, `/history`).
- DynamoDB Repositories for fetching/saving User and State objects.
- Zod validation schemas for all incoming POST requests.
- API Documentation (e.g., Swagger/OpenAPI spec or Postman Collection).

## Dependencies
- Phase 2 (Simulation Core) must be complete.
- LocalStack container must be running (Phase 0).

## Backend
- Setup Express Router and modularize routes.
- Implement Middleware for JWT verification and global error handling.
- Write DynamoDB DocumentClient wrappers to perform `GetItem`, `PutItem`, and `Query`.
- **The Orchestration Flow:** The `/advance-month` route must: 
  1. Fetch `OldState` from DB.
  2. Pass `OldState` to `SimulationEngine`.
  3. Save `NewState` to DB.
  4. Return `NewState` to the client.

## Frontend
- *Not applicable for this phase.*

## Database
- Create the local DynamoDB tables.
- Define the Partition Key (`PK`) and Sort Key (`SK`) patterns in the repository code.

## UI / UX
- *Not applicable for this phase.*

## Risks
- **Security Risk:** Users modifying the JSON payload to artificially inflate their Net Worth.
  - *Mitigation:* The backend MUST fetch the "current cash" from the trusted database, not rely on what the client sends. The client only sends *decisions* (e.g., "Invest 500"), and `Zod` validates that `500` is a positive integer less than or equal to their actual cash.
- **Data Loss Risk:** Overwriting the state without saving history.
  - *Mitigation:* Ensure every `/advance-month` call writes to both the `STATE` record and appends a `HISTORY#<month>` record in DynamoDB.

## Testing
- Integration Testing: Use `Supertest` to simulate HTTP requests against the Express app and verify 200 OK or 400 Bad Request responses.
- Ensure Zod correctly rejects malformed JSON payloads.

## Definition of Done
- A developer can use Postman to register an account, fetch their state, and successfully advance the simulation by 1 month.
- All API routes return the correct HTTP status codes.

## Milestone
**Milestone 4:** Backend APIs Complete.

### Team Allocation

Backend
- Build Express App, Routes, and Middleware.
- Implement JWT Auth.
- Write DynamoDB Repositories.
- Connect Controllers to the `SimulationEngine`.

Frontend
- *No tasks assigned.*

UI/UX
- *No tasks assigned.*

Documentation
- Update `API_SPECIFICATION.md` with final request/response payloads.

Testing
- Write `Supertest` integration tests for all API endpoints.

Estimated Duration: 5 Days
Completion Criteria: Successful Postman flow from Registration to 3 months of simulation advancement.

---

# Phase 4: Frontend Development

## Why
With the backend APIs live, the UI/UX components built in Phase 1 must now be wired up to real data. This phase transforms the static dashboard into a fully functional Single Page Application where users can log in, see their state, and make financial decisions.

## Objectives
- Integrate React Router for navigation between Auth, Dashboard, and Reports.
- Build the API Client (`axios` interceptors for JWT injection).
- Connect the React Context provider to manage the global `PlayerState`.
- Implement `Recharts` to draw the historical Net Worth progression.

## Scope
This phase covers data fetching, state management, and chart rendering on the client side.

## Deliverables
- Fully functional Login / Registration flows.
- Populated KPI Dashboard (Cash, Assets, Liabilities).
- Interactive Decision Form (Sliders/Inputs for allocating budget).
- Responsive Line Chart displaying the array returned by `/api/simulation/history`.

## Dependencies
- Phase 1 (UI Components) must be complete.
- Phase 3 (Backend APIs) must be deployed locally or stubbed.

## Backend
- *Not applicable for this phase.*

## Frontend
- Set up an `AuthContext` to hold the JWT in memory (or secure `localStorage`).
- Create custom hooks (e.g., `useSimulation()`) to abstract API calls away from the UI components.
- Wire up the Event Modal: When `/advance-month` returns an `eventTriggered` object, display a popup describing the hazard (e.g., "Medical Emergency") before refreshing the dashboard numbers.

## Database
- *Not applicable for this phase.*

## UI / UX
- Handle loading states gracefully (Skeleton loaders during API calls).
- Handle error states gracefully (Toast notifications for 400 Bad Request if the user tries to overspend).

## Risks
- **State De-sync Risk:** The UI displaying outdated numbers after an action.
  - *Mitigation:* Ensure that every successful `/advance-month` response completely overwrites the global `PlayerState` context, triggering a top-down re-render.
- **Chart Performance Risk:** Rendering 600 data points on a mobile device may cause lag.
  - *Mitigation:* Use `Recharts` with data downsampling if the array exceeds 100 points.

## Testing
- **E2E Testing:** Use Cypress or Playwright to test the full flow: Login -> View Dashboard -> Advance Month -> See updated Chart.
- Test responsive layout on actual mobile devices using local network hosting.

## Definition of Done
- A user can log in, allocate funds, click "Advance Month", see a loading spinner, and watch their Net Worth chart update in real-time.
- No console errors exist.

## Milestone
**Milestone 5:** Frontend Interactive MVP Complete.

### Team Allocation

Backend
- *No tasks assigned.*

Frontend
- Wire up Axios interceptors and Auth logic.
- Implement React Context for global state.
- Integrate Recharts and bind historical data.
- Handle Loading and Error UI states.

UI/UX
- Review the implemented UI against the original Phase 1 Figma designs.

Documentation
- *No tasks assigned.*

Testing
- Write Cypress E2E tests for the core gameplay loop.

Estimated Duration: 5 Days
Completion Criteria: Successful E2E test run on the frontend repository.

---

# Phase 5: Integration

## Why
While the frontend and backend have been built and tested in isolation, the point where they connect is where 90% of critical bugs occur. Integration testing ensures that the UI correctly maps the actual JSON payloads returned by the server, rather than relying on mocked data.

## Objectives
- Remove all mock data from the Frontend React application.
- Ensure the Frontend correctly handles and visualizes the Backend's Random Events.
- Verify CORS configuration allows communication between the Vite dev server and Express.
- Audit the end-to-end performance of a full simulation run (from Month 1 to Month 600).

## Scope
This phase focuses on cross-boundary communication. No net-new features should be built here; the goal is stabilization and connection.

## Deliverables
- A fully integrated, playable loop running on LocalStack and local Docker containers.
- Performance audit report identifying any bottlenecks in the `advance-month` API.
- Fixed CORS policies in the Express middleware.

## Dependencies
- Phase 3 (Backend) and Phase 4 (Frontend) must be complete.

## Backend
- Configure CORS to accept requests from the frontend origin.
- Ensure all environment variables (e.g., JWT secrets) are properly documented in `.env.example`.

## Frontend
- Delete all local JSON mock files.
- Ensure the Global Context seamlessly handles the `403 Forbidden` response if a JWT expires, correctly redirecting the user to the Login screen.

## Database
- *Not applicable for this phase.*

## UI / UX
- Review the End-of-Game screens (Bankruptcy and Retirement). Ensure they trigger correctly when the backend API rejects further advancement.

## Risks
- **CORS Errors:** The most common blocker during integration.
  - *Mitigation:* Explicitly whitelist the frontend dev port (usually `localhost:5173`) in the Express setup.
- **Payload Mismatches:** Backend changes a key from `cash` to `currentCash` breaking the frontend.
  - *Mitigation:* Share a single `types/` folder between the `/client` and `/server` in the monorepo to enforce contract consistency.

## Testing
- Conduct full manual exploratory testing of the entire game loop.
- Run Cypress E2E tests against the live local backend rather than mocked network routes.

## Definition of Done
- A user can register, play 600 months, and retire without experiencing a single console error, network failure, or UI desync.

## Milestone
**Milestone 6:** Full System Integration Complete.

### Team Allocation

Backend
- Configure CORS and security headers (Helmet).
- Monitor server logs during frontend integration to catch payload issues.

Frontend
- Purge mock data.
- Handle JWT expiration edge cases.

UI/UX
- Perform a UX audit on the live, integrated application.

Documentation
- *No tasks assigned.*

Testing
- Execute manual end-to-end tests covering all edge cases (Bankruptcy, Retirement, 100% savings, 100% debt).

Estimated Duration: 3 Days
Completion Criteria: Flawless execution of the 600-month game loop on a local machine.

---

# Phase 6: Testing & Quality Assurance

## Why
Financial software requires zero tolerance for mathematical drift or data corruption. While unit tests were written during earlier phases, this phase focuses on adversarial testing: trying to deliberately break the game through edge cases, extreme user inputs, and simulating years of gameplay in seconds.

## Objectives
- Conduct deep Simulation Testing (running bots through the engine).
- Perform Load / Performance Testing on the API.
- Execute Security Testing against the JWT and payload validation.
- Bug fixing and stabilization ahead of deployment.

## Scope
No new features are permitted. The entire team shifts to a Quality Assurance (QA) mindset. Every bug found must be ticketed, triaged, and fixed.

## Deliverables
- Comprehensive Test Report (Unit, Integration, E2E results).
- Automated bot scripts capable of playing 50 years in <1 second.
- Resolved bug tickets for all `P0` (Critical) and `P1` (High) issues.

## Dependencies
- Phase 5 (Integration) must be 100% complete and merged to `main`.

## Backend
- Run load testing tools (e.g., `k6` or `Artillery`) against the `/advance-month` endpoint.
- Verify DynamoDB throttling limits are not hit during rapid API calls.

## Frontend
- Run Lighthouse audits. Ensure Performance, Accessibility, and Best Practices scores are all >90.
- Verify the UI does not crash if the backend returns a 500 Internal Server Error.

## Database
- Verify that orphaned data is not being created (e.g., historical snapshots without an associated User Profile).

## UI / UX
- Test the application on actual mobile devices (iOS Safari, Android Chrome). Ensure sliders and touch targets are responsive and thumb-friendly.

## Risks
- **Testing Fatigue:** Developers testing their own code often miss obvious bugs.
  - *Mitigation:* Enforce cross-testing. The frontend developer tests the backend API using Postman; the backend developer tests the UI using Cypress.
- **Edge Case Crashes:** What happens if a user allocates 0 to everything for 600 months?
  - *Mitigation:* The automated simulation bots must run millions of random permutations to find crashes.

## Testing
- **Unit Testing:** Maintain 100% on `engine/`.
- **Integration Testing:** Maintain API route coverage.
- **E2E Testing:** Execute Cypress suites against a staging environment.
- **Simulation Testing:** Execute "Monte Carlo" style bot scripts against the `SimulationEngine`.

## Definition of Done
- All automated tests pass in the CI/CD pipeline.
- Lighthouse scores >90.
- Zero known `P0` or `P1` bugs remain open in the issue tracker.

## Milestone
**Milestone 7:** Release Candidate 1 (RC1) Approved.

### Team Allocation

Backend
- Write and execute API load tests (`k6`).
- Fix any `P0`/`P1` backend bugs discovered.

Frontend
- Execute Lighthouse audits and fix accessibility issues.
- Fix any `P0`/`P1` UI bugs discovered.

UI/UX
- Perform Mobile Device testing.

Documentation
- Draft the Release Notes for RC1.

Testing
- Write automated "Bot" scripts to stress-test the `SimulationEngine` with random decisions.

Estimated Duration: 4 Days
Completion Criteria: Zero critical bugs remaining; team sign-off on RC1.

---

# Phase 7: Deployment

## Why
A local application is invisible to the internship evaluators. We must move the MVP from our local machines to the open internet in a secure, scalable, and cost-effective manner.

## Objectives
- Containerize the Backend Node.js application via Docker.
- Compile and bundle the Frontend React application.
- Deploy the DynamoDB table to real AWS infrastructure.
- Set up domain routing and SSL certificates.

## Scope
This phase transitions the system from LocalStack to production AWS services (or equivalent platforms like Vercel/Render, if budget is constrained).

## Deliverables
- `Dockerfile` for the Node.js backend.
- Deployed frontend accessible via a public URL (e.g., `https://simulator.example.com`).
- Deployed backend accessible via a public URL (e.g., `https://api.simulator.example.com`).
- Live production DynamoDB table.

## Dependencies
- Phase 6 (QA) must be completed. RC1 must be tagged in Git.

## Backend
- Update the AWS SDK configuration in the codebase to use production credentials (via IAM Roles, NOT hardcoded keys) instead of pointing to `localhost:4566`.
- Deploy the Docker container to AWS AppRunner or ECS.

## Frontend
- Run `npm run build` to generate the production optimized static bundle.
- Deploy the `/dist` folder to AWS S3 and place CloudFront (CDN) in front of it.
- Update the Axios base URL to point to the production API.

## Database
- Provision a real DynamoDB table via the AWS Console or Terraform.
- Ensure On-Demand capacity is selected to minimize idle costs.

## UI / UX
- *Not applicable for this phase.*

## Risks
- **Deployment Costs:** Leaving infrastructure running post-internship can accrue massive AWS bills.
  - *Mitigation:* Document teardown scripts. Set AWS Billing Alarms to trigger at $10.
- **Environment Variable Leaks:** Accidentally committing production `.env` files to GitHub.
  - *Mitigation:* Double-check `.gitignore`. Use GitHub Secrets for CI/CD injection.

## Testing
- Perform a "Smoke Test" on the live production URL to ensure the database connection works and static assets load quickly.

## Definition of Done
- The internship evaluators can access the application from their own laptops without needing to install any software.
- The repository's `main` branch automatically deploys to production upon push.

## Milestone
**Milestone 8:** Project Live.

### Team Allocation

Backend
- Write `Dockerfile`.
- Provision AWS AppRunner and DynamoDB table.
- Configure AWS IAM Policies.

Frontend
- Configure AWS S3 and CloudFront.
- Handle production environment variables.

UI/UX
- *No tasks assigned.*

Documentation
- Write the final Internship Presentation referencing the live URL.

Testing
- Execute the production Smoke Test.

Estimated Duration: 2 Days
Completion Criteria: Live public URL shared with the internship evaluators.

---

# Phase 8: Post Internship Roadmap

## Why
With the internship successfully completed and graded, the team can pivot the MVP into a legitimate startup product. This phase outlines the "cool" features that were deliberately deferred to protect the initial timeline.

## Objectives
- Integrate Large Language Models (LLMs) to serve as a personalized AI Financial Coach.
- Implement Multiplayer architecture (Co-Op households).
- Transition from static Random Events to a dynamic Macro-Economy simulation.
- Introduce an Asset Marketplace for realistic stock trading and real estate.

## Scope
This phase represents the next 6-12 months of startup development. It requires significant architectural shifts, including WebSockets and Redis.

## Deliverables
- Pitch Deck for seed funding based on MVP metrics.
- AI Storyteller module built with LangChain / OpenAI API.
- Global Leaderboard and Economy microservices.

## Dependencies
- Phase 7 (Deployment) and the successful completion of the internship.

## Backend
- **Multiplayer Migration:** Introduce WebSockets (Socket.io or API Gateway WebSockets) to sync state between two users playing as a "Household" (e.g., Husband and Wife).
- **Caching:** Introduce Redis to handle real-time locking so both players must confirm their monthly decisions before the engine ticks.

## Frontend
- Build a chat interface for the "AI Coach" using a streaming text response component.
- Build the Global Marketplace screens.

## Database
- Refactor the DynamoDB single-table design to support `HOUSEHOLD` partition keys instead of individual `USER` keys.

## UI / UX
- Redesign the Dashboard to accommodate dual-player metrics.

## Risks
- **LLM Hallucinations:** The AI Coach giving genuinely bad financial advice.
  - *Mitigation:* The LLM must be strictly prompted to *explain* the math, never to prescribe investment strategies. It must run in a highly constrained RAG (Retrieval-Augmented Generation) pipeline.
- **WebSocket Scaling:** Handling thousands of concurrent TCP connections.
  - *Mitigation:* Rely on managed services like AWS API Gateway WebSockets rather than self-hosting a massive Redis pub/sub cluster early on.

## Testing
- Introduce chaos testing to handle dropped WebSocket connections gracefully.

## Definition of Done
- The simulator is no longer a single-player calculator, but a massive multiplayer ecosystem where players can compare their Net Worth and consult an AI for learning.

## Milestone
**Milestone 9:** Seed Funding Pitch.

### Team Allocation

Backend
- Prototype the WebSocket architecture.
- Integrate the OpenAI API.

Frontend
- Build the AI Chat Interface.
- Build Multiplayer Lobbies.

UI/UX
- Design the Multiplayer Dashboard.

Documentation
- Draft the Startup Pitch Deck.

Testing
- Evaluate LLM responses for safety and accuracy.

Estimated Duration: 3 - 6 Months
Completion Criteria: The project evolves into a fully-fledged EdTech product.

---

# Section 13: Team Planning & Execution

## Overview
A flawless plan is useless without rigorous execution. This section defines how the founding engineering team will operate, communicate, and ensure high-quality output throughout the phases defined in Section 12.

## 1. Roles & Responsibilities
To prevent bottlenecks, domain responsibilities are strictly siloed, but cross-testing is enforced.

- **Backend Tasks:** Database modeling, API route creation, Zod schema validation, Core Math Engine implementation.
- **Frontend Tasks:** Component building (React/Vite), global state management (Zustand), API integration (Axios), charting (Recharts).
- **UI/UX Tasks:** Figma design token management, mobile layout optimization, SVG illustrations, CSS Tailwind configuration.
- **Testing Tasks:** Cypress E2E flows, Jest unit tests for the math engine, manual QA on target devices.
- **Documentation Tasks:** API Swagger docs, architecture diagrams, and updating this Blueprint.

## 2. Sprint Planning
We will execute this project following the Scrum framework customized for async collaboration:
- **Sprints:** 2-week timeboxes.
- **Tracking:** GitHub Projects (Kanban board) with columns: `To Do`, `In Progress`, `In Review`, `Done`.
- **Tickets:** Every task must be converted into a GitHub Issue before work begins. No code is written without a ticket.

## 3. Communication Strategy
- **Async First:** All technical decisions, blockers, and bug reports must be documented in GitHub Issues, not lost in Slack/Discord chats.
- **Daily Sync:** A 15-minute daily standup (synchronous or async text) answering: What did you do? What are you doing? Are you blocked?

## 4. Branch Strategy
- `main`: Production-ready code only. Highly protected. Deploys automatically to AWS.
- `develop`: Integration branch. The default target for all new features.
- `feature/<ticket-number>-<short-desc>`: Created off `develop` for active work (e.g., `feature/42-auth-api`).
- `fix/<ticket-number>-<short-desc>`: Created off `develop` for bug fixes.

## 5. Review Process
1. Developer opens a Pull Request (PR) from `feature/*` against `develop`.
2. GitHub Actions automatically runs Prettier, ESLint, and Jest Unit Tests.
3. PR must be reviewed and approved by at least **one other engineer** on the team.
4. Reviewer checks for: Logic errors, missing tests, architectural violations, and adherence to the Definition of Done.
5. Once approved and CI passes, the PR is squashed and merged.

## 6. Definition of Done (DoD)
A feature or phase is NOT complete until it meets the following criteria:
1. Code is merged into `develop`.
2. 0 ESLint warnings or errors.
3. 100% unit test coverage for any code touching the `SimulationEngine`.
4. Feature has been manually tested on both a Desktop Browser and a Mobile Device.
5. UI passes Lighthouse accessibility audits (>90 score).

## 7. Milestones
- **Milestone 1:** Engineering Foundation (Phase 0)
- **Milestone 2:** UI Design System (Phase 1)
- **Milestone 3:** Math Engine Complete (Phase 2)
- **Milestone 4:** Backend APIs Complete (Phase 3)
- **Milestone 5:** Frontend Connected (Phase 4)
- **Milestone 6:** Full System Integration (Phase 5)
- **Milestone 7:** Release Candidate 1 (RC1) Approved (Phase 6)
- **Milestone 8:** Project Live (MVP Complete) (Phase 7)
- **Milestone 9:** Seed Funding Pitch (Phase 8)
