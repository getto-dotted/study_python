
show databases;

use employees;

show tables;

select * from employees;

select * from titles;

select first_name, last_name from employees;

-- select col, cols from table;

show tables;

show table status;

/*

select * from salaries;

select emp_no, salary from salaries;

*/

describe employees;

select first_name, gender, hire_date from employees;

select first_name as '성', gender as '성별', hire_date as '입사일' from employees;

drop database if exists sqldb;

create database sqldb;


use sqldb;

-- table 생성 : table 이름 (usertbl), column (userid char(8), name varchar(10))



-- create 객체 객체명;

create table usertbl (

userid char(8),

name varchar(10));



show tables;



drop table usertbl;



create table usertbl(

userid char(8) not null,

name varchar(10) not null,

birthyear int not null,

addr char(2) not null,

mobile1 char(3),

mobile2 char(8),

height smallint,

mdate date);



show tables;

describe usertbl;


create table buytbl(

num int,

userid char(8) not null,

prodname char(6) not null,

groupname char(4),

price int not null,

amount smallint not null);


show tables;

-- userble 

-- 'LSG','이승기', 1987, '서울', '011', 1111111', 182, '2008-8-8'

-- buytble

-- null, 'KBS', '운동화', null, 30, 2

-- insert into 테이블명 values (데이터값.....)



insert into usertbl values ('LSG','이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');

insert into buytbl values (null, 'KBS', '운동화', null, 30, 2);

select * from usertbl;

select * from buytbl;

/*

usertbl

'KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4'

'KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7'

'JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4'

'SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12

-12'

'LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9'

'YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-

5-5'

'EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3'

'JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010

-10-10'

'BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5'

*/

INSERT INTO userTbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');

INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');

INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');

INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');

INSERT INTO userTbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');

INSERT INTO userTbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');

INSERT INTO userTbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');

INSERT INTO userTbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');

INSERT INTO userTbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');

INSERT INTO userTbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');

select * from usertbl;

select name, birthyear from usertbl;

select name, birthyear from usertbl where height>170;

/*
buytbl
*/
INSERT INTO buytbl VALUES(null, 'KBS', '운동화', null, 30, 2);
INSERT INTO buytbl VALUES(null, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(null, 'JYP', '모니터', '전자', 200, 1);
INSERT INTO buytbl VALUES(null, 'BBK', '모니터', '전자', 200, 5);
INSERT INTO buytbl VALUES(null, 'KBS', '청바지', '의류', 50, 3);
INSERT INTO buytbl VALUES(null, 'BBK', '메모리', '전자', 80, 10);
INSERT INTO buytbl VALUES(null, 'SSK', '책', '서적', 15, 5);
INSERT INTO buytbl VALUES(null, 'EJW', '책', '서적', 15, 2);
INSERT INTO buytbl VALUES(null, 'EJW', '청바지', '의류', 50, 1);
INSERT INTO buytbl VALUES(null, 'BBK', '운동화', null, 30, 2);
INSERT INTO buytbl VALUES(null, 'EJW', '책', '서적', 15, 1);
INSERT INTO buytbl VALUES(null, 'BBK', '운동화', null, 30, 2);

select * from buytbl;

-- 김경호의 데이터를 출력alter

select * from usertbl;

select * from usertbl where name = '김경호';

-- 출생이 1970이후/ 키가 182 이상

select userid, name, birthyear, height from usertbl where birthyear>=1970 and height>=182;

select userid, name, birthyear, height from usertbl where birthyear>=1970 or height>=182;

-- 키 180이상 183 이하

select * from usertbl where height >=180 and height <=183;

select * from usertbl where height between 180 and 183;

-- 주소지 경남/ 전남/ 경북/ 에 거주하는 사람들

select name, addr from usertbl where addr = '경남' or addr = '전남' or addr = '경북';

select name, addr from usertbl where addr in('경남', '전남', '경북');

-- 이름이 '김'으로 시작하는 사람의 데이터를 출력

select * from usertbl where name like '김%';

-- 이름이 '종신' 인 모든 사람

select name, height from usertbl where name like '_종신';

-- 김경호보다 키가 큰사람의 데이터//서브쿼리문

select name, height from usertbl where height >= (select height from usertbl where name ='김경호');

select * from usertbl;

-- 경남 거주하는 사람보다 키가 큰 사람의 이름과 키

select name, height from usertbl where height >= (select height from usertbl where addr ='경남'); 
-- 서브쿼리의 결과가 복수개이므로 에러발생

-- 복수개의 대상의 비교연산 : 전체만족 or 부분만족

select name, height from usertbl where height >= all(select height from usertbl where addr ='경남');

select name, height from usertbl where height >= any(select height from usertbl where addr ='경남');

-- 경남에 사는 사람과 키가 동일한 사람의 데이터

select name, height from usertbl where height in (select height from usertbl where addr ='경남' ); -- min~max가 아니라 or임

-- name, mdate를 추출 날짜기준 올림차순 -> order by 조건절의 맨 뒤에 붙임

select name, mdate from usertbl order by mdate;

-- 내림차순
select name, mdate from usertbl order by mdate desc;

-- height 내림차순 name 오름차순으로 name height출력

select name, height from usertbl order by height desc, name asc;

-- usertbl에서 주소를 중복값을 제외하고 출력alter

select distinct(addr) from usertbl;

-- employees에서 employees 테이블의 사원번호, 입사일 기준 올림차순으로 출력
-- 입사일자가 가장 오래된 사원 순 5명

use employees;

select emp_no, hire_date from employees order by hire_date limit 5;

-- 가장최근 입사5명
select emp_no, hire_date from employees order by hire_date desc limit 5;

-- 가장 최근 입사한 순으로 밑에서 6~ 10등                           (limit : 5개만   offset: 5번째부터)
select emp_no, hire_date from employees order by hire_date desc limit 5 offset 5;

-- table copy

use sqldb;

CREATE TABLE buytbl2 (SELECT * FROM buytbl);
select * from buytbl2;

CREATE TABLE buytbl3 (SELECT userid, prodname FROM buytbl);
select * from buytbl3;


-- groupby
# group by 컬럼1, 컬럼2...으로 멀티인덱스를 잡을 수 있다.

select * from buytbl;
-- id별 구매총량
select userid, sum(amount) from buytbl group by userid;

-- id별 구매총액
select userid as '아이디', sum(price*amount) as '총액' from buytbl group by userid;

-- 아이디별 평균 구매량

select userid as '아이디', avg(amount) as '평균구매량' from buytbl group by userid;

-- 아이디별 최대 구매총액

select userid as '아이디', max(price*amount) as '최대 구매액' from buytbl group by userid;

-- 키가 가장 큰 사람의 키와 이름, 키가 가장 작은 사람의 키와 이름

select name, height from usertbl where height = (select max(height) from usertbl) or height = (select min(height) from usertbl);

select name, height from usertbl where height in ((select max(height) from usertbl), (select min(height) from usertbl));


-- 회원의 수
use sqldb;

select count(*) from usertbl where mobile1 is not null and mobile2 is not null;

select count(*) from usertbl;

select count(distinct(userid)) from usertbl;

-- 휴대폰이 있는 사용자수

select count(distinct(mobile2)) from usertbl;

select distinct(userid), count(distinct(mobile2)) from usertbl;

-- 회원별 구매 총액이 1000이상인 회원의 id와 구매액

select userid, sum(price*amount) from buytbl group by userid having sum(price*amount) >=1000;


-- 구매총액이 200이 넘는 회원중 상위 2명
select userid'아이디', sum(price*amount)'구매총액' from buytbl group by userid having sum(price*amount) >=100 order by sum(price*amount) desc limit 2;


-- testtbl1 테이블 생성 id int, username char(3) age int

create table testtbl1(
id int,
username char(3),
age int);

insert into testtbl1 values(1, '홍길동', 25);
insert into testtbl1 values(2, '설현', null); -- insert into testtbl1(id, username) values(2, '설현');
insert into testtbl1 values(3, '초아', 26); -- insert into testtbl1(username, id, age) values('초아',3, 26 );

select * from testtbl1;


use sqldb;

create table testtbl2(
id int auto_increment primary key,
username char(3),
age int);

insert into testtbl2 values (null, '지민', 25);
insert into testtbl2 values (null, '유나', 22);
insert into testtbl2 values (null, '유경', 21);

select * from testtbl2;

create table testtbl5(select emp_no, first_name, last_name from employees.employees);

create table testtbl4(id int, fname varchar(50), lname varchar(50));

insert into testtbl4(select emp_no, first_name, last_name from employees.employees);

select * from testtbl4;

update testtbl4 set lname='없음' where fname= 'Parto';

select * from testtbl4 where fname='Parto';

select * from buytbl;

update buytbl set price=price*1.5;


delete from testtbl4 where fname='Berni';

select * from testtbl4 where fname='Berni';

delete from testtbl4 where fname='Parto' limit 100;

select count(*) from testtbl4 where fname='Parto';


create table bigtbl1 (select * from employees.employees);
create table bigtbl2 (select * from employees.employees);
create table bigtbl3 (select * from employees.employees);

select * from bigtbl1;
select * from bigtbl2;
select * from bigtbl3;

show tables;

delete from bigtbl1; -- 데이터삭제 및 로그기록남김

drop table bigtbl2; -- 테이블 삭제

truncate table bigtbl3; -- 데이터 삭제
