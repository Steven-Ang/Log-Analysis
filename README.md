# Log Analysis
Writing Python code to make a business analysis from a database with millions of rows. The analysis will answer these three questions:
1. **What are the most popular three articles of all time?**
2. **Who are the most popular article authors of all time?**
3. **On which days did more than 1% of requests lead to errors?**

The results will be displayed inside the terminal by running `python logs.py`.

# Prerequisites:
### You will need to have following technologies to run this program:
* [Python 3](https://www.python.org/downloads/)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)

# Installation Guide:
### Guide on Python:
1. Visit this [link](https://www.python.org/downloads/), find the latest version of Python 3 and download it.
2. Once it's finished, click on it.
3. Follow the instructions provided by the wizard.
4. To check if Python is successfully installed into your computer, open up your terimal and type the following `python --version`. If it's successful, it will displays the version of the Python you're using.

### Guide on VM (Virtual Box):
1. Visit this [link](https://www.virtualbox.org/wiki/Downloads), find the host that is compatible with your operating system and download it.
2. Once it's finished, click on it.
3. Follow the instructions provided by the wizard.
4. Opening the software is not required, vagrant will do the work for it.

### Guide on Vagrant:
1. Visit this [link]((https://www.vagrantup.com/downloads.html), find the package that is proper for your operating system and download it.
2. Once it's finished, click on it.
3. Follow the instructions provided by the wizard.
4. To check if it's successfully installed into your computer, open your terimal and type the following `vagrant --version`.
5. The rest of it will be cover in the **How To Run The Program** section.

# SQL Views:
The following SQL views are required to run the program. Run `psql news` inside the /vagrant directory and either copy paste them individually or type them manually.

## articles_view
This query calculates the number of time an article occur in the table.
```SQL
CREATE view articles_view as
select title, count(*) as views
FROM articles, log
WHERE log.path = concat('/article/', articles.slug)
GROUP BY title ORDER BY views DESC;
```
## authors_view
This query calculates the total number of views each authors have.
```SQL
CREATE view authors_view as
SELECT name, sum(articles_view.views) as total
FROM articles_view, authors
WHERE authors.id = articles_view.author
GROUP BY authors.name
ORDER BY total DESC;
```
## failed_requests
This query calculates the number of failed requests each date in the database.
```SQL
CREATE view failed_requests as
SELECT date(time) as date, count(status) as errors
FROM log where status != '200 OK'
GROUP BY date
ORDER BY date;
```
## total_requests
This query calculates the total number of requests in the database.
```SQL
CREATE view total_requests as
SELECT date(time) as date, count(status) as requests
FROM log
GROUP BY date
ORDER BY date;
```
## error_percentages
This query uses *failed_requests* and *total_requests* to calculates the error percentgaes of each date in the database.
```SQL
CREATE view error_percentages as
SELECT total_requests.date,
ROUND((100.0 * failed_requests.errors)/total_requests.requests, 2) as error_percentages;
```

# How To Run The Program:
#### If the instructions aren't very clear, please tell me. I will improve it, criticisms are very much appreciated.
* If you haven't already, download all of the required technologies needed for this program from the **Installation Guide**.
* Download this repository or clone it by using the following command: `git clone https://github.com/Steven-Ang/Log-Analysis`
* Visit this [repository](https://github.com/udacity/fullstack-nanodegree-vm), download the folder or clone it by using the following command: `git clone https://github.com/udacity/fullstack-nanodegree-vm`
* Download this zip [file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it when it's finished.
* Move **newsdata.sql** and the folder, **logs** into **FSND-Virtual_Machine/vagrant**.
* Inside the **vagrant** directory which located inside **FSND-Virtual_Machine**. Open your terminal and run this command `vagrant up`. When you ran it, it may takes a few minutes or an hour (depending on your internet connection) to finish.
* Once it's done, run this command `vagrant ssh`. This command will start the vagrant virtual machine. Inside your terminal, do this `cd /vagrant`. This command will move your current path to vagrant's path.
* Inside your terminal, do this command `psql news`. It will takes you inside the news database. And now copy paste all of the views from **SQL views** section.
* Once it's done, do `CTRL + Z` or `CMD + Z` to exit.
* Now inside your terminal, do this `cd logs\` then run `python logs.py`. This will start the program and displayed the analysis inside the terminal.
