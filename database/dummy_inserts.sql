INSERT INTO public.carts (id, quantity_product_id) VALUES (1, null);
INSERT INTO public.carts (id, quantity_product_id) VALUES (2, null);

INSERT INTO public.users (id, first_name, last_name, county, city, address, birth_date, email, phone_number, cnp, username, password, access_level, cart_id) VALUES (1, 'Dragos', 'Doru', '', '', null, null, 'dragosdoru@email.com', null, null, 'dragosdoru', '$2b$12$RAtcHKrILl/KvjX9G97vg.YXJRwmsFDWI88WZdiTxGAHmVfqTP6hG', null, 1);
INSERT INTO public.users (id, first_name, last_name, county, city, address, birth_date, email, phone_number, cnp, username, password, access_level, cart_id) VALUES (2, 'Valentin', 'Dragan', null, null, null, null, 'valentindragan@mail.ru', null, null, 'valentindragan', '$2b$12$RAtcHKrILl/KvjX9G97vg.YXJRwmsFDWI88WZdiTxGAHmVfqTP6hG', null, 2);
