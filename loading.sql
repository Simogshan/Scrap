create table temp (first_name varchar(60), last_name varchar(60), stree_name varchar(60), city varchar(50), state varchar(60), post_code varchar(15), email varchar(78), date_of_birth date, company_name varchar(70));

source /home/ec2-user/loads/file.sql

alter table temp modify column street_name varchar(60);

select count(*) from temp;

create table company( company_id int not null auto_increment primary key, company_name varchar(75));

insert into company (company_name) select distinct company_name from temp;

select company_name from temp group by company_name;

select count(*) from company;

create table person (person_id int not null auto_increment primary key, company_id int, first_name varchar(60), last_name varchar(60), email varchar(78), date_of_birth date, age int, foreign key (company_id) references company(company_id));

insert into person (company_id,first_name,last_name,email,date_of_birth) select c.company_id, t.first_name, t.last_name, t.email, t.date_of_birth from company c, temp t where c.company_name = t.company_name;

update  person set age = date_format(from_days(datediff(now(),date_of_birth)), '%Y') + 0;

select age from person;

delete from person where age > 58;

delete from person where age < 18;

create table time_temp (date date, time time, person_id int);

source /home/ec2-user/loads/time_temp.sql

create table attendance (attendance_id int not null auto_increment primary key, person_id int, date date, in_time time, foreign key (person_id) references person(person_id));

insert into attendance (person_id,date,in_time) select p.person_id, t.date, t.time from person p, time_temp t where p.person_id = t.person_id ;

select * from attendance ;

select in_time from attendance where person_id = 1;

select avg(in_time) from attendance where person_id = 1;

select dayname(date) from attendance where person_id = 1;

delete from attendance where dayname(date) = 'Saturday';

delete from attendance where dayname(date) = 'Sunday';

select timediff(in_time, "09:00:00") from attendance where person_id = 1;

select extract(dayfrom(timediff(in_time, "09:00:00"))) from attendance where person_id = 1 and date = "2023-03-31";

select sum(day(timediff(in_time, "09:00:00"))) from attendance where person_id = 1 and date = "2023-03-31";

select sum(day(timediff(in_time, "09:00:00"))) from attendance where person_id = 1 and date = "2023-03-31";

select convert(timediff(in_time, "09:00:00"), time) from attendance where person_id = 1 and date = "2023-03-31";

select day(timediff(in_time, "09:00:00")) from attendance where person_id = 1 and date = "2023-03-31";

select day(timediff(in_time, "09:00:00")) from attendance where person_id = 1;

select sum(day(timediff(in_time, "09:00:00"))) from attendance where person_id = 1;

select avg(day(timediff(in_time, "09:00:00"))) from attendance where person_id = 1;

select convert(sum(timediff(in_time, "09:00:00")), time) from attendance where person_id = 1;

create table statecode (state_code_id int not null auto_increment primary key, state_code varchar(10), state varchar(30));

source /home/ec2-user/state.sql;

create table address (address_id  int not null auto_increment primary key, person_id int, street_name varchar(40), city varchar(40), state int, post_code varchar(15), foreign key (person_id) references person(person_id), foreign key (state) references statecode (state_code_id));

insert into address (person_id, street_name, city, state, post_code) select p.person_id, t.street_name, t.city, s.state_code_id, t.post_code  from person p, temp t, statecode s where p.email = t.email and  t.state = s.state_code;










drop database db_name;
