import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

# ==================================
# GOOGLE SHEETS CONNECTION
# ==================================

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

import os
import json
import tempfile

credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")

with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
    temp_file.write(credentials_json)
    temp_file.flush()

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        temp_file.name,
        scope
    )

client = gspread.authorize(creds)

sheet = client.open("Project Rebuild Memory")

logs_sheet = sheet.worksheet("Logs")
memory_sheet = sheet.worksheet("Memory")
habits_sheet = sheet.worksheet("Habits")
goals_sheet = sheet.worksheet("Goals")
schedule_sheet = sheet.worksheet("Schedule")
food_sheet = sheet.worksheet("Food")
score_sheet = sheet.worksheet("Score")

# ==================================
# LOGS
# ==================================

def save_log(user_id, name, message):

    logs_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        name,
        message
    ])


def get_log_count():

    records = logs_sheet.get_all_values()

    return max(0, len(records) - 1)


# ==================================
# MEMORY
# ==================================

def save_memory(user_id, memory_type, content):

    memory_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        memory_type,
        content
    ])


def get_memory_count():

    records = memory_sheet.get_all_values()

    return max(0, len(records) - 1)


# ==================================
# HABITS
# ==================================

def save_habit(user_id, habit, value):

    habits_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        habit,
        value
    ])


def get_today_habits(user_id):

    data = habits_sheet.get_all_records()

    today = datetime.now().strftime("%Y-%m-%d")

    result = {}

    for row in data:

        if str(row["UserID"]) == str(user_id):

            row_date = str(row["Date"])[:10]

            if row_date == today:

                result[row["Habit"]] = row["Value"]

    return result

# ==================================
# GET MEMORIES
# ==================================

def get_memories(user_id):

    data = memory_sheet.get_all_records()

    memories = []

    for row in data:

        if str(row["UserID"]) == str(user_id):
            memories.append(row["Content"])

    return memories

# ==================================
# WEEKLY ANALYTICS
# ==================================

def get_weekly_stats(user_id):

    data = habits_sheet.get_all_records()

    seven_days_ago = datetime.now() - timedelta(days=7)

    cigarettes = []
    water = []
    sleep = []

    for row in data:

        if str(row["UserID"]) != str(user_id):
            continue

        try:
            row_date = datetime.strptime(
                str(row["Date"])[:19],
                "%Y-%m-%d %H:%M:%S"
            )
        except:
            continue

        if row_date < seven_days_ago:
            continue

        habit = row["Habit"]
        value = row["Value"]

        try:
            value = float(value)
        except:
            continue

        if habit == "cigarettes":
            cigarettes.append(value)

        elif habit == "water":
            water.append(value)

        elif habit == "sleep":
            sleep.append(value)

    return {
        "avg_cigarettes": round(sum(cigarettes)/len(cigarettes), 1)
        if cigarettes else 0,

        "avg_water": round(sum(water)/len(water), 1)
        if water else 0,

        "avg_sleep": round(sum(sleep)/len(sleep), 1)
        if sleep else 0,

        "entries": len(data)
    }

# ==================================
# GOALS ENGINE
# ==================================

def save_goal(user_id, goal_name, target):

    goals_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        goal_name,
        target
    ])


def get_goals(user_id):

    data = goals_sheet.get_all_records()

    goals = {}

    for row in data:

        if str(row["UserID"]) == str(user_id):

            goals[row["Goal"]] = row["Target"]

    return goals

# ==================================
# STREAK ENGINE
# ==================================

def get_workout_streak(user_id):

    data = habits_sheet.get_all_records()

    workout_days = set()

    for row in data:

        if str(row["UserID"]) != str(user_id):
            continue

        if row["Habit"] != "workout":
            continue

        workout_days.add(
            str(row["Date"])[:10]
        )

    streak = 0

    current_day = datetime.now()

    while True:

        day_str = current_day.strftime("%Y-%m-%d")

        if day_str in workout_days:

            streak += 1
            current_day -= timedelta(days=1)

        else:
            break

    return streak

# ==================================
# SCHEDULE ENGINE
# ==================================

def save_schedule(user_id, state, value):

    schedule_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        state,
        value
    ])


def get_schedule(user_id):

    data = schedule_sheet.get_all_records()

    schedule = {}

    for row in data:

        if str(row["UserID"]) == str(user_id):

            schedule[row["State"]] = row["Value"]

    return schedule

# ==================================
# FOOD ENGINE
# ==================================

def save_food(user_id, meal_type, meal):

    food_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        meal_type,
        meal
    ])


def get_food(user_id):

    data = food_sheet.get_all_records()

    meals = []

    for row in data:

        if str(row["UserID"]) == str(user_id):

            meals.append(
                f"{row['Meal Type']} → {row['Meal']}"
            )

    return meals

# ==================================
# SCORE ENGINE
# ==================================

def save_score(user_id, score, grade):

    score_sheet.append_row([
        str(datetime.now()),
        str(user_id),
        score,
        grade
    ])