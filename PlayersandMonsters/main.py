from PlayersandMonsters.elf import Elf
from PlayersandMonsters.hero import Hero
from PlayersandMonsters.soulMaster import SoulMaster
from PlayersandMonsters.wizard import Wizard

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
wizard = Wizard('W', 7)
print(wizard.username)
print(wizard.__class__.__bases__[0].__name__)
soulMaster = SoulMaster('Ergon', 16)
print(soulMaster.username)
print(soulMaster.level)
print(soulMaster.__class__.__bases__[0].__name__)