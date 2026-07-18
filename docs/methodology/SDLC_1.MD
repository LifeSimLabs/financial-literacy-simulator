# Software Development Life Cycle (SDLC) and Project Management Methodology

## 1. Introduction

Software development is not only about writing code. A successful software project requires proper planning, requirement analysis, development, testing, deployment, maintenance, and collaboration among team members.

To manage these activities effectively, software development teams use structured approaches such as the **Software Development Life Cycle (SDLC)** and project management methodologies such as **Agile** and **Scrum**.

This document explains the basic concepts of:

* Software Development Life Cycle (SDLC)
* SDLC Models
* Agile Methodology
* Scrum Framework
* Sprints
* Jira
* GitHub Issues and GitHub Projects
* Recommended methodology for the Financial Literacy Simulator

The goal is to identify a practical development and project management approach for the **Financial Literacy Simulator**, especially considering that it is an open-source project where multiple contributors may collaborate asynchronously.

---

# 2. What is SDLC?

**SDLC** stands for **Software Development Life Cycle**.

It is a structured process followed by software development teams to plan, design, develop, test, deploy, and maintain software applications.

In simple terms, SDLC provides a roadmap for developing software from the initial idea to the final product and its continued maintenance.

Instead of directly starting to write code, developers first understand:

* What problem needs to be solved?
* Who will use the software?
* What features are required?
* How should the system be designed?
* How will the software be tested?
* How will it be deployed?
* How will future bugs and updates be handled?

Following an SDLC helps development teams build software in an organized and systematic way.

---

# 3. Why is SDLC Important?

SDLC helps software development teams:

* Clearly understand project requirements.
* Organize development activities.
* Estimate project resources and timelines.
* Reduce development risks.
* Improve software quality.
* Detect problems earlier.
* Improve communication between team members.
* Manage changes effectively.
* Maintain software after deployment.

For an open-source project, SDLC also provides contributors with a clear understanding of how an idea moves from an issue to an implemented and tested feature.

---

# 4. Main Phases of SDLC

A typical SDLC consists of the following phases.

## 4.1 Planning

Planning is the first stage of software development.

During this phase, the team identifies:

* The purpose of the project.
* The problem being solved.
* Target users.
* Project scope.
* Required resources.
* Possible risks.
* High-level development goals.

For the Financial Literacy Simulator, planning may involve deciding which financial concepts should be simulated and what learning outcomes the application should provide.

---

## 4.2 Requirement Analysis

In this phase, the team gathers and analyzes the functional and non-functional requirements of the software.

### Functional Requirements

These describe what the application should do.

Examples:

* Users should be able to create an account.
* Users should be able to simulate a monthly budget.
* Users should be able to track income and expenses.
* Users should receive results based on their financial decisions.

### Non-Functional Requirements

These describe how the system should perform.

Examples:

* The application should be secure.
* The interface should be easy to use.
* The application should respond quickly.
* User data should be handled safely.

Clear requirements help prevent confusion during development.

---

## 4.3 System Design

During the design phase, the technical structure of the application is planned.

This may include:

* System architecture.
* Database design.
* API design.
* User interface design.
* Technology selection.
* Security design.
* Data flow.

A good design provides developers with a blueprint before implementation begins.

---

## 4.4 Development

During the development phase, developers write the actual code.

Developers may:

* Create frontend components.
* Develop backend APIs.
* Design and connect databases.
* Implement financial simulation logic.
* Integrate authentication.
* Add required features.

In an open-source project, contributors typically work on separate issues using individual Git branches.

---

## 4.5 Testing

Testing ensures that the software works correctly and meets the defined requirements.

Common types of testing include:

* Unit Testing
* Integration Testing
* System Testing
* User Interface Testing
* Performance Testing
* Security Testing
* User Acceptance Testing

Testing helps identify bugs before software reaches users.

---

## 4.6 Deployment

Deployment is the process of making the application available to users.

Depending on the project, deployment may include:

* Building the application.
* Configuring the production environment.
* Deploying the backend.
* Deploying the frontend.
* Configuring the database.
* Monitoring the application.

Modern development teams often use Continuous Integration and Continuous Deployment (CI/CD) to automate parts of this process.

---

## 4.7 Maintenance

Software development does not end after deployment.

During maintenance, developers:

* Fix bugs.
* Improve performance.
* Resolve security vulnerabilities.
* Update dependencies.
* Add new features.
* Improve existing functionality.

For an open-source project, maintenance is often continuous because users and contributors can report new issues and suggest improvements.

---

# 5. Common SDLC Models

Different projects use different SDLC models depending on their requirements.

Some common models are:

## 5.1 Waterfall Model

The Waterfall model follows a sequential approach.

Each phase must generally be completed before moving to the next phase.

The flow is:

`Requirements → Design → Development → Testing → Deployment → Maintenance`

### Advantages

* Easy to understand.
* Clearly defined phases.
* Suitable when requirements are stable.

### Limitations

* Difficult to handle changing requirements.
* Feedback may arrive late.
* Problems may only be discovered during later stages.

---

## 5.2 Iterative Model

In the Iterative model, software is developed and improved through repeated development cycles.

A basic version is created first and then enhanced over time.

This allows teams to learn from earlier versions and improve future iterations.

---

## 5.3 Incremental Model

The Incremental model divides the application into smaller features or modules.

Each increment adds new functionality to the system.

For example, the Financial Literacy Simulator could be developed incrementally:

1. User authentication
2. Budget simulator
3. Savings simulator
4. Investment simulator
5. Financial reports

---

## 5.4 Agile Model

Agile focuses on iterative development, continuous feedback, collaboration, and adapting to changing requirements.

Instead of waiting until the entire project is complete, teams deliver smaller pieces of working software frequently.

This makes Agile suitable for projects where requirements may evolve over time.

---

# 6. What is Agile Methodology?

Agile is a flexible and iterative approach to software development.

Traditional development approaches often try to define most requirements at the beginning of a project. Agile recognizes that software requirements can change based on user feedback, technical challenges, and new ideas.

Agile development focuses on:

* Working software.
* Frequent delivery.
* Customer and user feedback.
* Team collaboration.
* Continuous improvement.
* Responding to change.

Development work is divided into smaller tasks that can be implemented and reviewed independently.

---

# 7. How Agile Development Works

A simplified Agile development cycle can be represented as:

`Plan → Develop → Test → Review → Get Feedback → Improve → Repeat`

Instead of performing these activities only once, the cycle is repeated throughout the project.

For example, the Financial Literacy Simulator could first release a simple budgeting feature.

Users could test it and provide feedback.

The development team could then improve the feature before moving on to more advanced financial simulations.

This allows the project to evolve based on actual user needs.

---

# 8. Benefits of Agile

Agile provides several advantages:

### Flexibility

Requirements can change as the project evolves.

### Faster Delivery

Small features can be completed and released without waiting for the entire application.

### Continuous Feedback

Users and contributors can provide feedback throughout development.

### Early Problem Detection

Frequent testing and reviews help identify issues earlier.

### Better Collaboration

Developers, maintainers, and contributors can communicate regularly.

### Continuous Improvement

The development process and the software can improve after every iteration.

---

# 9. What is Scrum?

**Scrum** is a popular Agile framework used to organize and manage development work.

Agile provides general principles for flexible software development, while Scrum provides a more structured framework for applying Agile practices.

Scrum divides development work into short development cycles known as **Sprints**.

The team selects tasks, works on them during the Sprint, reviews the completed work, and then plans the next Sprint.

---

# 10. Scrum Roles

A traditional Scrum team includes three main responsibilities.

## 10.1 Product Owner

The Product Owner focuses on maximizing the value of the product.

Responsibilities include:

* Defining product priorities.
* Managing the Product Backlog.
* Clarifying requirements.
* Prioritizing features.

In an open-source project, maintainers may perform responsibilities similar to those of a Product Owner.

---

## 10.2 Scrum Master

The Scrum Master helps the team understand and apply Scrum practices.

Responsibilities may include:

* Helping remove blockers.
* Facilitating Scrum activities.
* Improving team collaboration.
* Supporting continuous improvement.

Open-source projects may not always have a dedicated Scrum Master.

---

## 10.3 Developers

Developers are responsible for creating the product.

Their activities may include:

* Designing features.
* Writing code.
* Testing.
* Fixing bugs.
* Reviewing Pull Requests.
* Improving documentation.

In open-source projects, community contributors can participate in these activities.

---

# 11. What is a Sprint?

A **Sprint** is a fixed period during which a team works toward a specific development goal.

Sprints commonly last between one and four weeks.

A typical Sprint may include:

### Sprint Planning

The team decides what work should be completed.

### Development

Developers work on selected tasks.

### Testing and Code Review

Changes are tested and reviewed.

### Sprint Review

The team reviews completed work.

### Sprint Retrospective

The team identifies what worked well and what could be improved.

The cycle then begins again for the next Sprint.

---

# 12. Product Backlog and Sprint Backlog

## Product Backlog

The Product Backlog contains the work that may need to be completed for the project.

It can include:

* Features.
* Bug fixes.
* Improvements.
* Documentation.
* Technical tasks.

## Sprint Backlog

The Sprint Backlog contains selected items that the team plans to work on during a specific Sprint.

In a GitHub-based open-source project, GitHub Issues can function similarly to backlog items.

---

# 13. What is Jira?

**Jira** is a project management and issue-tracking tool developed by Atlassian.

It is widely used by software development teams, particularly teams following Agile methodologies.

Jira can be used to manage:

* Tasks.
* Bugs.
* User stories.
* Epics.
* Backlogs.
* Sprints.
* Scrum boards.
* Kanban boards.

Each piece of work can be represented as an issue or ticket.

A common workflow might be:

`Backlog → To Do → In Progress → Code Review → Testing → Done`

This provides visibility into the current status of project work.

---

# 14. How Jira Helps Project Management

Jira helps teams:

* Assign tasks to team members.
* Track task progress.
* Prioritize development work.
* Manage backlogs.
* Plan Sprints.
* Track bugs.
* Visualize workflows.
* Generate project reports.

It is particularly useful for larger organizations that need structured workflows and advanced project tracking.

---

# 15. Jira vs GitHub Issues and GitHub Projects

The Financial Literacy Simulator is an open-source project hosted on GitHub.

Therefore, it is useful to compare Jira with GitHub's built-in project management capabilities.

| Feature                   | Jira                          | GitHub Issues / Projects                     |
| ------------------------- | ----------------------------- | -------------------------------------------- |
| Issue Tracking            | Yes                           | Yes                                          |
| Sprint Management         | Strong support                | Can be organized using iterations/milestones |
| Kanban Boards             | Yes                           | Yes                                          |
| Code Integration          | Requires integration          | Native GitHub integration                    |
| Pull Request Integration  | Available through integration | Native                                       |
| Open-Source Accessibility | Additional platform           | Directly available to contributors           |
| Setup Complexity          | Moderate to high              | Relatively simple                            |
| Best Use Case             | Enterprise and complex teams  | Developer and open-source projects           |

Jira is powerful for complex organizational workflows.

However, GitHub Issues and GitHub Projects can be more convenient for an open-source project because the source code, issues, discussions, and Pull Requests remain within the same platform.

---

# 16. Recommended Methodology for the Financial Literacy Simulator

For the **Financial Literacy Simulator**, the recommended approach is:

**Agile development with Scrum-inspired practices adapted for open-source collaboration.**

A strict implementation of Scrum may not be ideal for the project because open-source contributors may:

* Work from different locations.
* Have different schedules.
* Join or leave the project at different times.
* Contribute voluntarily.
* Work asynchronously.

Therefore, the project can adopt useful Scrum concepts without requiring every traditional Scrum ceremony.

---

# 17. Recommended Development Workflow

The following workflow can be used:

`Idea → GitHub Issue → Backlog → Assigned/In Progress → Development → Pull Request → Code Review → Testing → Merge → Done`

### Step 1: Create an Issue

New features, bugs, and improvements should be documented as GitHub Issues.

### Step 2: Prioritize the Backlog

Maintainers can prioritize issues based on project goals and user needs.

### Step 3: Assign or Select an Issue

Contributors can select appropriate issues to work on.

### Step 4: Create a Branch

Development should be performed in a separate Git branch.

### Step 5: Implement and Test

The contributor develops the feature and performs appropriate testing.

### Step 6: Submit a Pull Request

The contributor submits a Pull Request describing the changes.

### Step 7: Code Review

Maintainers or other contributors review the changes.

### Step 8: Testing

Automated tests and manual testing can verify the implementation.

### Step 9: Merge

After approval, the Pull Request is merged.

### Step 10: Continuous Improvement

Feedback and new requirements are converted into future issues.

---

# 18. Why Agile Suits the Financial Literacy Simulator

## 18.1 Changing Requirements

Financial rules, educational requirements, and user expectations can change.

Agile allows the project to adapt to these changes.

## 18.2 Incremental Feature Development

Different simulator modules can be developed independently.

Examples include:

* Budget planning.
* Savings simulation.
* Investment education.
* Loan and EMI simulation.
* Tax awareness.
* Financial quizzes.

## 18.3 Open-Source Collaboration

Clearly defined GitHub Issues allow contributors to work on manageable tasks independently.

## 18.4 Continuous User Feedback

Users can test new features and suggest improvements.

## 18.5 Better Software Quality

Pull Request reviews and continuous testing can help maintain code quality.

## 18.6 Transparency

GitHub Issues and Projects allow contributors to understand:

* What needs to be done.
* What is currently being developed.
* What has been completed.

---

# 19. Recommended Project Management Tools

For the current stage of the Financial Literacy Simulator, the recommended tools are:

### GitHub Issues

For:

* Bug reports.
* Feature requests.
* Documentation tasks.
* Development tasks.

### GitHub Projects

For organizing work into stages such as:

`Backlog → To Do → In Progress → In Review → Done`

### GitHub Pull Requests

For:

* Code submission.
* Code review.
* Discussions.
* Approval before merging.

### GitHub Milestones

For grouping issues related to:

* Releases.
* Development goals.
* Project phases.

Jira can be considered in the future if the project grows and requires more advanced Sprint management, reporting, or complex organizational workflows.

---

# 20. Final Recommendation

The Financial Literacy Simulator should follow an **Agile SDLC approach with Scrum-inspired practices**.

The project should not necessarily enforce strict Scrum because open-source development is often asynchronous.

Instead, the project should combine:

* Agile iterative development.
* Small and clearly defined GitHub Issues.
* A prioritized backlog.
* Sprint-like iterations or milestones.
* Feature branches.
* Pull Requests.
* Peer code reviews.
* Continuous testing.
* Continuous Integration.
* Regular releases.
* Continuous user and contributor feedback.

For project management, **GitHub Issues and GitHub Projects** are recommended as the primary tools.

This approach provides the flexibility of Agile, the organizational benefits of Scrum, and the simplicity required for an open-source development environment.

---

# 21. Conclusion

SDLC provides a structured foundation for developing software from initial planning through maintenance. Agile improves this process by allowing software to be developed iteratively while responding to changing requirements and continuous feedback.

Scrum provides useful practices such as backlogs, Sprints, planning, reviews, and retrospectives. However, strict Scrum may not always fit an asynchronous open-source community.

For the Financial Literacy Simulator, an **Agile approach with selected Scrum practices and GitHub-based project management** provides a practical balance between structure and flexibility.

Using GitHub Issues, GitHub Projects, Pull Requests, code reviews, and continuous testing will allow maintainers and contributors to collaborate effectively while continuously improving the Financial Literacy Simulator.
