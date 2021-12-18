drop table if exists phone_number_prefixes CASCADE;
drop table if exists cities CASCADE;
drop table if exists counties CASCADE;
drop table if exists consultations CASCADE;
drop table if exists subscriptions CASCADE;
drop table if exists orders CASCADE;
drop table if exists order_products CASCADE;
drop table if exists carts CASCADE;
drop table if exists users CASCADE;
drop table if exists access_levels CASCADE;
drop table if exists subscription_types CASCADE;
drop table if exists products CASCADE;
drop table if exists suppliers CASCADE;
drop table if exists categories CASCADE;
drop table if exists cart_products CASCADE;



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
    password     text,
    access_level integer
        default 1
            constraint users_access_levels_id_fk
                references access_levels,
    cart_id      integer
);



create table if not exists carts
(
    id                  serial
        constraint carts_pk
            primary key
);


alter table users
    add constraint users_carts_id_fk
        foreign key (cart_id) references carts;

create table if not exists orders
(
    id           serial
        constraint orders_pk
            primary key,
    status       text default 'Processing'::text,
    payment_type text,
    user_id      integer
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



create table cart_products
(
    product_id integer
        constraint cart_products_products_id_fk
            references products,
    quantity   integer,
    cart_id    integer
        constraint cart_products_carts_id_fk
            references carts
);



create table cart_products
(
    product_id integer
        constraint cart_products_products_id_fk
            references products,
    quantity   integer,
    cart_id    integer
        constraint cart_products_carts_id_fk
            references carts
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