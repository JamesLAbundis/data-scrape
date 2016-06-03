function drawDonuts(){
	
		var data=[1200, 4050];
		var rIn=125
		var rOut= 175;

		var color= d3.scale.ordinal()
			.range(["blue", "yellow"]);


		var canvas=d3.selectAll(".circontainer").append("svg")
				.attr("width",600)
				.attr("height",600);

		var group = canvas.append("g")
		.attr("transform","translate(300,300)");
			
		var arc= d3.svg.arc()
				.innerRadius(rIn)
				.outerRadius(rOut);
				

		var pie= d3.layout.pie()
			.value(function (d) {return d;});

		//add a graphic title to the center of pie with
		//description
		group.append("text")
			.attr("font-size","2.5em")
			.attr("text-anchor", "middle")
			.style("font-weight","bold")
			.text("Strength");

		group.append("text")
			.attr("font-size","1.75em")
			.attr("text-anchor", "middle")
			.attr("transform","translate(0,35)")
			.style("font-style","italic")
			.text("(soldiers)");
			//makes the key in center of circle

		group.append("rect")
		    .attr("x", 5)
		    .attr("y", 70)
		    .attr("width", 50)
	        .attr("height", 10)
		    .attr("fill", "blue");

		group.append("rect")
		    .attr("x", 5)
		    .attr("y", 90)
		    .attr("width", 50)
		    .attr("height", 10)
	        .attr("fill", "yellow");

		group.append("text")
		    .attr("font-size","1em")
			.attr("text-anchor", "middle")
			.attr("transform","translate(-15,80)")
			.style("font-weight","bold")
			.text("UAF");

		group.append("text")
			.attr("font-size","1em")
			.attr("text-anchor", "middle")
			.attr("transform","translate(-15,100)")
			.style("font-weight","bold")
			.text("DPR");

		var arcs= group.selectAll(".arc")
			.data(pie(data))
			.enter()
			.append("g")
			.attr("class", "arc");

		arcs.append("path")
			.attr("d", arc)
			.attr("fill", function(d) { return color(d.data); });

		arcs.append("text")
			.attr("transform", function (d) { return "translate("+ arc.centroid(d)+ ")";})
			.attr("text-anchor", "middle")
			.attr("font-size","1.5em")
			.style("font-weight","bold")
			//.style("fill","black")
			.text(function(d) {return d.data;});
		


		
}