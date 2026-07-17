# BaseTool is the foundation of every ToolCraft tool.
# Every tool has a name, inputs, outputs, and an execute() method.
class BaseTool:
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []
# execute() is the main entry point for running a tool.
    def execute(self):
        print(f"Running {self.name}...")
