#! /usr/bin/env python

# Required library used to connect to the database
import psycopg2


# Make the database name into a variable
DBNAME = "news"


def connect():
    """
    Function for connecting the database,
    reduce typing and readability
    """
    return psycopg2.connect(database=DBNAME)

# Results of the top three articles in the database
top3_articles = "SELECT title, views FROM articles_view LIMIT 3;"
# Results of the top authors in the database
top_authors = "SELECT * FROM authors_view;"
# Results of the day with the most error percentage
error_percent = """SELECT to_char(date, 'Mon DD, YYYY') as date,
error_percentages FROM error_percentages
WHERE error_percentages > 1.0;"""


def top_articles():
    """
    This function is used to solve problem 1,
    and also print out the outputs in the end
    """
    db = connect()
    c = db.cursor()
    c.execute(top3_articles)
    results = c.fetchall()
    db.close()
    print("\n")
    print("The most popular three articles of all time are:".title())
    for i in range(len(results)):
        title = results[i][0]
        views = results[i][1]
        print("""
        "{}" - {} views
        """.format(title, views))
    print("\n")


def popular_authors():
    """
    This function is used to solve problem 2,
    and also print out the outputs in the end
    """
    db = connect()
    c = db.cursor()
    c.execute(top_authors)
    results = c.fetchall()
    db.close()
    print("The most popular article authors of all time are:".title())
    for i in range(len(results)):
        author = results[i][0]
        total_views = results[i][1]
        print("""
        {} - {} views
        """.format(author, total_views))
    print("\n")


def high_percent_error():
    """
    This function is used to solve problem 3,
    and also print out the outputs in the end
    """
    db = connect()
    c = db.cursor()
    c.execute(error_percent)
    results = c.fetchall()
    db.close()
    print("The day with more than 1% of requests lead to errors are:".title())
    for i in range(len(results)):
        date = results[i][0]
        percentages = results[i][1]
        print("""
        {} - {}%
        """.format(date, percentages))
    print("\n")

# Prints out the analysis in the terminal
top_articles()
popular_authors()
high_percent_error()
