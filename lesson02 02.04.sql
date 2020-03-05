select cast('2020-10-19 12:35:29.123' as date) as 'Date';
select cast('2020-10-19 12:35:29.123' as time) as 'Time';
select cast('2020-10-19 12:35:29.123' as datetime) as 'datetime';

use sqldb;

set @myvar1 = 5;
set @myvar2 = 3;
set @myvar3 = 4.25;
set @myvar4 = '가수이름 =>';

select @myvar1;
select @myvar2 +@myvar3;
select @myvar4, name from usertbl where height > 180;

-- prepare/execute

prepare myquery from 'select name, height from usertbl order by height limit 5';

execute myquery;

prepare myquery1 from 'select name, height from usertbl order by height limit ?';

execute myquery1 using @myvar2;

select avg(amount) as '평균구매개수' from buytbl;

select cast(avg(amount) as signed integer) as '평균구매개수' from buytbl;

select convert(avg(amount), signed integer) as '평균구매개수' from buytbl;

-- price/amount 를 char로 형변환후 concat으로 x와 = 과 함께 이어버림

select num, concat(cast(price as char(10)), ' X ', cast(amount as char(4)), ' =') as '단가 x 수량', price*amount as '구매액'  from buytbl;


select '100' + '200' ;
select '100' + 'ㅁ200' ; -- 문자가 앞에 있으면 숫자로 변환불가능
select concat('100' + '200') ;
select concat(100 + '200') ;
select 1 > '2mega'; -- 거짓 0
select 3 > '2MEGA'; -- 참 1
select 0 = 'mega2'; -- 참 1 mega를 변환하지 못하여 0으로 인식함

select if (100>200, '참이다', '거짓이다'); -- if (x,y) 참이면 x 거짓이면 y 출력
select ifnull(null, '널이구요'), ifnull(100, '널이군요'); -- ifnull(x,y) x가 null이면 y 출력, x가 null이 아니면 x 출력
select nullif(100,100), nullif(200,100); -- nullif(x,y) x=y이면 null출력, x≠y이면 x 출력

select case 10  -- case~ when else 구문
	when 1 then'일'
	when 5 then'오'
	when 10 then'십'
    else '모름'
end;

select bit_length('abc'), char_length('abc'), length('abc');

select bit_length('가나다'), char_length('가나다'), length('가나다');

select concat_ws('-', '2020', '01', '01');

select format(123456.123456, 2);

select ascii('A');

select cast(char(65) as char);

select insert('abcdefghi', 3,2,'@@@'); -- 3번부터 2개를 @@@로 변환
select insert('abcdefghi', 2,3,'@@@'); -- 3번부터 2개를 @@@로 변환
select left('abcdefghi', 3);  -- 왼쪽에서 3개 추출
select right('abcdefghi', 3); -- 오른쪽에서 3개 추출

select lower('aBCDEFg');
select upper('aBCDEFg');

select lpad('이것이', 5, '##'); -- 5칸에서 문자열을 채우고 남는 공간이 있으면 왼쪽에 ##을 채움
select rpad('이것이', 5, '##'); -- 5칸에서 문자열을 채우고 남는 공간이 있으면 오른쪽에 ##을 채움

select ltrim('  이것이'); -- 왼쪽 공백제거
select rtrim('이것이   '); -- 왼쪽 공백제거

select repeat('이것이',3); -- repeat(x,y) x를 y회 반복

select replace('이것이 MySQL이다', '이것이', 'This is'); -- replace(A, B, C)  A에서 B를 C로 변경

select reverse('mysql'); -- 순서를 거꾸로 출력

select concat('이것이', space(10), 'MySql이다');

select substring('대한민국만세', 3,2);

select substring_index('cafe.naver.com', '.',2); -- substring_index(a,b,c) a를 b로 나누어서 앞에서부터 c개를 가져옴
select substring_index('cafe.naver.com', '.',-2); -- substring_index(a,b,c) a를 b로 나누어서 뒤에서부터 c개를 가져옴

select abs(-100);

select ceiling(4.7); -- 올림

select floor(4.7); -- 내림

select round(4.7); -- 반올림

select mod(157, 10); -- 나머지

select pow(2,3); -- pow(x,y) x의 y제곱

select sqrt(9); -- 제곱근

select sign(100); -- 양수면 1
select sign(-100); -- 음수면 -1
select sign(0); -- 0이면 0

select truncate(12345.12345,2); -- 소수점 자릿수
select truncate(12345.12345,-2); -- 음수를 적을경우 x번째 자릿수까지 0으로 표기함


select adddate('2020-01-01', interval 31 day);
select adddate('2020-01-01', interval 1 month);

select subdate('2020-01-01', interval 31 day);
select subdate('2020-01-01', interval 3 month);

select addtime('2020-01-01 23:59:59', '1:1:1');
select subtime('2020-01-01 23:59:59', '1:1:1');

select curdate();

select curtime();

select current_time();

select now();

select year(curdate());

select month(curdate());

select dayofweek(curdate()); -- 일요일부터 1 월요일 2 화요일 3 ...

select hour(curtime());
select minute(curtime());
select second(curtime());

select date(now());

select time(now());

select datediff('2020-01-01', now());
select timediff('23:23:59', '12:11:19');

select dayofweek(curdate());

select monthname(curdate());

select dayofyear(curdate());
select dayofmonth(curdate());

select last_day('2020-02-01');
select makedate(2020,65);
select maketime(12,11,10);

select period_add(202001,11);
select period_diff(202001, 201812);

select quarter('2020-07-07');

select time_to_sec('12:11:10');


use sqldb;
create table maxtbl(
col1 longtext,
col2 longtext);

insert into maxtbl values(repeat('a', 1000000), repeat('가', 1000000));

select length(col1), length(col2) from maxtbl;

insert into maxtbl values(repeat('a', 10000000), repeat('가', 10000000));


select * into outfile 'C:/temp/usertbl.txt' from usertbl;

select * from usertbl;
select * from buytbl;

select * from buytbl inner join usertbl on buytbl.userid = usertbl.userid;

select buytbl.userid, name, prodname, addr from buytbl inner join usertbl on buytbl.userid = usertbl.userid;

select buytbl.userid, name, prodname, concat(mobile1,'-', mobile2) as '연락처' , addr from buytbl inner join usertbl on buytbl.userid = usertbl.userid;

select buytbl.userid, name, prodname, concat(mobile1,'-', mobile2) as '연락처' , addr from buytbl inner join usertbl on buytbl.userid = usertbl.userid where usertbl.userid='Jyp';

select b.userid, name, prodname, concat(mobile1,'-', mobile2) as '연락처' , addr from buytbl b inner join usertbl u on b.userid = u.userid order by u.userid;

select * from buytbl b left outer join usertbl u on b.userid = u.userid order by u.userid;

select * from buytbl b right outer join usertbl u on b.userid = u.userid order by u.userid;

select * from buytbl b join usertbl u on b.userid = u.userid order by u.userid;

select * from usertbl u, buytbl b where u.userid=b.userid; -- join을 쓰지 않고 바로 합치기


drop database if exists shopdb;
drop database if exists moel;
drop database if exists shopdb;
drop database if exists tabledb;

create database tabledb;
use tabledb;

drop table if exists buytbl, usertbl;

create table usertbl(
userid char(8),
name nvarchar(10),
birthyear int,
addr nchar(2),
mobile1 char(3),
mobile2 char(8),
height smallint,
mdate date);

create table buytbl(
num int,
userid char(8),
prodname nchar(6),
groupname nchar(4),
price int,
amount smallint
);
/* constraint 제약조건 설정하기
primary key
foreign key
unique
default
null, not null

*/


drop table if exists buytbl, usertbl;

create table usertbl(
userid char(8) primary key,
name nvarchar(10) not null,
birthyear int not null,
addr nchar(2) not null,
mobile1 char(3) null,
mobile2 char(8) null,
height smallint null,
mdate date);

-- on update/ on delete cascade 부모키의 수정/삭제시 자식키도 같이 변동됨

create table buytbl(
num int auto_increment primary key,
userid char(8) not null,
prodname nchar(6) not null,
groupname nchar(4) not null,
price int not null,
amount smallint  not null,
foreign key(userid) references usertbl(userid)
on update cascade on delete cascade
);

insert into usertbl values('LSG','이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO userTbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO userTbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO userTbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');

select * from usertbl;
select * from buytbl;

-- ignore  에러가 나지 않은 데이터는 정상입력됨

INSERT ignore INTO buytbl VALUES(null, 'JYP', '모니터', '전자', 200, 1);
INSERT ignore INTO buytbl VALUES(null, 'KBS', '노트북', '전자', 1000, 1);
INSERT ignore INTO buytbl VALUES(null, 'KBS', '운동화', null, 30, 2);

update usertbl set userid='ppp' where userid='jyp';

delete from usertbl where userid='ppp';
delete from usertbl where userid='ppp';

select * from buytbl;



drop table if exists buytbl;
drop table if exists usertbl;

create table usertbl(
userid char(8) primary key,
name nvarchar(10) not null,
birthyear int not null default -1,
addr nchar(2) not null default '서울',
mobile1 char(3) null,
mobile2 char(8) null,
height smallint null default 170,
mdate date);

insert into usertbl values('LL','이혜리', default,  default, '011', '123456', default, null);

select* from usertbl;

insert into usertbl(userid, name) values('Kay', '김아영');

insert into usertbl values('WB','원빈',1982,'대전','019','9876543',176,'2017.5.5');

alter table usertbl add homepage varchar(30) default 'http://www.naver.com' null;

alter table usertbl drop column mobile1;

alter table usertbl change column name uname varchar(20) null;

alter table usertbl add constraint pk_userid primary key (userid);

select* from usertbl;


create table buytbl(
num int auto_increment primary key,
userid char(8) not null,
prodname nchar(6) not null,
groupname nchar(4) not null,
price int not null,
amount smallint  not null
);

alter table buytbl add constraint fk_usertbl_buytbl foreign key (userid) references usertbl (userid);

describe buytbl;

alter table buytbl drop foreign key fk_usertbl_buytbl;







