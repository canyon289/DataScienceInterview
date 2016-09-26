var zoom
var svg
var initial_transform
var g

var margin = {top: 50, right: 0, bottom: 0, left: 50};
var width = 50 + margin.left + margin.right;
var height = 50 + margin.top + margin.right;

//Create Initial Zoom Behavior
zoom = d3.zoom()

//Set Initial Transform
initial_transform = d3.zoomIdentity.translate(margin.top,margin.left)

svg = d3.select("#margin_zoom").append("svg")
   .attr("width", width)
   .attr("height", height);

//Bounding Box
svg.append("rect")
   .attr("width", width)
   .attr("height", height)
   .attr("stroke", "black")
   .attr("stroke-width", "2px")
   .attr("fill", "none");
   
//Replace initial SVG zoomTransform object with our previously transformed one
svg.call(zoom.transform, initial_transform)


g = svg.append("g")
  //Rather than manually write transform string let d3 do the work for us
  .attr("transform", initial_transform.toString())

g.append("circle")
   .attr("cx", 0)
   .attr("cy", 0)
   .attr("r", 10);

//Set the zoom Behavior, use the one initialized above instead of creating a new one
svg
.call(zoom.on("zoom", function() {g.attr("transform", d3.event.transform)}))

console.log("Function Ran")
