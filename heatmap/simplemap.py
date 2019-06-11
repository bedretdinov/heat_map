


def showMap(coordinates,zoom=5, center='55.748228, 37.660954', radius=15, opacities=0.6):
	from IPython.display import display, HTML 
	import json
	import datetime
	ts_id = str(datetime.datetime.now().timestamp()).replace('.','')

	js = '''
	<script src="http://api-maps.yandex.ru/2.1/?lang=ru_RU" type="text/javascript"></script> 
	<script src="http://yandex.github.io/mapsapi-heatmap/Heatmap.min.js" type="text/javascript"></script> 
	<div id="mapTypeId_'''+ts_id+'''" style='width: 100%; height: 699px; background: gainsboro;'></div>
	<script>
	  
		ymaps.ready(function () {
		    var map = new ymaps.Map('mapTypeId_'''+ts_id+'''', {
		            center: ['''+str(center)+'''], 
		            controls: ['zoomControl',   'fullscreenControl'],
		            zoom: '''+str(zoom)+''', type: 'yandex#satellite', 
		        }),
	 
		        gradients = [{
		            0.1: 'rgba(128, 255, 0, 0.7)',
		            0.2: 'rgba(255, 255, 0, 0.8)',
		            0.7: 'rgba(234, 72, 58, 0.9)',
		            1.0: 'rgba(162, 36, 25, 1)'
		        }, {
		            0.1: 'rgba(162, 36, 25, 0.7)',
		            0.2: 'rgba(234, 72, 58, 0.8)',
		            0.7: 'rgba(255, 255, 0, 0.9)',
		            1.0: 'rgba(128, 255, 0, 1)'
		        }],
		        radiuses = [5, 10, 20, 30],
		        opacities = [0.4, 0.6, 0.8, 1];


		    map.setType('yandex#map')

		    ymaps.modules.require(['Heatmap'], function (Heatmap) {
		        var heatmap = new Heatmap('''+json.dumps(coordinates)+''', {
		            gradient: gradients[0],
		            radius:'''+str(radius)+''',
		            opacity:'''+str(opacities)+''',
		        });
		        heatmap.setMap(map);

		        buttons.dissipating.events.add('press', function () {
		            heatmap.options.set(
		                'dissipating', !heatmap.options.get('dissipating')
		            );
		        });
		        buttons.opacity.events.add('press', function () {
		            var current = heatmap.options.get('opacity'),
		                index = opacities.indexOf(current);
		            heatmap.options.set(
		                'opacity', opacities[++index == opacities.length ? 0 : index]
		            );
		        });
		        buttons.radius.events.add('press', function () {
		            var current = heatmap.options.get('radius'),
		                index = radiuses.indexOf(current);
		            heatmap.options.set(
		                'radius', radiuses[++index == radiuses.length ? 0 : index]
		            );
		        });
		        buttons.gradient.events.add('press', function () {
		            var current = heatmap.options.get('gradient');
		            heatmap.options.set(
		                'gradient', current == gradients[0] ? gradients[1] : gradients[0]
		            );
		        });
		        buttons.heatmap.events.add('press', function () {
		            heatmap.setMap(
		                heatmap.getMap() ? null : map
		            );
		        });

		        for (var key in buttons) {
		            if (buttons.hasOwnProperty(key)) {
		                map.controls.add(buttons[key]);
		            }
		        }
		    });
		});  
	</script> 
	'''
	display(HTML(js))
