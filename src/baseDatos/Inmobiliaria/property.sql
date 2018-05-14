
CREATE OR REPLACE FUNCTION property (
  IN p_property_id                integer,
  IN p_creation_timestamp         timestamp,
  IN p_property_type_id           integer,
  IN p_operation                  text,
  IN p_region_id                  integer,
  IN p_surface                    double precision,
  IN p_price                      money,
  IN p_selling_timestamp          timestamp,
  IN p_seller_dni                 integer
) RETURNS property AS
$$
  INSERT INTO property (property_id, creation_timestamp, property_type_id,
  operation, region_id. surface, price, selling_timestamp, seller_dni)
    VALUES (p_property_id, p_creation_timestamp, p_property_type_id,
    p_operation, p_region_id, p_surface, p_price, p_selling_timestamp,
    p_seller_dni);
