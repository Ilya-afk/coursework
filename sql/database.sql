CREATE TABLE IF NOT EXISTS public.user_data
(
    user_data_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    surname character varying(255) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    middle_name character varying(255) COLLATE pg_catalog."default",
    phone_number character varying(12) COLLATE pg_catalog."default" NOT NULL,
    address text COLLATE pg_catalog."default" NOT NULL,
    balance integer,
    CONSTRAINT user_data_pkey PRIMARY KEY (user_data_id)
);

CREATE TABLE IF NOT EXISTS public.tariff_period
(
    tariff_period_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    payment_id bigint,
    start_date date NOT NULL,
    end_date date NOT NULL,
    CONSTRAINT tariff_period_pkey PRIMARY KEY (tariff_period_id)
);

CREATE TABLE IF NOT EXISTS public.tariff
(
    tariff_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    tariff_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    price integer NOT NULL,
    cost_per_min integer NOT NULL,
    number_of_free_min integer NOT NULL,
    tariff_period_id bigint NOT NULL,
    CONSTRAINT tariff_pkey PRIMARY KEY (tariff_id),
    CONSTRAINT tariff_period_fk FOREIGN KEY (tariff_period_id)
        REFERENCES public.tariff_period (tariff_period_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);

CREATE TABLE IF NOT EXISTS public.payment
(
    payment_id bigint NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    user_data_id bigint NOT NULL,
    payment_date date NOT NULL,
    payment_amount integer NOT NULL,
    tariff_id bigint NOT NULL,
    CONSTRAINT payment_pkey PRIMARY KEY (payment_id),
    CONSTRAINT tariff_fk FOREIGN KEY (tariff_id)
        REFERENCES public.tariff (tariff_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID,
    CONSTRAINT user_data_fk FOREIGN KEY (user_data_id)
        REFERENCES public.user_data (user_data_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID
);

/* create view */
DROP VIEW IF EXISTS info_view;
CREATE VIEW info_view AS
SELECT payment.payment_id,
       payment.payment_amount,
	   payment.payment_date, 
	   tar.price, 
	   tar_per.start_date, 
	   tar_per.end_date, 
	   us.surname, 
	   us.first_name, 
	   us.middle_name
FROM payment
		JOIN user_data us ON payment.user_data_id = us.user_data_id
		JOIN tariff tar ON payment.tariff_id = tar.tariff_id
		JOIN tariff_period tar_per ON tar.tariff_period_id = tar_per.tariff_period_id
ORDER BY payment_amount;

SELECT * FROM info_view;

/* триггер чтобы изменять view */
CREATE OR REPLACE FUNCTION info_view_updatable()
    RETURNS TRIGGER AS
$$
BEGIN
    UPDATE payment
    SET payment_amount = new.payment_amount,
        payment_date = new.payment_date
    WHERE payment_id = (SELECT payment_id FROM payment WHERE payment_id = old.payment_id);
    UPDATE tariff
    SET price = new.price
    WHERE tariff_id = (SELECT tariff_id FROM payment WHERE payment_id = old.payment_id);
	UPDATE tariff_period
	SET start_date = new.start_date, 
		end_date = new.end_date
	WHERE tariff_period_id = (SELECT tariff_period_id FROM tariff
							 WHERE tariff_id = (SELECT tariff_id FROM payment WHERE payment_id = old.payment_id));
    UPDATE user_data
    SET surname = new.surname, 
		first_name = new.first_name, 
		middle_name = new.middle_name
    WHERE user_data_id = (SELECT user_data_id FROM payment WHERE payment_id = old.payment_id);
    RETURN new;
END
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tr_info_view_updatable ON info_view;
CREATE TRIGGER tr_info_view_updatable
    INSTEAD OF UPDATE
    ON info_view
    FOR EACH ROW
EXECUTE PROCEDURE info_view_updatable();

/* изменение info_view */
CREATE OR REPLACE FUNCTION update_info_view(
       p_payment_id BIGINT,
       p_payment_amount INT DEFAULT NULL,
	   p_payment_date DATE DEFAULT NULL, 
	   p_price INT DEFAULT NULL, 
	   p_start_date DATE DEFAULT NULL, 
	   p_end_date DATE DEFAULT NULL, 
	   p_surname VARCHAR DEFAULT NULL, 
	   p_first_name VARCHAR DEFAULT NULL, 
	   p_middle_name VARCHAR DEFAULT NULL)
    RETURNS VARCHAR AS
$$
BEGIN
    if (not exists(SELECT * FROM info_view WHERE payment_id = p_payment_id)) then
        raise exception 'Строки с данным id не существует.';
    end if;
    if (p_payment_amount is not null) then
        UPDATE info_view SET payment_amount = p_payment_amount WHERE payment_id = p_payment_id;
    end if;
    if (p_payment_date is not null) then
        UPDATE info_view SET payment_date = p_payment_date WHERE payment_id = p_payment_id;
    end if;
    if (p_price is not null) then
        UPDATE info_view SET price = p_price WHERE payment_id = p_payment_id;
    end if;
    if (p_start_date is not null) then
        UPDATE info_view SET start_date = p_start_date WHERE payment_id = p_payment_id;
    end if;
    if (p_end_date is not null) then
        UPDATE info_view SET end_date = p_end_date WHERE payment_id = p_payment_id;
    end if;
    if (p_surname is not null) then
        UPDATE info_view SET surname = p_surname WHERE payment_id = p_payment_id;
    end if;
    if (p_first_name is not null) then
        UPDATE info_view SET first_name = p_first_name WHERE payment_id = p_payment_id;
    end if;
	if (p_middle_name is not null) then
        UPDATE info_view SET middle_name = p_middle_name WHERE payment_id = p_payment_id;
    end if;
    return 'View успешно обновлена.';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE cursor_update_user(
    user_id BIGINT,
    user_phone VARCHAR)
AS
$$
DECLARE
    c1 CURSOR FOR SELECT * FROM user_data;
    us_id    BIGINT;
    phone VARCHAR;
BEGIN
    OPEN c1;
    LOOP
        FETCH c1 INTO us_id, phone;
        EXIT WHEN NOT FOUND;
        IF (user_id = us_id) THEN
            UPDATE user_data SET phone_number = user_phone WHERE CURRENT OF c1;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


CREATE EXTENSION pg_trgm; -- расширение для использования индекса GIN
CREATE INDEX index_usr_data_address ON user_data USING gin (address gin_trgm_ops);


CREATE INDEX index_tariff_id ON tariff(tariff_id);

CREATE INDEX index_tariff_period_start_end_date ON tariff_period(start_date, end_date);


INSERT INTO user_data(surname, first_name, middle_name, phone_number, address, balance)
VALUES ('Vodolazky', 'Ilya', 'Viktorovich', '88005553535', 'Strominka 20', 500),
       ('Ivanov', 'Ivan', 'Ivanovich', '77777777777', 'Pushkina 228', 3000),
       ('Pupkin', 'Leha', null, '33333333333', 'Saratov', 2000),
       ('Nazarov', 'Vladimir', 'Vladimirovich', '11111111111', 'Krasnaya ploshad', 10000);
       
INSERT INTO tariff_period(payment_id, start_date, end_date)
VALUES (null, '2022-03-24', '2028-03-24'),
       (null, '1337-08-22', '2021-02-03'),
       (null, '2020-01-23', '2022-01-23'),
       (null, '2022-01-01', '2023-01-01');
       
INSERT INTO tariff(tariff_name, price, cost_per_min, number_of_free_min, tariff_period_id)
VALUES ('all inclusive', 1337, 0, 10000, 1),
       ('for students', 300, 10, 100, 4),
       ('discount', 5, 1, 1000, 2);
       
INSERT INTO payment(user_data_id, payment_date, payment_amount, tariff_id)
VALUES (1, '2022-05-10', 500, 1),
       (2, '2022-05-01', 300, 2),
       (3, '2022-01-01', 500, 3),
       (4, '2022-05-01', 1337, 1);


/* insert */
CREATE OR REPLACE FUNCTION payment_insert()
    RETURNS TRIGGER
AS
$$
BEGIN
    UPDATE user_data
    SET balance = balance - new.payment_amount
    WHERE user_data_id = new.user_data_id;
    RETURN new;
END
$$
LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tr_payment_new ON payment;
CREATE TRIGGER tr_payment_new
    AFTER INSERT
    ON payment
    FOR EACH ROW
EXECUTE PROCEDURE payment_insert();

/* delete */
CREATE OR REPLACE FUNCTION payment_delete()
    RETURNS TRIGGER
AS
$$
BEGIN
    UPDATE user_data
    SET balance = balance + old.payment_amount
    WHERE user_data_id = old.user_data_id;
    RETURN new;
END
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tr_payment_delete ON payment;
CREATE TRIGGER tr_payment_delete
    AFTER DELETE
    ON payment
    FOR EACH ROW
EXECUTE PROCEDURE payment_delete();

/* update */
CREATE OR REPLACE FUNCTION payment_update()
    RETURNS TRIGGER
AS
$$
BEGIN
    UPDATE user_data
    SET balance = balance - new.payment_amount
    WHERE user_data_id = new.user_data_id;
    UPDATE user_data
    SET balance = balance + old.payment_amount
    WHERE user_data_id = old.user_data_id;
    RETURN new;
END
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tr_payment_update ON payment;
CREATE TRIGGER tr_payment_update
    AFTER UPDATE
    ON payment
    FOR EACH ROW
EXECUTE PROCEDURE payment_update();


/* payment */
/* add*/
CREATE OR REPLACE FUNCTION add_payment(p_user_data_id BIGINT, 
				       p_payment_date DATE, 
				       p_payment_amount INT, 
				       p_tariff_id BIGINT)
RETURNS VARCHAR
AS
$$
BEGIN
	INSERT INTO payment(user_data_id, payment_date, payment_amount, tariff_id)
	VALUES (p_user_data_id, p_payment_date, p_payment_amount, p_tariff_id);
	return 'оплата добавлена';
END
$$ LANGUAGE plpgsql;

/* delete */
CREATE OR REPLACE FUNCTION delete_payment(p_payment_id BIGINT)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM payment WHERE payment_id = p_payment_id)) then
        return 'Оплаты с данным id не существует.';
    end if;
    DELETE FROM payment WHERE payment_id = p_payment_id;
    return 'Оплата успешно удалена.';
END
$$ LANGUAGE plpgsql;

/* update */
CREATE OR REPLACE FUNCTION update_payment(
    p_payment_id BIGINT,
    p_user_data_id BIGINT DEFAULT NULL,
    p_payment_date DATE DEFAULT NULL,
    p_payment_amount INT DEFAULT NULL,
	p_tariff_id BIGINT DEFAULT NULL)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM payment WHERE payment_id = p_payment_id)) then
        raise exception 'Оплаты с данным id не существует.';
    end if;
    if (p_user_data_id is not null) then
        UPDATE payment
        SET user_data_id = p_user_data_id
        WHERE payment_id = p_payment_id;
    end if;
    if (p_payment_date is not null) then
        UPDATE payment
        SET payment_date = p_payment_date
        WHERE payment_id = p_payment_id;
    end if;
    if (p_payment_amount is not null) then
        UPDATE payment
        SET payment_amount = p_payment_amount
        WHERE payment_id = p_payment_id;
    end if;
    if (p_tariff_id is not null) then
        UPDATE payment
        SET tariff_id = p_tariff_id
        WHERE payment_id = p_payment_id;
    end if;
    return 'Оплата успешно обновлена.';
END
$$ LANGUAGE plpgsql;

/* tariff */
/* add*/
CREATE OR REPLACE FUNCTION add_tariff(p_tariff_name VARCHAR, 
				       p_price INT, 
				       p_cost_per_min INT, 
					   p_number_of_free_min INT,
				       p_tariff_period_id BIGINT)
RETURNS VARCHAR
AS
$$
BEGIN
	INSERT INTO tariff(tariff_name, price, cost_per_min, number_of_free_min, tariff_period_id)
	VALUES (p_tariff_name, p_price, p_cost_per_min, p_number_of_free_min, p_tariff_period_id);
	return 'тариф добавлен';
END
$$ LANGUAGE plpgsql;

/* delete */
CREATE OR REPLACE FUNCTION delete_tariff(p_tariff_id BIGINT)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM tariff WHERE tariff_id = p_tariff_id)) then
        return 'Тарифа с данным id не существует.';
    end if;
    DELETE FROM tariff WHERE tariff_id = p_tariff_id;
    return 'Тариф успешно удален.';
END
$$ LANGUAGE plpgsql;

/* update */
CREATE OR REPLACE FUNCTION update_tariff(
    p_tariff_id BIGINT,
    p_tariff_name VARCHAR DEFAULT NULL, 
	p_price INT DEFAULT NULL, 
	p_cost_per_min INT DEFAULT NULL, 
	p_number_of_free_min INT DEFAULT NULL,
	p_tariff_period_id BIGINT DEFAULT NULL)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM tariff WHERE tariff_id = p_tariff_id)) then
        raise exception 'Тарифа с данным id не существует.';
    end if;
    if (p_tariff_name is not null) then
        UPDATE tariff
        SET tariff_name = p_tariff_name
        WHERE tariff_id = p_tariff_id;
    end if;
    if (p_price is not null) then
        UPDATE tariff
        SET price = p_price
        WHERE tariff_id = p_tariff_id;
    end if;
    if (p_cost_per_min is not null) then
        UPDATE tariff
        SET cost_per_min = p_cost_per_min
        WHERE tariff_id = p_tariff_id;
    end if;
    if (p_number_of_free_min is not null) then
        UPDATE tariff
        SET number_of_free_min = p_number_of_free_min
        WHERE tariff_id = p_tariff_id;
    end if;
	if (p_tariff_period_id is not null) then
        UPDATE tariff
        SET tariff_period_id = p_tariff_period_id
        WHERE tariff_id = p_tariff_id;
    end if;
    return 'Тариф успешно обновлен.';
END
$$ LANGUAGE plpgsql;

/* tariff_period */
/* add*/
CREATE OR REPLACE FUNCTION add_tariff_period(p_payment_id BIGINT, 
				       p_start_date DATE, 
				       p_end_date DATE)
RETURNS VARCHAR
AS
$$
BEGIN
	INSERT INTO tariff_period(payment_id, start_date, end_date)
	VALUES (p_payment_id, p_start_date, p_end_date);
	return 'период тарифа добавлен';
END
$$ LANGUAGE plpgsql;

/* delete */
CREATE OR REPLACE FUNCTION delete_tariff_period(p_tariff_period_id BIGINT)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM tariff_period WHERE tariff_period_id = p_tariff_period_id)) then
        return 'периода тарифа с данным id не существует.';
    end if;
    DELETE FROM tariff_period WHERE tariff_period_id = p_tariff_period_id;
    return 'период тарифа успешно удален.';
END
$$ LANGUAGE plpgsql;

/* update */
CREATE OR REPLACE FUNCTION update_tariff_period(
    p_tariff_period_id BIGINT,
	p_payment_id BIGINT DEFAULT NULL, 
	p_start_date DATE DEFAULT NULL, 
	p_end_date DATE DEFAULT NULL)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM tariff_period WHERE tariff_period_id = p_tariff_period_id)) then
        raise exception 'периода тарифа с данным id не существует.';
    end if;
    if (p_payment_id is not null) then
        UPDATE tariff_period
        SET payment_id = p_payment_id
        WHERE tariff_period_id = p_tariff_period_id;
    end if;
    if (p_start_date is not null) then
        UPDATE tariff_period
        SET start_date = p_start_date
        WHERE tariff_period_id = p_tariff_period_id;
    end if;
    if (p_end_date is not null) then
        UPDATE tariff_period
        SET end_date = p_end_date
        WHERE tariff_period_id = p_tariff_period_id;
    end if;
    return 'период тарифа успешно обновлен.';
END
$$ LANGUAGE plpgsql;

/* user_data */
/* add*/
CREATE OR REPLACE FUNCTION add_user(p_surname VARCHAR, 
				       p_first_name VARCHAR, 
				       p_middle_name VARCHAR,
					   p_phone_number VARCHAR,
					   p_address VARCHAR,
					   p_balance INT)
RETURNS VARCHAR
AS
$$
BEGIN
	INSERT INTO user_data(surname, first_name, middle_name, phone_number, address, balance)
	VALUES (p_surname, p_first_name, p_middle_name, p_phone_number, p_address, p_balance);
	return 'пользователь добавлен';
END
$$ LANGUAGE plpgsql;

/* delete */
CREATE OR REPLACE FUNCTION delete_user(p_user_data_id BIGINT)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM user_data WHERE user_data_id = p_user_data_id)) then
        return 'пользователя с данным id не существует.';
    end if;
    DELETE FROM user_data WHERE user_data_id = p_user_data_id;
    return 'пользователь успешно удален.';
END
$$ LANGUAGE plpgsql;

/* update */
CREATE OR REPLACE FUNCTION update_user(
	p_user_data_id BIGINT,
    p_surname VARCHAR DEFAULT NULL, 
	p_first_name VARCHAR DEFAULT NULL, 
	p_middle_name VARCHAR DEFAULT NULL,
	p_phone_number VARCHAR(12) DEFAULT NULL,
	p_address VARCHAR DEFAULT NULL,
	p_balance INT DEFAULT NULL)
    RETURNS VARCHAR
AS
$$
BEGIN
    if (not exists(SELECT * FROM user_data WHERE user_data_id = p_user_data_id)) then
        raise exception 'пользователя с данным id не существует.';
    end if;
    if (p_surname is not null) then
        UPDATE user_data
        SET surname = p_surname
        WHERE user_data_id = p_user_data_id;
    end if;
    if (p_first_name is not null) then
        UPDATE user_data
        SET first_name = p_first_name
        WHERE user_data_id = p_user_data_id;
    end if;
    if (p_middle_name is not null) then
        UPDATE user_data
        SET middle_name = p_middle_name
        WHERE user_data_id = p_user_data_id;
    end if;
	if (p_phone_number is not null) then
        UPDATE user_data
        SET phone_number = p_phone_number
        WHERE user_data_id = p_user_data_id;
    end if;
	if (p_address is not null) then
        UPDATE user_data
        SET address = p_address
        WHERE user_data_id = p_user_data_id;
    end if;
	if (p_balance is not null) then
        UPDATE user_data
        SET balance = p_balance
        WHERE user_data_id = p_user_data_id;
    end if;
    return 'пользователь успешно обновлен.';
END
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE change_tariff(
    new_tariff_id BIGINT,
    p_payment_id BIGINT)
AS
$$
declare
    old_tariff_id int;
BEGIN
    old_tariff_id = (SELECT tariff_id FROM payment WHERE payment_id = p_payment_id);
    UPDATE payment
    SET tariff_id = new_tariff_id,
        payment_amount = (SELECT price FROM tariff WHERE tariff_id = new_tariff_id)
    WHERE payment_id = p_payment_id;
    if ((SELECT balance FROM user_data WHERE (user_data_id = (SELECT user_data_id FROM payment WHERE payment_id = p_payment_id))) < 0)
    then
        rollback;
        raise exception 'Недостаточно денег на балансе';
    end if;
    commit;
END
$$ LANGUAGE plpgsql;


/* скалярная функция */
CREATE OR REPLACE FUNCTION get_payment_sum() RETURNS INT AS
$$
DECLARE
	payment_sum int;
BEGIN
    payment_sum := (SELECT SUM(payment_amount) FROM payment);
	RETURN payment_sum;
END
$$ LANGUAGE plpgsql;

/* векторная функция */
CREATE OR REPLACE FUNCTION get_payment() RETURNS SETOF int AS
$$
BEGIN
    RETURN QUERY SELECT payment_amount FROM payment;
END
$$ LANGUAGE plpgsql;


CREATE ROLE "User" WITH PASSWORD 'user' LOGIN;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "User";
GRANT SELECT ON info_view TO "User";
CREATE ROLE "Admin" WITH PASSWORD 'admin' SUPERUSER LOGIN;


