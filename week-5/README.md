# 實驗記錄

## 要求一

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled.png)

## 要求二

```sql
create database website;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%201.png)

```sql
use website;
```

```sql
create table member (
    id bigint auto_increment, 
    name varchar(255) not null, 
    username varchar(255) not null, 
    password varchar(255) not null, 
    follower_count int not null default 0, 
    time datetime not null default (now()), 
    primary key (id)
);
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%202.png)

## 要求三

```sql
insert into member (name, username, password, follower_count) 
            values ("Freddy", "test", "test", 396);
insert into member (name, username, password, follower_count) 
            values ("Abby", "abby0307", "0307abby", 23);
insert into member (name, username, password, follower_count) 
            values ("Amee", "amee1216", "1216amee", 45);
insert into member (name, username, password, follower_count) 
            values ("Shi Chiang", "shiri", "qwert", 214);
insert into member (name, username, password, follower_count) 
            values ("gandolfreddy", "thering", "ofthelord", 34);
insert into member (name, username, password, follower_count) 
            values ("Sirius", "sirius", "black", 102);
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%203.png)

```sql
select * from member;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%204.png)

```sql
select * from member order by time desc;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%205.png)

```sql
SELECT * from member order by time desc limit 1, 3;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%206.png)

```sql
select * from member where username="test";
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%207.png)

```sql
select * from member where username="test" AND password="test";
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%208.png)

```sql
update member set name="test2" where username="test";
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%209.png)

## 要求四

```sql
select count(*) from member;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2010.png)

```sql
select sum(follower_count) from member;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2011.png)

```sql
select avg(follower_count) from member;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2012.png)

## 要求五

```sql
create table message (
    id bigint auto_increment, 
    member_id bigint not null, 
    content varchar(255) not null, 
    time datetime not null default (now()), 
    primary key (id),
    foreign key (member_id) references member (id)
);
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2013.png)

```sql
insert into message (member_id, content) 
            values (3, "Heyyyyyyy~");
insert into message (member_id, content) 
            values (1, "this is a pen.");
insert into message (member_id, content) 
            values (4, "Hello MySQL");
insert into message (member_id, content) 
            values (6, "Guess who's back, back again.");
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2014.png)

```sql
select name, content from message 
inner join member 
on message.member_id=member.id;
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2015.png)

```sql
select name, content from message 
inner join member 
on message.member_id=member.id AND member.username="test";
```

![Untitled](%E5%AF%A6%E9%A9%97%E8%A8%98%E9%8C%84%2083ca0962d88e4f60b5fe456dc149de8c/Untitled%2016.png)