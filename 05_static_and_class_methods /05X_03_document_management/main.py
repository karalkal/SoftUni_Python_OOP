from project.document import Document
from project.storage import Storage
from project.topic import Topic
from project.category import Category

t88 = Topic(88, "whatever", "C:\\work_documents")
print(t88)
t88.edit("new topic", "new folder")
print(t88)

c101 = Category(101, "drink")
c102 = Category(102, "enjoy wine")
c103 = Category(103, "travel")
c104 = Category(104, "fuck")
print(c101)
c101.edit("enjoy life")
print(c101)

docu = Document(44, 44, 2, "Nothing")
print(docu)
docu.remove_tag("empty")
docu.add_tag("this must be a tag")
docu.add_tag("another tag")
print(docu)
docu.remove_tag("another tag")
print(docu)

docu_class = Document.from_instances(69, c101, t88, "some file name")
print(docu_class)
docu_class.add_tag("this is the class instance")
print(docu_class)

docu.edit("New Name")
print(docu)
print()

my_storage = Storage()
my_storage.add_category(c101)
my_storage.add_category(c102)
my_storage.add_category(c103)
my_storage.add_category(c104)
my_storage.add_topic(t88)
my_storage.add_document(docu)
my_storage.add_document(docu_class)
print(my_storage)

print(t88)
my_storage.edit_topic(88, "this is changed", "changed folder")
print(t88)

print(c102)
my_storage.edit_category(102, "not wine now, but whisky")
print(c102)

print(docu_class)
my_storage.edit_document(69, "changed name of class instantiated object")
print(docu_class)

print()
#####
print()

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")
#
d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
#
print(c1)
print(t1)
# print(d1)
print(storage.get_document(1))
print(storage)
