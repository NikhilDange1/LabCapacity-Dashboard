function drawMap(labData) {
	var labDataKeys = Object.keys(labData);
	console.log(labDataKeys)
	var scl = [[0,'rgb(9, 0, 0)'],[0.25,'rgb(118, 22, 22)'],[0.5,'rgb(201, 114, 114)'], [0.65,'rgb(218, 69, 69)'],[0.85,'rgb(249, 61, 61)'],[1,'rgb(225, 0, 0)']];

	var data = [{
		type : 'scattergeo',
		mode : 'markers+text',
		hovertemplate: '<b>Lab Name<b>: %{text}' +
                        '<br><b>Lab Avalibility</b>: %{marker.color}' + 
                        "<extra></extra>",
		text : labData['Lab_Name'],
		lon : labData['Lab_Longitude'],
		lat : labData['Lab_Latitude'],
		marker : {
			size : 18,
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
		Plotly.newPlot(mapDiv, data, layout, {responsive: true})

		var clickTarget = document.getElementById('clicked-mark-info');
		mapDiv.on('plotly_click', function(data){
	    var pts = '';

	    for(var i=0; i < data.points.length; i++){

			keyIndex = labData['Lab_Name'].indexOf(data.points[i].text)
	        pts = 'Lab Name: '+labData['Lab_Name'][keyIndex] +'<br>Lab Intake '+
	            labData['Lab_Intake'][keyIndex] + '\n\n';
	    }

	    if (document.getElementById('clicked-mark-info').innerHTML.toString().trim().includes(pts.toString().trim())){
	    	document.getElementById('clicked-mark-info').innerHTML = ""
	    } else {
	    	document.getElementById('clicked-mark-info').innerHTML = `<div><center><p>${pts}</p></center></div`
	    }
	    //alert('Closest point clicked:\n\n'+pts);

	});
}

function postMetrics(labData) {
	var metricsDiv = document.getElementById('metrics-Div'); 

	var maxLabAvalilility = Math.max(...labData['Lab_Avalilility']);
	keyIndex = labData['Lab_Avalilility'].indexOf(maxLabAvalilility);

	console.log(keyIndex)

	metricsDiv.innerHTML = `<center><p><b>Max Avalibility:</b> ${maxLabAvalilility} &nbsp; <b>Lab Name:</b> ${labData['Lab_Name'][keyIndex]}</p></center>`
}