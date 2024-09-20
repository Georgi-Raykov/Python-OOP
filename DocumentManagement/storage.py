from DocumentManagement.category import Category
from DocumentManagement.document import Document
from DocumentManagement.topic import Topic


class Storage:

    def __init__(self):

        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__find_category_by_id(category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__find_topic_by_id(topic_id)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.__find_document_by_id(document_id)

        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__find_category_by_id(category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_topic_by_id(topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):

        document = self.__find_document_by_id(document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):

        document = self.__find_document_by_id(document_id)
        return document

    def __str__(self):
        return '\n'.join([repr(x) for x in self.documents])

    def __find_category_by_id(self, id):
        for category in self.categories:
            if category.id == id:
                return category
        return None

    def __find_topic_by_id(self, id):

        for topic in self.topics:
            if topic.id == id:
                return topic
        return None

    def __find_document_by_id(self, id):
        for document in self.documents:

            if document.id == id:
                return document
        return None
