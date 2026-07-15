# Project Setup & Community Guidelines

Welcome to the Financial Literacy Simulator! This document outlines how our open-source community operates, our contributor roles, and the initial tasks required before active development begins.

## 👥 Contributor Role Definitions

To build a world-class simulation, we need diverse expertise. Here are the roles within our community:

1. **Maintainer**: Oversees the project vision, manages releases, merges pull requests, and enforces the Code of Conduct.
2. **Core Contributor**: Highly active community members (developers, researchers, or designers) with significant influence over architecture and project direction.
3. **Research Contributor**: Focuses on financial modeling, data gathering, historical research, and ensuring scenario realism. No coding required!
4. **Documentation Contributor**: Maintains the README, wikis, tutorials, and setup guides to ensure the project remains accessible to newcomers.
5. **Designer**: Works on UX/UI, wireframes, accessibility (a11y), and visual assets (icons, layouts, branding).
6. **Developer**: Writes the application code, fixes bugs, implements features, and writes tests.
7. **Reviewer**: Helps review code and research proposals, ensures quality standards, and manually tests pull requests.

## 🏗️ Architecture Discussion Topics

Before writing the first line of code, the core team and community must align on the technical foundation. We will use GitHub Discussions for the following topics:

- **Monolith vs Microservices**: Should the core engine be a monolithic package, or decoupled services?
- **Simulation Engine Design**: How do we handle ticks/turns (e.g., monthly vs. yearly steps)?
- **Event Engine**: How are random and deterministic life events generated, queued, and resolved?
- **Financial Rule Engine**: How do we abstract formulas (taxes, compound interest) so they can be localized or updated easily?
- **State Management**: How do we persist a user's 50-year life state efficiently?
- **API Design**: How will the frontend communicate with the simulation engine?

## 📊 Initial Research Issues

We have defined 50 critical research questions that need answering to ensure the simulator's realism. These are tracked as GitHub issues with the `research` label. 

1. How should salary progression work across different career paths?
2. How should inflation affect users' purchasing power?
3. Should investments use historical market data or simulated random walks?
4. How should health insurance work?
5. How should income taxes differ across countries/regions?
6. How should random life events (e.g., medical emergencies, car accidents) be modeled?
7. How does education level correlate with income potential in the simulation?
8. What is the impact of student loans on early career finances?
9. How should property value appreciation be calculated?
10. How should the cost of raising children be modeled over time?
11. Should we model different types of debt (credit cards, personal loans, mortgages)?
12. How do macroeconomic cycles (recessions, booms) affect the user?
13. How should retirement accounts (401k, IRA, pension) be differentiated?
14. What happens when a user goes bankrupt in the simulation?
15. How should cost of living vary by simulated geographic location?
16. Should we include behavioral finance factors (e.g., impulse buying)?
17. How is credit score calculated and what does it impact?
18. How should capital gains taxes be implemented?
19. How do we model the gig economy and freelance income?
20. Should cryptocurrency and high-risk investments be included?
21. What are the financial impacts of marriage and divorce?
22. How should unemployment periods and severance packages work?
23. How do we model natural disasters and home insurance?
24. Should we simulate the effects of inflation on different asset classes separately?
25. How do we account for systemic biases or socioeconomic starting conditions?
26. How should inheritance and generational wealth be handled?
27. What are the rules for early withdrawal penalties on retirement accounts?
28. How should variable vs. fixed-rate mortgages behave?
29. Should we model the cost of eldercare or supporting parents?
30. How do government welfare programs factor into the simulation?
31. What is the economic impact of renting vs. buying a home over 30 years?
32. How do we model depreciation of assets like cars?
33. How should disability insurance and long-term care be handled?
34. Should we simulate entrepreneurship and business failure rates?
35. How does currency exchange affect international users or scenarios?
36. What is the formula for calculating property taxes based on location?
37. How should utility costs and maintenance scale with home ownership?
38. How do we model the psychological toll of high debt (if at all)?
39. Should we simulate the impact of automation/AI on job security?
40. How do different savings accounts (high-yield vs. standard) operate?
41. What are the financial costs of continuing education or career switching?
42. How should stock dividends and reinvestment be modeled?
43. How do we handle peer pressure or lifestyle creep in the simulation?
44. Should there be varying levels of financial literacy for the character vs. the player?
45. How do we accurately reflect the cost of public vs. private education?
46. How should state vs. federal taxes be decoupled?
47. What is the financial impact of having a criminal record in the simulation?
48. How do we model inflation's impact on fixed-income retirees?
49. Should we include the economics of starting a family later vs. earlier?
50. How do we validate our financial models against real-world data?

## 🎨 Initial Design Issues

We have defined 30 core UI/UX elements that need designing before frontend implementation begins. These are tracked as GitHub issues with the `design` label.

1. Dashboard UX layout for the main simulation screen
2. Timeline visualization for 50+ years of simulated life
3. Monthly/Yearly financial report summary design
4. Financial graphs for net worth progression over time
5. Achievement system badges and unlock UX
6. Notification system for random life events
7. User Profile and character stats screen
8. Settings page for simulation parameters
9. Onboarding flow for new players
10. Scenario selection menu
11. Investment portfolio breakdown chart
12. Budget allocation sliders for monthly expenses
13. Mortgage and loan calculator pop-up interface
14. Job market and career selection screen
15. Real estate purchasing interface
16. End of Life summary and score screen
17. Dark mode vs. light mode color palettes
18. Mobile responsive layout for the main dashboard
19. Typography selection for readability of complex financial data
20. Iconography for different expense categories
21. Tooltip system for explaining complex financial terms
22. Taxation breakdown infographic UI
23. Education and skill-tree UI
24. News ticker for macroeconomic events
25. Shopping and major purchase catalog interface
26. Bank statement and transaction history log
27. Credit score speedometer/gauge design
28. Avatar customization for the simulated character
29. Loading screens with financial literacy tips
30. Accessibility (a11y) design for colorblindness and screen readers

## 🚀 Getting Started (Maintainers)

If you are a maintainer setting up this repository for the first time on GitHub:
1. Ensure your initial commit is pushed to GitHub (`git push -u origin main`).
2. Run the `./setup_github.sh` script to automatically generate all labels, milestones, research issues, and design issues via the GitHub CLI.
