import csv
from collections import defaultdict, namedtuple

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    d = defaultdict(list)
    reader = csv.DictReader(open(MOVIE_DATA, 'r', encoding='utf8'))
    for row in reader:
        d[row['director_name']].append(Movie(title=row['movie_title'], year=row['title_year'], score=row['imdb_score']))
    return d


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    d = defaultdict(list)
    for director, movie in directors.items():
        if len(movie) >= 4:
            d[director] = round(_calc_mean(movie), 1)
    return d


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    return sum(float(x.score) for x in movies) / len(movies)


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60

    avg_sorted = sorted(get_average_scores(directors).items(), key=lambda x: x[1], reverse=True)
    i = 1
    for director_name, director_avg_score in avg_sorted:
        print(fmt_director_entry.format(counter=i, director=director_name, avg=director_avg_score))
        print(sep_line)
        for movie in sorted(directors[director_name], key=lambda x: x.score, reverse=True):
            print(fmt_movie_entry.format(year=movie.year, title=movie.title, score=movie.score))
        print()
        i += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    directors_avg = get_average_scores(directors)
    print_results(directors)


if __name__ == '__main__':
    main()
