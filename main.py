
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from telegram import BotCommand

async def setup_commands(app):

    commands = [
    BotCommand("today", "Today's summary"),
    BotCommand("week", "Weekly analytics"),
    BotCommand("status", "Current status"),
    BotCommand("score", "Daily score"),

    BotCommand("smoke", "Log cigarettes"),
    BotCommand("water", "Log water"),
    BotCommand("weight", "Log weight"),
    BotCommand("sleep", "Log sleep"),
    BotCommand("workout", "Log workout"),

    BotCommand("food", "Log food"),
    BotCommand("foodlog", "View food log"),

    BotCommand("setschedule", "Set schedule"),
    BotCommand("schedule", "View schedule"),

    BotCommand("setgoal", "Create goal"),
    BotCommand("goals", "View goals"),
    BotCommand("progress", "Goal progress"),

    BotCommand("identity", "View identity"),
    BotCommand("streak", "Workout streak"),

    BotCommand("remember", "Store memory"),
    BotCommand("memories", "View memories"),

    BotCommand("sensei", "Daily coaching"),
    BotCommand("reset", "Reset tracker")
]

    await app.bot.set_my_commands(commands)

from config import BOT_TOKEN

from sheets import (
    save_log,
    get_log_count,
    get_memory_count,
    save_habit,
    get_today_habits,
    save_goal,
    get_goals,
    save_memory,
    get_memories,
    get_workout_streak,
    get_weekly_stats,
    save_schedule,
    get_schedule,
    save_food,
    get_food,
    save_score,
)

# ==================================
# START
# ==================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("/start received")
    await update.message.reply_text(
        "🔥 Project Rebuild Activated"
    )


# ==================================
# HELP
# ==================================

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
    "/today\n"
    "/week\n"
    "/status\n\n"
    "/smoke 3\n"
    "/water 2\n"
    "/weight 50\n"
    "/sleep 7\n"
    "/workout yes\n\n"
    "/setgoal cigarettes 0\n"
    "/goals\n"
    "/progress\n"
    "/streak\n\n"
    "/remember text\n"
    "/memories\n"
    "/sensei\n"
    "/food\n"
    "/foodlog\n\n"
    "/setschedule\n"
    "/schedule\n\n"
    "/identity\n"
    "/score\n"
    "/reset"
)

# ==================================
# SMOKE
# ==================================

async def smoke(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage: /smoke 3"
        )
        return

    value = context.args[0]

    save_habit(
        update.effective_user.id,
        "cigarettes",
        value
    )

    await update.message.reply_text(
        f"🚬 Cigarettes Logged: {value}"
    )


# ==================================
# WATER
# ==================================

async def water(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage: /water 2"
        )
        return

    value = context.args[0]

    save_habit(
        update.effective_user.id,
        "water",
        value
    )

    await update.message.reply_text(
        f"💧 Water Logged: {value}L"
    )


# ==================================
# WEIGHT
# ==================================

async def weight(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage: /weight 50"
        )
        return

    value = context.args[0]

    save_habit(
        update.effective_user.id,
        "weight",
        value
    )

    await update.message.reply_text(
        f"⚖️ Weight Logged: {value}kg"
    )


# ==================================
# SLEEP
# ==================================

async def sleep(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage: /sleep 7"
        )
        return

    value = context.args[0]

    save_habit(
        update.effective_user.id,
        "sleep",
        value
    )

    await update.message.reply_text(
        f"😴 Sleep Logged: {value} hrs"
    )

# ==================================
# WORKOUT
# ==================================

async def workout(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:
        await update.message.reply_text(
            "Usage: /workout yes"
        )
        return

    value = context.args[0]

    save_habit(
        update.effective_user.id,
        "workout",
        value
    )

    await update.message.reply_text(
        f"🏋️ Workout Logged: {value}"
    )

# ==================================
# STATUS
# ==================================

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    habits = get_today_habits(user_id)

    smoke_count = habits.get("cigarettes", 0)
    water_count = habits.get("water", 0)
    weight_value = habits.get("weight", "N/A")
    sleep_hours = habits.get("sleep", "N/A")
    workout_status = habits.get("workout", "No")

    await update.message.reply_text(
        f"📊 Today's Status\n\n"
        f"🚬 Cigarettes: {smoke_count}\n"
        f"💧 Water: {water_count}L\n"
        f"⚖️ Weight: {weight_value}kg\n"
        f"😴 Sleep: {sleep_hours} hrs\n"
        f"🏋️ Workout: {workout_status}"
    )


# ==================================
# MESSAGE LOGGER
# ==================================

async def log_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id
    name = update.effective_user.first_name
    message = update.message.text

    print(
        f"[MESSAGE] User:{user_id} | "
        f"Name:{name} | "
        f"Text:{message}"
    )

    save_log(
        user_id,
        name,
        message
    )

    await update.message.reply_text("✅ Logged")

# ==================================
# TODAY
# ==================================

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    habits = get_today_habits(user_id)

    smoke_count = habits.get("cigarettes", 0)
    water_count = habits.get("water", 0)
    weight_value = habits.get("weight", "N/A")
    sleep_hours = habits.get("sleep", "N/A")
    workout_status = habits.get("workout", "No")

    await update.message.reply_text(
        f"📊 Today's Summary\n\n"
        f"🚬 Cigarettes: {smoke_count}\n"
        f"💧 Water: {water_count}L\n"
        f"⚖️ Weight: {weight_value}kg\n"
        f"😴 Sleep: {sleep_hours} hrs\n"
        f"🏋️ Workout: {workout_status}"
    )

# ==================================
# WEEK
# ==================================

async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    stats = get_weekly_stats(user_id)

    await update.message.reply_text(
        f"📈 Weekly Report\n\n"
        f"🚬 Avg Cigarettes: {stats['avg_cigarettes']}/day\n"
        f"💧 Avg Water: {stats['avg_water']}L/day\n"
        f"😴 Avg Sleep: {stats['avg_sleep']} hrs/day\n\n"
        f"📝 Entries Logged: {stats['entries']}"
    )

# ==================================
# GOALS
# ==================================

async def goals(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    goals_data = get_goals(user_id)

    if not goals_data:

        await update.message.reply_text(
            "No goals set yet."
        )
        return

    response = "🎯 Current Goals\n\n"

    for goal, target in goals_data.items():

        response += f"• {goal} → {target}\n"

    await update.message.reply_text(response)

# ==================================
# SET GOAL
# ==================================

async def setgoal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:

        await update.message.reply_text(
            "Usage:\n/setgoal cigarettes 0"
        )
        return

    goal_name = context.args[0]
    target = context.args[1]

    save_goal(
        update.effective_user.id,
        goal_name,
        target
    )

    await update.message.reply_text(
        f"🎯 Goal Saved\n\n"
        f"{goal_name} → {target}"
    )

# ==================================
# PROGRESS
# ==================================

async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    goals_data = get_goals(user_id)

    habits = get_today_habits(user_id)

    if not goals_data:

        await update.message.reply_text(
            "No goals configured."
        )
        return

    response = "📈 Goal Progress\n\n"

    for goal, target in goals_data.items():

        current = habits.get(goal, "No Data")

        response += (
            f"{goal}\n"
            f"Target: {target}\n"
            f"Current: {current}\n\n"
        )

    await update.message.reply_text(response)    


# ==================================
# REMEMBER
# ==================================

async def remember(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) == 0:

        await update.message.reply_text(
            "Usage:\n/remember Your memory here"
        )
        return

    memory_text = " ".join(context.args)

    save_memory(
        update.effective_user.id,
        "memory",
        memory_text
    )

    await update.message.reply_text(
        f"🧠 Memory Stored:\n\n{memory_text}"
    )

# ==================================
# MEMORIES
# ==================================

async def memories(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    memory_list = get_memories(user_id)

    if not memory_list:

        await update.message.reply_text(
            "No memories stored yet."
        )
        return

    response = "🧠 Stored Memories\n\n"

    for memory in memory_list:
        response += f"• {memory}\n"

    await update.message.reply_text(response)

# ==================================
# STREAK
# ==================================

async def streak(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    streak_count = get_workout_streak(user_id)

    await update.message.reply_text(
        f"🔥 Workout Streak\n\n"
        f"Current Streak: {streak_count} day(s)"
    )    

# ==================================
# SET SCHEDULE
# ==================================

async def setschedule(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:

        await update.message.reply_text(
            "Usage:\n/setschedule sleep 09:00-16:00"
        )
        return

    state = context.args[0]
    value = " ".join(context.args[1:])

    save_schedule(
        update.effective_user.id,
        state,
        value
    )

    await update.message.reply_text(
        f"📅 Schedule Saved\n\n"
        f"{state}: {value}"
    )

# ==================================
# SCHEDULE
# ==================================

async def schedule(update: Update, context: ContextTypes.DEFAULT_TYPE):

    schedule_data = get_schedule(
        update.effective_user.id
    )

    if not schedule_data:

        await update.message.reply_text(
            "No schedule configured."
        )
        return

    response = "📅 Your Schedule\n\n"

    for state, value in schedule_data.items():

        response += (
            f"{state}: {value}\n"
        )

    await update.message.reply_text(response)

# ==================================
# FOOD
# ==================================

async def food(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if len(context.args) < 2:

        await update.message.reply_text(
            "Usage:\n/food breakfast 4 eggs"
        )
        return

    meal_type = context.args[0]
    meal = " ".join(context.args[1:])

    save_food(
        update.effective_user.id,
        meal_type,
        meal
    )

    await update.message.reply_text(
        f"🍽 Food Logged\n\n"
        f"{meal_type}: {meal}"
    )
    
# ==================================
# FOOD LOG
# ==================================

async def foodlog(update: Update, context: ContextTypes.DEFAULT_TYPE):

    meals = get_food(
        update.effective_user.id
    )

    if not meals:

        await update.message.reply_text(
            "No meals logged."
        )
        return

    response = "🍽 Food Log\n\n"

    for meal in meals:

        response += f"• {meal}\n"

    await update.message.reply_text(response)

# ==================================
# IDENTITY
# ==================================

async def identity(update: Update, context: ContextTypes.DEFAULT_TYPE):

    goals_data = get_goals(
        update.effective_user.id
    )

    streak_count = get_workout_streak(
        update.effective_user.id
    )

    response = (
        "⚔ PROJECT REBUILD\n\n"
        "Current Identity\n\n"
        f"🔥 Workout Streak: {streak_count}\n\n"
    )

    if goals_data:

        response += "🎯 Active Goals\n"

        for goal, target in goals_data.items():

            response += (
                f"• {goal}: {target}\n"
            )

    await update.message.reply_text(response)                

# ==================================
# SCORE
# ==================================

async def score(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    habits = get_today_habits(user_id)

    smoke = float(habits.get("cigarettes", 0))
    water = float(habits.get("water", 0))
    sleep = float(habits.get("sleep", 0))

    workout = str(
        habits.get("workout", "no")
    ).lower()

    total = 0

    # Smoking

    if smoke == 0:
        total += 25
    elif smoke <= 3:
        total += 20
    elif smoke <= 6:
        total += 15
    elif smoke <= 10:
        total += 10
    else:
        total += 5

    # Water

    if water >= 3:
        total += 25
    elif water >= 2:
        total += 20
    elif water >= 1:
        total += 10

    # Sleep

    if sleep >= 7:
        total += 25
    elif sleep >= 6:
        total += 20
    elif sleep >= 5:
        total += 10

    # Workout

    if workout == "yes":
        total += 25

    # Grade

    if total >= 90:
        grade = "A+"
    elif total >= 80:
        grade = "A"
    elif total >= 70:
        grade = "B"
    elif total >= 60:
        grade = "C"
    else:
        grade = "D"

    save_score(
        user_id,
        total,
        grade
    )

    await update.message.reply_text(
        f"🏆 Daily Score\n\n"
        f"Score: {total}/100\n"
        f"Grade: {grade}"
    )

# ==================================
# SENSEI
# ==================================

async def sensei(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    habits = get_today_habits(user_id)

    smoke = float(habits.get("cigarettes", 0))
    water = float(habits.get("water", 0))
    sleep = float(habits.get("sleep", 0))

    report = "🧠 Sensei Report\n\n"

    # Smoking Analysis
    if smoke >= 10:
        report += (
            "⚠ Smoking Risk High\n"
            f"Current: {smoke}\n\n"
        )
    elif smoke > 0:
        report += (
            "🚬 Smoking Recorded\n"
            f"Current: {smoke}\n\n"
        )
    else:
        report += (
            "✅ No cigarettes logged today\n\n"
        )

    # Water Analysis
    if water < 2:
        report += (
            "💧 Water Intake Low\n"
            f"Current: {water}L\n"
            "Target: 3L\n\n"
        )
    else:
        report += (
            "✅ Hydration Good\n\n"
        )

    # Sleep Analysis
    if sleep < 6:
        report += (
            "😴 Sleep Below Target\n"
            f"Current: {sleep} hrs\n"
            "Target: 7 hrs\n\n"
        )
    else:
        report += (
            "✅ Sleep Healthy\n\n"
        )

    # Workout Analysis
    streak_count = get_workout_streak(user_id)

    report += (
        f"🔥 Workout Streak: {streak_count} day(s)\n\n"
    )

    # Final Recommendation
    report += (
        "🎯 Focus Today:\n"
        "- Drink more water\n"
        "- Protect sleep\n"
        "- Reduce cigarettes"
    )

    await update.message.reply_text(report)

# ==================================
# RESET
# ==================================

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔄 Reset feature coming soon."
    )  

# ==================================
# MAIN
# ==================================

# ==================================
# MAIN
# ==================================

def main():

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(setup_commands)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("today", today))
    app.add_handler(CommandHandler("week", week))
    app.add_handler(CommandHandler("goals", goals))
    app.add_handler(CommandHandler("setgoal", setgoal))
    app.add_handler(CommandHandler("progress", progress))
    app.add_handler(CommandHandler("sensei", sensei))
    app.add_handler(CommandHandler("streak", streak))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("smoke", smoke))
    app.add_handler(CommandHandler("water", water))
    app.add_handler(CommandHandler("weight", weight))
    app.add_handler(CommandHandler("sleep", sleep))
    app.add_handler(CommandHandler("workout", workout))
    app.add_handler(CommandHandler("remember", remember))
    app.add_handler(CommandHandler("memories", memories))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(CommandHandler("setschedule", setschedule))
    app.add_handler(CommandHandler("schedule", schedule))
    app.add_handler(CommandHandler("food", food))
    app.add_handler(CommandHandler("foodlog", foodlog))
    app.add_handler(CommandHandler("identity", identity))
    app.add_handler(CommandHandler("score", score))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,log_message))

    print("🚀 Project Rebuild Running")

    app.run_polling()


if __name__ == "__main__":
    main()
