# tgx

Универсальная библиотека для Telegram-ботов на `python-telegram-bot`.

## Установка

```bash
pip install git+https://github.com/Stanislav-Shavlinsly/tgx.git
```

### Пример использования

```angular2html
from tgx import BaseBot, test_f

print(test_f(10))  # 20

bot = BaseBot("YOUR_BOT_TOKEN")
bot.run()
```
