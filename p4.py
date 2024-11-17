import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the Netflix dataset
df_netflix = pd.read_csv('net.csv')

# Create figure and subplots for dashboard
plt.figure(figsize=(15,10))

# Plot 1: Kids content comparison
plt.subplot(2,2,1)
kids_filter_movie = df_netflix['listed_in'].str.contains("Children & Family Movies", case=False, regex=False)
kids_filter_tv = df_netflix['listed_in'].str.contains("Kids' TV", case=False, regex=False)
df_kids = df_netflix[kids_filter_movie | kids_filter_tv]

# Count kids vs non-kids content
kids_count = len(df_kids)
total_count = len(df_netflix)
non_kids_count = total_count - kids_count

# Create bar plot
content_types = ['Kids Content', 'Other Content']
counts = [kids_count, non_kids_count]
sns.barplot(x=content_types, y=counts)
plt.title('Kids Content vs Other Content')
plt.ylabel('Number of Titles')

# Plot 2: Kids content by type (Movie vs TV Show)
plt.subplot(2,2,2)
sns.countplot(data=df_kids, x='type')
plt.title('Distribution of Kids Content by Type')
plt.ylabel('Count')

# Plot 3: Top 10 kids content categories
plt.subplot(2,2,3)
categories = df_kids['listed_in'].str.split(',', expand=True).stack()
category_counts = categories.value_counts().head(10)
sns.barplot(x=category_counts.values, y=category_counts.index)
plt.title('Top 10 Categories in Kids Content')
plt.xlabel('Count')

# Plot 4: Kids content by rating
plt.subplot(2,2,4)
sns.countplot(data=df_kids, y='rating', order=df_kids['rating'].value_counts().index)
plt.title('Distribution of Kids Content by Rating')
plt.xlabel('Count')

# Adjust layout
plt.tight_layout()
plt.suptitle('DASHBOARD A: Netflix Kids Content Analysis', y=1.02, fontsize=16)

# Show plot
plt.show()

# Rating explanations:
# TV-Y: Programming designed for very young children
# TV-Y7: Programming designed for children age 7 and above
# TV-G: General audience - Suitable for all ages
# TV-PG: Parental guidance suggested
# G: General audience (for movies)
# PG: Parental guidance suggested (for movies)
