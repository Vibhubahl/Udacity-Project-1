THE FIRST PROJECT

************REQUIREMENTS AND INSTALLATION
VAGRANT linux is required go to vagrant.com and download it for your os
now go in vagrant file in terminal and type vagrant up followed by vagrant ssh to download vagrant linux and start using it
ORACLE VIRTUAL BOX

*************PREREQUISITES
BASIC KNOWLEDGE OF OBJECT ORIENTED PYTHON 
BASIC KNOWLEDGE OF HTML AND CSS
BASIC KNOWLEDGE OF GIT (BASH)

**************THE QUESTIONS AND THE SOLUTION FILES
1) What are the most popular three articles?
The first question Question 1.py is the answer of first query that is(Three most viewed articles) whose database is in the Question1db.py
Running the file will display two columns named title , views as result

*QUERIES OF VIEW
create view nam as select title, concat('/article/',slug)as slu from articles
create view name as select path, count(*) as n from log Join nam on nam.slu like log.path group by path order by n desc limit 3

2) Who are the most popular authors?
The second question Question2.py is the answer of first query that is(Most popular article authors) whose database is in the Question2db.py
Running the file will display two columns named name , views as result

*QUERIES OF VIEW
create view r1 as select author,concat('/article/',slug) as s1 from articles
create view name as select path , count(*) as num from log Join r1 on r1.s1 like log.path group by path order by num desc
create view name1 as select author , num from name Join r1 on r1.s1 like name.path order by num desc

3) Print the errors per date if greater than 1%?
The first question Question1.py is the answer of first query that is(More than 1% of requests lead to errors) whose database is in the Question3db.py
Running the file will display two columns named date , errors as result

*QUERIES OF VIEW
create view status as select date(time) as date1, count(status) as stat from log group by date(time)
create view status4 as select date(time) as date1 , status from log where status like '404%'
create view status2 as select date1 , count(status) as notf from status4 group by date1
create view status3 as select date1 , notf from status2
create view status5 as select status3.date1 as fdate,cast(notf as float) , cast(stat as float) from status join status3 on status.date1 = status3.date1

*************HOW TO ADD DATABASE FILE****************
AFTER PERFORMING VAGRANT SSH 
go in vagrant directory in the terminal by performing cd /vagrant
it is containing the newsdata.sql file https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
perform 
psql -d news -f newsdata.psql
create a database named news
\dt to view all data tables
\d tablename to view particular table

************HOW TO RUN FILES****************
GO IN THE SOLUTION DIRECTORY WHICH CONTAINS ALL THE SOLUTION FILES in git (bash)
type python filename.py
then go to chrome and type localhost:portnumber on which port the file is running

***********SOLUTION FILE***********
the solution of all queries are stored in requiredans.txt file
refer this file for solutions