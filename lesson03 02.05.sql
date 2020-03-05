create database sqlquiz;

use sqlquiz;

create table emp(
	id char(3) primary key not null,
	POSITION char(10) not null,
	party_nm char(10) not null,
	manager_id char(10) not null,
	team_nm char(10) not null,
	grade char(10) not null
);

insert into emp values('650','대리','이재훈','1270','마케팅부','1');
insert into emp values('540','과장','장성수','3221','리스크부','2');
insert into emp values('210','차장','문보미','3914','인사팀','3');
insert into emp values('347','차장','정호천','3942','기획팀','3');
insert into emp values('970','부장','김영성','3221','리스크부','2');
insert into emp values('234','대리','오윤경','1270','마케팅부','2');
insert into emp values('711','과장','이재중','3914','인사팀','2');

-- 어떤 직급이 있는가

select distinct(position) from emp;

-- 직급에 따라 어떤 고과를 받았는가

select position, grade from emp group by position;

-- 인사고과 주는 사람 구하기

select party_nm from emp where team_nm like '%인사%';

-- 인사고과를 몇명이 주고 있는가
select count(team_nm) from emp where team_nm like '%인사%';




CREATE TABLE CARD_TRAN_201311

(

	CMF CHAR(4) PRIMARY KEY NOT NULL,

	PARTY_NM CHAR(10) NOT NULL,

	SEG CHAR(10) NOT NULL,

	PIF_AMT DECIMAL(15,0),

	INST_AMT DECIMAL(15,0),

	OVRS_AMT DECIMAL(15,0),

	CASH_AMT DECIMAL(15,0)

);



INSERT INTO CARD_TRAN_201311 VALUES ('2356', '김아름', 'PB', 1234041, null, 1301710, null);

INSERT INTO CARD_TRAN_201311 VALUES ('4570', '이선우', 'MASS', null, null, 524560, null);

INSERT INTO CARD_TRAN_201311 VALUES ('4563', '홍지은', 'MASS', 213570, null, null, 3700000);

INSERT INTO CARD_TRAN_201311 VALUES ('3266', '윤일상', 'MASS', 89641, null, null, null);

INSERT INTO CARD_TRAN_201311 VALUES ('8904', '이동건', 'PB', 1278960, 500000, null,null );

INSERT INTO CARD_TRAN_201311 VALUES ('4678', '최혜연', 'MASS', 4567780, null,null ,null );

INSERT INTO CARD_TRAN_201311 VALUES ('1746', '임하영', 'PB', 7836100, 3213400, null,null );

INSERT INTO CARD_TRAN_201311 VALUES ('3120', '김지철', 'PB', null, null, null, null);

INSERT INTO CARD_TRAN_201311 VALUES ('8974', '강성범', 'MASS', 655456, null, null,null );

INSERT INTO CARD_TRAN_201311 VALUES ('3255', '김지연', 'MASS', 213, null, null,null );

INSERT INTO CARD_TRAN_201311 VALUES ('8977', '김지현', 'PB', 1300, null, 54000, 100000);



-- cmf - 고객번호, party_nm - 이름, seg - 고객등급, pif_amt - 일시불, inst_amt - 할부사용금액,

-- ovrs_amt - 해외사용금액, cash_amt - 현금서비스



-- coalesce함수 사용
select coalesce(inst_amt,0) from CARD_TRAN_201311;


-- 1. cmf, 이름, 총 사용금액을 총 사용금액 기준 내림차순으로 출력하시오
select cmf, party_nm, coalesce(pif_amt,0)+coalesce(inst_amt,1)+coalesce(ovrs_amt,0)+coalesce(cash_amt,0) as t_amt from CARD_TRAN_201311 order by t_amt desc;

-- 2. 신규 무이자 할부 카드의 홍보대상 고객을 추출하시오
select party_nm from CARD_TRAN_201311 where inst_amt >0;

-- 3. pb고객을 대상으로 일시불사용금액의 1%를 캐시백해주는 캠페인을 진행하면 누가 얼마의 금액을 받을 것인가
select party_nm, pif_amt*0.01 from CARD_TRAN_201311 where seg = 'pb';


-- 4. 고객 등급별 총사용 금액을 추출하고 총사용금액 기준 내림차순 정렬

select seg, sum(coalesce(pif_amt,0)+coalesce(inst_amt,0)+coalesce(ovrs_amt,0)+coalesce(cash_amt,0)) as t_amt from CARD_TRAN_201311 group by seg order by t_amt desc;

-- 5. 사용금액이 가장 많은 서비스는

select greatest(sum(pif_amt),sum(inst_amt),sum(ovrs_amt),sum(cash_amt)) from CARD_TRAN_201311;

-- 6. 사용횟수가 가장 많은 서비스는

select greatest(count(pif_amt),count(inst_amt),count(ovrs_amt),count(cash_amt)) from CARD_TRAN_201311;

-- 7. pb 고객이 가장 많이 사용한 서비스는
select greatest(sum(pif_amt),sum(inst_amt),sum(ovrs_amt),sum(cash_amt)) from CARD_TRAN_201311 where seg ='PB';


#7. pb 고객이 가장 많이 사용한 서비스는(금액)

select 

	greatest(t.p,t.i,t.o,t.c) as max_value,

    if(p- greatest(t.p,t.i,t.o,t.c)=0, 'O','X')as pif,

    if(i- greatest(t.p,t.i,t.o,t.c)=0,'O','X' )as inst,

    if(o- greatest(t.p,t.i,t.o,t.c)=0,'O','X' )as ovrs,

    if(c- greatest(t.p,t.i,t.o,t.c)=0,'O','X' )as cash

from (

	select 

		sum(coalesce(pif_amt,0))as p,

        sum(coalesce(inst_amt,0))as i,

        sum(coalesce(ovrs_amt,0))as o,

        sum(coalesce(cash_amt,0))as c 

	from CARD_TRAN_201311

    where seg = 'PB'

    ) t;


create table purchase_tran (

id int,

purchase_amt int,

purchase_cnt int,

last_amt int,

last_cnt int);



insert into purchase_tran values 

(145, 2000000, 12, 1231000, 21),

(455, 1273100, 1, 2237230, 22),

(463, 111463, 3, 214047, 1),

(324, 154769, 3, 7474663, 13),

(568, 25786652, 47, 1000047, 3),

(662, 106868, 1, 277763, 1),

(871, 9694470, 123, 798874, 2),

(460, 65650000, 1200, 6557741, 320),

(277, 5766300, 470, 57663000, 444),

(309, 5579800, 415, 2333000, 135);


select * from purchase_tran;
 

-- 1. 올해 구매금액이 1백만원 이상인 고객의 고객번호와 올해 구매금액을 추출하시오.

select id, purchase_amt from purchase_tran where purchase_amt >= 1000000;

-- 2. 작년 구매금액이 1백만원 이상 5천만원 이하인 고객의 고객 번호와 작년 구매금액을 출력하시오.

select id, last_amt from purchase_tran where last_amt between 1000000 and 50000000;


-- 3. 올해 구입건수가 작년 구입건수 보다 많은 고객들의 고객번호, 올해구입건수, 작년구입건수를 출력하고 올래구입건수를 기준으로 오름차순 정렬하시오.

select id, purchase_cnt, last_cnt from purchase_tran where purchase_cnt > last_cnt order by purchase_cnt;

-- 4. 올해 건당 구입금액을 구하고 이름을 평균구매금액으로 출력하시오.

select id, purchase_amt/purchase_cnt as '평균구매금액' from purchase_tran;

-- 5. 올해와 작년의 구매건수 당 평균 구매금액을 구하시오

select id, purchase_amt/purchase_cnt as '올해 평균구매금액', last_amt/last_cnt as '작년 평균구매금액' from purchase_tran;







create table ins_info (
id int,
cnrt_no int,
cnrt_dt date,
cnrt_cd int,
prdt_nm char(15),
cncl_dt date,
cnrt_amt int);

insert ignore into ins_info values
(224, 2533274, '2013-07-01', 1,'다이렉트자동차보험', null, 1000000),
(224, 6111075, '2012-08-07', 2, '5년만기저축보험', '2014-01-21', 300000),
(684, 4447330, '2014-06-12', 1, '다이렉트자동차보험', null, 100000),
(233, 4932004, '2011-11-23', 3, '자동차보험', null, 200000),
(762, 9633703, '2013-05-31', 2, '10년만기저축보험', '2013-11-03', 700000),
(789, 1378934,    '2013-01-12', 2, '3년만기저축보험', null, 5000001),
(183, 3701447, '2010-05-05', 1, '다이렉트자동차보험', null, 900000),
(183, 6678966, '2011-12-08', 3, '10년만기저축보험', null, 10000000),
(831, 8463112, '2013-04-16', 1, '다이렉트자동차보험', '2013-08-11', 1000000);

drop table ins_info;
select * from ins_info;

 
-- 1. 가입금액이 1백만원 이상인 고객들의 고객번호, 계약번호, 가입금액을 추출하시오.
select id, cnrt_no, cnrt_amt from ins_info where cnrt_amt >=1000000;

-- 2. 다이렉트자동차보험 가입 고객들의 고객번호, 상품명, 계약일을 계약일 오름차순으로 출력하시오
select id, prdt_nm, cnrt_dt from ins_info where prdt_nm = '다이렉트자동차보험' order by cnrt_dt;

-- 3. 상품계약일이 2013년 4월 16일 이후인 고객들의 고객번호, 계약일, 상품명을 고객번호 오름차순으로 출력하시오.
select id, cnrt_dt, prdt_nm from ins_info where cnrt_dt > '2013-04-16' order by cnrt_no;

-- 4. 보험 계약을 해지한 고객의 고객번호를 출력하시오.
select id from ins_info where cncl_dt is not null;

-- 5. 계약 종류 별 평균가입금액과 가입수를 추출하시오.
select prdt_nm,avg(cnrt_amt),sum(cnrt_cd) '가입자수' from ins_info group by prdt_nm;

-- 6. 계약이 해지된 계약의 종류와 수를 추출하시오
select prdt_nm, count(prdt_nm) from ins_info where cncl_dt is not null group by prdt_nm;

-- 7. 2013년에 가입한 계약의 수와 평균 가입금액을 추출하시오
select sum(cnrt_cd), avg(cnrt_amt) from ins_info where cnrt_dt between '2013-01-01' and '2013-12-31';

-- 8. 살아있는 계약의 고객번호, 상품명, 가입금액을 추출하시오
select id, prdt_nm, cnrt_amt from ins_info where cncl_dt is null;


select * from ins_info group by prdt_nm having prdt_nm is not null;



CREATE TABLE CASA_201312

(

	CUST_ID CHAR(13) PRIMARY KEY NOT NULL,

	CUST_SEG CHAR(10) NOT NULL,

	BALANCE_201311 DECIMAL(15,0),

	BALANCE_201312 DECIMAL(15,0)

);

INSERT INTO CASA_201312 VALUES ('54560', 'SILVER', 1000000, 2000000);

INSERT INTO CASA_201312 VALUES ('68477', 'GOLD', 112000, 3500);

INSERT INTO CASA_201312 VALUES ('96147', 'SILVER', 300000, 1000010);

INSERT INTO CASA_201312 VALUES ('32134', 'GOLD', 2354000, 3200000);

INSERT INTO CASA_201312 VALUES ('12478', 'DIAMOND', 6015000, 5800000);

INSERT INTO CASA_201312 VALUES ('54789', 'SILVER', 200000, 300000);

INSERT INTO CASA_201312 VALUES ('34181', 'GOLD', 4200000, 4100000);

INSERT INTO CASA_201312 VALUES ('23458', 'DIAMOND', 5000000, 6200000);

INSERT INTO CASA_201312 VALUES ('12344', 'SILVER', 210000, 200000);



select * from casa_201312;


-- 11월과 12월의 고객별 수신잔고 평균

select cust_id, (BALANCE_201311+BALANCE_201312)/2 from casa_201312 group by cust_id;


-- 1. 11월 캠페인결과 잔고증가율이 10%이상인 고객은 1, 아니면 0으로  캠페인 성공 여부를 새로운 칼럼으로 표시하시오
select cust_id, 
case when (BALANCE_201312-BALANCE_201311)/BALANCE_201311 > 0.1 then 1 else 0 end as '성공여부'  
from casa_201312;


-- 2. 캠페인 성공률을 계산하시오
select (select count(*) from casa_201312 where(BALANCE_201312-BALANCE_201311)/BALANCE_201311 > 0.1)/count(*) from casa_201312;

select cust_id, 
avg(case when (BALANCE_201312-BALANCE_201311)/BALANCE_201311 > 0.1 then 1 else 0 end) as '성공여부'  
from casa_201312;

-- 3. 캠페인의 결과로 증가된 수신고 순 증가분을 구하시오
select sum(BALANCE_201312)-sum(BALANCE_201311) as '증가분' from casa_201312;
-- 4. 캠페인 결과 수신고 증가율을 구하시오 
select (sum(BALANCE_201312)-sum(BALANCE_201311))/sum(BALANCE_201311)*100 from casa_201312;



create database company;

use company;



CREATE TABLE CUST_INFO

(

 RESIDENCE_ID CHAR(13) PRIMARY KEY NOT NULL,

 FIRST_NM CHAR(10) NOT NULL,

 LAST_NM CHAR(10) NOT NULL,

 ANNL_PERF DECIMAL(15,2)

);



INSERT INTO CUST_INFO VALUES ('8301111999999', 'JIHUN', 'KIM', 330.08);

INSERT INTO CUST_INFO VALUES ('7012012888888', 'JINYOUNG', 'LEE', 857.61);

INSERT INTO CUST_INFO VALUES ('6705302777666', 'MIJA', 'HAN', -76.77);

INSERT INTO CUST_INFO VALUES ('8411011555666', 'YOUNGJUN', 'HA', 468.54);

INSERT INTO CUST_INFO VALUES ('7710092666777', 'DAYOUNG', 'SUNG', -890);

INSERT INTO CUST_INFO VALUES ('7911022444555', 'HYEJIN', 'SEO', 47.44);



select * from cust_info;

-- 1.남성은 1로 여성은 2로 출력하시오
select case when substring(RESIDENCE_ID,7, 1) = 1 then '남성' else '여성' end as '성별',
substring(RESIDENCE_ID,7, 1) as '주민번호 앞자리' from cust_info;

-- 2. 이메일을 보내기 위해 성과 이름을 결합하시오
select RESIDENCE_ID, concat(last_nm,' ' ,first_nm) from cust_info;

-- 3. 고객의 수익을 소수점 첫 째자리에서 반올림하시오. */
select RESIDENCE_ID, round(ANNL_PERF,1) from cust_info;


create table clerk (
id int,
staff_nm char(5),
def_nm char(10),
gender char(2),
birth_dt date,
emp_flag char(2) );



insert into clerk values
(135, '이민성', '마케팅부', 'm', '1984-02-11', 'y'),
(142, '김선명', '영업지원부', 'm', '1971-12-08', 'y'),
(121, '신지원', '리스크부', 'f', '1978-05-28','y'),
(334, '고현정', '전략기획부', 'f', '1965-01-12', 'y'),
(144, '이기동', '마케팅분석부', 'm', '1981-03-03', 'y'),
(703, '송지희', '검사부', 'f', '1985-05-14', 'f'),
(732, '연승환', '기업영업지원부', 'm', '1990-01-26', 'y'),
(911, '이명준', '여의도지점', 'm', '1988-06-11', 'n');


select * from clerk;


-- 1. 직원의 생일을 기준으로 내림차순으로 정렬하시오
select * from clerk order by birth_dt;

-- 2. 직원의 나이를 구하시오
select staff_nm, year(now()) - year(birth_dt) as age from clerk order by age;

select staff_nm, floor(datediff(now(), birth_dt)/365) as age from clerk order by age;

-- 3. 직원의 생일에 1달을 더한 날짜를 구하시오
select staff_nm, adddate(birth_dt, 30) from clerk;

-- 4. 남성의 평균 나이와 여성의 평균 나이를 구하시오
select gender, avg(year(curdate()) - year(birth_dt)) as age from clerk group by gender;

-- 5. 평균 연령이 가장 낮은 부서는 어디인가
select def_nm, avg(year(curdate()) - year(birth_dt)) as age from clerk group by def_nm order by age limit 1;


 
create database testdb;

use testdb;

CREATE TABLE PERF

(

	CMF CHAR(4) PRIMARY KEY NOT NULL,

	PARTY_NM CHAR(10) NOT NULL,

	SEG CHAR(10) NOT NULL,

	TAMT1 DECIMAL(15,0),

	TAMT2 DECIMAL(15,0),

	TAMT3 DECIMAL(15,0)

);

INSERT INTO PERF VALUES ('2356', '김아름', 'PB', 790, 1770, 4780);

INSERT INTO PERF VALUES ('4570', '이선우', 'MASS', 90700, 5789, 87986);

INSERT INTO PERF VALUES ('4563', '홍지은', 'MASS', null, null, null);

INSERT INTO PERF VALUES ('3268', '윤일상', 'MASS', 88805, 659860, 5130);

INSERT INTO PERF VALUES ('8904', '이동건', 'PB', 9846000, 5708900, 7600000);

INSERT INTO PERF VALUES ('4678', '최혜연', 'MASS', null, 6000,null );

INSERT INTO PERF VALUES ('1748', '임하영', 'PB', 1000400, 788000, 2378696);

INSERT INTO PERF VALUES ('3120', '김지철', 'PB',null ,null , null);

INSERT INTO PERF VALUES ('8974', '강성범', 'MASS', 540, null, 7700);

INSERT INTO PERF VALUES ('3255', '김지연', 'MASS', 254860, 578321, 432004);

INSERT INTO PERF VALUES ('8977', '김지현', 'PB', 687063, 870000, 545400);

drop table PERF;

select * from PERF;


-- cmf - 고객번호, seg - 고객등급, tamt1 - 한달 전 사용금액, tamt2 - 두 달 전 사용금액, tamt3 - 세 달 전 사용금액

-- coalesce함수 사용

-- 1. 3개월 연속 1만원 미만 사용 고객 - 비활성화 고객
select * , PARTY_NM as '비활성화 고객' from PERF where tamt1 < 10000 and tamt2 < 10000 and tamt3 < 10000;

-- 2. pb이면서 비활성화 고객
select * from PERF where seg = 'pb' and tamt1 < 10000 and tamt2 < 10000 and tamt3 < 10000;

-- 3. 직전 3개월 동안 카드사용금액이 매달 줄어드는 고객
select * from PERF where ifnull(tamt3,0) > ifnull(tamt2,0) and ifnull(tamt2,0) > ifnull(tamt1,0);
select * from PERF where tamt3 > tamt2 and tamt2 > tamt1;

-- 4. 직전 3개월 카드사용금액이 7천원 이상인 고객
select * from PERF group by PARTY_NM having sum(tamt3+tamt2+tamt1)>=7000;

-- 5. 3개월 카드사용금액이 매달 줄어들면서 3개월 카드사용 금액이 7천원 이상인 고객
select * from PERF where ifnull(tamt3,0) > ifnull(tamt2,0) and ifnull(tamt2,0) > ifnull(tamt1,0) group by PARTY_NM having sum(tamt3+tamt2+tamt1)>=7000;

-- 6. 지난 3개월간 매월 총 카드사용금액 합계
select *, sum(ifnull(tamt3,0)+ifnull(tamt2,0)+ifnull(tamt1,0)) as '합계' from PERF group by PARTY_NM;

-- 7. 매달 카드 사용금액이 증가하는 고객
select * from PERF where ifnull(tamt3,0) < ifnull(tamt2,0) and ifnull(tamt2,0) < ifnull(tamt1,0);

-- 8. pb고객의 매달 카드사용금액의 합계
select *, sum(ifnull(tamt3,0)+ifnull(tamt2,0)+ifnull(tamt1,0)) as '합계' from PERF where seg = 'pb' group by PARTY_NM;

-- 9. 고객 등급별 지난 달 최고 카드사용 고객

select PARTY_NM, tamt1 from perf where tamt1 in (select max(tamt1) from perf group by seg);

select PARTY_NM, tamt1 from perf where (tamt1, seg) in (select max(tamt1),seg from perf group by seg);


