
-- Create a table
CREATE TABLE employeeInfo (
	EmpId int Primary Key NOT NULL,
	LastName nvarchar(50) NOT NULL,
	FirstName nvarchar(50) NOT NULL, 
	Street varchar(50) NOT NULL,
	City nvarchar(50) NOT NULL,
	Province nvarchar(50) NOT NULL,
	Postal nvarchar(50) NOT NULL,
	SinNo nvarchar(50) NOT NULL,
	BirthDate "datetime" NULL,
);

CREATE TABLE SupervisorDetails (
    S_Id int Primary Key NOT NULL,
	S_Name nvarchar(50) NOT NULL,
	S_Phone nvarchar(50) NULL
);

CREATE TABLE JobDetails (
	JobCode int Primary Key NOT NULL,
	Position nvarchar(50) NOT NULL, 
	PayRate float NULL,
	S_Id int NOT NULL,
	FOREIGN KEY (S_Id) REFERENCES SupervisorDetails(S_Id)
);

CREATE TABLE employeeJob (
    EmpId int Primary Key NOT NULL,
	JobCode int NOT NULL,
	IncTax nvarchar(50) NOT NULL, 
	HireDate "datetime" NULL,
	FOREIGN KEY (EmpId) REFERENCES employeeInfo(EmpId),
	FOREIGN KEY (JobCode) REFERENCES JobDetails(JobCode),
);



CREATE TABLE employeePayroll (
	CompositeId int Identity(1001,1) Primary Key NOT NULL,
	EmpId int NOT NULL,
	PayWeekendDate nvarchar(50) NULL,
	DaysAvailable int NULL, 
	HoursWorked float NULL,
	OverTime float NULL,
	FOREIGN KEY (EmpId) REFERENCES employeeInfo(EmpId)
);


CREATE TABLE Committee (
	ComId int Primary Key NOT NULL,
	ComName nvarchar(50) NOT NULL,
	MeetingNight nvarchar(50) NOT NULL,

);

CREATE TABLE EmpCommittee (
	EC_Id int IDENTITY(100,1) PRIMARY KEY NOT NULL,
	EmpId int NOT NULL,
	ComId int NOT NULL,
	FOREIGN KEY (EmpId) REFERENCES employeeInfo(EmpId),
	FOREIGN KEY (ComId) REFERENCES Committee(ComId)
);

Insert into dbo.employeeInfo values ('97319',	'Novak',	'Gerry', 	'6803 Park Ave.',	'Moose Jaw',	'SK',	'S6H 1X7',	'516303417',	'24-Aug-86'),
('33982',	'Boychuk',	'Robin',	'117 East Broadway',	'Moose Jaw',	'SK',	'S6H 3P5',	'867481381',	'04-Mar-71'),
('51537',	'Smith',	'Kim',	'9745 University Drive',	'Regina',	'SK',	'S4P 7A3',	'112893584',	'29-Nov-82'),
('41822',	'Miller',	'Chris',	'72 Railway Ave.',	'Pense',	'SK',	'S0T 1K4',	'717505366',	'15-Nov-68'),
('3571',	'Hashimoto',	'Jo',	'386 High Street',	'Tuxford',	'SK',	'S0L 8V6',	'374853129',	'23-Jun-56'),
('85833',	'Singh',	'Lindsey',	'1216 Willow Cres.',	'Pasqua',	'SK',	'S0H 5T8',	'466128562',	'15-Mar-75'),
('81216',	'Hansen',	'Jaimie',	'95 Lakeshore Blvd.',	'Caronport',	'SK',	'S0T 3S7',	'615917448',	'04-Mar-83'),
('32177',	'DaSilva',	'Robbie',	'4319 Main St.',	'Moose Jaw',	'SK',	'S6H 2M2',	'306114858',	'18-Feb-51'),
('52421',	'ODay',	'Shelley',	'27 High St.',	'Tuxford',	'SK',	'S0L 8V6',	'936654021',	'31-Jul-63'),
('72690',	'Wong',	'Jodie',	'59 Oslo Square',	'Moose Jaw',	'SK',	'S6H 2H9',	'655971502',	'01-Jan-87'),
('72201',	'Ramirez',	'Kelly',	'1015 Brunswick Lane',	'Moose Jaw',	'SK',	'S6H 4T5',	'635111876',	'29-Sep-86');

Insert into dbo.SupervisorDetails values ('11','Jason Goldberg','306.304.4545'),
('12','Chand Long','306.304.1212'),
('13','Melissa Jones','306.304.8878'),
('14','Joseph Snowdale','306.304.9091');

Insert into dbo.JobDetails values ('3000','Stockperson','12.99','11'),
('5000','Butcher','18','12'),
('2000','Cashier','11.99','13'),
('1000','Greeter','10.25','13'),
('7000','Pharmacist','30','14'),
('8000','Assistant Baker','15.5','12'),
('4000','Baker','17.5','12'),
('6000','Cleaner','13.5','11');

Insert into dbo.employeeJob values (
'97319',	'3000',	'N',	'07-Jul-03'),
('33982',	'5000',	'Y',	'11-Oct-98'),
('51537',	'2000',	'Y',	'02-Dec-01'),
('41822',	'2000',	'Y',	'19-Feb-85'),
('3571',	'1000',	'Y',	'20-Mar-80'),
('85833',	'7000',	'Y',	'27-Jul-02'),
('81216',	'8000',	'Y',	'21-May-02'),
('32177',	'4000',	'Y',	'07-Jul-83'),
('52421',	'6000',	'Y',	'08-Nov-97'),
('72690',	'6000',	'N',	'26-Aug-03'),
('72201',	'3000',	'N',	'26-Aug-03');

Insert into dbo.employeePayroll values ('97319','','','',''),
('33982','23-May-13','7','40.00','0.00'),
('51537','23-May-13','7','27.00','0.00'),
('41822','23-May-13','7','40.00','0.00'),
('3571','23-May-13','7','40.00','0.00'),
('85833','23-May-13','7','37.50','0.50'),
('81216','23-May-13','7','40.00','0.00'),
('32177','23-May-13','7','40.00','3.70'),
('52421','23-May-13','7','22.00','0.00'),
('72690','23-May-13','7','36.00','0.00'),
('72201','30-May-13','6','18.00','0.00'),
('33982','30-May-13','6','38.25','0.00'),
('41822','30-May-13','6','38.00','1.25'),
('3571','30-May-13','6','40.00','0.00'),
('85833','30-May-13','6','22.00','0.00'),
('32177','30-May-13','6','40.00','2.25'),
('52421','30-May-13','6','40.00','4.50');

Insert into dbo.Committee values ('1','OH&S','Fri'),
('2','Party Committee','Wed'),
('3','Social Res. Com.','Mon');

Insert into dbo.EmpCommittee values ('97319','1'),
('72201','1'),
('33982','1'),
('32177','1'),
('51537','2'),
('41822','2'),
('81216','2'),
('72690','2'),
('97319','3'),
('41822','3'),
('32177','3'),
('72690','3');
