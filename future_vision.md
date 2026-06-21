# Project Rebuild Future Vision

Source: `C:\Users\Shabahat\Downloads\remember.json`

This document preserves the future direction for Project Rebuild so the next feature pass can continue from the deployed Telegram bot without re-discovering the product goals.

## Current State

- Codename: Jiraiya Sensei
- Current storage: Google Sheets
- Current deployment: Railway
- Current interface: Telegram bot commands
- Current architecture: modular command-based Python system

## Product Vision

Project Rebuild should evolve into a personal operating system for health, wealth, career, discipline, identity, family responsibility, and long-term growth.

The system should not behave like a generic chatbot. It should behave like a mentor, strategist, accountability partner, coach, and second brain that uses stored data before giving advice.

## Existing Modules

- Habit tracking: smoking, water, sleep, weight, workout
- Food tracking
- Schedule tracking
- Memory engine
- Goal engine
- Identity engine
- Weekly analytics
- Daily score
- Workout streak engine
- Rule-based Sensei report

## Future Sensei Roles

### Health Coach

Responsibilities:

- Analyze smoking trends
- Analyze sleep trends
- Analyze hydration trends
- Analyze workout consistency
- Analyze food quality
- Identify root causes
- Suggest actionable improvements

Example insights:

- Smoking increased after sleep dropped.
- Water intake decreases on workdays.
- Workout consistency improves when sleep exceeds 7 hours.

### Financial Coach

Responsibilities:

- Track debts
- Track monthly savings
- Track income
- Track expenses
- Suggest debt repayment priorities
- Detect wasteful spending
- Build financial discipline

Known debts from the planning file:

- Shakeeb: 100000
- Priyanka: 112000
- Oday: 20000
- Irfan: 10000
- Shaker Mama: 50000

Known salary from the planning file:

- 40000

Future finance commands:

- `/expense`
- `/income`
- `/budget`
- `/debt`
- `/finance`

### Career Coach

Responsibilities:

- Monitor learning progress
- Track AI projects
- Track portfolio projects
- Track certifications
- Track job applications
- Recommend next career actions

Career targets:

- AI Automation Engineer
- Agent Engineer
- LLMOps
- Automation Consultant

### Identity Coach

Responsibilities:

- Protect the long-term mission
- Monitor habits
- Monitor discipline
- Monitor consistency
- Track personal growth

Identity statements:

- Responsible Father
- Disciplined Professional
- Healthy Athlete
- AI Builder
- Financially Responsible Man

## Future Memory System

Short-term memory:

- Today's habits
- Today's meals
- Today's score

Mid-term memory:

- 7-day trends
- 30-day trends

Long-term memory:

- Life goals
- Personal beliefs
- Career objectives
- Family responsibilities
- Financial obligations

## Future Sensei Behavior

Must do:

- Explain why a recommendation is made.
- Reference historical data.
- Reference trends.
- Reference goals.
- Identify bottlenecks.
- Prioritize highest-impact improvements.

Must not do:

- Give generic motivational speeches.
- Ignore stored data.
- Give advice without evidence.
- Act like a simple chatbot.

## Suggested Next Feature Phase

The best next phase is the finance foundation, because it has clear commands, clear data shapes, and high long-term value.

Recommended order:

1. Add Google Sheets worksheets for finance data.
2. Add `/expense`, `/income`, and `/debt` logging commands.
3. Add `/budget` and `/finance` summary commands.
4. Add simple rule-based finance insights before adding AI.
5. Later, connect AI coaching to Sheets-backed health, finance, career, and identity memory.
