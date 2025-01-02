const geologicalMapType = new google.maps.ImageMapType({
    getTileUrl: function(coord, zoom) {
        // Logic to fetch geological data tiles
    },
    tileSize: new google.maps.Size(256, 256),
    name: "Geological Data"
});

map.mapTypes.set('geological', geologicalMapType);
map.setMapTypeId('geological');