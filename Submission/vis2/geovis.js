var projection = d3.geo.mercator()
    .scale(100)
    .translate([400, 300])
    .precision(0.1);

var path = d3.geo.path()
		.projection(projection);

var countryData;
var worldMapData; //TODO Is this too large?

var active;

// (1) FUNCTION LOAD - DATA

function loadData(){
	var loadCountryDataPromise = loadCountryData();

	loadCountryDataPromise.done(function(){
		DisplayCountries();
		loadMap();
	});
}

// (2) FUNCTION LOAD COUNTRY DATA

function loadCountryData(){
	var def = $.Deferred();      //Have a callback queue -> defer operation
	d3.csv("data/highest_priority.csv", function(errorCountryData, inCountryData){
		countryData = inCountryData;
		def.resolve();
	});
	return def.promise();
}

// (3) FUNCTION SORT AND DISPLAY COUNTRIES

function DisplayCountries(){
	var select = d3.select("#countrySelect");
	select.selectAll("optgroup").remove();
	select.selectAll("option").remove();

		select.selectAll("option").data(countryData).enter()
		.append("option")
		.attr("value", function(d){console.log(d.mapID); return d.mapID;}) //calc map id
		.text(function(d){return d.Country;});
}

// (4) SELECT LOCATION SCOPE

function selectLocationScope(id){
	//in case it was a map click, select the value
	$('#countrySelect option[value=' + id + ']').prop("selected", true);

	var thisCountryData = _.find(countryData, function(d){ return d.mapID == id;});

	d3.selectAll("#mapMain > g > path").classed("selectedCountry", false);
	d3.select("#m_" + id).classed("selectedCountry", true).moveToFront();

	d3.select("h2#countryNameDisp").text(thisCountryData.Country);

  d3.select("svg#countryMain").text('');

  var bardata = [{people:parseInt(thisCountryData.Price), factor:'Price'},
                 {people:parseInt(thisCountryData.Features),factor:'Features'},
                 {people:parseInt(thisCountryData.Safety),factor:'Safety'},
                 {people:parseInt(thisCountryData.Security),factor:'Security'},
                 {people:parseInt(thisCountryData.Privacy),factor:'Privacy'},
                 {people:parseInt(thisCountryData.Reliability),factor:'Reliability'},
                 {people:parseInt(thisCountryData["User Reviews"]),factor:'User Reviews'},
                 {people:parseInt(thisCountryData["Expert Recommendation"]),factor:'Expert Recommendation'},
                 {people:parseInt(thisCountryData["Friend or Family Recommendation"]),factor:'Friend or Family Recommendation'},
                 {people:parseInt(thisCountryData.Convenience),factor:'Convenience'}];

  var svg = d3.selectAll("svg#countryMain");
  var g = svg.append("g");

  var margin = {top: 10, right: 0, bottom: 100, left: 100};

  var width = 450 - margin.left - margin.right;
	var height = 350 - margin.top - margin.bottom;

  var factors = bardata.map(function(t) {
    return t.factor;
  });

  var svg = d3.select("svg#countryMain").append("svg")
              .attr('width', width + margin.left + margin.right)
              .attr('height', height + margin.top + margin.bottom)
              .append("g")
              .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

  var factorScale = d3.scale.ordinal()
              .domain(factors)
              .rangeRoundBands([0, width/2],0.05);
              //.paddingInner(0.1);

  //var bandwidth = factorScale.bandwidth();

  var maxpeople = d3.max(bardata, function(d) { return d.people; });

  var peopleScale = d3.scale.linear()
                      .domain([0,maxpeople])
                      .range([height,0]);
                      //.nice();

  var xAxis = d3.svg.axis()
                .scale(factorScale)
                .orient("bottom");

  var yAxis = d3.svg.axis()
                .scale(peopleScale)
                .orient("left")
                .ticks(5);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")
                        .style("text-anchor", "end")
                        .attr("dx", "-.8em")
                        .attr("dy", ".15em")
                        .attr("transform", "rotate(-65)");;
      /*
      .append("text")
      .style("text-anchor", "end")
      .attr("dx", ".8em")
      .attr("dy", ".55em")
      .attr("transform", "rotate(0)")
      .text("Factors");
      */
                      

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
      .append("text")
      .attr('transform', 'rotate(-90)translate(-' + height/2 + ',0)')
      //.attr("y", 6)
      .attr("dy", "-5em")
      .style("text-anchor", "middle")
      .text("# of People Voted");

  svg.selectAll("bar")
             .data(bardata)
             .enter().append('rect')
             .style("fill", "steelblue")
             .attr('x', function(d){
               return factorScale(d.factor);
             })
             .attr('width', factorScale.rangeBand())
             .attr('y',function(d){
               return peopleScale(d.people);
             })
             .attr('height',function(d){
               return height - peopleScale(d.people);
             });

    var features = topojson.feature(worldMapData, worldMapData.objects.countries).features.filter(function(d){return d.id == id; });
   	mapClick(d3.select("#m_" + id).data()[0]);

}

// (5) LOAD THE MAP

function loadMap(){
	var svg = d3.selectAll("svg#mapMain");

	var g = svg.append("g");

	var width = svg.attr("width", 800);
	var height = svg.attr("height", 430);

	d3.json("data/worldmap.json", function(errorMap, world) {
		worldMapData = world;
		var features = topojson.feature(topojson.presimplify(world), world.objects.countries).features.filter(function(d){if (d.id != 10){return d;} });

		g.selectAll("path")
		.data(features).enter().append("path")
		.attr({
			d: path,
			id: function(d) {return "m_" + d.id;},
			stroke: '#000',
			'stroke-opacity': 0.5,
			'stroke-width': 1,
			'class': function(d){
				var thisData = _.find(countryData, function(fd){ return d.id == fd.mapID;});
				if (thisData === undefined){
            return "invalidCountry";
        }
        else {
          if (thisData['Priority'] === "Price") {
            return "price";
          }
          else if (thisData['Priority'] === "Features") {
            return "features";
          }
          else if (thisData['Priority'] === "Safety") {
            return "safety";
          }
          else if (thisData['Priority'] === "Security") {
            return "security";
          }
          else if (thisData['Priority'] === "Privacy") {
            return "privacy";
          }
          else if (thisData['Priority'] === "Reliability") {
            return "reliability";
          }
          else if (thisData['Priority'] === "User Reviews") {
            return "userrev";
          }
          else if (thisData['Priority'] === "Friend or Family Recommendation") {
            return "friend";
          }
          else if (thisData['Priority'] === "Expert Recommendation") {
            return "expert";
          }
          else if (thisData['Priority'] === "Convenience") {
            return "convenience";
          }
        }
			}
		})
		.on('click', function(d){
			if ( _.find(countryData, function(fd){ return d.id == fd.mapID;}) !== undefined){
				selectLocationScope(d.id);
			}
		}

		);//mapClick);
	});
}

// (6) MAP CLICK

function mapClick(d) {
	var mouseClick;
	var selection;
	var svg = d3.selectAll("svg#mapMain");
	var width = svg.attr("width");
	var height = svg.attr("height");

	if(this.window === undefined){//click on map
		mouseClick = d3.mouse(this);
		selection = this;
	}
	else { //click on select
		mouseClick = [width/2,height/2];
		selection = d3.select("#m_" + d.id)[0][0];
	}

	if (active === d) return resetMap();

	var g = svg.select("g");

	g.selectAll(".selectedCountry").classed("selectedCountry", false);
	d3.select(selection).classed("selectedCountry", active = d);

	var b = path.bounds(d);
	var loadCountryDataPromise = $.Deferred();

	if ((b[1][0] - b[0][0]) > 600){ //If bounding box is close to entire length of viewport, rotate the projection and redraw
		d3.transition()
        .duration(500)
        .tween("rotate", function() {
			var endNumber = mouseClick[0] < 400 ? 180 : -180;
			var r = d3.interpolateNumber(0, endNumber);
			return function(t) {
				projection.rotate([r(t), 0, 0]);
				g.selectAll("path").attr({d: path});
			};
		}).each("end", function(){
			b = path.bounds(d);
			loadCountryDataPromise.resolve();
		});
	}
	else {
		loadCountryDataPromise.resolve();
	}

	loadCountryDataPromise.done(function(){
		var scaleModifier = 0.95 / Math.max((b[1][0] - b[0][0]) / width, ((b[1][1] - b[0][1]) / height));

		g.transition().duration(500).attr("transform",
			"translate(" + projection.translate() + ")" +
			"scale(" + scaleModifier + ")" +
			"translate(" +
			-(b[1][0] + b[0][0]) / 2 +
			"," +
			((-(b[1][1] + b[0][1]) / 2 ) - ((165 / scaleModifier)/2))+
			")");

		g.selectAll("path").transition().duration(500).attr({
			"stroke-width": 1/scaleModifier
		});
	});

}

// (7) RESET MAP

function resetMap() {
	active = undefined;
	var g = d3.select("svg#mapMain > g");
	$('#countrySelect option').prop("selected", false);
	d3.select("h2#countryNameDisp").text('');
  //$("svg#countryMain").empty();
  d3.select("svg#countryMain").text('');

	if (Math.abs(projection.rotate()[0]) == 180){
		d3.transition()
        .duration(500)
        .tween("rotate", function() {
			var r = d3.interpolateNumber(projection.rotate()[0], 0);
			return function(t) {
				projection.rotate([r(t), 0, 0]);
				g.selectAll("path").attr({d: path});
			};
		});
	}

	g.selectAll("path").attr({
		"stroke-width": 1
	});

  g.selectAll(".selectedCountry").classed("selectedCountry", false);
  g.transition().duration(500).attr("transform", "");
}

d3.selection.prototype.moveToFront = function() {
  return this.each(function(){
    this.parentNode.appendChild(this);
  });
};
