\# Netflix ETL Pipeline using Apache Airflow



\*\*Author:\*\* Tanushree Ambade



\## Project Overview



This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using Apache Airflow.



\### Technologies Used



\- Apache Airflow

\- Python

\- Docker

\- PostgreSQL

\- Pandas

\- SQLAlchemy

\- Git \& GitHub



\## Workflow



1\. Extract Netflix dataset

2\. Transform data

3\. Load data into PostgreSQL



\## Dataset



\- Netflix Movies \& TV Shows Dataset

\- Total Records: \*\*8807\*\*



\## Project Structure



```

Airflow\_ETL\_Project/

│

├── dags/

├── data/

├── config/

├── screenshots/

├── docker-compose.yaml

├── README.md

└── .gitignore

```



\## Screenshots



\### Airflow Graph



!\[Graph](screenshots/airflow\_graph.png)



\### Airflow Grid



!\[Grid](screenshots/airflow\_grid.png)



\### PostgreSQL



!\[Postgres](screenshots/postgres\_count.png)



\### GitHub Repository



!\[Repository](screenshots/github\_repo.png)



\## PostgreSQL Verification



```sql

SELECT COUNT(\*) FROM netflix\_data;

```



Output



```

8807

```



\## Future Improvements



\- AWS EC2 Deployment

\- CI/CD using GitHub Actions

\- Data Validation

\- Email Notifications

\- Scheduling enhancements

