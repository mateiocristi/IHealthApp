INSERT INTO public.categories (id, name, description) VALUES (default, 'Raceala si gripa', null);
INSERT INTO public.categories (id, name, description) VALUES (default, 'ingrijire personala', null);

INSERT INTO public.suppliers (id, name, description, rating, phone_number, email, website) VALUES (default, 'Plafar', null, 0, null, null, null);
INSERT INTO public.suppliers (id, name, description, rating, phone_number, email, website) VALUES (default, 'Sun-Medical', null, 0, null, null, null);

INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Aspirator nazal', null, 0, null, null, 0, null, null);
INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Termometru', null, 0, null, null, 0, null, null);

INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Pastila', null, 0, null, null, 0, null, null);
INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Aerosoli', null, 0, null, null, 0, null, null);

INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Ceva', null, 0, null, null, 0, null, null);
INSERT INTO public.products (id, name, description, stock, default_price, actual_price, rating, category_id, supplier_id) VALUES (default, 'Altceva', null, 0, null, null, 0, null, null);