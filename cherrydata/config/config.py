import time

# Podstawowe parametry bota
TOKEN = "NTk2NDE5Njk1Mzg5OTY2MzQ2.XR5f8Q.LCyFkuGAWcGin9HRe3LMm4R_B8U"
bug_channel = 596762365857366039
bot_channel = 596424653816332299
commands_prefix = "!"
wersja = "0.15"
boot_date = time.strftime("%H:%M %d.%m.%Y UTC")
# Nazwy kategorii
CATEGORY_1 = "Błąd gry"
CATEGORY_2 = "Propozycja zmiany"
CATEGORY_3 = "Problem z botem"
CATEGORY_4 = "Inne"
# Rozszerzenia
__cogs__ = [
    "cherrydata.cogs.Utilities",
    "cherrydata.cogs.Entertainment"
    ]
