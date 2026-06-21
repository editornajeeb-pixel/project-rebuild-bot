from telegram import ReplyKeyboardMarkup


DASHBOARD = "📊 Dashboard"
GOALS = "🎯 Goals"
NUTRITION = "🥗 Nutrition"
FITNESS = "💪 Fitness"
MEMORY = "🧠 Memory"
SCHEDULE = "📅 Schedule"
DISCIPLINE = "⚔️ Discipline"
SENSEI = "🎓 Sensei"
SETTINGS = "⚙️ Settings"
ANALYTICS = "📈 Analytics"
BACK = "🔙 Back"


MAIN_MENU_LAYOUT = [
    [DASHBOARD, GOALS],
    [NUTRITION, FITNESS],
    [MEMORY, SCHEDULE],
    [DISCIPLINE, SENSEI],
    [SETTINGS, ANALYTICS],
]


SUBMENU_LAYOUTS = {
    DASHBOARD: [
        ["📅 Today", "📈 Week"],
        ["🏆 Score", "📊 Status"],
        [BACK],
    ],
    GOALS: [
        ["➕ Add Goal", "📋 View Goals"],
        ["🎯 Current Goal"],
        [BACK],
    ],
    NUTRITION: [
        ["🍳 Log Food", "📊 Nutrition Summary"],
        [BACK],
    ],
    FITNESS: [
        ["🏋️ Log Workout", "🔥 Workout Streak"],
        ["📊 Fitness Summary"],
        [BACK],
    ],
    MEMORY: [
        ["📝 Remember", "📚 Recall Memories"],
        [BACK],
    ],
    SCHEDULE: [
        ["➕ Add Schedule", "📅 View Schedule"],
        [BACK],
    ],
    DISCIPLINE: [
        ["🚬 Log Smoke", "✅ Habit Complete"],
        ["🔥 Streaks"],
        [BACK],
    ],
    SENSEI: [
        ["🧠 Daily Advice", "📊 Analyze Progress"],
        ["⚡ Coaching"],
        [BACK],
    ],
    ANALYTICS: [
        ["📈 Weekly Analytics", "📊 Monthly Analytics"],
        [BACK],
    ],
    SETTINGS: [
        ["ℹ️ Help", "🔄 Refresh Menu"],
        [BACK],
    ],
}


MAIN_MENU_BUTTONS = set(SUBMENU_LAYOUTS)

ACTION_BUTTONS = {
    "📅 Today",
    "📈 Week",
    "🏆 Score",
    "📊 Status",
    "➕ Add Goal",
    "📋 View Goals",
    "🎯 Current Goal",
    "🍳 Log Food",
    "📊 Nutrition Summary",
    "🏋️ Log Workout",
    "🔥 Workout Streak",
    "📊 Fitness Summary",
    "📝 Remember",
    "📚 Recall Memories",
    "➕ Add Schedule",
    "📅 View Schedule",
    "🚬 Log Smoke",
    "✅ Habit Complete",
    "🔥 Streaks",
    "🧠 Daily Advice",
    "📊 Analyze Progress",
    "⚡ Coaching",
    "📈 Weekly Analytics",
    "📊 Monthly Analytics",
    "ℹ️ Help",
    "🔄 Refresh Menu",
    BACK,
}

MENU_BUTTONS = sorted(MAIN_MENU_BUTTONS | ACTION_BUTTONS)


def main_menu():
    return ReplyKeyboardMarkup(
        MAIN_MENU_LAYOUT,
        resize_keyboard=True,
        is_persistent=True,
    )


def submenu(name):
    return ReplyKeyboardMarkup(
        SUBMENU_LAYOUTS[name],
        resize_keyboard=True,
        is_persistent=True,
    )
