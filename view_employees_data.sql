Create or replace VIEW  employees_data AS
    SELECT e.emp_no,
           e.birth_date,
           e.first_name,
           e.last_name,
           e.gender,
           e.hire_date,
           d.dept_no,
           d.dept_name,
           s.from_date,
           s.to_date,
           s.salary
From employees e
JOIN dept_emp de ON e.emp_no = de.emp_no
JOIN departments d ON de.dept_no = d.dept_no
JOIN salaries s ON e.emp_no = s.emp_no;

SELECT * FROM employees_data;
