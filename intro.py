'''Введение в PostgreSQL. Создание БД, таблиц'''

'''PostgreSQL - Система упраления базами данных. Набор программ, позволяющий организовывать, контролировать и администрировать базы данных'''

# MySQL, Firestore, MongoDB, SQLite ...

'''Почему PostgreSQL'''
# 1. Унего больше функция
# 2. объектно-реляционная система
# 3. Расширяемая система
# 4. Поддержка ACID
# A(atomacity) - атомарность 
# C(consistency) - согласованость
# I(isolation) - изолированность
# D(durability) - стойкость


# Postgres - сама база данных(БД)

# БД - это организованная структура предназначеная для хранения, изменения и обработки взаимосвязанной информации

# SQL(Structure Query Language) -> язык запросов в БД (для управления данными)

# клиент -> сайт -> принятие данных -> запись в БД


# sudo -i -u postgres -> вход в postgres аккаунт
# exit -> для выхода
# sudo -u postgres psql -> командная строка
# \q -> выход

# psql 

# \du -> просмотр списка юзеров
# \l -> просмотр списка БД


# CREATE USER <user_name> WITH PASSWORD 'password';
# ALTER ROLE <user> WITH SUPERUSER CREATEROLE CREATEDB;  даем привилегии (права)
# CREATE DATABASE <db_name>; содание БД
# DROP ROLE <user>; -> удаление юзера
# DROP DATABASE <db_name>; -> удаление БД


'''Типы полей Postgres'''
# 1. Numeric Type (Числовые типы):
    # a. smallint(2 bytes) -32768 до 32768 # если введем больше будет ошибка
    # b. integer (4 bytes) -2147483648 до 2147483648 
    # c. bigint (8 bytes) -9223372036854775808 до 9223372036854775808 
    # d. serial(4 bytes) -> целые числа с автоинкрементом 1 до 2147483648
    # e. smallserial (2 bytes) 1 до 32768
    # f. bigserial (8 bytes) 1 до 9223372036854775808
# ...

# 2. Character Types (Стороковые/Текстовые типы)
    # a. varchar(кол-во символов) -> если укажем 50, но заполним 10, то остальные будут свободны (будет занимать меньше памяти) VARCHAR(10) -> test -> 'test'
    # Макс. кол-во символов 255

    # b. char(кол-во символов) -> строка с постоянной длиной. CHAR(10) -> test -> 'test      '. ошибка, если больше

    # c. text() -> Неограниченное кол-во символов

# 3. Boolean Type:
    # 1 byte  -> TRUE/FALSE

# 4. date -> календарная дата(год.месяц.день)
# 5. location -> координатная точка -> (254, -15) (x, y)
# 6. Enumerated Types: ('a', 'b', 'c', 'd')
    # CREATE TYPE <любое название> AS ENUM ('happy', 'sad', 'bad')


'''Ограничения (constraint)'''
# 1. UNIQUE -> все значения в столбце должны быть уникальными
# 2. DEFAULT -> у столбца будет значение по умолчанию
# 3. NULL | NOT NULL -> определяет, будет ли столбец обязателен к заполнению
# 4. CHECK ->  используется для проверки значений столбца
# 5. PRIMARY KEY -> определяет, будет ли столбец идентификатором . Первичный ключ
# 6. FOREIGN KEY ->   задается для ссылки на другую таблицу. Внешний ключ

'''Заполнение таблиц'''
# '''запись данных в таблицу (заполнение всех полей)'''
# insert into <table_name> values ('data');
# insert into <table_name> (columns_name) values ('data');
# insert into <table_name> (columns_name) values ('data'), ('data'), ('data');


'''Вывод данных из таблицы'''
# select * from <table_name>; # -- получение всех записей с таблицы (всех полей) 
# select <column_name> from <table_name>; 

'''Условия'''
# ORDER BY: Позволяет нам сортировать данные по убыванию или возрастанию. ASC(по возрастанию) и DESC(по убыванию) используються для определения сортировки
# SELECT * FROM <table_name> ORDER BY <column_name>; -- сортировка по определенному полю (по возрастанию ASC)
# SELECT * FROM  <table_name>  ORDER BY <column_name> DESC; -- сортировка по определенному полю (по убыванию DESC)


# LIMIT: Позволяет нам вернуть данные в ограниченном количестве
# SELECT * FROM  <table_name>  LIMIT 5; -- выводит первые 5 записей
# SELECT * FROM  <table_name>  OFFSET 5; -- пропускает первые 5 записей
# SELECT * FROM  <table_name>  LIMIT 4 OFFSET 3;
# -- пропускает первые 3 записей
# -- выбирает следующие 4 записей

# DISTINCT: Позволяет нам убирать дубликаты и возвращает только уникальные значения
# SELECT DISTINCT <column_name> FROM  <table_name> ;

# =========================================== операции сравнения
# >, <, >=, <=, =, != или <>
# ======================== where - для фильтрации текста
# WHERE: Используется для фильтрации по полям. Будут выводиться только те условия которые верны WHERE
# SELECT <column_name> FROM  <table_name>  WHERE <condition>; -- получение всех записей соответствующих этому условию

# Логические операции: and, or, not
# select * from product where not price > 15;
# проверка на вхождение (in)
# select * from product where name in ('world', 'name'); # IN
# SELECT * FROM product WHERE price >= 200 AND price <= 5000;
# BETWEEN - проверка на нахождение в диапазоне
# SELECT * FROM product WHERE price BETWEEN 200 AND 1500;



# LIKE: Выводит результать который соостветсвует введеному шаблону. Чувствителен к регистру
# ILKIE: Тоже самое только не зависит от регистра
# where name like 'A%' - имена нач на A
# like %@gmail.com
# %a% - что бы была а в слове
# like 'Ki_%' после только один символ
# like '__Ki%' перед 2 символа
# ilike не чувст к регистру

# SELECT * FROM  <table_name>  WHERE <column_name> like '%world%';

# SELECT * FROM <table_name>  WHERE <column_name> ilike '%world%'; --не чувтвителен к регистру


'''Удаление записей из таблицы'''
# DELETE FROM  <table_name> ; --удаление всех записей из таблицы
'''Условия'''
# delete from <table_name>  where <condition>; -- удаление всех записей соответствующих этому условию


'''Обновление записей в таблице'''
# UPDATE  <table_name>  SET <column_name> = new_val; -- обновление всех записей в таблице
'''Условия'''
# UPDATE  <table_name>  SET <column_name> = new_val WHERE <condition>; -- обновление всех записей соответствующих этому условию



'''================================='''
# GROUP BY - это ключевое слово которое позволяет выводить значение из колонок объеденённые в группы.
# GROUP BY: разделяет строки, возвращаемы оператором SELECT на группы. И теперь для каждой группы можно применить фукнцию

# Синтаксис: SELECT <column_name>, COUNT(*) from  <table_name> GROUP BY <column_name>;

# HAVING: Работает так же как и WHERE только он используется в GROUP BY
# HAVING
# HAVING - ключевое слово которое ВСЕГДА
# используется с GROUP BY конструкцией.
# HAVING VS WHERE
# HAVING как и WHERE отвечает за создание
# какого-либо условия для вывода на экран
# только определённых строк кода. Однако если WHERE отвечает за вывод строк по условию,
# то HAVING отвечает за вывод целых груп/
# категорий значений имеющих общие признаки.
# ПРИМЕР:
# SELECT *
# FROM clients
# GROUP BY profession
# HAVING salary > 2500;

# select * from post group by id having id > 1;






''' ======================== ALTER TABLE #редактирование таблицы (Служит для изменения макета таблицы после того, как она была создана с помощью инструкции CREATE TABLE.) ========================'''

# изменение и удаление таблиц

#переименование таблицы
# ALTER TABLE  <table_name>  RENAME TO  <new_table_name> ;

#добавление нового столбца
# ALTER TABLE  <table_name>  ADD COLUMN <column_name> <type> <constraint>;

#удаление столбца
# ALTER TABLE  <table_name>  DROP COLUMN <column_name>;

#переименование столбца
# ALTER TABLE  <table_name>  RENAME COLUMN <column_name> TO <new_column_name>;

#изменение типа столбца
# ALTER TABLE  <table_name>  ALTER COLUMN <column_name> TYPE <new_type>;


# ALTER TABLE  <table_name>  ALTER COLUMN <column_name> SET/DROP NOT NULL;









'''связи'''

# pk fk
# primary key (pk) - первичный ключ, ограничение, которое накладывается на поле, которое будет использованно в связях (создает btree для быстрого поиска) foreign key (fk) - внешний ключ, ограничение, которое накладывается на поле, которое ссылается на pk в другой таблице

# CREATE TABLE author (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );

# CREATE TABLE book (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(100),
#     published YEAR,
#     author_id INT,

#     CONSTRAINT fk_book_author FOREIGN KEY (author_id)
#     REFERENCES author (id)
# );

# Виды связей

# One to one - один к одному
# один человек - один ID
# один автор - одна автобиография

# One to many - один ко многим
# один блоггер - много постов
# один куратор - много студентов
# один продукт - много комментариев

# Many to many - многие ко мгногим
# один ментор - много студентов. один студент - много менторов
# один разработчик - много проектов. один проект - много разработчиков
# один банк - много клиентов. один клиент - много банков

# FOREIGN KEY -> внешний ключ(с помощью него создаются связи)

# PRIMARY KEY -> Первичный ключ(по нему создается связь)

# Виды связей (практика)
# One to one
# CREATE TABLE author (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     age INT
# );

# CREATE TABLE autobiography (
#     id SERIAL PRIMARY KEY,
#     body TEXT,
#     created_at DATE,
#     author_id INT UNIQUE, -- unique мы ставим, чтобы сделать one 2 one

#     CONSTRAINT fk_author_bio 
#     FOREIGN KEY (author_id) REFERENCES author (id)
# );
# One to Many
# CREATE TABLE curator (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50)
# );

# CREATE TABLE student (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     email VARCHAR(100),
#     language VARCHAR(2),
#     curator_id INT,

#     CONSTRAINT fk_student_curator
#     FOREIGN KEY (curator_id) REFERENCES curator (id)
# );
# Many to Many
# CREATE TABLE developer (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50),
#     experience INT
# );

# CREATE TABLE project (
#     id SERIAL PRIMARY KEY,
#     title VARCHAR(50),
#     tz TEXT,
#     start DATE,
#     finish DATE
# );

# CREATE TABLE dev_proj (
#     dev_id INT,
#     proj_id INT,

#     CONSTRAINT fk_dev FOREIGN KEY (dev_id) REFERENCES developer (id),
#     CONSTRAINT fk_proj FOREIGN KEY (proj_id) REFERENCES project (id)
# );

'''join'''
# Соединённая таблица ­­­­­­— это таблица, полученная из двух других таблиц в соответствии с правилами соединения конкретного типа. Общий синтаксис описания соединённой таблицы:

# JOIN - инструкция, которая позволяет в запросах SELECT брать данные из нескольких таблиц

# INNER JOIN (JOIN) - достаются только те записи, у которых есть связь

# FULL JOIN - достаются все записи с обеих таблиц

# LEFT JOIN - достает все записи с левой таблицы, и с правой таблицы у которых есть связь с левой таблицей

# RIGHT JOIN - достает все записи с правой таблицы, и с левой таблицы у которых есть связь с правой таблицей

# где 'левая' таблица - та, которая написана до join а 'правая' таблица - та, которая написана после join



'''индекс'''

#         0
#    0         0
# 0     0   0     0

# типы индексов в postgres
# 1) B-tree
# 2) хеш
# 3) Gist
# 4) sp-gist
# 5) gin
# 6) brin

# по умолчанию создается один
# b-tree 


