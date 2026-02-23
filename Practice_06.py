import polars as pl
import duckdb

mysql_uri = "mysql://root:Lera2005@@localhost:3306/employees"




df = pl.read_database_uri(
    query="SELECT * FROM employees_data",
    uri=mysql_uri,
    engine="connectorx"
)

emp_rollup = df.group_by('emp_no').agg([
    pl.col('birth_date').min(),
    pl.col('first_name').min(),
    pl.col('last_name').min(),
    pl.col('gender').min(),
    pl.col('hire_date').min(),
    pl.col('dept_no').n_unique().alias('departments_worked'),
    pl.col('dept_name').min().alias('first_dept_name'),
    pl.col('from_date').min().alias('first_salary_from_date'),
    pl.col('to_date').max().alias('last_salary_to_date'),
    pl.col('emp_no').count().alias('salary_records'),
    pl.col('salary').min().alias('min_salary'),
    pl.col('salary').max().alias('max_salary'),
    pl.col('salary').mean().alias('avg_salary'),
    pl.col('salary').median().alias('median_salary')
]).with_columns((pl.col('max_salary') - pl.col('min_salary')).alias('salary_growth'))

connection = duckdb.connect('practice_6.duckdb')
connection.execute("CREATE OR REPLACE TABLE emp_rollup AS SELECT * FROM emp_rollup")
