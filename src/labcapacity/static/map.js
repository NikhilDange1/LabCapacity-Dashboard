function drawMap() {
	var labData = fetchData();

	var labDataKeys = Object.keys(labData);
	console.log(labDataKeys)
	var scl = [[0,'rgb(5, 10, 172)'],[0.35,'rgb(40, 60, 190)'],[0.5,'rgb(70, 100, 245)'], [0.6,'rgb(90, 120, 245)'],[0.7,'rgb(106, 137, 247)'],[1,'rgb(220, 220, 220)']];

	var data = [{
		type : 'scattergeo',
		mode : 'markers+text',
		hovertemplate: '<b>Lab Name<b>: %{text}' +
                        '<br><b>Lab Intake</b>: %{marker.size}<br>' +
                        '<b>Lab Avalibility</b>: %{marker.color}' + 
                        "<extra></extra>",
		text : labData['Lab_Name'],
		lon : labData['Lab_Longitude'],
		lat : labData['Lab_Latitude'],
		marker : {
			size : labData['Lab_Intake'],
			opacity: 0.8,
			reversescale : true,
			line: {
		            width: 1,
		            color: 'rgb(102,102,102)',
		    	},
		    colorscale: scl,
		    color : labData['Lab_Avalilility'],
		    colorbar : {
		    	title : 'Lab Avalilility',
		    },
		},

	}];

	var layout = {
			width: 700,
        	height: 700,
		    title: 'Michigan Labs',
		    font: {
		        family: 'Droid Serif, serif',
		        size: 12,
		        color: '#000000'
		    },
		    titlefont: {
		        size: 16
		    },
		    geo: {
		        scope: 'north america',
		        resolution: 50,
		        lonaxis: {
		            'range': [-90, -80]
		        },
		        lataxis: {
		            'range': [40, 48]
		        },
		        showrivers: true,
		        rivercolor: '#fff',
		        showlakes: true,
		        lakecolor: '#fff',
		        showland: true,
		        landcolor: '#EAEAAE',
		        countrycolor: '#d3d3d3',
		        countrywidth: 1.5,
		        subunitcolor: '#d3d3d3'
		    }
		};


		var mapDiv = document.getElementById('map-Div');
		var hoverInfo = document.getElementById('hoverinfo');
		Plotly.newPlot(mapDiv, data, layout)

}


/*
function drawMap () {
		var data = [{
		    type: 'scattergeo',
		    mode: 'markers+text',
		    text: [
		        'Lab1', 'Lab2', 'Lab3'
		    ],
		    lon: [
		        -84.55, -83.74, -83.14
		    ],
		    lat: [
		        42.73, 42.28, 42.60
		    ],
		    marker: {
		        size: 7,
		        color: [
		            '#bebada', '#fdb462', '#fb8072'
		        ],
		        line: {
		            width: 1
		        }
		    },
		    name: '',
		    textposition: [
		        'top right', 'top left', 'top center', 'bottom right', 'top right',
		        'top left', 'bottom right', 'bottom left', 'top right', 'top right'
		    ],
		}];

		var layout = {
			width: 700,
        	height: 700,
		    title: 'Michigan Labs',
		    font: {
		        family: 'Droid Serif, serif',
		        size: 12
		    },
		    titlefont: {
		        size: 16
		    },
		    geo: {
		        scope: 'north america',
		        resolution: 50,
		        lonaxis: {
		            'range': [-90, -80]
		        },
		        lataxis: {
		            'range': [40, 48]
		        },
		        showrivers: true,
		        rivercolor: '#fff',
		        showlakes: true,
		        lakecolor: '#fff',
		        showland: true,
		        landcolor: '#EAEAAE',
		        countrycolor: '#d3d3d3',
		        countrywidth: 1.5,
		        subunitcolor: '#d3d3d3'
		    }
		};

		var mapDiv = document.getElementById('map-Div');
		Plotly.newPlot(mapDiv, data, layout)

	}


window.onload = function() {
		var data = [{
		    type: 'scattergeo',
		    mode: 'markers+text',
		    text: [
		        'Lab1', 'Lab2', 'Lab3'
		    ],
		    lon: [
		        -84.55, -83.74, -83.14
		    ],
		    lat: [
		        42.73, 42.28, 42.60
		    ],
		    marker: {
		        size: 7,
		        color: [
		            '#bebada', '#fdb462', '#fb8072'
		        ],
		        line: {
		            width: 1
		        }
		    },
		    name: '',
		    textposition: [
		        'top right', 'top left', 'top center', 'bottom right', 'top right',
		        'top left', 'bottom right', 'bottom left', 'top right', 'top right'
		    ],
		}];

		var layout = {
			width: 700,
        	height: 700,
		    title: 'Michigan Labs',
		    font: {
		        family: 'Droid Serif, serif',
		        size: 12
		    },
		    titlefont: {
		        size: 16
		    },
		    geo: {
		        scope: 'north america',
		        resolution: 50,
		        lonaxis: {
		            'range': [-90, -80]
		        },
		        lataxis: {
		            'range': [40, 48]
		        },
		        showrivers: true,
		        rivercolor: '#fff',
		        showlakes: true,
		        lakecolor: '#fff',
		        showland: true,
		        landcolor: '#EAEAAE',
		        countrycolor: '#d3d3d3',
		        countrywidth: 1.5,
		        subunitcolor: '#d3d3d3'
		    }
		};

		var mapDiv = document.getElementById('map-Div');
		Plotly.newPlot(mapDiv, data, layout)

	}
*/