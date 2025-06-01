
🇷🇺 Для русской версии прокрутите вниз | For Russian version scroll down

# LogosTrinity

**LogosTrinity** — the core of trinary semantic logic and sense-based computation.

A modular library for modeling and translating semantic structures (STN, Semon-Trinary Network), supporting trinary logic, stream sense operations, natural language annotations, and temporal control.

---

## 📦 Project Structure:

LogosTrinity/
├── core/ # Core trinary logic and main modules
│ └── tests/ # Unit tests for the core
├── docs/ # Documentation, diagrams, theoretical notes
├── examples/ # Usage examples and demo scripts
├── scripts/ # Utilities, parsers, experiments
├── LICENSE.md # MIT License
├── requirements.txt
├── README.md
└── .gitignore

## 🚀 Quick Start:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yvgnysblv/LogosTrinity.git
   cd LogosTrinity
2.Install dependencies:
   pip install -r requirements.txt
3.Run tests:
pytest core/tests

Core Modules:

   core/node.py — STNNode class, main data structures.

   core/ternary_ops.py — Trinary logic operators (and, or, not, superpose, collapse).

   core/tempo.py — Temporal control operator (SPEED).

   core/stream_ops.py — Stream sense operations (map/reduce).

   core/annotation.py — Natural language annotation support.

Usage Example:
   from core.node import STNNode
   from core.tempo import SPEED

   n = STNNode(state=0, annotation="Input semon")
   SPEED(n, 2)
   print(n)

Documentation:

    Theory and diagrams — see docs/ folder

    Example scripts — in examples/

TODO / Roadmap:
    STN graph visualization

    REST/CLI interface

    Telegram bot integration

   Expanded trinary logic

   Automatic annotation generation

## 🤝 Contributing

We welcome contributions from the community!

- If you find a bug or want to suggest a feature, please open an [issue](https://github.com/yvgnysblv/LogosTrinity/issues).
- To contribute code:
    1. Fork the repository.
    2. Create a new branch for your changes.
    3. Make your edits and write tests if needed.
    4. Submit a pull request (PR) with a description of your changes.

**Requirements:**
- Follow PEP8 style for Python code.
- Add or update tests for your contributions.
- Write clear commit messages and PR descriptions.

For major changes, please open an issue to discuss what you would like to change first.


License: 

MIT License.
Free to use, modify, and distribute — copyright notice required.


## 📬 Contacts

- Author: Yevgeniy Sobolev 
- GitHub: [yvgnysblv](https://github.com/yvgnysblv)
- Email: yvgnysblv@yahoo.com
- Telegram: https://t.me/LogosTrinityOpenChat

If you have questions, ideas, or proposals for collaboration — feel free to contact! 




----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# LogosTrinity

**LogosTrinity** — ядро троичной смысловой логики и семантических вычислений.  
Модульная библиотека для моделирования и трансляции смысловых структур (STN, Semon-Trinary Network), поддержка троичной логики, операций с потоками смыслов, аннотаций и темпорального управления.

---

## 📦 Структура проекта:

LogosTrinity/
├── core/ # Ядро троичной логики, все основные модули
│ └── tests/ # Юнит-тесты для ядра
├── docs/ # Документация, схемы, теоретические описания
├── examples/ # Примеры использования библиотеки
├── scripts/ # Вспомогательные утилиты, парсеры и демо
├── LICENSE.md # Лицензия MIT
├── requirements.txt
├── README.md
└── .gitignore

##
---

## 🚀 Быстрый старт:

1. **Клонируйте репозиторий:**
   
   git clone https://github.com/yvgnysblv/LogosTrinity.git
   cd LogosTrinity
2.Установите зависимости:
   pip install -r requirements.txt
3.Запуск тестов:
   pytest core/tests

Основные модули:

   core/node.py — класс STNNode, основные структуры данных.

   core/ternary_ops.py — троичные логические операторы (and, or, not, superpose, collapse).

   core/tempo.py — оператор управления темпом событий (SPEED).

   core/stream_ops.py — функции для потоковой обработки смыслов (map/reduce).

   core/annotation.py — поддержка естественно-языковых аннотаций.

Пример использования:

   from core.node import STNNode
   from core.tempo import SPEED
 
   n = STNNode(state=0, annotation="Входной семон")
   SPEED(n, 2)
   print(n)


Документация:

   Теория и схемы — см. папку docs/

   Примеры скриптов — в examples/

TODO / Планы:

  Визуализация графа STN

  REST/CLI интерфейс

  Интеграция с Telegram-ботом

  Расширение троичной логики

  Автоматическая генерация аннотаций

Лицензия:

Свободное использование, модификация и распространение — с сохранением копирайта.

## 🤝 Как внести вклад

Мы приветствуем участие сообщества!

- Нашли баг или хотите предложить улучшение? Откройте [issue](https://github.com/yvgnysblv/LogosTrinity/issues).
- Чтобы внести изменения в код:
    1. Сделайте форк репозитория.
    2. Создайте новую ветку для ваших правок.
    3. Внесите изменения, добавьте тесты (если требуется).
    4. Оформите pull request с описанием изменений.

**Требования:**
- Соблюдайте PEP8 для Python-кода.
- Добавляйте или обновляйте тесты.
- Пишите понятные сообщения коммитов и pull request.

Перед значительными изменениями откройте issue для обсуждения!



## 📬 Contacts

- Author: Yevgeniy Sobolev 
- GitHub: [yvgnysblv](https://github.com/yvgnysblv)
- Email: yvgnysblv@yahoo.com
- Telegram: https://t.me/LogosTrinityOpenChat

If you have questions, ideas, or proposals for collaboration — feel free to contact! 

Если у Вас есть вопросы, идеи или предложения по сотрудничеству — не стесняйтесь обращаться!



