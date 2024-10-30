from robots_app.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name):
        super().__init__(name, capacity=15)

    def details(self):
        result = f"{self.name} Secondary Service:\n"
        if self.robots:
            result += f"Robots: {' '.join([r.name for r in self.robots])}\n"
        else:
            result += 'Robots: none'
        return result.strip()
