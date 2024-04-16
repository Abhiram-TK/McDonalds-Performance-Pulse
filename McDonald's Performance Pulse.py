#!/usr/bin/env python
# coding: utf-8

# # <div style ="text-align: center;">McDonald's Performance Pulse: Unraveling the Metrics Behind the Arches</div>

# #### <div style="text-align: right;">By Abhiram TK</div>

# ---

# ## Data Preparation & Cleaning

# 1. Load the file using **Pandas**.
# 2. Look at some information about the data & columns.
# 3. Fix any missing or incorrect values.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv(r'McDonalds_financial_statements.csv')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.columns


# In[7]:


df.info()


# In[8]:


df.isna().sum()


# In[9]:


df.describe()


# ---

# ## Exploratory Analysis & Visualization

# ### <u>Financial Performance Metrics<u>
#    

# In[10]:


df.columns


# #### Revenue ($B) Trend Over Years

# In[11]:


plt.figure(figsize=(14, 7))
sns.set_style("whitegrid") 

ax=sns.lineplot(data=df, x='Year', y='Revenue ($B)', label='Earnings ($B)', color='#FFC72C', linewidth=4)
plt.title('Revenue Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

# Ensuring x-axis ticks are integers
plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# #### Earnings ($B) Trend Over Years

# In[12]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.lineplot(data=df, x='Year', y='Earnings ($B)', label='Earnings ($B)', color='#DA291C', linewidth=4)
plt.title('Earnings Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#FFC72C')
plt.show()


# ---

# #### EPS ($) Trend Over Years

# In[13]:


plt.figure(figsize=(14, 7))
sns.set_style("whitegrid") 

ax=sns.lineplot(data=df, x='Year', y='EPS ($)', label='EPS ($)', color='#FFC72C', linewidth=4)
plt.title('EPS Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# #### Dividend Yield (%) History Over Years

# In[14]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.barplot(data=df, x='Year', y='Dividend Yield (%)', label='Dividend Yield (%)', color='#DA291C')
plt.title('Dividend Yield History Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)



plt.xticks(range(len(df['Year'])), df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#FFC72C')
plt.show()


# ---

# #### Dividend (stock  split adjusted) ($) History Over Years

# In[15]:


plt.figure(figsize=(14, 7))
sns.set_style("whitegrid") 

ax=sns.barplot(data=df, x='Year', y='Dividend (stock split adjusted) ($)', label='Dividend ($)', color='#FFC72C')
plt.title('Dividend (stock split adjusted) History Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)



plt.xticks(range(len(df['Year'])), df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# #### Operating Margin (%) Trend Over Years

# In[16]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.lineplot(data=df, x='Year', y='Operating Margin (%)', label='Operating Margin (%)', color='#DA291C', linewidth=4)
plt.fill_between(df['Year'], df['Operating Margin (%)'], color='#DA291C', alpha=0.3)
plt.title('Operating Margin Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#FFC72C')
plt.show()


# ---

# #### Shares Outstanding ($B) Trend Over Years

# In[17]:


plt.figure(figsize=(14, 7))
sns.set_style("whitegrid") 

ax=sns.scatterplot(data=df, x='Year', y='Shares Outstanding ($B)', label='Shares Outstanding ($B)', color='#FFC72C', s=100)
plt.title('Shares Outstanding Trend Over Years', fontsize=14)
plt.legend(loc='upper right', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# ### <u>Market Metrics<u>

# In[18]:


df.columns


# #### Market Cap ($B) Trend Over Years

# In[19]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.lineplot(data=df, x='Year', y='Market cap ($B)', label='Market cap ($B)', color='#DA291C', linewidth=4)
plt.title('Market Cap Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#FFC72C')
plt.show()


# ---

# #### Valuation Ratios Over Years

# In[20]:


plt.figure(figsize=(14, 7))
sns.set_style("whitegrid") 

ax = sns.barplot(data=df, x='Year', y='P/E ratio', label='P/E Ratio', color='#FFC72C', alpha=0.90)
ax = sns.barplot(data=df, x='Year', y='P/S ratio', label='P/S Ratio', color='#27251F', alpha=0.80)
ax = sns.barplot(data=df, x='Year', y='P/B ratio', label='P/B Ratio', color='#a8c23a', alpha=0.85)


plt.title('Valuation Ratios Over Years', fontsize=14)

plt.legend(loc='upper left', fontsize=12)

plt.xticks(range(len(df['Year'])), df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# ### <u>Financial Structure & Position<u>

# In[21]:


df.columns


# #### Assets Trend Over Years

# In[22]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.lineplot(data=df, x='Year', y='Total assets ($B)', label='Total assets ($B)', color='#DA291C', linewidth=4)
ax=sns.lineplot(data=df, x='Year', y='Net assets ($B)', label='Net assets ($B)', color='#27251F', linewidth=4)
plt.title('Assets Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#FFC72C')
plt.show()


# ---

# #### Liabilities & Debt Trend Over Years

# In[23]:


plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 

ax=sns.lineplot(data=df, x='Year', y='Total liabilities ($B)', label='Total liabilities ($B)', color='#FFC72C', linewidth=5)
plt.fill_between(df['Year'], df['Total liabilities ($B)'], color='#FFC72C', alpha=0.75)
ax=sns.lineplot(data=df, x='Year', y='Total debt ($B)', label='Total debt ($B)', color='#FFFFFF', linewidth=3)
plt.fill_between(df['Year'], df['Total debt ($B)'], color='#FFFFFF', alpha=0.25)
ax=sns.lineplot(data=df, x='Year', y='Cash on Hand ($B)', label='Cash on Hand ($B)', color='#27251F', linewidth=3)
plt.fill_between(df['Year'], df['Cash on Hand ($B)'], color='#27251F', alpha=0.25)
plt.title('Liabilities, Debt & Cash On Hand Trend Over Years', fontsize=14)
plt.legend(loc='upper left', fontsize=12)

plt.gca().xaxis.get_major_locator().set_params(integer=True)

plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# ---

# # Ask & Answer Questions

# ## <u>Trend Analysis<u>

# #### How does **Revenue**, **Earnings**, and **EPS** change over the years?

# In[24]:


indicators = ['Revenue ($B)', 'Earnings ($B)', 'EPS ($)']


# In[25]:


custom_palette = ['#DA291C','#FFC72C','#27251F']

df.plot(x='Year', y=indicators, subplots=True, layout=(3, 3), figsize=(15, 10), sharex=True, rot=90, color=custom_palette);
plt.show()


# - **Revenue**, **Earnings**, and **EPS** exhibit varying patterns over the years, with **Revenue** and **Earnings** generally showing growth trends with fluctuations, while **EPS** demonstrates a more consistent upward trajectory with occasional fluctuations. The data suggests periods of growth followed by stabilization or slight declines, followed by subsequent growth phases. The significant increase observed in **2021** for all three metrics may indicate a particularly strong performance year for the company.

# ---

# ## <u>Correlation Analysis<u>

# #### Do changes in **Operating Margin** correlate with changes in **Net Assets** or **Total Assets**?

# In[26]:


# Step 1: Calculate the percentage change in operating margin, net assets, and total assets

df['Operating Margin Change'] = df['Operating Margin (%)'].pct_change() * 100
df['Net Assets Change'] = df['Net assets ($B)'].pct_change() * 100
df['Total Assets Change'] = df['Total assets ($B)'].pct_change() * 100

# Step 2: Compute the correlation coefficient between changes in operating margin and changes in net assets

correlation_net_assets = df['Operating Margin Change'].corr(df['Net Assets Change'])

# Compute the correlation coefficient between changes in operating margin and changes in total assets

correlation_total_assets = df['Operating Margin Change'].corr(df['Total Assets Change'])

print("Correlation between changes in operating margin and changes in net assets:", correlation_net_assets)

print("Correlation between changes in operating margin and changes in total assets:", correlation_total_assets)


# These values suggest that there is a minimal positive correlation between changes in **Operating Margin** and changes in **Net Assets** or **Total Assets**. However, the correlations are quite weak, implying that changes in **Operating Margin** may not be strongly associated with changes in **Net Assets** or **Total Assets**.

# ---

# ## <u>Performance Analysis<u>

# #### What is the average P/E ratio of all time?

# In[27]:


pe_ratio_column = df['P/E ratio']

average_pe_ratio = pe_ratio_column.mean()

plt.figure(figsize=(14, 7))
sns.set_style("darkgrid") 
sns.histplot(pe_ratio_column, bins=20, color=('#FFC72C'))
plt.axvline(average_pe_ratio, color='#27251F', linestyle='--', linewidth=2, label='Average P/E Ratio')
plt.title('Distribution of P/E Ratio with Average', fontsize=16)
plt.xlabel('P/E Ratio')
plt.ylabel('Frequency')
plt.legend()
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()

print("Average P/E ratio of all time:", average_pe_ratio)


# ---

# ## <u>Financial Analysis<u>

# #### How does total debt compare to net assets and total assets?

# In[28]:


df['Debt_to_Net_Assets'] = df['Total debt ($B)'] / df['Net assets ($B)']

df['Debt_to_Total_Assets'] = df['Total debt ($B)'] / df['Total assets ($B)']

plt.figure(figsize=(14, 7))
sns.set_style("darkgrid")

ax=sns.lineplot(data=df, x='Year', y='Debt_to_Total_Assets', label='Debt_to_Total_Assets ($B)', color='#FFFFFF', linewidth=4)
ax=sns.lineplot(data=df, x='Year', y='Debt_to_Net_Assets', label='Debt_to_Net_Assets ($B)', color='#FFC72C', linewidth=4)

plt.title('Debt-to-Net-Assets and Debt-to-Total-Assets Ratios Over Time', fontsize=16)
plt.legend(loc='upper left', fontsize=12)

plt.legend(title='Ratio Type')
plt.gca().xaxis.get_major_locator().set_params(integer=True)
plt.xticks(df['Year'])
plt.xlabel('')
plt.ylabel('Ratio Value')
plt.grid(linewidth=0.25)
plt.gca().set_facecolor('#DA291C')
plt.show()


# The **Debt-to-Net-Assets ratio** ranges from negative values to positive values, indicating varying levels of **Net Asset** coverage relative to **Total Debt**. For instance, in some years, the company's **Net Assets** exceed its **Total Debt**, while in others, **Total Debt** exceeds **Net Assets**.
# 
# Similarly, the **Debt-to-Total-Assets ratio** fluctuates around 1, indicating changes in the proportion of **Total Debt** relative to **Total Assets** over time.

# ---

# # Summary & Conclusion

# **Summary:**
# 
# 1. **Revenue Trends:** Revenue exhibits varying patterns over the years, with periods of growth followed by stabilization or slight declines, and subsequent growth phases.
# 2. **Dividend Yield and Dividend History:** Dividend Yield history over years is depicted in a bar graph, while Dividend (stock split adjusted) history is illustrated in both bar and area graphs, showcasing the dividend payment trends.
# 3. **Shares Outstanding and Market Cap Trends:** Shares Outstanding trend over years is represented in a scatter graph, while Market Cap trend is depicted in a line graph, providing insights into the changes in shares and market capitalization over time.
# 4. **Valuation Ratios:** Valuation ratios over years are illustrated in a grouped bar graph, allowing for a comparison of various valuation metrics.
# 5. **Assets and Liabilities Trends:** Assets trend over years is presented in a line graph, while Liabilities & Debt trend is shown in an area graph, highlighting the changes in assets and liabilities over time.
# 
# **Conclusions:**
# 
# 1. **Revenue, Earnings, and EPS:** Revenue and earnings generally show growth trends with fluctuations, while EPS demonstrates a more consistent upward trajectory. The significant increase observed in 2021 for all three metrics may indicate a particularly strong performance year.
# 2. **Operating Margin and Net Assets/Total Assets:** There is a minimal positive correlation between changes in Operating Margin and changes in Net Assets or Total Assets. However, the correlations are weak, suggesting that changes in Operating Margin may not be strongly associated with changes in Net Assets or Total Assets.
# 3. **Average P/E Ratio:** The average P/E ratio of all time is approximately 21.66, as depicted in the histogram.
# 4. **Debt Comparison:** The Debt-to-Net-Assets and Debt-to-Total-Assets ratios fluctuate over time, indicating varying levels of Net Asset coverage relative to Total Debt and changes in the proportion of Total Debt relative to Total Assets.
# 
# These conclusions provide valuable insights into the financial performance and position of the company over the years, helping stakeholders make informed decisions.
# 
