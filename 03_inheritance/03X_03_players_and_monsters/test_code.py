from project.blade_knight import BladeKnight
from project.dark_knight import DarkKnight
from project.dark_wizard import DarkWizard
from project.elf import Elf
from project.hero import Hero
from project.knight import Knight
from project.muse_elf import MuseElf
from project.soul_master import SoulMaster
from project.wizard import Wizard

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
print()

elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
print()

muse = MuseElf("jiji", 77)
print(muse)
print()

wizi = Wizard("lklkl", 5)
print(wizi.username)
print(wizi)
print()

dary = DarkWizard("darktuy", 5)
print(dary.username)
print(dary)
print()

soul = SoulMaster("SM", 99)
print(soul)
print()

ricar = Knight("ricar", 666)
print(ricar)
print()

kur = DarkKnight("Kur", 78)
print(kur)
print()


blade = BladeKnight("blade", 88433)
print(blade)