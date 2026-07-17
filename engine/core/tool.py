class BaseTool:
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f"Running {self.name}...")
