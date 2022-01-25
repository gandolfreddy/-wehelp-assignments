# 實驗記錄

## 要求一

* 進入 MySQL Shell。
    ![image](https://user-images.githubusercontent.com/22278312/151010117-41917420-0689-46e4-8cc8-6deb650667b3.png)

## 要求二

* 建立 website 資料庫。
    ```sql
    create database website;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151010164-bdf56d1a-be42-4969-97f5-edd1a6a601e8.png)

* 使用 website 資料庫，並建立 member 資料表。
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
    ![image](https://user-images.githubusercontent.com/22278312/151010189-b8c53a74-4467-4cc5-9429-2deb26a721eb.png)

## 要求三

* 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
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
    ![image](https://user-images.githubusercontent.com/22278312/151011636-3a8a0d8f-607f-45d6-9607-85e417a1119f.png)
* 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
    ```sql
    select * from member;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012562-d39227df-2404-43e5-9140-5ee3b01aea18.png)
* 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
    ```sql
    select * from member order by time desc;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012678-f5693553-1519-400a-b63a-6d7ba745a669.png)
* 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。<div style="color:red">( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )</div>
    ```sql
    SELECT * from member order by time desc limit 1, 3;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012659-960ea781-39ae-4265-a156-eebdc4a1b1dd.png)
* 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
    ```sql
    select * from member where username="test";
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012755-8fe4fb93-efb2-4526-8fe0-b850bf7879a3.png)
* 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
    ```sql
    select * from member where username="test" AND password="test";
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012819-7e50fb03-d700-4a64-ade1-8418210b3fd9.png)
* 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
    ```sql
    update member set name="test2" where username="test";
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151012905-e328a465-deaf-47ac-a168-8e8e29b64e57.png)

## 要求四

* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
    ```sql
    select count(*) from member;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151013016-8c10d35d-a406-42e9-99a1-f1edf2ffc9dd.png)
* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
    ```sql
    select sum(follower_count) from member;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151013146-16eff36e-db03-461a-be95-04682349e9f4.png)
* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
    ```sql
    select avg(follower_count) from member;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151013210-996f9bfb-af13-46d0-ace7-32aa1a64aff4.png)

## 要求五

* 在資料庫中，建立新資料表，取名字為 message。資料表中必須包含以下欄位設定：
    ![image](https://user-images.githubusercontent.com/22278312/151016990-631d76d7-a58a-4c73-9d63-83f459501f9c.png)
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
    ![image](https://user-images.githubusercontent.com/22278312/151013425-ce2f2425-9005-4ea1-9356-81ace7386d03.png)
* 於 messsage 資料表插入測試用資料。
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
    ![image](https://user-images.githubusercontent.com/22278312/151013861-ce0cd784-1fec-4e03-80c9-b304c6534b94.png)
* 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
    ```sql
    select name, content from message 
    inner join member 
    on message.member_id=member.id;
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151013967-f2654b74-53bb-47b9-9f75-09ad849f19ef.png)
* 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
    ```sql
    select name, content from message 
    inner join member 
    on message.member_id=member.id AND member.username="test";
    ```
    ![image](https://user-images.githubusercontent.com/22278312/151014127-e9995151-9c38-4d08-884a-8b0e879c43ce.png)

