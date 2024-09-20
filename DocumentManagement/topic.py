class Topic:

    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage_folder):

        if self.topic != new_topic:
            self.topic = new_topic
        if self.storage_folder != new_storage_folder:
            self.storage_folder = new_storage_folder

    def __repr__(self):

        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
