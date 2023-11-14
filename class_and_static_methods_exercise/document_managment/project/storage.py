from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = list()
        self.topics = list()
        self.documents = list()

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.return_category(category_id)
        category.edit(new_name)

    def return_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        return category

    def return_topic(self, topic_id):
        topic = [t for t in self.topics if t.id == topic_id][0]
        return topic

    def get_document(self, document_id):
        document = [d for d in self.documents if d.id == document_id][0]
        return document

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.return_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove(self.return_category(category_id))

    def delete_topic(self, topic_id):
        self.topics.remove(self.return_topic(topic_id))

    def delete_document(self, document_id):
        self.documents.remove(self.get_document(document_id))

    def __repr__(self):
        return "\n".join([
            *[str(d) for d in self.documents]
        ])

