CREATE DATABASE studentdatabase;
USE studentdatabase;

CREATE TABLE colleges
(
    college_code varchar (10) not null,
    college_name varchar (50) not null,
    primary key (college_code)

);

CREATE TABLE courses 
(
    course_code varchar (10) not null,
    course_name varchar (100) not null,
    colleges varchar (50) not null,
    primary key (course_code),
    foreign key (college_code) references colleges (college_code) 
);

CREATE TABLE students
(
    id_number varchar (9) not null,
    firstname varchar (50) not null,
    lastname varchar (20) not null,
    yearlevel int not null,
    gender varchar (10) not null
    coursecode varchar (10) not null
    primary key (id_number),
    foreign key (course) references courses (code)
);