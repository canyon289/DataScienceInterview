/* D3 Visualization of min max network creation
and how solution is found
*/

var height = 500
var width = 500
var radius = 5
/*
var d3_data = {
        nodes:[
                {0:'0'},
                {1:'1'},
                {2:'2'}
                ],
        edges:[
                {'source':0,'target':1},
                {'source':1,'target':2},
                {'source':2,'target':0}
                ]
            };
*/


//Click Header to start animation
d3.select("body").select("#start_animation")
        .on("click", function() {draw_network()})
        
draw_network()
function draw_network(){ 

    var svg = d3.select("body").append("svg")
           .attr("width", width)
           .attr("height", height);

    var force = d3.layout.force()
        .size([width,height])
        .nodes(d3_data["nodes"])
        //Initializing with no nodes here
        .links([])
        .linkDistance([100])
        .charge([-600])
        .start();
    
    var link = svg.selectAll(".link")
            .data(d3_data["edges"])
            .enter()
            .append("line")
            .attr("class", "edge")
            .style("stroke-width", 2)
                
    var node = svg.selectAll(".node")
                .data(d3_data["nodes"])
                .enter()
                .append("circle")
                .attr("class", "node")
                .attr("id", function(d) {return(d["number"])})
                .attr("r", radius)
                //.call(force.drag)
    


    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });
      });
}
