CREATE TABLE property (
    property_id          integer PRIMARY KEY,
    creation_timestamp   timestamp with time zone DEFAULT now() NOT NULL,
    property_type_id     integer NOT NULL REFERENCES property_type(property_type_id),
    operation            text NOT NULL CHECK (operation IN ('Alquiler', 'Venta')),
    region_id            integer NOT NULL REFERENCES region(region_id),
    surface              double precision NOT NULL,
    price                money NOT NULL CHECK (price >= 0::money),
    selling_timestamp    timestamp with time zone CHECK(selling_timestamp >= creation_timestamp OR selling_timestamp IS NULL),
    seller_dni           integer REFERENCES seller(seller_dni)
);
