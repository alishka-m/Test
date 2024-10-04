import os
import logging
import random
import sympy as sp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from decouple import config

# Инициализация бота
token = config('BOT_TOKEN')
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Уровень логирования
logging.basicConfig(level=logging.INFO)

# Состояния для машины состояний
class Form(StatesGroup):
    equation = State()
    system = State()
    derivative = State()
    integral = State()
    trigonometry = State()
    simple_math = State()
    english = State()
    history = State()

# Функции для математических операций
def solve_equation(equation):
    x = sp.symbols('x')
    solution = sp.solve(equation, x)
    return solution

def solve_system(equations):
    x, y = sp.symbols('x y')
    solutions = sp.solve(equations, (x, y))
    return solutions

def compute_derivative(expression):
    x = sp.symbols('x')
    derivative = sp.diff(expression, x)
    return derivative

def compute_integral(expression):
    x = sp.symbols('x')
    integral = sp.integrate(expression, x)
    return integral

def compute_trigonometric_function(func, angle):
    if func == 'sin':
        return sp.sin(sp.rad(angle))
    elif func == 'cos':
        return sp.cos(sp.rad(angle))
    elif func == 'tan':
        return sp.tan(sp.rad(angle))
    else:
        return "Unknown function"

def simple_math_problem():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)
    if operation == '/':
        num1 *= num2  # чтобы избежать деления на ноль
    return num1, operation, num2

# Исторические факты
history_facts = [
    "Древний Египет построил свои пирамиды примерно 2500 лет до нашей эры.",
    "Великая китайская стена была построена для защиты от завоевателей.",
    "Римская империя достигла своего пика в I веке нашей эры.",
]

# Слова для изучения английского языка
english_words = {
    "cat": "кот",
    "dog": "собака",
    "tree": "дерево",
    "house": "дом",
    "car": "машина"
}

# Команды бота
@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}! Я учебный бот. Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(commands=['pic'])
async def send_picture(message: types.Message):
    photo_path = os.path.join("картинки", "photo_2024-10-04_10-35-05.jpg")  # Укажите правильный путь к вашей картинке
    with open(photo_path, "rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="Вот ваша картинка!"
        )

def main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "Решить уравнение",
        "Решить систему уравнений",
        "Вычислить производную",
        "Вычислить интеграл",
        "Вычислить тригонометрическую функцию",
        "Решить простые примеры",
        "Изучить английский",
        "История"
    ]
    keyboard.add(*buttons)
    return keyboard

@dp.message_handler(lambda message: message.text == "Изучить английский")
async def handle_english(message: types.Message):
    word, translation = random.choice(list(english_words.items()))
    await message.answer(f"Как переводится '{word}'?")
    await Form.english.set()
    await dp.current_state().update_data(correct_translation=translation)

@dp.message_handler(state=Form.english)
async def receive_english_answer(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    correct_translation = data.get('correct_translation')

    if msg.text.lower() == correct_translation:
        await msg.answer("Правильно!")
    else:
        await msg.answer(f"Неправильно. Правильный ответ: {correct_translation}")

    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "История")
async def handle_history(message: types.Message):
    fact = random.choice(history_facts)
    await message.answer(f"Интересный факт: {fact}")
    await message.answer("Хотите узнать еще интересный факт?", reply_markup=yes_no_menu())

def yes_no_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Да", "Нет"]
    keyboard.add(*buttons)
    return keyboard

@dp.message_handler(lambda message: message.text == "Да")
async def handle_more_history(message: types.Message):
    fact = random.choice(history_facts)
    await message.answer(f"Интересный факт: {fact}")

@dp.message_handler(lambda message: message.text == "Нет")
async def handle_no_more_history(message: types.Message):
    await message.answer("Хорошо, выбирайте другую задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Решить уравнение")
async def handle_solve_equation(message: types.Message):
    await message.answer("Введите уравнение (например, x**2 - 4):")
    await Form.equation.set()

@dp.message_handler(state=Form.equation)
async def receive_equation(msg: types.Message, state: FSMContext):
    result = solve_equation(eval(msg.text))
    await msg.answer(f"Решение уравнения: {result}")
    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Решить систему уравнений")
async def handle_solve_system(message: types.Message):
    await message.answer("Введите систему уравнений (например, x + y - 10, x - y - 2):")
    await Form.system.set()

@dp.message_handler(state=Form.system)
async def receive_system(msg: types.Message, state: FSMContext):
    equations = [eval(eq) for eq in msg.text.split(',')]
    result = solve_system(equations)
    await msg.answer(f"Решение системы уравнений: {result}")
    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Вычислить производную")
async def handle_derivative(message: types.Message):
    await message.answer("Введите функцию для дифференцирования (например, x**3 + 2*x):")
    await Form.derivative.set()

@dp.message_handler(state=Form.derivative)
async def receive_derivative(msg: types.Message, state: FSMContext):
    result = compute_derivative(eval(msg.text))
    await msg.answer(f"Производная функции: {result}")
    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Вычислить интеграл")
async def handle_integral(message: types.Message):
    await message.answer("Введите функцию для интегрирования (например, x**2):")
    await Form.integral.set()

@dp.message_handler(state=Form.integral)
async def receive_integral(msg: types.Message, state: FSMContext):
    result = compute_integral(eval(msg.text))
    await msg.answer(f"Неопределенный интеграл функции: {result}")
    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Вычислить тригонометрическую функцию")
async def handle_trigonometry(message: types.Message):
    await message.answer("Введите тригонометрическую функцию (sin, cos, tan) и угол в градусах (например, sin 30):")
    await Form.trigonometry.set()

@dp.message_handler(state=Form.trigonometry)
async def receive_trigonometry(msg: types.Message, state: FSMContext):
    parts = msg.text.split()
    func = parts[0]
    angle = float(parts[1])
    result = compute_trigonometric_function(func, angle)
    await msg.answer(f"Результат: {result}")
    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

@dp.message_handler(lambda message: message.text == "Решить простые примеры")
async def handle_simple_math(message: types.Message):
    num1, operation, num2 = simple_math_problem()
    await message.answer(f"Решите: {num1} {operation} {num2}")
    await Form.simple_math.set()
    await dp.current_state().update_data(num1=num1, operation=operation, num2=num2)

@dp.message_handler(state=Form.simple_math)
async def receive_simple_math(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    num1 = data.get('num1')
    operation = data.get('operation')
    num2 = data.get('num2')

    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Неверная операция."

        await msg.answer(f"Результат: {result}")
    except Exception as e:
        await msg.answer(f"Произошла ошибка: {str(e)}")

    await state.finish()
    await msg.answer("Выберите задачу:", reply_markup=main_menu())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)