#! /usr/bin/env python

# Import the necessary module
import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Having problem connecting to the database.")


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
    try:
        db, cursor = connect()
        cursor.execute(top3_articles)
        results = cursor.fetchall()
        db.close()
        print("\n")
        print("The most popular three articles of all time are:".title())
        for i in range(len(results)):
            title = results[i][0]
            views = results[i][1]
            print("""
            "{}" - {:,} views
            """.format(title, views))
        print("\n")
    except:
        print("\nHaving problem fetching data about the top articles.\n")


def popular_authors():
    """
    This function is used to solve problem 2,
    and also print out the outputs in the end
    """
    try:
        db, cursor = connect()
        cursor.execute(top_authors)
        results = cursor.fetchall()
        db.close()
        print("The most popular article authors of all time are:".title())
        for i in range(len(results)):
            author = results[i][0]
            total_views = results[i][1]
            print("""
            {} - {:,} views
            """.format(author, total_views))
        print("\n")
    except:
        print("\nHaving problem fetching data about the popular authors.\n")


def high_percent_error():
    """
    This function is used to solve problem 3,
    and also print out the outputs in the end
    """
    try:
        db, cursor = connect()
        cursor.execute(error_percent)
        results = cursor.fetchall()
        db.close()
        print("The day with more than 1% of requests lead to errors are:".title())
        for i in range(len(results)):
            date = results[i][0]
            percentages = results[i][1]
            print("""
            {} - {}% errors
            """.format(date, percentages))
    except:
        print("\nHaving problem fetching data about the percentage of errors\n")

# Prints out the analysis in the terminal
if __name__ == "__main__":
    top_articles()
    popular_authors()
    high_percent_error()
