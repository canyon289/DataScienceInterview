var zoom
var svg
var initial_transform

zoom = d3.zoom()
initial_transform = d3.zoomIdentity.translate(50,50)

svg = d3.select("body").append("svg")
   
//Adjust SVG Transform
svg.call(zoom.transform, initial_transform)


console.log(d3.zoomTransform(svg))
console.log(d3.zoomTransform(svg.node()))
