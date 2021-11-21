from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []  # accepts Category objects
        self.topics = []  # accepts Topic objects
        self.documents = []  # accepts Document objects

    def add_category(self, category: Category):  # – add the category if it is not in the list
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):  # – add the topic if it does not exist
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):  # – add the document if it does not exist
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):  # – edit the name of the category with the provided id
        for this_cat in self.categories:
            if this_cat.id == category_id:
                this_cat.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):  # – edit the topic with the given id
        for this_topic in self.topics:
            if this_topic.id == topic_id:
                this_topic.edit(new_topic, new_storage_folder)


    def edit_document(self, document_id: int, new_file_name: str):  # – edit the document with the given id
        for this_doc in self.documents:
            if this_doc.id == document_id:
                this_doc.edit(new_file_name)

    def delete_category(self, category_id):  # – delete the category with the provided id
        for this_cat in self.categories:
            if this_cat.id == category_id:
                self.categories.remove(this_cat)

    def delete_topic(self, topic_id):  # – delete the topic with the provided id
        for this_topic in self.topics:
            if this_topic.id == topic_id:
                self.topics.remove(this_topic)

    def delete_document(self, document_id):  # – delete the document with the provided id
        for this_doc in self.documents:
            if this_doc.id == document_id:
                self.documents.remove(this_doc)

    def get_document(self, document_id):
        for this_doc in self.documents:
            if this_doc.id == document_id:
                return this_doc.__repr__()

    def __repr__(self):
        result = ""
        for doc in self.documents:
            result += doc.__repr__()
            result += "\n"
        return result
