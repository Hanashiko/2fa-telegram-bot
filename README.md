
# 🛡️ Aiogram 2FA Bot

Бот з двофакторною автентифікацією (2FA) на базі **Python** та **Aiogram**. Працює з базою даних для зберігання інформації про користувачів і використовує **Google Authenticator** для генерації одноразових кодів.

## 📁 Структура проєкту

```
.
├── database/             # Робота з БД (ORM, запити)
├── handlers/             # Обробники команд бота
├── .gitignore            # Ігноровані файли для Git
├── creaate_bot.py        # Ініціалізація бота та Dispatcher
├── main.py               # Точка входу в застосунок
├── requirements.txt      # Залежності Python
└── README.md             # Документація
```

## 🧪 Встановлення та запуск

1. **Клонувати репозиторій:**
```bash
git clone https://github.com/Hanashiko/2fa-telegram-bot.git
cd 2fa-telegram-bot
```

2. **Створити та активувати віртуальне середовище (опційно):**
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Встановити залежності:**
```bash
pip install -r requirements.txt
```

4. **Створити `.env` файл:**

> ⚠️ `.env` файл використовується для зберігання конфіденційних даних (не додавайте його до репозиторію).

```env
BOT_TOKEN=YOUR_BOT_TOKEN

LOG_CHAT=LOGGING_CHAT_ID
OWNER_ID=YOUR_TELEGRAM_ID

DB_HOST=localhost
DB_DATABASE=your_database
DB_USER=your_user
DB_PASSWORD=your_password
```

5. **Запуск бота:**
```bash
python main.py
```

## 📲 Команди бота

### 📦 Загальні команди
| Команда         | Опис                                                         |
|----------------|--------------------------------------------------------------|
| `/start`        | Запускає бота та додає ваш акаунт до бази даних             |
| `/make_qrcode`  | Генерує QR-код для додатку Google Authenticator             |
| `/check_2fa`    | Перевірка коду з Google Authenticator                       |
| `/cancel`       | Скасовує поточний стан FSM (Finite State Machine)           |

### 🛠️ Адмінські команди
> Доступні лише для `OWNER_ID` або авторизованих користувачів

| Команда               | Опис                                                |
|------------------------|-----------------------------------------------------|
| `/create_user_table`   | Створює таблицю користувачів у базі даних          |
| `/delete_user_table`   | Видаляє таблицю користувачів                       |
| `/get_users`           | Виводить список всіх зареєстрованих користувачів  |

## 🔐 Як працює 2FA

1. Користувач викликає команду `/make_qrcode`, бот генерує секретний ключ.
2. За цим ключем формується QR-код, який потрібно додати в Google Authenticator.
3. Після цього користувач може проходити 2FA, вводячи OTP код через `/check_2fa`.

## 🧾 Залежності

Усі залежності вказані в `requirements.txt`. Серед основних:

- `aiogram` — Telegram Bot Framework
- `python-dotenv` — для зчитування `.env` файлу
- `pyqrcode`, `pypng` — генерація QR-коду
- `pyotp` — генерація та перевірка одноразових кодів

## 🤝 Автор / Контакти

> Підтримку та пропозиції можна надсилати власнику бота.  
При бажанні – відкривайте issue або робіть pull request ✨
