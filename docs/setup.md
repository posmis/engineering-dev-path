# Установка инструментов

Работа идёт на двух машинах: **macOS** и **Windows**. Различия по системам отмечены 🍎 / 🪟.

- [Git](#git)
- [Python](#python)
- [PyCharm и виртуальное окружение](#pycharm-и-виртуальное-окружение)
- [Работа на двух компьютерах](#работа-на-двух-компьютерах)
- [C#](#c)

---

## Git

- 🍎 Обычно уже есть: `git --version`. Если macOS предложит установить Command Line Tools — согласиться.
- 🪟 Скачать с <https://git-scm.com/download/win>, установить с настройками по умолчанию.

На **каждой** машине один раз:
```bash
git config --global user.name "Ваше Имя"
git config --global user.email "ваш@email"
git clone https://github.com/posmis/engineering-dev-path.git
```

---

## Python

Нужна версия 3.12+.

| | 🍎 macOS | 🪟 Windows |
|---|---|---|
| Установка | <https://www.python.org/downloads/macos/> или `brew install python@3.13` | <https://www.python.org/downloads/>, отметить **Add python.exe to PATH** |
| Команда | **`python3`** (просто `python` нет) | `python` |
| Проверка | `python3 --version` | `python --version` |

Внутри активированного виртуального окружения на обеих системах работает просто `python`.

---

## PyCharm и виртуальное окружение

Одно окружение `.venv` в корне репозитория на все Python-проекты. `.venv` указан в `.gitignore` и в репозиторий не попадает — **на каждой машине оно создаётся своё**.

### Через PyCharm

1. **File → Open** → корень репозитория `engineering-dev-path`.
2. Настройки: 🍎 **PyCharm → Settings** (`⌘,`) · 🪟 **File → Settings** (`Ctrl+Alt+S`).
3. **Project: engineering-dev-path → Python Interpreter → Add Interpreter → Add Local Interpreter → Virtualenv → New**:
   - **Location:** `<путь к репозиторию>/.venv`
   - **Base interpreter:** Python 3.12+

### Через терминал

Терминал в PyCharm: 🍎 `⌥F12` · 🪟 `Alt+F12`.

| | 🍎 macOS | 🪟 Windows |
|---|---|---|
| Создать | `python3 -m venv .venv` | `python -m venv .venv` |
| Активировать | `source .venv/bin/activate` | `.venv\Scripts\activate` |
| Интерпретатор для PyCharm (*Existing*) | `.venv/bin/python` | `.venv\Scripts\python.exe` |

### Запуск скрипта с аргументами

**Run → Edit Configurations → + → Python**:
- **Script path:** нужный `.py`
- **Script parameters:** аргументы, например `data/cube.obj`
- **Working directory:** папка проекта, например `python/01-obj-analyzer`

### Git в PyCharm

Текущая ветка — в правом нижнем углу (или в заголовке окна).
Коммит: 🍎 `⌘K` · 🪟 `Ctrl+K`. Push: 🍎 `⇧⌘K` · 🪟 `Ctrl+Shift+K`.
Первое время полезно делать всё через терминал, чтобы понимать, что происходит.

### Альтернатива: VS Code

<https://code.visualstudio.com/>, расширения **Python**, **Pylance**, **Ruff**, **Jupyter**.
Интерпретатор: `Ctrl+Shift+P` / `⇧⌘P` → *Python: Select Interpreter* → `.venv`.

---

## Работа на двух компьютерах

GitHub — единственный способ синхронизации между машинами.

- **Закончил на одной машине** → закоммитить и `git push` (даже незаконченную работу в своей ветке).
- **Начинаешь на другой** → `git fetch`, переключиться на ветку, `git pull`.
- Окончания строк: в репозитории всегда `LF` (настроено в `.gitattributes`), Git сам приводит их при коммите с Windows. Ничего делать не нужно.
- Пути в коде не хардкодить в стиле одной ОС (`C:\...` или `/Users/...`) — в Python для этого есть `pathlib`.

---

## C#

Понадобится с проекта 02.

- 🪟 Visual Studio Community (<https://visualstudio.microsoft.com/>), рабочая нагрузка **Разработка классических приложений .NET**. Или JetBrains Rider.
- 🍎 .NET SDK (<https://dotnet.microsoft.com/download>) и JetBrains Rider (интерфейс как у PyCharm) или VS Code с расширением C# Dev Kit.

Add-in'ы для Inventor разрабатываются и запускаются только на 🪟 Windows (Inventor не выпускается под macOS). Остальные C#-проекты (WPF — тоже только Windows; консольные утилиты, веб-API — на обеих системах) уточним при старте каждого проекта.
