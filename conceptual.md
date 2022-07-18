### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
PostgreSQL is an Open Source Relational DataBase Management System.
- What is the difference between SQL and PostgreSQL?
SQL is the database standard which PostgreSQL is based on. PostgreSQL manages databases using using SQL syntax and commands.
- In `psql`, how do you connect to a database?
\c "database_name"
- What is the difference between `HAVING` and `WHERE`?
'HAVING' refers to the 'GROUP BY' command. 'WHERE' filters the values searched by the 'SELECT' command.
- What is the difference between an `INNER` and `OUTER` join?
Inner Join only groups rows that match the condition in both tables.
Outer Join groups rows that match the condition in both tables as well as one of the two tables, or both. 
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
Left Join includes the shared rows that match the condition in both tables in addition to the left table in the argument. Right Joins include the table in the right argument instead.
- What is an ORM? What do they do?
A code library that transfers data from relational database tables into objects used in application code (i.e. Python).
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
The AJAX HTTP POST/GET requests are strictly between the browser and the API or the browser and the Flask Server. AJAX is a front-end method. The 'requests' method from Flask requests data between the flask server and the API
- What is CSRF? What is the purpose of the CSRF token?
CSRF is a token that serves as a hidden input key that is passed along with a post request to the Flask server. This token validates that the request is secure. CSRF stands for Cross-Site request forgery.
- What is the purpose of `form.hidden_tag()`?
'form.hidden_tag()' are form inputs that are tagged as 'hidden' and not rendered on the browser display. These hidden tags are associated with secure information list CSRF tokens.