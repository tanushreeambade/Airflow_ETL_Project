\# Netflix ETL Pipeline using Apache Airflow



\*\*Author:\*\* Tanushree Ambade



\---



\# Netflix ETL Pipeline



This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using \*\*Apache Airflow\*\*, \*\*Python\*\*, \*\*PostgreSQL\*\*, and \*\*Docker\*\*.



The pipeline automatically extracts Netflix dataset, performs data cleaning and transformation, and loads the processed data into PostgreSQL.



\---



\## Technologies Used



\- Apache Airflow 3

\- Python

\- PostgreSQL

\- Docker \& Docker Compose

\- Pandas

\- SQLAlchemy



\---



\## ETL Workflow



1\. Extract Netflix dataset

2\. Transform and clean data

3\. Load processed data into PostgreSQL



\---



\## Dataset



\- Netflix Movies \& TV Shows Dataset

\- Total Records Loaded: \*\*8807\*\*



\---



\## Output



\- Automated ETL Pipeline

\- Data Cleaning \& Transformation

\- PostgreSQL Integration

\- Airflow DAG Scheduling

\- Dockerized Environment



\---



\## Project Structure



```text

Airflow\_ETL\_Project/

│

├── dags/

│   └── netflix\_etl\_dag.py

│

├── config/

│

├── data/

│   ├── netflix\_titles.csv

│   └── netflix\_final.csv

│

├── screenshots/

│   ├── airflow\_graph.png

│   ├── airflow\_grid.png

│   ├── postgres\_count.png

│   └── github\_repo.png

│

├── docker-compose.yaml

├── requirements.txt

├── README.md

└── .gitignore

```



\---



\# Screenshots



\## Airflow Graph



!\[Airflow Graph](screenshots/airflow\_graph.png)



\---



\## Airflow Grid



!\[Airflow Grid](screenshots/airflow\_grid.png)



\---



\## PostgreSQL Verification



!\[PostgreSQL](screenshots/postgres\_count.png)



\---



\## GitHub Repository



!\[GitHub Repository](screenshots/github\_repo.png)



\---



\## PostgreSQL Verification Query



```sql

SELECT COUNT(\*) FROM netflix\_data;

```



Output



```text

&#x20;count

\-------

&#x20;8807

```



Verify Movie \& TV Show Count



```sql

SELECT type, COUNT(\*)

FROM netflix\_data

GROUP BY type;

```



Output



```text

&#x20;type      | count

\-----------+-------

&#x20;Movie     | 6131

&#x20;TV Show   | 2676

```



\---



\## Future Improvements



\- Add data validation checks

\- Integrate AWS S3 storage

\- Deploy Airflow on Kubernetes

\- Build Power BI Dashboard

\- Add email notifications



\---



\# Conclusion



This project demonstrates a complete ETL pipeline built using Apache Airflow, Python, PostgreSQL, and Docker. It automates the process of extracting, transforming, and loading Netflix data into a relational database while showcasing workflow orchestration and task scheduling.



This project helped strengthen my understanding of data engineering concepts, ETL automation, Docker containerization, and workflow management using Apache Airflow.



\---



⭐ If you found this project useful, consider giving it a star on GitHub.





