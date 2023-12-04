CREATE DATABASE IF NOT EXISTS air_bnb;
USE air_bnb;
DROP TABLE IF EXISTS apartment_photo;
DROP TABLE IF EXISTS apartment_has_amenities;
DROP TABLE IF EXISTS apartment_rules;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS reservation_order;
DROP TABLE IF EXISTS renter;
DROP TABLE IF EXISTS apartment;
DROP TABLE IF EXISTS lessor;
DROP TABLE IF EXISTS apartment_rating;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS amenities;

CREATE TABLE lessor
(
    id         BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email      VARCHAR(255) NOT NULL,
    phone      VARCHAR(100) NOT NULL,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL
);

CREATE INDEX idx_lessor_phone
    ON lessor (phone);

CREATE INDEX idx_lessor_email
    ON lessor (email);

CREATE TABLE address
(
    id           BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    city_name    VARCHAR(50)  NOT NULL,
    country_name VARCHAR(50)  NOT NULL,
    geo_location VARCHAR(150) NOT NULL,
    street       VARCHAR(100) NOT NULL,
    building     VARCHAR(45)  NOT NULL,
    flat         VARCHAR(45)  NULL,
    CONSTRAINT UNIQUE (city_name, country_name, geo_location, street, building, flat)
);

CREATE INDEX idx_address_country_name
    ON address (country_name);

CREATE INDEX idx_address_city_name
    ON address (city_name);

CREATE TABLE apartment_rating
(
    rating_id        BIGINT   NOT NULL AUTO_INCREMENT PRIMARY KEY,
    count_of_reviews INT      NOT NULL,
    avg_point        FLOAT    NOT NULL,
    time_created     DATETIME NOT NULL,
    time_modified    DATETIME NOT NULL
);

CREATE INDEX idx_apartment_rating_avg_point
    ON apartment_rating (avg_point);
CREATE INDEX idx_apartment_rating_time_modified
    ON apartment_rating (time_modified);

CREATE TABLE apartment
(
    id                BIGINT      NOT NULL AUTO_INCREMENT PRIMARY KEY,
    area_of_territory VARCHAR(45) NOT NULL,
    enable_to_reserve BOOLEAN     NOT NULL DEFAULT TRUE,
    cost_per_hour     VARCHAR(45) NOT NULL,
    lessor_id         BIGINT      NOT NULL,
    address_id        BIGINT      NOT NULL,
    rating_id         BIGINT      NOT NULL,
    FOREIGN KEY (rating_id) REFERENCES apartment_rating (rating_id),
    FOREIGN KEY (lessor_id) REFERENCES lessor (id) ON DELETE CASCADE,
    FOREIGN KEY (address_id) REFERENCES address (id),
    UNIQUE KEY (rating_id)
);


CREATE INDEX idx_apartment_rating
    ON apartment (rating_id);
CREATE INDEX idx_apartment_cost_per_hour
    ON apartment (cost_per_hour);


CREATE TABLE amenities
(
    amenities_id BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name         VARCHAR(150) NOT NULL,
    description  VARCHAR(500) NOT NULL,
    category     VARCHAR(150) NOT NULL
);

CREATE INDEX idx_amenities_name
    ON amenities (name);
CREATE INDEX idx_amenities_category
    ON amenities (category);

CREATE TABLE apartment_photo
(
    id           BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    photo_url    VARCHAR(700) NOT NULL,
    description  VARCHAR(500) NULL,
    apartment_id BIGINT       NOT NULL,
    FOREIGN KEY (apartment_id) REFERENCES apartment (id),
    CONSTRAINT UNIQUE (photo_url)
);

CREATE INDEX idx_apartment_photo_url
    ON apartment_photo (photo_url);
CREATE INDEX idx_apartment_photo_description
    ON apartment_photo (description);

CREATE TABLE apartment_has_amenities
(
    amenities_id BIGINT NOT NULL,
    apartment_id BIGINT NOT NULL,
    FOREIGN KEY (amenities_id) REFERENCES amenities (amenities_id),
    FOREIGN KEY (apartment_id) REFERENCES apartment (id)
);


CREATE TABLE renter
(
    id         BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
    last_name  VARCHAR(50)  NOT NULL,
    email      VARCHAR(250) NOT NULL UNIQUE,
    phone      VARCHAR(150) NOT NULL
);

CREATE INDEX idx_renter_email
    ON renter (email);
CREATE INDEX idx_renter_phone
    ON renter (phone);

CREATE TABLE reservation_order
(
    id           BIGINT   NOT NULL AUTO_INCREMENT PRIMARY KEY,
    is_confirmed BOOLEAN  NOT NULL DEFAULT (FALSE),
    start_date   DATETIME NOT NULL,
    end_date     DATETIME NOT NULL,
    apartment_id BIGINT   NOT NULL,
    renter_id    BIGINT   NOT NULL,
    FOREIGN KEY (apartment_id) REFERENCES apartment (id),
    FOREIGN KEY (renter_id) REFERENCES renter (id)
);

CREATE INDEX idx_reservation_order_dates
    ON reservation_order (start_date, end_date);
CREATE INDEX idx_reservation_order_is_confirmed
    ON reservation_order (is_confirmed);

CREATE TABLE reviews
(
    review_id            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    description          VARCHAR(500),
    point                DECIMAL(3, 2),
    renter_id            BIGINT NOT NULL,
    apartment_id         BIGINT NOT NULL,
    reservation_order_id BIGINT NOT NULL,
    FOREIGN KEY (renter_id) REFERENCES renter (id),
    FOREIGN KEY (apartment_id) REFERENCES apartment (id),
    FOREIGN KEY (reservation_order_id) REFERENCES reservation_order (id)
);

CREATE INDEX idx_reviews_apartment_renter
    ON reviews (apartment_id, renter_id);
CREATE INDEX idx_review_point
    ON reviews (point);

CREATE TABLE transaction
(
    id                   BIGINT       NOT NULL AUTO_INCREMENT PRIMARY KEY,
    transaction_type     VARCHAR(150) NOT NULL,
    amount               DECIMAL      NOT NULL,
    reservation_order_id BIGINT       NOT NULL,
    apartment_id         BIGINT       NOT NULL,
    renter_id            BIGINT       NOT NULL,
    FOREIGN KEY (reservation_order_id) REFERENCES reservation_order (id),
    FOREIGN KEY (apartment_id) REFERENCES reservation_order (apartment_id),
    FOREIGN KEY (renter_id) REFERENCES reservation_order (renter_id)
);

CREATE INDEX idx_transaction_type
    ON transaction (transaction_type);
CREATE INDEX idx_transaction_amount
    ON transaction (amount);



CREATE TABLE apartment_rules
(
    id           BIGINT PRIMARY KEY AUTO_INCREMENT,
    apartment_id BIGINT,
    rule_type    VARCHAR(150) DEFAULT ('living_rule'),
    description  VARCHAR(500),
    FOREIGN KEY (apartment_id) REFERENCES apartment (id)
);

INSERT INTO lessor (email, phone, first_name, last_name)
VALUES ('q@gmail.com', '123-456-7890', 'John', 'Doe'),
       ('lessor2@example.com', '987-654-3210', 'Jane', 'Smith'),
       ('lessor3@example.com', '555-555-5555', 'Alice', 'Johnson'),
       ('lessor4@example.com', '999-999-9999', 'Bob', 'Williams'),
       ('lessor5@example.com', '111-222-3333', 'Sarah', 'Brown'),
       ('lessor6@example.com', '777-888-9999', 'David', 'Lee'),
       ('lessor7@example.com', '333-444-5555', 'Emily', 'Davis'),
       ('lessor8@example.com', '222-333-4444', 'Robert', 'Clark'),
       ('lessor9@example.com', '444-555-6666', 'Laura', 'Martinez'),
       ('lessor10@example.com', '666-777-8888', 'Michael', 'Scott');

INSERT INTO address (city_name, country_name, geo_location, street, building, flat)
VALUES ('New York', 'USA', '12345, LatLong', '123 Main St', 'Apt 101', NULL),
       ('Los Angeles', 'USA', '54321, LatLong', '456 Elm St', 'Apt 202', 4),
       ('Chicago', 'USA', '98765, LatLong', '789 Oak St', 'Apt 303', NULL),
       ('Miami', 'USA', '65432, LatLong', '987 Palm St', 'Apt 404', 15),
       ('San Francisco', 'USA', '24680, LatLong', '123 Pine St', 'Apt 505', 145),
       ('Houston', 'USA', '13579, LatLong', '456 Maple St', 'Apt 606', NULL),
       ('Dallas', 'USA', '87654, LatLong', '789 Cedar St', 'Apt 707', 125),
       ('Atlanta', 'USA', '11111, LatLong', '987 Spruce St', 'Apt 808', NULL),
       ('Seattle', 'USA', '22222, LatLong', '123 Birch St', 'Apt 909', 126),
       ('Boston', 'USA', '33333, LatLong', '456 Fir St', 'Apt 1010', 12);

INSERT INTO apartment_rating (count_of_reviews, avg_point, time_created, time_modified)
VALUES (10, 4.5, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (15, 4.2, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (11, 3.8, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (14, 4.1, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (12, 4.3, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (13, 4.0, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (15, 4.5, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (10, 4.7, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (13, 3.9, '2023-10-28 14:00:00', '2023-12-12 14:00:00'),
       (12, 4.4, '2023-10-28 14:00:00', '2023-12-12 14:00:00');

INSERT INTO apartment (area_of_territory, enable_to_reserve, cost_per_hour, lessor_id, address_id, rating_id)
VALUES ('1000 sq ft', TRUE, '$100', 1, 1, 1),
       ('800 sq ft', TRUE, '$90', 2, 2, 2),
       ('1200 sq ft', TRUE, '$110', 3, 3, 3),
       ('900 sq ft', TRUE, '$95', 4, 4, 4),
       ('1100 sq ft', TRUE, '$105', 5, 5, 5),
       ('950 sq ft', TRUE, '$85', 6, 6, 6),
       ('1300 sq ft', TRUE, '$120', 7, 7, 7),
       ('850 sq ft', TRUE, '$80', 8, 8, 8),
       ('1250 sq ft', TRUE, '$115', 9, 9, 9),
       ('1050 sq ft', TRUE, '$100', 10, 10, 10);

INSERT INTO apartment_rules (apartment_id, rule_type, description)
VALUES (1, 'home_rules', 'No smoking allowed in the apartment.'),
       (2, 'safety_rules', 'Quiet hours after 10 PM.'),
       (3, 'home_rules', 'Pets are allowed with prior approval.'),
       (4, 'home_rules', 'Guests must check out by 11 AM.'),
       (5, 'home_rules', 'Recycling is mandatory.'),
       (6, 'home_rules', 'No loud music after 9 PM.'),
       (7, 'safety_rules', 'Parking is available for one vehicle only.'),
       (8, 'home_rules', 'Please keep the common areas clean.'),
       (9, 'safety_rules', 'Security deposit required for pets.'),
       (10, 'safety_rules', 'Use designated smoking areas.');

INSERT INTO amenities (name, description, category)
VALUES ('Swimming Pool', 'An outdoor swimming pool', 'Swimming'),
       ('Gym', 'Fully equipped fitness center', 'Sport'),
       ('Parking', 'On-site parking available', 'Car'),
       ('Wi-Fi', 'High-speed internet access', 'Network'),
       ('Laundry', 'Laundry facilities on-site', 'Washing'),
       ('Balcony', 'Private balcony or terrace', ''),
       ('Kitchen', 'Fully equipped kitchen', 'Kitchen'),
       ('Air Conditioning', 'Central air conditioning', ''),
       ('Pet-Friendly', 'Pets allowed in the apartment', 'Pets'),
       ('Security', '24/7 security services', 'Security');

INSERT INTO apartment_photo (photo_url, description, apartment_id)
VALUES ('photo1.jpg', 'Living room', 1),
       ('photo2.jpg', 'Bedroom', 1),
       ('photo3.jpg', 'Pool area', 2),
       ('photo4.jpg', 'Kitchen', 3),
       ('photo5.jpg', 'View from balcony', 3),
       ('photo6.jpg', 'Lobby', 4),
       ('photo7.jpg', 'Fitness center', 5),
       ('photo8.jpg', 'Bathroom', 5),
       ('photo9.jpg', 'Exterior', 6),
       ('photo10.jpg', 'Dining area', 6);

INSERT INTO apartment_has_amenities (amenities_id, apartment_id)
VALUES (1, 1),
       (2, 1),
       (1, 2),
       (3, 3),
       (4, 3),
       (2, 4),
       (5, 5),
       (3, 5),
       (6, 6),
       (4, 6);

INSERT INTO renter (first_name, last_name, email, phone)
VALUES ('Alice', 'Johnson', 'alice@example.com', '555-123-4567'),
       ('Bob', 'Smith', 'bob@example.com', '555-987-6543'),
       ('Emily', 'Davis', 'emily@example.com', '555-111-2222'),
       ('Daniel', 'Lee', 'daniel@example.com', '555-333-4444'),
       ('Sophia', 'Wilson', 'sophia@example.com', '555-777-8888'),
       ('Oliver', 'Brown', 'oliver@example.com', '555-666-5555'),
       ('Ava', 'Jones', 'ava@example.com', '555-222-3333'),
       ('Ethan', 'Taylor', 'ethan@example.com', '555-444-7777'),
       ('Mia', 'Hall', 'mia@example.com', '555-555-9999'),
       ('Liam', 'White', 'liam@example.com', '555-888-9999');

INSERT INTO reservation_order (is_confirmed, start_date, end_date, apartment_id, renter_id)
VALUES (TRUE, '2023-10-25 12:00:00', '2023-10-28 12:00:00', 1, 1),
       (FALSE, '2023-11-05 14:00:00', '2023-11-10 12:00:00', 2, 2),
       (TRUE, '2023-10-30 11:00:00', '2023-11-02 11:00:00', 3, 3),
       (TRUE, '2023-11-15 10:00:00', '2023-11-20 10:00:00', 4, 4),
       (FALSE, '2023-11-10 13:00:00', '2023-11-15 13:00:00', 5, 5),
       (TRUE, '2023-10-28 15:00:00', '2023-11-02 15:00:00', 6, 6),
       (FALSE, '2023-11-03 09:00:00', '2023-11-08 09:00:00', 7, 7),
       (TRUE, '2023-11-20 14:00:00', '2023-11-25 14:00:00', 8, 8),
       (TRUE, '2023-10-30 12:00:00', '2023-11-02 12:00:00', 9, 9),
       (FALSE, '2023-11-25 11:00:00', '2023-11-30 11:00:00', 10, 10);

INSERT INTO reviews (description, point, renter_id, apartment_id, reservation_order_id)
VALUES ('Great stay!', 4.770, 1, 1, 1),
       ('Nice place, but noisy neighbors.', 3.5, 2, 1, 2),
       ('Perfect location and amenities.', 4.8, 3, 3, 3),
       ('Comfortable and clean.', 4.6, 4, 4, 4),
       ('Not as expected, needs improvement.', 3.0, 5, 5, 5),
       ('Amazing view from the balcony.', 4.9, 6, 6, 6),
       ('Great gym facilities.', 4.5, 7, 7, 7),
       ('Prompt and friendly service.', 4.7, 8, 8, 8),
       ('Wonderful experience overall.', 4.8, 9, 9, 9),
       ('Highly recommended!', 4.9, 10, 10, 10);

INSERT INTO transaction (transaction_type, amount, reservation_order_id, apartment_id, renter_id)
VALUES ('Payment', 300, 1, 1, 1),
       ('Refund', 90, 2, 2, 2),
       ('Payment', 350, 3, 3, 3),
       ('Payment', 250, 4, 4, 4),
       ('Refund', 75, 5, 5, 5),
       ('Payment', 280, 6, 6, 6),
       ('Refund', 100, 7, 7, 7),
       ('Payment', 400, 8, 8, 8),
       ('Payment', 325, 9, 9, 9),
       ('Refund', 80, 10, 10, 10);


