--Query 1 (with duplicates)
select ep.EmpId, CONCAT(ef.FirstName,' ',ef.LastName) as 'Full Name', sd.S_Name as 'Supervisor Name', ep.HoursWorked as 'Hours' from employeePayroll as ep 
inner join employeeInfo as ef on ep.EmpId=ef.EmpId 
inner join  employeeJob as ej on ej.EmpId=ep.EmpId 
inner join JobDetails as jd on jd.JobCode=ej.JobCode 
inner join SupervisorDetails as sd on sd.S_Id=jd.S_Id
where ep.HoursWorked>25 and ef.LastName like '%s%';

--(without duplicates)
select Distinct(a.EmpId),a.[Full Name],a.Hours,a.[Supervisor Name] from 
(select ep.EmpId, CONCAT(ef.FirstName,' ',ef.LastName) as 'Full Name', sd.S_Name as 'Supervisor Name', ep.HoursWorked as 'Hours' from employeePayroll as ep 
inner join employeeInfo as ef on ep.EmpId=ef.EmpId 
inner join  employeeJob as ej on ej.EmpId=ep.EmpId 
inner join JobDetails as jd on jd.JobCode=ej.JobCode 
inner join SupervisorDetails as sd on sd.S_Id=jd.S_Id
where ep.HoursWorked>25 and ef.LastName like '%s%') as a;

-- Query 2 
select ep.EmpId, CONCAT(ef.FirstName,' ',ef.LastName) as 'Full Name', ep.PayWeekendDate, ep.OverTime from employeePayroll as ep 
inner join employeeInfo as ef on ep.EmpId=ef.EmpId
where PayWeekendDate = '30-May-13' and OverTime > 0;


--Query 3
select ej.JobCode, sd.S_Name as 'Manager Name', sd.S_Phone as 'Manager Cell Number' from employeeInfo as ep 
inner join employeeJob as ej on ep.EmpId=ej.EmpId 
inner join JobDetails as jd on ej.JobCode=jd.JobCode 
inner join SupervisorDetails as sd on sd.S_Id=jd.S_Id 
where ep.EmpId='33982';


--Query 4 
select ei.EmpId, CONCAT(ei.FirstName,' ',ei.LastName) as 'Full Name', jd.Position as 'Skill' from employeeInfo as ei inner join employeeJob as ej on ei.EmpId=ej.EmpId 
inner join JobDetails as jd on jd.JobCode=ej.JobCode
where ei.City='Moose Jaw' ;


--Query 5 
select ei.EmpId,CONCAT(ei.FirstName,' ',ei.LastName) as 'Full Name', jd.Position as 'Job Description' from Committee as c inner join EmpCommittee as ec on ec.ComId = c.ComId 
inner join employeeJob as ej on ej.EmpId=ec.EmpId 
inner join JobDetails as jd on jd.JobCode=ej.JobCode inner join employeeInfo as ei on ei.EmpId=ej.EmpId
where c.ComName = 'OH&S';


--Query 6 
select ei.EmpId, CONCAT(ei.FirstName,' ',ei.LastName) as 'Full Name', jd.JobCode from SupervisorDetails as sd inner join JobDetails as jd on jd.S_Id=sd.S_Id 
inner join employeeJob ej on ej.JobCode=jd.JobCode inner join employeeInfo as ei on ei.EmpId=ej.EmpId
where sd.S_Name like '%Goldberg%' ;

--Query 7 
Select PayWeekendDate, sum(HoursWorked+OverTime) as PersonHoursWorked from employeePayroll where PayWeekendDate != ' ' group by PayWeekendDate;

-- Query 8 
select jd.s_id as 'Supervisor Id', count(distinct(ej.empId)) as 'No. Of Employees' from employeeJob ej inner join JobDetails jd on ej.JobCode=jd.JobCode 
group by jd.S_Id having count(ej.empId)>2 ;

--Query 9 
select S_Id,S_Name from supervisordetails as sd where exists
(select jd.S_Id from employeeJob ej 
inner join JobDetails jd on ej.JobCode=jd.JobCode
where jd.S_Id=sd.S_Id
group by jd.S_Id having count(distinct(ej.empId))>2) ;

--Query 10 (RUN BELOW VIEW STATEMENT IN A NEW QUERY EDITOR)
Create view CommitteeMeetingForDay as 
select ei.EmpId,Concat(ei.FirstName,' ',ei.LastName) as 'Full Name', c.ComId as 'Committee Id', 
c.MeetingNight, c.ComName as 'Committee Name', sd.S_Id as 'Supervisor Id',sd.s_Name as 'Supervisor Name'
from committee c 
inner join EmpCommittee ec on c.ComId=ec.ComId 
inner join employeeInfo ei on ei.EmpId=ec.EmpId 
inner join employeeJob ej on ej.EmpId=ei.EmpId 
inner join JobDetails jd on jd.JobCode=ej.JobCode 
inner join SupervisorDetails sd on sd.S_Id=jd.S_Id;

Select * from CommitteeMeetingForDay where Meetingnight='Mon';


