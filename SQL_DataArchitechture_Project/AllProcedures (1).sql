-- Run the procedure query in seperate query editor


-- Query 3 using Procedures:

Create Procedure EmployeeManagerDetails @empId nvarchar(50)
as
BEGIN
       select ej.JobCode, sd.S_Name as 'Manager Name', sd.S_phone as 'Manager Cell Number' from employeeInfo as ep
inner join employeeJob as ej on ep.EmpId=ej.EmpId inner join JobDetails as jd on ej.JobCode=jd.JobCode
inner join SupervisorDetails as sd on sd.S_Id=jd.S_Id where ep.EmpId=@empId
END;

Exec EmployeeManagerDetails @empId='33982';


--Query 4 using procedures:

CREATE PROCEDURE SkillsByCity @city nvarchar(50)
AS
BEGIN
select ei.EmpId, CONCAT(ei.FirstName,' ',ei.LastName) as 'Full Name', jd.Position as   'Skill' from employeeInfo as ei inner join employeeJob as ej on ei.EmpId=ej.EmpId 
	 inner join JobDetails as jd on jd.JobCode=ej.JobCode
	 where ei.City=@city
 END;

Exec SkillsByCity @city='Moose Jaw'; 

-- Query 7 using procedure:

Create Procedure PersonHoursWorkedWithOT 
AS 
BEGIN 
SELECT PayWeekendDate, sum(HoursWorked+OverTime) AS TotalHoursWorked FROM employeePayroll where PayWeekendDate != ‘ ’ group by PayWeekendDate; 
END;

Exec PersonHoursWorkedWithOT;

