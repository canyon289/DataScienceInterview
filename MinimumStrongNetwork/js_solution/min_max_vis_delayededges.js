/* D3 Visualization of min max network creation
and how solution is found
*/

var height = 500
var width = 500
var radius = 5
var initial_radius = 100
var angle = (2*Math.PI)/d3_data["nodes"].length

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

    var drawn_links = [];

    var svg = d3.select("body").append("svg")
           .attr("width", width)
           .attr("height", height);

    
    var force = d3.layout.force()
        .size([width,height])
        .nodes(d3_data["nodes"])
        //Initializing with no nodes here
        .links(drawn_links)
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
                .attr("cx", function(d,i) {return width/2 + Math.cos(angle*i)*initial_radius})
                .attr("cy", function(d,i) {return height/2 + Math.sin(angle*i)*initial_radius})
                ;

    force.on("tick", function() {
        link.attr("x1", function(d) { return d.source.x; })
            .attr("y1", function(d) { return d.source.y; })
            .attr("x2", function(d) { return d.target.x; })
            .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x = Math.max(radius, Math.min(width - radius, d.x)); })
        .attr("cy", function(d) { return d.y = Math.max(radius, Math.min(height - radius, d.y)); });
    
      });


    // magic is here
    run();
    function run() {
        // use the set time out to wait a second between steps
        setTimeout(function() {
            // append the next link
            var res = appendLink();
            // but only step forward if there are more links
            if (res) {
                run();
            }
        }, 1000);
    }


    function appendLink() {
        // get the next edge
        //debugger
        var newedge = d3_data.edges.shift();
        drawn_links.push(newedge);
        console.log(newedge)
        
        // update the constraints to the force diagram
        force.links(drawn_links);
        // restart the simulation
        force.start();

        // now add the links to the svg element
        link = svg.selectAll(".edge")
            .data(drawn_links);

        link.enter()
            .append("line")
            .attr("class", "edge") // make sure that the class is the same as the selector
            .style("stroke-width", 2)
        link.exit().remove();

        // return true if there are more links to append
        return d3_data.edges.length > 0;
    }
}
