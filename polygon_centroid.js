var turf = require('@turf/turf');
var fs = require('fs');
var features = fs.readFileSync('./hanamigawa.geojson');
features = JSON.parse(features)
arr = []
features.features.map((f) => {
  center = turf.centroid(f, {"key": f.properties["KEY_CODE"]})
  arr.push(center)
})
var collection = turf.featureCollection(arr)
fs.writeFileSync('./hanamigawa_points.geojson', JSON.stringify(collection));
