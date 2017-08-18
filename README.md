# Log Analysis

# Prerequisites
### You will need to have following technologies to run this program:
* [Python 3](https://www.python.org/downloads/)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

# SQL Views
##### articles_view
* This query calculate the number of time an article occur in the table.
```
CREATE view articles_view as
select title, count(*) as views
FROM articles, log
WHERE log.path = concat('/article/', articles.slug)
GROUP BY title ORDER BY views DESC;
```
##### authors_view
```
CREATE view authors_view as
SELECT name, sum(articles_view.views) as total
FROM articles_view, authors
WHERE authors.id = articles_view.author
GROUP BY authors.name
ORDER BY total DESC;
```
##### failed_requests
* This query calculates the number of failed requests each date.
```
CREATE view failed_requests as
SELECT date(time) as date, count(status) as errors
FROM log where status != '200 OK'
GROUP BY date
ORDER BY date;
```
##### total_requests
* This query calculates the total number of requests in the database.
```
CREATE view total_requests as
SELECT date(time) as date, count(status) as requests
FROM log
GROUP BY date
ORDER BY date;
```
##### error_percentages
```
CREATE view error_percentages as
SELECT total_requests.date,
ROUND((100.0 * failed_requests.errors)/total_requests.requests, 2) as error_percentages
```

# Get Started
* If you haven't already, install [Virtual Box](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html)
* Download this repo from the download section or simply clone it by using the following command:
``` ```
*
