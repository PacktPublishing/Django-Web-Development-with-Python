(function ($, undefined) {
    var gMap;
    var gettext = window.gettext || function (val) {return val;};
    var gMarker;

    function getAddress4search() {
        var address = [];
        var sStreetAddress2 = $('#id_street_address2').val();
        if (sStreetAddress2) {
            sStreetAddress2 = ' ' + sStreetAddress2;
        }
        address.push($('#id_street_address').val() + sStreetAddress2);
        address.push($('#id_city').val());
        address.push($('#id_country').val());
        address.push($('#id_postal_code').val());
        return address.join(', ');
    }
    function updateMarker(lat, lng) {
        var point = new google.maps.LatLng(lat, lng);
        if (gMarker) {
            gMarker.setPosition(point);
        } else {
            gMarker = new google.maps.Marker({
                position: point,
                map: gMap
            });
        }
        gMap.panTo(point, 15);
        gMarker.setDraggable(true);
        google.maps.event.addListener(gMarker, 'dragend', function () {
            var point = gMarker.getPosition();
            updateLatitudeAndLongitude(point.lat(), point.lng());
        });
    }
    function updateLatitudeAndLongitude(lat, lng) {
        lat = Math.round(lat * 1000000) / 1000000;
        lng = Math.round(lng * 1000000) / 1000000;
        $('#id_latitude').val(lat);
        $('#id_longitude').val(lng);
    }
    function autocompleteAddress(results) {
        var $foundLocations = $('#map_locations').html('');
        var i, len = results.length;

        // console.log(JSON.stringify(results, null, 4)); // DEBUG

        if (results) {
            if (len > 1) {
                for (i=0; i<len; i++) {
                    $('<a href="">' + results[i].formatted_address + '</a>').data('gmap_index', i).click(function (e) {
                        e.preventDefault();
                        var result = results[$(this).data('gmap_index')];
                        updateAddressFields(result.address_components);
                        var point = result.geometry.location;
                        updateLatitudeAndLongitude(point.lat(), point.lng());
                        updateMarker(point.lat(), point.lng());
                        $foundLocations.hide();
                    }).appendTo($('<li>').appendTo($foundLocations));
                }
                $('<a href="">' + gettext('None of the listed') + '</a>').click(function (e) {
                    e.preventDefault();
                    $foundLocations.hide();
                }).appendTo($('<li>').appendTo($foundLocations));
                $foundLocations.show();
            } else {
                $foundLocations.hide();
                var result = results[0];
                updateAddressFields(result.address_components);
                var point = result.geometry.location;
                updateLatitudeAndLongitude(point.lat(), point.lng());
                updateMarker(point.lat(), point.lng());
            }
        }
    }
    function updateAddressFields(addressComponents) {
        var i, len=addressComponents.length;
        var streetName, streetNumber;
        for (i=0; i<len; i++) {
            var obj = addressComponents[i];
            var obj_type = obj.types[0];
            if (obj_type == 'locality') {
                $('#id_city').val(obj.long_name);
            }
            if (obj_type == 'street_number') {
                streetNumber = obj.long_name;
            }
            if (obj_type == 'route') {
                streetName = obj.long_name;
            }
            if (obj_type == 'postal_code') {
                $('#id_postal_code').val(obj.long_name);
            }
            if (obj_type == 'country') {
                $('#id_country').val(obj.short_name);
            }
        }
        if (streetName) {
            var streetAddress = streetName;
            if (streetNumber) {
                streetAddress += ' ' + streetNumber;
            }
            $('#id_street_address').val(streetAddress);
        }
    }

    $(function (){
        $('#locate_address').click(function () {
            var oGeocoder = new google.maps.Geocoder();
            oGeocoder.geocode(
                {address: getAddress4search()},
                function (results, status) {
                    if (status === google.maps.GeocoderStatus.OK) {
                        autocompleteAddress(results);
                    } else {
                        autocompleteAddress(false);
                    }
                }
            );
        });

        $('#remove_geo').click(function () {
            $('#id_latitude').val('');
            $('#id_longitude').val('');
            gMarker.setMap(null);
            gMarker = null;
        });

        gMap = new google.maps.Map($('#map_canvas').get(0), {
            scrollwheel: false,
            zoom: 16,
            center: new google.maps.LatLng(51.511214, -0.119824),
            disableDoubleClickZoom: true
        });
        google.maps.event.addListener(gMap, 'dblclick', function (event) {
            var lat = event.latLng.lat();
            var lng = event.latLng.lng();
            updateLatitudeAndLongitude(lat, lng);
            updateMarker(lat, lng);
        });
        $('#map_locations').hide();

        var $lat = $('#id_latitude');
        var $lng = $('#id_longitude');
        if ($lat.val() && $lng.val()) {
            updateMarker($lat.val(), $lng.val());
        }
    });

}(django.jQuery));
