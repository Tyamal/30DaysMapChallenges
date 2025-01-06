SELECT 
    site_id, 
    site_name, 
    latitude, 
    longitude, 
    mineral_type 
FROM 
    mining_sites 
WHERE 
    active = 1;  -- Assuming you only want active mining sites