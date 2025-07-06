import pandas as pd
import os

# === CONFIGURATION ===
INPUT_FILE = "data/raw/SDG4_Education.csv"  # Update if file name is different
OUTPUT_FILE = "data/processed/education_cleaned.csv"

# === STEP 1: LOAD DATA ===
print("🔄 Loading dataset...")
df = pd.read_csv(INPUT_FILE)

# === STEP 2: CLEAN COLUMN NAMES ===
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Preview
print("📊 Columns:", df.columns.tolist())
print("✅ Rows loaded:", df.shape[0])

# === STEP 3: FILTER USEFUL DATA ===
# Example indicators to keep (customize based on actual file)
indicators = [
    'Literacy rate',
    'Completion rate at primary education',
    'Internet access in schools',
    'Percentage of population using the Internet',
    'Mobile broadband subscriptions'
]

df = df[df['indicator_name'].isin(indicators)]

# Filter: last 10+ years
df = df[df['year'] >= 2010]

# Optional: keep key columns
columns_to_keep = [
    'country_name', 'year', 'sex', 'age_group', 'indicator_name', 'value'
]
df = df[columns_to_keep]

# Rename for clarity
df.rename(columns={
    'country_name': 'country',
    'indicator_name': 'indicator',
    'value': 'score'
}, inplace=True)

# Drop missing values
df.dropna(subset=['score'], inplace=True)

# === STEP 4: SAVE CLEANED FILE ===
os.makedirs("data/processed", exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned dataset saved to {OUTPUT_FILE}")
