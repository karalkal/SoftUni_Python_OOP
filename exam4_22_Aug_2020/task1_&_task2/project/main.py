from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from rooms.young_couple import YoungCouple
from rooms.young_couple_with_children import YoungCoupleWithChildren
from people.child import Child
from everland import Everland

everland = Everland()

young_couple = YoungCouple("Johnsons", 150, 205)

child1 = Child(5, 1, 2, 1)
child2 = Child(3, 2)
young_couple_with_children = YoungCoupleWithChildren("Peterson", 600, 520, child1, child2)

everland.add_room(young_couple)
everland.add_room(young_couple_with_children)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())
print()

old_geezer = AloneOld("IVAN", 20)
young_buddy = AloneYoung("pesho", 9)

everland.add_room(old_geezer)
everland.add_room(young_buddy)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())
print()

young_buddy = AloneYoung("pesho2", 1000)
old_couple = OldCouple("old_couple", 500, 500)
young_couple = OldCouple("young_couple", 500, 500)

everland.add_room(young_buddy)
everland.add_room(old_couple)
everland.add_room(young_couple)

print(everland.get_monthly_consumptions())
print(everland.pay())
print(everland.status())
print()
