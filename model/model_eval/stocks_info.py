import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

# For reading stock data from yahoo
import yfinance as yf

# For time stamps
from datetime import datetime


# The tech stocks we'll use for this analysis
tech_list = ['AAPL', 'GOOG', 'MSFT', 'NVDA', 'AMZN', 'META', 'TSM', 'TSLA', 'WMT', 'V']

end = datetime.now()
#start = datetime(end.year - 1, end.month, end.day)
start='2019-01-01'

for stock in tech_list:
    globals()[stock] = yf.download(stock, start, end)


company_list = [AAPL, GOOG, MSFT, NVDA, AMZN, META, TSM, TSLA, WMT, V]
company_names = ["APPLE", "GOOGLE", "MICROSOFT", "NVIDIA", "AMAZON", "META", "TSMC", "TESLA", "WALMART", "VISA"]

for company, com_name in zip(company_list, company_names):
    company["company_name"] = com_name
    
df = pd.concat(company_list, axis=0)
print(df.tail(10))

#print(AAPL.describe())
#print(AAPL.info())

#plotting close prices of the 4 given companies
plt.figure(figsize=(15, 10))
plt.subplots_adjust(top=1.25, bottom=1.2)

for i, company in enumerate(company_list, 1):
    plt.subplot(5, 2, i)
    company['Adj Close'].plot()
    plt.ylabel('Adj Close')
    plt.xlabel(None)
    plt.title(f"Closing Price of {company_names[i - 1]}")
    
plt.tight_layout()
plt.show()

# Now let's plot the total volume of stock being traded each day
plt.figure(figsize=(15, 10))
plt.subplots_adjust(top=1.25, bottom=1.2)

for i, company in enumerate(company_list, 1):
    plt.subplot(5, 2, i)
    company['Volume'].plot()
    plt.ylabel('Volume')
    plt.xlabel(None)
    plt.title(f"Sales Volume for {company_names[i - 1]}")
    
plt.tight_layout()
plt.show()

ma_day = [10, 20, 50]

for ma in ma_day:
    for company in company_list:
        column_name = f"MA for {ma} days"
        company[column_name] = company['Adj Close'].rolling(ma).mean()
        

fig, axes = plt.subplots(5, 2, figsize=(15, 20))  # Create a 5x2 grid

for i, (company, title, ax) in enumerate(zip(company_list, company_names, axes.flatten())):
    company[['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot(ax=ax)
    ax.set_title(title)
    ax.set_xlabel(None)  # Remove x-label to avoid clutter

plt.tight_layout()
plt.show()

# Calculate daily returns for each company
for company in company_list:
    company['Daily Return'] = company['Adj Close'].pct_change()

# Create a 5x2 grid for plotting
fig, axes = plt.subplots(5, 2, figsize=(15, 20))

# Plot daily returns for each company
for company, title, ax in zip(company_list, company_names, axes.flatten()):
    company['Daily Return'].plot(ax=ax, legend=True, linestyle='--', marker='o')
    ax.set_title(title)
    ax.set_xlabel(None)  # Remove x-label to avoid clutter
    ax.set_ylabel('Daily Return')  # Set y-label for clarity

# Adjust layout to prevent overlap
fig.tight_layout()

# Show the plot
plt.show()

plt.figure(figsize=(12, 9))

for i, company in enumerate(company_list, 1):
    plt.subplot(5, 2, i)
    company['Daily Return'].hist(bins=50)
    plt.xlabel('Daily Return')
    plt.ylabel('Counts')
    plt.title(f'{company_names[i - 1]}')
    
plt.tight_layout()
plt.show()

closing_df = yf.download(tech_list, start=start, end=end)['Adj Close']

# Make a new tech returns DataFrame
tech_rets = closing_df.pct_change()
tech_rets.head()

#pairplot of all daily returns comparisons
# sns.pairplot(tech_rets, kind='reg')
# plt.show()

# plt.figure(figsize=(20, 20))

# plt.subplot(5, 2, 1)
# sns.heatmap(tech_rets.corr(), annot=True, cmap='summer')
# plt.title('Correlation of stock return')

# plt.subplot(5, 2, 2)
# sns.heatmap(closing_df.corr(), annot=True, cmap='summer')
# plt.title('Correlation of stock closing price')

# plt.show()

plt.figure(figsize=(20, 18))

plt.subplot(5, 2, 1)
sns.heatmap(tech_rets.corr(), annot=True, cmap='summer')
plt.title('Correlation of stock return')

plt.subplot(5, 2, 2)
sns.heatmap(closing_df.corr(), annot=True, cmap='summer')
plt.title('Correlation of stock closing price')

# Add more subplots if needed (empty subplots for visual balance, for instance)
for i in range(3, 11):
    plt.subplot(5, 2, i)
    plt.axis('off')  # Turn off the axis for these additional plots

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()

rets = tech_rets.dropna()

area = np.pi * 20

plt.figure(figsize=(10, 8))
plt.scatter(rets.mean(), rets.std(), s=area)
plt.xlabel('Expected return')
plt.ylabel('Risk')

for label, x, y in zip(rets.columns, rets.mean(), rets.std()):
    plt.annotate(label, xy=(x, y), xytext=(50, 50), textcoords='offset points', ha='right', va='bottom', 
                 arrowprops=dict(arrowstyle='-', color='blue', connectionstyle='arc3,rad=-0.3'))

plt.show()