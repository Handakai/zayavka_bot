from aiogram.dispatcher.filters.state import State, StatesGroup

class main(StatesGroup):
    waiting_for_greet = State()
    waiting_for_rules_confirmation = State()
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    summary_confirmation = State()

# Reddington - t.me/RichmondSeller
