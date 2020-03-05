use sqldb;

create table stud_score (

student_id int,

math_score int,

eng_score int,

phil_score int,

music_score int);



insert into stud_score values 

(123511,89,78,45,90),

(255475,88,90,null,87),

(9921100,87,null, null, 98),

(9732453,69,98,78,78),

(578981,59,90,89,null),

(768789,94,80,87,99),

(565789,58,64,72,null);



select * from stud_score;



-- 1. null값을 포함해서 행의 개수를 구하시오
select count(*) from stud_score;

-- 2. null값을 제외한 음악점수 보유자의 숫자를 구하시오
select count(*) from stud_score where music_score is not null;
-- 3. null값 및 중복값을 제외한 영어점수 보유자의 수자를 구하시오
select count(distinct(eng_score)) from stud_score where eng_score is not null;
-- 4. 수학점수의 총합을 구하시오
select sum(math_score) from stud_score;
-- 5. 음악 점수의 평균을 구하시오
select avg(ifnull(music_score,0)) from stud_score;
-- 6. 전과목 최고득점자의 학번을 구하시오
select student_id ,sum(ifnull(math_score,0)+ifnull(eng_score,0)+ ifnull(phil_score,0)+ifnull(music_score,0)) s from stud_score group by student_id order by s desc limit 1;

-- 7. 수학점수의 최고점수와 최저점수를 구하시오
select max(math_score), min(math_score) from stud_score;
-- 8. 평균점수가 가장 높은 과목은 무엇인가
select avg(ifnull(math_score,0)) m, avg(ifnull(eng_score,0)) e, avg(ifnull(phil_score,0)) p, avg(ifnull(music_score,0)) mu, greatest(avg(ifnull(math_score,0)), avg(ifnull(eng_score,0)), avg(ifnull(phil_score,0)), avg(ifnull(music_score,0))) g
from stud_score;
-- 9. 분산이 가장 작은 과목은 무엇인가
select var_samp(ifnull(math_score,0)), variance(ifnull(math_score,0)),variance(ifnull(eng_score,0)),variance(ifnull(phil_score,0)),variance(ifnull(music_score,0)),
least(variance(ifnull(math_score,0)),variance(ifnull(eng_score,0)),variance(ifnull(phil_score,0)),variance(ifnull(music_score,0))) from stud_score;


-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------

create table staff_sal (

id int,

job char(10),

current_sal int,

eng_score int);


insert into staff_sal value

(2148,'officer',40000,90),

(5780,'clerk',32000,98),

(6870, 'manager', 100000,80),

(4565, 'clerk', 30000,79),

(9687,'clerk', 33000,66),

(7337, 'manager', 100000,95),

(1321,'officer', 43000,80),

(9595, 'clerk', 30000, 50);


select * from staff_sal;


-- 1. 직위 별 연봉 평균을 구하시오
select job, avg(current_sal) from staff_sal group by job;


-- 2. clerk은 7%, officer는 5%, manager는 3% 연봉을 인상하기로 하였다. 직원별 인상된 연봉을 현재연봉과 함께 계산하시오
select id, job, current_sal '현재연봉',
case 
	when job = 'officer' then current_sal*1.05
	when job = 'clerk' then current_sal*1.07
	when job = 'manager' then current_sal*1.03     
end as '인상연봉'
from staff_sal;


-- 3. 연봉인상 기준이 직급과 영어점수에 따라 다음과 같다면 사원별 인상되는 연봉금액을 계산하시오. 
select * from staff_sal;

/*
         80점 이상              80점 미만

clerk       7%                  6%

officer     5%                  4%

manager     3%                  2%
*/
select id, job, current_sal '현재연봉',
case 
	when job='clerk' then if( eng_score>=80,current_sal*(1.07),current_sal*(1.06) )
	when job='officer' then if( eng_score>=80,current_sal*(1.05),current_sal*(1.04) )
	when job='manager' then if( eng_score>=80,current_sal*(1.03),current_sal*(1.02) )
end as '인상연봉'
from staff_sal;

-- 4. 위와 같이 연봉이 인상된다면 추가되는 임금비용은 얼마인가?
select sum(current_sal) as '현재',
sum(case 
	when job='clerk' then if( eng_score>=80,current_sal*(1.07),current_sal*(1.06) )
	when job='officer' then if( eng_score>=80,current_sal*(1.05),current_sal*(1.04) )
	when job='manager' then if( eng_score>=80,current_sal*(1.03),current_sal*(1.02) )
end) '추가' , sum(case 
	when job='clerk' then if( eng_score>=80,current_sal*(1.07),current_sal*(1.06) )
	when job='officer' then if( eng_score>=80,current_sal*(1.05),current_sal*(1.04) )
	when job='manager' then if( eng_score>=80,current_sal*(1.03),current_sal*(1.02) )
end) - sum(current_sal) '증가비용'
from staff_sal;



use sqlquiz;
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------



CREATE TABLE PPC_MAST_201312

(

	SSN CHAR(13) NOT NULL , -- PRIMARY KEY ,

	ACCT_NO CHAR(10) NOT NULL,

	ACCT_CD DECIMAL(10) NOT NULL,

	PRFT DECIMAL(15,0),

	BALANCE_AMT DECIMAL(15,0)

);



CREATE INDEX PPC_MAST_201312_i ON PPC_MAST_201312 (SSN, ACCT_NO);





INSERT INTO PPC_MAST_201312 VALUES ('7802221111111', '22033', 130, 504, 56746);

INSERT INTO PPC_MAST_201312 VALUES ('8307153333444', '54412', 110, 585, 23540);

INSERT INTO PPC_MAST_201312 VALUES ('5605099999222', '65433', 340, 213, 987800);

INSERT INTO PPC_MAST_201312 VALUES ('8012301111333', '58721', 320, 780, 310000);

INSERT INTO PPC_MAST_201312 VALUES ('6711032222111', '23422', 120, 5679, 3);

INSERT INTO PPC_MAST_201312 VALUES ('8910103333222', '89811', 310, 240, 40011);

INSERT INTO PPC_MAST_201312 VALUES ('7802221111111', '78022', 100, 899, 4565000);

INSERT INTO PPC_MAST_201312 VALUES ('6711032222111', '35714', 300, 3780, 2545640);

INSERT INTO PPC_MAST_201312 VALUES ('8910103333222', '68740', 310, 233, 522312);

INSERT INTO PPC_MAST_201312 VALUES ('5605099999222', '96870', 330, 7000, 2158);

INSERT INTO PPC_MAST_201312 VALUES ('7802221111111', '89770', 140, 1000, 566600);

INSERT INTO PPC_MAST_201312 VALUES ('6711032222111', '33270', 130, 5600, 68770);

INSERT INTO PPC_MAST_201312 VALUES ('7802221111111', '87890', 340, 1270, 5500000);



select * from PPC_MAST_201312;



/* acct_cd

수신  예금- 100, 110, 120, 130, 140 

여신 대출- 300, 310, 320, 330, 340

수익률 prft

*/


#1. 자산, 부채 총액을 계산하시오..
select 
sum(case
	when BALANCE_AMT then if(ACCT_CD < 300,BALANCE_AMT,0)
end) '부채총액',
sum(case
	when BALANCE_AMT then if(ACCT_CD >= 300,BALANCE_AMT,0)
end) '자산총액',
sum(
case
	when BALANCE_AMT then if(ACCT_CD < 300,-BALANCE_AMT,BALANCE_AMT)
end) '자산-부채'
from PPC_MAST_201312;


#2. 고객당 가입상품수(PPC)
select ssn,count(ssn) from PPC_MAST_201312 group by ssn;

#3. PPC가 3 이상인 고객..
select ssn,count(ssn) from PPC_MAST_201312 group by ssn having count(ssn) >=3;

#4. 고객의 PPC와 총수입

select ssn '고객번호', count(ssn) '고객ppc',
	sum(case when ACCT_CD < 300 then PRFT else 0 end) '고객수익', 
	sum(case when ACCT_CD >= 300 then PRFT else 0 end) '은행수익',
    (select sum(case when ACCT_CD < 300 then PRFT else 0 end) from ppc_mast_201312) '고객총수익',
    (select sum(case when ACCT_CD >= 300 then PRFT else 0 end) from ppc_mast_201312) '은행총수익'
from ppc_mast_201312 group by ssn;

#5. 고객 당 평균 잔고
select ssn,
sum(case
	when BALANCE_AMT then if(ACCT_CD < 300,BALANCE_AMT,-BALANCE_AMT)
end) '잔고',
count(ssn) '계좌수',
round(avg(case
	when BALANCE_AMT then if(ACCT_CD < 300,BALANCE_AMT,-BALANCE_AMT)
end)) '평균잔고'
from PPC_MAST_201312 group by ssn;



use sqlquiz;
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------

USE TESTDB;



CREATE TABLE EMPLOYEE

(

	EMP_ID CHAR(5) PRIMARY KEY NOT NULL,

	GRADE CHAR(10) NOT NULL,

	NM CHAR(10),

	TEL_NO CHAR(20)

);



INSERT INTO EMPLOYEE VALUES ('15501', '8', 'YK MO', '5740');

INSERT INTO EMPLOYEE VALUES ('15687', '8', 'SS CHANG', '5547');

INSERT INTO EMPLOYEE VALUES ('16780', '5', 'HY YOO', '2327');

INSERT INTO EMPLOYEE VALUES ('63278', '7', 'JW PARK', '2304');

INSERT INTO EMPLOYEE VALUES ('87871', '7', 'SW HONG', '2367');

INSERT INTO EMPLOYEE VALUES ('23578', '6', 'JI CHOI', '4654');

INSERT INTO EMPLOYEE VALUES ('32480', '6', 'JM CHA', '1270');

INSERT INTO EMPLOYEE VALUES ('23480', '5', 'KE LEE', '5466');




CREATE TABLE customers

(

	cust_ID int(5) ,

	cust_nm CHAR(10) NOT NULL,

	home_tel CHAR(20)

);



INSERT INTO customers VALUES (5464, 'JH KIM', '02-333-1111');

INSERT INTO customers VALUES (6570, 'LY KIM', '031-111-1133');

INSERT INTO customers VALUES (8780, 'AR KIM', '032-998-5555');

INSERT INTO customers VALUES (5632, 'KK LEE', '02-6677-8888');

INSERT INTO customers VALUES (2445, 'HJ WANG', '055-4444-5666');

INSERT INTO customers VALUES (3210, 'HH AN', '031-888-0111');

INSERT INTO customers VALUES (2596, 'DK SUNG', '02-113-3331');


CREATE TABLE orders

(

	order_ID CHAR(10),

	cust_id CHAR(10),

	emp_id CHAR(10),

	order_df date

);



INSERT INTO orders VALUES ('10000', '2596', '23480', '2013-12-06');

INSERT INTO orders VALUES ('10001', '5464', '16780', '2013-11-01');

INSERT INTO orders VALUES ('10002', '3210', '63278', '2014-03-02');

INSERT INTO orders VALUES ('10003', '2445', '15501', '2014-02-23');

INSERT INTO orders VALUES ('10004', '5632', '15687', '2013-11-13');



select * from employee;

select * from customers;

select * from orders;

#1. 주문이력이 있는 고객아이디, 고객이름, 주문번호..

select c.CUST_ID, cust_nm, order_ID from orders o inner join customers c on o.CUST_ID = c.CUST_ID;

#2. 주문이력이 있는 고객아이디, 고객이름, 주문번호, 판매직원아이디, 판매직원이름

select c.CUST_ID, c.cust_nm, o.order_ID, e.EMP_ID, e.nm from orders o ,customers c, employee e where o.CUST_ID = c.CUST_ID and o.emp_id = e.emp_id;

#3. 주문이력이 있는 곡개은 1, 없는 고객은 0으로 표시

select cust_nm,
	case when order_ID is not null then 1 else 0 end
from customers c left join orders o on c.CUST_ID = o.CUST_ID ;

#4. 주문이력이 있는 고객과 없는 고객의 수..
select 
	sum(case when order_ID is not null then 1 else 0 end) '주문이력o',
	sum(case when order_ID is null then 1 else 0 end)	'주문이력x'
from customers c left join orders o on c.CUST_ID = o.CUST_ID ;

select 
	case when order_ID is not null then '주문했음' else '안했음' end g,
    count(*)
from customers c left join orders o on c.CUST_ID = o.CUST_ID group by g desc;

#5. 판매 이력이 있는 직원은 1, 없는 직원은 0으로 표시..
select
	sum(case when order_ID is not null then 1 else 0 end) '판매이력o',
	sum(case when order_ID is null then 1 else 0 end) '판매이력x'
from employee e left join orders o on e.EMP_ID = o.EMP_ID;

select e.EMP_ID,
	case when order_ID is not null then 1 else 0 end g
from employee e left join orders o on e.EMP_ID = o.EMP_ID;



#6. 직원아이디, 직원 이름, 맡았던 주문번호, 주문 고객아이디, 고객이름을 출력..
select
	o.EMP_ID, nm, o.order_ID, c.CUST_ID, c.cust_nm
from orders o 
	left outer join employee e on e.EMP_ID = o.EMP_ID
	left outer join customers c on c.cust_id = o.cust_id;

select o.EMP_ID, nm, o.order_ID, c.CUST_ID, c.cust_nm 
from customers c, orders o, employee e
where c.CUST_ID = o.CUST_ID and o.EMP_ID = e.EMP_ID;



-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
use sqlquiz;


drop table if exists rcpt_acct;

CREATE TABLE RCPT_ACCT

(

	SSN CHAR(13) NOT NULL,

	ACCT_NO CHAR(10) PRIMARY KEY NOT NULL,

	NEW_DT DATE,

	CNCL_DT DATE,

	RCPT_AMT DECIMAL(15,0)

);


INSERT INTO RCPT_ACCT VALUES ('5707121111000', '578221', '2012-03-26',null , 500000);

INSERT INTO RCPT_ACCT VALUES ('7706302222111', '687322', '2011-12-22', '2013-12-01', 0);

INSERT INTO RCPT_ACCT VALUES ('6508112222333', '658720', '2013-06-08',null , 41324);

INSERT INTO RCPT_ACCT VALUES ('8204073333111', '554520', '2013-09-28', null, 5678740);

INSERT INTO RCPT_ACCT VALUES ('5707121111000', '656421', '2009-11-17',null , 354210);

INSERT INTO RCPT_ACCT VALUES ('7706302222111', '668721', '2010-07-27', null, 547700);

INSERT INTO RCPT_ACCT VALUES ('8204073333111', '223620', '2010-09-11', null, 1000357);

INSERT INTO RCPT_ACCT VALUES ('8204073333111', '275123', '2013-11-26', null, 123000);



drop table if exists cust_party;

CREATE TABLE CUST_PARTY

(

	SSN CHAR(13) PRIMARY KEY NOT NULL,

	PARTY_NM CHAR(10) NOT NULL,

	CUST_ID CHAR(10) NOT NULL,

	TEL_NO CHAR(20) NOT NULL,

	MOBILE_NO CHAR(20) NOT NULL

);


INSERT INTO CUST_PARTY VALUES ('5707121111000', 'AR KIM', '5670', '02-555-6678', '010-1111-1111');

INSERT INTO CUST_PARTY VALUES ('6912081111222', 'SH HONG', '2357', '031-4456-9887', '010-2222-2222');

INSERT INTO CUST_PARTY VALUES ('8311221111333', 'MK KANG', '3977', '051-999-8888', '010-3333-3333');

INSERT INTO CUST_PARTY VALUES ('7105252222000', 'JH KIM', '8988', '032-333-1111', '010-4444-4444');

INSERT INTO CUST_PARTY VALUES ('7706302222111', 'JH LEE', '7702', '033-111-3355', '010-5555-5555');

INSERT INTO CUST_PARTY VALUES ('6508112222333', 'JH RYU', '3574', '02-6666-4444', '010-6666-6666');

INSERT INTO CUST_PARTY VALUES ('8204073333111', 'YC JUNG', '5670', '02-2222-1111', '010-7777-7777');

INSERT INTO CUST_PARTY VALUES ('8911293333222', 'JH JUN', '6989', '031-224-2222', '010-8888-8888');

INSERT INTO CUST_PARTY VALUES ('9011034444111', 'SH LEE', '5570', '033-333-3333', '010-9999-9999');



select * from cust_party;

select * from rcpt_acct;


#1. 현재 살아있는 고객의 휴대폰 번호를 찾고, 살아있는 계좌수를 기준으로 오름차순 정렬하시오
select c.ssn, MOBILE_NO, ACCT_NO, count(ACCT_NO)
from cust_party c, rcpt_acct r 
where c.SSN = r.SSN and cncl_dt is null 
group by ssn order by count(ACCT_NO);

#2. 현재 살아있는 계좌수가 두 개 이상이고 수신잔액의 총합이 50만원 이상인 고객의 주민번호, 이름, 휴대전화, 계좌수, 수신잔액 총합을 주민번호기준으로 오름차순 정렬하시오. 

select c.ssn, PARTY_NM, MOBILE_NO, count(c.ssn) '계좌수', sum(RCPT_AMT) 
from rcpt_acct r, cust_party c 
where c.SSN = r.SSN and cncl_dt is null 
group by c.ssn 
having count(c.ssn)>=2 and sum(RCPT_AMT) >=500000 
order by c.ssn;

#3. 현재 살아있는 계좌수가 두 개 이상이고 모든 수신 잔액의 합이 50만원 이상인 고객 대상 sns 마케팅을 하려고 하는데 ..
select * from rcpt_acct r, cust_party c where c.SSN = r.SSN and cncl_dt is null group by c.ssn having count(*)>=2 and sum(RCPT_AMT) >=500000;

 

-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------

CREATE TABLE card_acct

(

	SSN CHAR(13) NOT NULL,

	cc_grade int(3) NOT NULL,

	issue_dt DATE,

	close_dt DATE,

	valid_yymm char(10),

	cash_use_flg CHAR(5),

    cc_variety_cd CHAR(5)

);



INSERT INTO card_acct VALUES ('5707121111000', '8', '2012-03-26', null, '201503', 'Y', '11111');

INSERT INTO card_acct VALUES ('7706302222111', '2', '2011-12-22', '2013-12-01', '201512', null, '44444');

INSERT INTO card_acct VALUES ('6508112222333', '8', '2013-06-08', null, '201806', 'Y', '11111');

INSERT INTO card_acct VALUES ('8204073333111', '8', '2013-09-28', null, '201809', 'Y', '22222');

INSERT INTO card_acct VALUES ('5707121111000', '1', '2009-11-17', null, '201411', null, '33333');

INSERT INTO card_acct VALUES ('7706302222111', '8', '2010-07-27', null, '201407', null, '22222');

INSERT INTO card_acct VALUES ('8204073333111', '2', '2010-09-11', null, '201509', 'Y', '44444');

INSERT INTO card_acct VALUES ('8204073333111', '1', '2013-11-26', null, '201811', null, '33333');



/* cc_variety_cc

11111 - 이기자카드

22222 - 지키자카드

33333 - sql카드

44444 - 행복한 카드

*/



drop table if exists cust_party;

CREATE TABLE CUST_PARTY



(

	SSN CHAR(13) PRIMARY KEY NOT NULL,

	PARTY_NM CHAR(10) NOT NULL,

	CUST_ID CHAR(10) NOT NULL,

	TEL_NO CHAR(20) NOT NULL,

	MOBILE_NO CHAR(20) NOT NULL

);



INSERT INTO CUST_PARTY VALUES ('5707121111000', 'AR KIM', '5670', '02-555-6678', '010-1111-1111');

INSERT INTO CUST_PARTY VALUES ('6912081111222', 'SH HONG', '2357', '031-4456-9887', '010-2222-2222');

INSERT INTO CUST_PARTY VALUES ('8311221111333', 'MK KANG', '3977', '051-999-8888', '010-3333-3333');

INSERT INTO CUST_PARTY VALUES ('7105252222000', 'JH KIM', '8988', '032-333-1111', '010-4444-4444');

INSERT INTO CUST_PARTY VALUES ('7706302222111', 'JH LEE', '7702', '033-111-3355', '010-5555-5555');

INSERT INTO CUST_PARTY VALUES ('6508112222333', 'JH RYU', '3574', '02-6666-4444', '010-6666-6666');

INSERT INTO CUST_PARTY VALUES ('8204073333111', 'YC JUNG', '5670', '02-2222-1111', '010-7777-7777');

INSERT INTO CUST_PARTY VALUES ('8911293333222', 'JH JUN', '6989', '031-224-2222', '010-8888-8888');

INSERT INTO CUST_PARTY VALUES ('9011034444111', 'SH LEE', '5570', '033-333-3333', '010-9999-9999');


select 
sum(case when close_dt is null then 0 else 1 end) '카드를 취소한사람',
sum(case when issue_dt is null then 1 else 0 end) '카드를 만들지 않은 사람'
from cust_party p left join card_acct a on a.ssn=p.SSN;

select a.ssn,
sum(case when close_dt is null and issue_dt is not null then 1 else 0 end) '현재 카드가 있는 사람',
sum(case when issue_dt is null or close_dt is not null then 1 else 0 end) '카드를 만들지 않았거나 취소한 사람'
from cust_party p left join card_acct a on a.ssn=p.SSN group by a.ssn;



select 
case when close_dt is null then 0 else 1 end canceled,
case when issue_dt is null then 1 else 0 end nCard
from cust_party p left join card_acct a on a.ssn=p.SSN ;

select 
*
from cust_party p left join card_acct a on a.ssn=p.SSN ;

select * from cust_party;

select * from card_acct a, cust_party p where a.ssn=p.SSN;

#1. 현재 살아있는 카드 보유고객과 미보유 고객수

select 
	case when close_dt is null then '있음' else '없음' end g,
    count(*)
from card_acct a, cust_party p where a.ssn=p.SSN group by g;

#2. 현재 살아있는 카드 보유 고객의 주민번호, 이름, 아이디, 자택번호 및 휴대번호
select 
	a.ssn, PARTY_NM, CUST_ID, TEL_NO, MOBILE_NO
from card_acct a, cust_party p where a.ssn=p.SSN and close_dt is null;

#3. 카드 등급이 1, 2에 해당하는 고객의 주민번호, 이름, 집번호, 핸드폰번호....
select 
	a.ssn, PARTY_NM, TEL_NO, MOBILE_NO, cc_grade
from card_acct a, cust_party p where a.ssn=p.SSN and close_dt is null and cc_grade in (1,2);



-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------

drop table if exists cust_party;

CREATE TABLE CUST_PARTY



(

	SSN CHAR(13) PRIMARY KEY NOT NULL,

	PARTY_NM CHAR(10) NOT NULL,

	CUST_ID CHAR(10) NOT NULL,

	TEL_NO CHAR(20) NOT NULL,

	MOBILE_NO CHAR(20) NOT NULL

);



INSERT INTO CUST_PARTY VALUES ('5707121111000', 'AR KIM', '5670', '02-555-6678', '010-1111-1111');

INSERT INTO CUST_PARTY VALUES ('6912081111222', 'SH HONG', '2357', '031-4456-9887', '010-2222-2222');

INSERT INTO CUST_PARTY VALUES ('8311221111333', 'MK KANG', '3977', '051-999-8888', '010-3333-3333');

INSERT INTO CUST_PARTY VALUES ('7105252222000', 'JH KIM', '8988', '032-333-1111', '010-4444-4444');

INSERT INTO CUST_PARTY VALUES ('7706302222111', 'JH LEE', '7702', '033-111-3355', '010-5555-5555');

INSERT INTO CUST_PARTY VALUES ('6508112222333', 'JH RYU', '3574', '02-6666-4444', '010-6666-6666');

INSERT INTO CUST_PARTY VALUES ('8204073333111', 'YC JUNG', '5670', '02-2222-1111', '010-7777-7777');

INSERT INTO CUST_PARTY VALUES ('8911293333222', 'JH JUN', '6989', '031-224-2222', '010-8888-8888');

INSERT INTO CUST_PARTY VALUES ('9011034444111', 'SH LEE', '5570', '033-333-3333', '010-9999-9999');




CREATE TABLE DLQ_PARTY

(

	SSN CHAR(13) NOT NULL,

	ACCT_NO CHAR(10) NOT NULL,

	DLQ_ST DATE,

	DLQ_END DATE,

	DLQ_DURATION DECIMAL(15,0),

	CURR_DLQ CHAR(10)

);

CREATE INDEX DLQ_PARTY_I ON DLQ_PARTY (SSN, ACCT_NO);



INSERT INTO DLQ_PARTY VALUES ('6912081111222', '32110', '2012-07-30', '2012-08-15', 16, 'N');

INSERT INTO DLQ_PARTY VALUES ('8204073333111', '88930', '2012-09-21', '2012-10-01', 10, 'N');

INSERT INTO DLQ_PARTY VALUES ('8204073333111', '35780', '2013-01-26', '2013-01-29', 3, 'N');

INSERT INTO DLQ_PARTY VALUES ('7706302222111', '78320', '2013-11-01', NULL, 31, 'Y');

INSERT INTO DLQ_PARTY VALUES ('6912081111222', '87120', '2013-10-01', NULL, 62, 'Y');

INSERT INTO DLQ_PARTY VALUES ('8204073333111', '56830', '2013-11-18', '2013-11-28', 10, 'N');

INSERT INTO DLQ_PARTY VALUES ('8311221111333', '78720', '2013-11-14', NULL, 18, 'Y');

INSERT INTO DLQ_PARTY VALUES ('8311221111333', '98730', '2013-11-16', NULL, 16, 'Y');

INSERT INTO DLQ_PARTY VALUES ('6508112222333', '57830', '2012-12-01', '2012-12-02', 1, 'N');

INSERT INTO DLQ_PARTY VALUES ('6508112222333', '78770', '2013-09-19', NULL, 74, 'Y');

select * from CUST_PARTY;

select * from dlq_party;

#1. 연체일이 30일 미만인 고객이 주민번호, 이름, 휴대번호
select ssn, PARTY_NM, MOBILE_NO from cust_party
	where ssn in (select distinct ssn from dlq_party 
		where CURR_DLQ = 'Y' and DLQ_DURATION <30);
        
#2. 현재 연체중이거나 과거 10일 이상 연체기록이 있는 고객을 제외한 고객의 주민번호, 이름. 휴대번호..
select ssn, PARTY_NM, MOBILE_NO from cust_party
	where ssn not in (select distinct ssn from dlq_party 
		where CURR_DLQ = 'Y' or DLQ_DURATION <10);


#3. 현재 10일 이상 연체중인 고객의 고객의 주민번호, 이름. 휴대번호, 연체일수, 현재의 연체 상태..
select c.ssn, PARTY_NM, MOBILE_NO, DLQ_DURATION,CURR_DLQ from cust_party c, dlq_party d
	where c.ssn = d.ssn and CURR_DLQ = 'Y' and DLQ_DURATION >=10 and c.ssn in (select distinct c.ssn from dlq_party);



-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------------------------------------------------------------------------------------------------------
 

create table customers (

id int,

name char(10),

city char(15),

country char(20) );



insert into customers values 

(1, 'sue', 'berlin', 'germany'),

(2, 'david', 'bern', 'switzerland'),

(3, 'sam', 'nantes', 'france'),

(4, 'kim', ' bergamo', 'brazil'),

(5, 'lee', 'versailles', 'brazil'),

(6, 'berney', 'bergamo', 'italy'),

(7, 'sandy', 'berlin', 'germany'),

(8, 'youn','seoul','korea');



select * from customers;




#1. 'NY'로 끝나는 나라에 거주하는 고객.. 추출..
select name,country from customers where country like '%ny';
#2. 'ES'를  포함한 도시에 사는 고객..
select name, city from customers where city like '%es%';
#3. 'BER'로 시작하는 도시에 사는 고객
select name, city from customers where city like 'ber%';
#4. 이름이 'SU'로 시작하는 3글자인 고객
select name from customers where name like 'su_';
#5. 도시이름이 'B'로 시작해서 'N'으로 끝나는 곳에 거주하는 고객
select name, city from customers where city like 'b%n';
