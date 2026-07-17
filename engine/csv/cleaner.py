import pandas as pd

from engine.core.tool import BaseTool


# CSVCleaner is a ToolCraft tool responsible for cleaning CSV files.
# It inherits the common structure from BaseTool:
# name, inputs, outputs, and execute().
class CSVCleaner(BaseTool):

    def __init__(self):
        super().__init__("CSV Cleaner")

    # execute() performs the CSV cleaning workflow:
    # 1. Read the input CSV file.
    # 2. Remove empty rows and duplicates.
    # 3. Clean text spaces.
    # 4. Save the cleaned output file.
    def execute(self):
        input_file = self.inputs[0]
        output_file = self.outputs[0]

        df = pd.read_csv(input_file)

        # Remove rows where all columns are empty.
        df = df.dropna(how="all")

        # Remove duplicated records.
        df = df.drop_duplicates()

        # Remove extra spaces from text columns.
        df = df.apply(
            lambda column: column.str.strip()
            if column.dtype == "object"
            else column
        )

        df.to_csv(output_file, index=False)

        print(f"Cleaned file saved: {output_file}")