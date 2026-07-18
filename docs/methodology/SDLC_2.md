# Software Development Life Cycle (SDLC) & Agile Methodology

## 1. What is SDLC (Software Development Life Cycle)?
Think of SDLC as a recipe or a blueprint for building software. Just like you wouldn't build a house without a plan, you shouldn't build software without SDLC. It is a step-by-step process used by software teams to design, develop, and test high-quality software. 

A typical SDLC has 6 main phases:
1. **Planning & Requirement Analysis:** "What do we want to build and what problem does it solve?"
2. **Design:** "How will it look and work under the hood?"
3. **Development (Coding):** "Let's actually write the code."
4. **Testing:** "Does it work correctly? Are there bugs?"
5. **Deployment:** "Let's release it to the users."
6. **Maintenance:** "Let's fix issues and add updates."

## 2. What is the Agile Methodology?
Agile is a specific *type* of SDLC. In the old days, teams used the "Waterfall" method—they would try to plan the *entire* app, build the *entire* app, and then release it a year later. Often, by the time it was released, the users didn't want it anymore.

Agile fixes this by breaking the project into tiny, manageable chunks. Instead of building the whole app at once, you build a small feature, test it, get feedback, and then move to the next feature. 
* **Key Idea:** Move fast, adapt to changes, and release working software frequently.

## 3. What is Scrum, and what are Sprints?
If Agile is the *philosophy* (like "eat healthy"), Scrum is the *specific framework* to achieve it (like "the Keto diet"). Scrum is the most popular way to "do Agile."

* **Sprints:** In Scrum, work is divided into short, fixed timeframes called "Sprints" (usually 1 to 4 weeks long, most commonly 2 weeks). During a sprint, the team commits to finishing a specific set of tasks. Once the sprint is over, they review what they built and start a new sprint.
* **Roles in Scrum:** 
  * *Product Owner:* Decides *what* needs to be built (prioritizes tasks).
  * *Scrum Master:* Helps the team follow the process and removes roadblocks.
  * *Developers:* The people who actually build it.

## 4. What is Jira, and how is it used in project management?
Jira is a software tool created by Atlassian. It is the industry standard for managing Agile/Scrum projects. 

* **How it works:** It acts as a digital whiteboard. You create "Tickets" (or Issues) for every single task, bug, or feature. 
* **The Board:** Tickets move across a board through columns like `To Do`, `In Progress`, `In Review`, and `Done`. 
* **Why it's useful:** It gives the whole team visibility. Everyone knows exactly who is working on what, what the current priorities are, and how much progress has been made in the current Sprint.

## 5. Jira vs. GitHub Issues
While Jira is the industry standard for enterprise companies, our project lives on GitHub. Here is the difference:

* **GitHub Issues:** A lightweight, developer-friendly to-do list that lives right next to the code. Perfect for open-source projects. Because it's tied to the code, developers can type "Fixes #87" in a commit, and it automatically closes the issue.
* **Jira:** A heavy-duty, standalone enterprise project management tool. It tracks complex workflows, permissions, and multi-team timelines, but can be slow and requires a lot of setup.

## 6. Which methodology would best suit our specific project and why?
For the **Financial Literacy Simulator**, an **Agile methodology using the Scrum framework** is the best choice.

**Why?**
1. **Open Source & Community Driven:** We have multiple contributors working asynchronously. Agile allows us to break down complex tasks (like building a specific tax calculation module) into small tickets that contributors can pick up easily.
2. **Iterative Feedback:** We are building a simulator. We need to build a basic version, test it with users, see if it's actually fun and educational, and adjust. Agile embraces this kind of feedback loop.
3. **Changing Requirements:** As we learn more about the NCFE's guidelines or Indian financial rules, we will need to pivot. Agile makes it easy to change direction at the start of any new Sprint, whereas traditional methods would lock us into an outdated plan.

*Tooling Recommendation:* Since this is a public open-source project on GitHub, we can use **GitHub Issues** and **GitHub Projects** (which works almost exactly like Jira) to manage our Sprints and Kanban boards. It keeps the code and the project management in the exact same place!
