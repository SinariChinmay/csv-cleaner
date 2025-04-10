import pandas as pd

# Step 1: Load your CSV
file_path = "C:/Users/csina/Downloads/sample_transactions.csv"  # Replace this with your actual file path
df = pd.read_csv(file_path)

# Step 2: View first few rows
print("Original Data:")
print(df.head())

# Step 3: Drop empty rows
df = df.dropna()

# Step 4: Rename columns (example)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Step 5: Optional - Filter by a condition
# Example: Only keep rows where amount > 100
# df = df[df['amount'] > 100]

# Step 6: Save cleaned file
df.to_csv("cleaned_file.csv", index=False)
print("✅ Cleaned file saved as 'cleaned_file.csv'")
