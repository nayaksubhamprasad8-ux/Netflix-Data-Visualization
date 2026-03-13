import pandas as pd
import matplotlib.pyplot as plt

#load the dataset
df = pd.read_csv('netflix_titles.csv')
print(df.head())

# clean data
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
plt.title('Number of Movies and TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

#

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Content by Rating on Netflix')
plt.axis('equal')
plt.tight_layout()
plt.savefig('rating_distribution.png')
plt.show()

#

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(8, 6))
plt.hist(movie_df['duration_int'], bins=30, color='purple', edgecolor='black')
plt.title('Distribution of Movie Durations on Netflix')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('movie_duration_distribution.png')
plt.show()

#

release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(release_count.index, release_count.values, marker='o', color='red')
plt.title('Release Year vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('release_year_distribution.png')
plt.show()

#

country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8, 6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Shows on Netflix')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_countries.png')
plt.show()

#

content_by_year = content_by_year = df.groupby(['release_year','type']).size().unstack(fill_value=0)

fig, ax = plt.subplots(1,2, figsize=(12, 5))

#first subplot:movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], marker='o', color='blue')
ax[0].set_title('Movies released each year')
ax[0].set_xlabel('Release Year')
ax[0].set_ylabel('Number of movies')

#second subplot:tv shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], marker='o', color='orange')
ax[1].set_title('TV Shows released each year')
ax[1].set_xlabel('Release Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows released each year')
plt.tight_layout()
plt.savefig('movies_vs_tvshows_comparison.png')
plt.show()