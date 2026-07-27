import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")

# Basic info
print(df.head())
print(df.info())
print(df.describe())

# Highest & Lowest
max_book = df[df['Price'] == df['Price'].max()]
print("Most Expensive Book:\n", max_book)

min_book = df[df['Price'] == df['Price'].min()]
print("Cheapest Book:\n", min_book)

# Average
avg_price = df['Price'].mean()
print("Average Price:", avg_price)

# 🔥 ADD NEW COLUMNS (REAL EDA)

# Category
def price_category(price):
    if price < 20:
        return "Cheap"
    elif price < 40:
        return "Medium"
    else:
        return "Expensive"

df['Category'] = df['Price'].apply(price_category)

# Above average
df['Above_Average'] = df['Price'] > avg_price

# Ranking
df['Rank'] = df['Price'].rank(ascending=False)

# Top 5
top5 = df.sort_values(by='Price', ascending=False).head()
print(top5)

# Graph
plt.hist(df['Price'], bins=5)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.show()

# Save NEW analyzed data
df.to_csv("analyzed_book.csv", index=False)

print("✅ Analyzed CSV file created!")