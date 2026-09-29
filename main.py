import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "data" / "raw_sales_data.csv"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(INPUT_FILE)

print("Original records:", len(df))

# Remove duplicate records
df = df.drop_duplicates()

# Clean text columns
text_columns = ["Customer", "Product", "Category", "Region"]

for col in text_columns:
    df[col] = df[col].astype("string").str.strip()

# Standardize categories
df["Category"] = df["Category"].str.title()
df["Region"] = df["Region"].str.title()

# Handle missing values
df["Customer"] = df["Customer"].fillna("Unknown")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce").fillna(df["Price"].median())

# Convert date
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Create total sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# Save cleaned data
cleaned_file = OUTPUT_DIR / "cleaned_sales_data.csv"
df.to_csv(cleaned_file, index=False)

# Summary report
total_sales = df["Total_Sales"].sum()
total_orders = len(df)
average_order = df["Total_Sales"].mean()

summary = pd.DataFrame({
    "Metric": [
        "Total Orders",
        "Total Sales",
        "Average Order Value"
    ],
    "Value": [
        total_orders,
        total_sales,
        average_order
    ]
})

# Excel report
report_file = OUTPUT_DIR / "sales_report.xlsx"

with pd.ExcelWriter(report_file, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    summary.to_excel(writer, sheet_name="Summary", index=False)

    region_report = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .reset_index()
        .sort_values("Total_Sales", ascending=False)
    )

    region_report.to_excel(
        writer,
        sheet_name="Region Report",
        index=False
    )

# Create visualization
plt.figure(figsize=(8, 5))

region_sales = df.groupby("Region")["Total_Sales"].sum()

region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()

chart_file = OUTPUT_DIR / "sales_by_region.png"
plt.savefig(chart_file)
plt.close()

print("\nData cleaning completed successfully!")
print("Cleaned file:", cleaned_file)
print("Excel report:", report_file)
print("Chart:", chart_file)
print("\nTotal Orders:", total_orders)
print("Total Sales:", total_sales)