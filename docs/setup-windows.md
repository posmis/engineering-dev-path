# Установка инструментов (Windows)

## Git

1. Скачать с <https://git-scm.com/download/win>, установить с настройками по умолчанию.
2. Представиться Git (один раз):
   ```bash
   git config --global user.name "Ваше Имя"
   git config --global user.email "ваш@email"
   ```
3. Клонировать репозиторий:
   ```bash
   git clone https://github.com/<ваш-логин>/engineering-dev-path.git
   ```

Альтернатива для новичка в Git — [GitHub Desktop](https://desktop.github.com/), но командная строка полезнее.

## Python

1. Скачать Python 3.12+ с <https://www.python.org/downloads/>.
2. При установке отметить **Add python.exe to PATH**.
3. Проверить: `python --version`.
4. Виртуальное окружение в папке проекта:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

## VS Code (для Python)

1. <https://code.visualstudio.com/>
2. Расширения: **Python**, **Pylance**, **Ruff**, **Jupyter**.
3. Выбрать интерпретатор из `.venv`: `Ctrl+Shift+P` → *Python: Select Interpreter*.

## Visual Studio (для C#, понадобится с проекта 02)

1. Visual Studio Community: <https://visualstudio.microsoft.com/>
2. Рабочие нагрузки: **Разработка классических приложений .NET**.
3. Для add-in'ов Inventor — версия .NET Framework / .NET должна соответствовать вашей версии Inventor (разберём в проекте 02).
