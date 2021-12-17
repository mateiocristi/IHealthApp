create table if not exists categories
(
    id          serial
        constraint categories_pk
            primary key,
    name        text,
    description text
);


create table if not exists suppliers
(
    id           serial
        constraint suppliers_pk
            primary key,
    name         text,
    description  text,
    rating       integer default 0,
    phone_number integer,
    email        text,
    website      text
);


create table if not exists products
(
    id            serial
        constraint products_pk
            primary key,
    name          text,
    description   text,
    stock         integer default 0,
    default_price integer,
    actual_price  integer,
    rating        integer default 0,
    category_id   integer
        constraint products_categories_id_fk
            references categories,
    supplier_id   integer
        constraint products_suppliers_id_fk
            references suppliers
);


create table if not exists subscription_types
(
    id          serial
        constraint subscription_types_pk
            primary key,
    name        text,
    description text,
    default_tax integer,
    actual_tax  integer
);


create table if not exists access_levels
(
    id   serial
        constraint access_levels_pk
            primary key,
    name text
);

create table if not exists users
(
    id           serial
        constraint users_pk
            primary key,
    first_name   text,
    last_name    text,
    county       text,
    city         text,
    address      text,
    birth_date   date,
    email        text,
    phone_number integer,
    cnp          integer,
    username     text,
    password     text,
    access_level integer
        constraint users_access_levels_id_fk
            references access_levels,
    cart_id      integer
);



create table if not exists carts
(
    id                  serial
        constraint carts_pk
            primary key,
    quantity_product_id text,
    user_id             integer
        constraint carts_users_id_fk
            references users
);


alter table users
    add constraint users_carts_id_fk
        foreign key (cart_id) references carts;

create table if not exists orders
(
    id                  serial
        constraint orders_pk
            primary key,
    quantity_product_id text,
    status              text,
    payment_type        text,
    user_id             integer
        constraint orders_users_id_fk
            references users
);

create table if not exists subscriptions
(
    id                serial
        constraint subscriptions_pk
            primary key,
    start_date        date default CURRENT_DATE,
    expiration_date   date,
    user_id           integer
        constraint subscriptions_users_id_fk
            references users,
    subscription_type integer
        constraint subscriptions_subscription_types_id_fk
            references subscription_types
);

create table if not exists consultations
(
    id                         serial
        constraint consultations_pk
            primary key,
    name                       text,
    description                text,
    booking_date               timestamp default CURRENT_TIMESTAMP,
    consultation_date_and_hour timestamp,
    user_id                    integer
        constraint consultations_users_id_fk
            references users
);


create table if not exists support_session
(
    id             serial
        constraint support_session_pk
            primary key,
    user_id        integer
        constraint support_session_users_id_fk
            references users,
    suport_user_id integer
        constraint support_session_users_id_fk_2
            references users
);



create table if not exists messages
(
    id      serial
        constraint messages_pk
            primary key,
    user_id integer
        constraint messages_users_id_fk
            references users,
    message text
);



create table if not exists support_sessions_messages
(
    session_id integer
        constraint "support_sessions_messages:_support_session_id_fk"
            references support_session,
    message_id integer
        constraint "support_sessions_messages:_messages_id_fk"
            references messages
);



create table if not exists counties
(
    id   serial
        constraint counties_pk
            primary key,
    name text
);



create table if not exists cities
(
    id        serial
        constraint cities_pk
            primary key,
    name      text,
    county_id integer
        constraint cities_counties_id_fk
            references counties
);


create table if not exists phone_number_prefixes
(
    id      serial
        constraint phone_number_prefixes_pk
            primary key,
    country text,
    prefix  text
);



--- INSERTS FOR COUNTIES

INSERT INTO counties(name) VALUES ('Alba');
INSERT INTO counties(name) VALUES ('Arad');
INSERT INTO counties(name) VALUES ('Argeș');
INSERT INTO counties(name) VALUES ('Bacău');
INSERT INTO counties(name) VALUES ('Bihor');
INSERT INTO counties(name) VALUES ('Bistrița-Năsăud');
INSERT INTO counties(name) VALUES ('Botoșani');
INSERT INTO counties(name) VALUES ('Brașov');
INSERT INTO counties(name) VALUES ('Brăila');
INSERT INTO counties(name) VALUES ('București');
INSERT INTO counties(name) VALUES ('Buzău');
INSERT INTO counties(name) VALUES ('Caraș-Severin');
INSERT INTO counties(name) VALUES ('Călărași');
INSERT INTO counties(name) VALUES ('Cluj');
INSERT INTO counties(name) VALUES ('Constanța');
INSERT INTO counties(name) VALUES ('Covasna');
INSERT INTO counties(name) VALUES ('Dâmbovița');
INSERT INTO counties(name) VALUES ('Dolj');
INSERT INTO counties(name) VALUES ('Galați');
INSERT INTO counties(name) VALUES ('Giurgiu');
INSERT INTO counties(name) VALUES ('Gorj');
INSERT INTO counties(name) VALUES ('Harghita');
INSERT INTO counties(name) VALUES ('Hunedoara');
INSERT INTO counties(name) VALUES ('Ialomița');
INSERT INTO counties(name) VALUES ('Iași');
INSERT INTO counties(name) VALUES ('Ilfov');
INSERT INTO counties(name) VALUES ('Maramureș');
INSERT INTO counties(name) VALUES ('Mehedinți');
INSERT INTO counties(name) VALUES ('Mureș');
INSERT INTO counties(name) VALUES ('Neamț');
INSERT INTO counties(name) VALUES ('Olt');
INSERT INTO counties(name) VALUES ('Prahova');
INSERT INTO counties(name) VALUES ('Satu Mare');
INSERT INTO counties(name) VALUES ('Sălaj');
INSERT INTO counties(name) VALUES ('Sibiu');
INSERT INTO counties(name) VALUES ('Suceava');
INSERT INTO counties(name) VALUES ('Teleorman');
INSERT INTO counties(name) VALUES ('Timiș');
INSERT INTO counties(name) VALUES ('Tulcea');
INSERT INTO counties(name) VALUES ('Vaslui');
INSERT INTO counties(name) VALUES ('Vâlcea');
INSERT INTO counties(name) VALUES ('Vrancea');
