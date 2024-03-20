create table student
	(student_id			serial, 
	 first_name			text not null, 
	 last_name		text not null, 
	 email		text not null unique,
	 enrollment_date	Date,
	 primary key (student_id)
	);
