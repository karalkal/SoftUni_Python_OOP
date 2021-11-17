from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo

chicho1 = Cheetah("Cheeto", "Male", 2),
chicho2 = Cheetah("Cheetia", "Female", 1)
ivan1 = Lion("Simba", "Male", 4)
pesho1 = Tiger("Zuba", "Male", 3)
pesho2 = Tiger("Tigeria", "Female", 1)
ivan2 = Lion("Nala", "Female", 4)
print(chicho2, ivan2, pesho1, pesho2, sep="\n")
print(ivan1.money_for_care, pesho2.money_for_care, chicho2.money_for_care, sep="\n")
print()

john = Keeper("John", 26, 100)
adam = Keeper("Adam", 29, 80)
anna = Keeper("Anna", 31, 95)
bill = Caretaker("Bill", 21, 68)
marie = Caretaker("Marie", 32, 105)
stacy = Caretaker("Stacy", 35, 140)
peter = Vet("Peter", 40, 300)
kasey = Vet("Kasey", 37, 280)
sam = Vet("Sam", 29, 220)
print(john, bill, sam, anna, sep="  ----  ")
