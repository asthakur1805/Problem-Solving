SELECT
	emp.name AS Employee
FROM 
	employee emp
		JOIN
			employee mgr
				ON emp.managerId = mgr.Id  
WHERE
	emp.salary > mgr.salary;