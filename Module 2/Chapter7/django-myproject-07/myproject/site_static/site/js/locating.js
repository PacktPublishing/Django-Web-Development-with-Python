(function($, undefined) {
    var gMap;
    var gettext = self.gettext || function(val) {return val;};
    var gMarker;

    function getAddress4search() {
        var address = [];
        var sStreetAddress2 = $("#id_street_address2").val();
        if (sStreetAddress2) {
            sStreetAddress2 = ' ' + sStreetAddress2;
        }
        address.push($("#id_street_address").val() + sStreetAddress2);
        address.push($("#id_city").val());
        address.push($("#id_country").val());
        address.push($("#id_postal_code").val());
        return address.join(", ");
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
        google.maps.event.addListener(gMarker, "dragend", function() {
            var point = gMarker.getPosition();
            updateLatitudeAndLongitude(point.lat(), point.lng());
        });
    }
    function updateLatitudeAndLongitude(lat, lng) {
        lat = Math.round(lat * 1000000) / 1000000;
        lng = Math.round(lng * 1000000) / 1000000;
        $("#id_latitude").val(lat);
        $("#id_longitude").val(lng);
    }
    function autocompleteAddress(results) {
        var $foundLocations = $('#map_locations').html("");
        var i, len = results.length;

        // console.log(JSON.stringify(results, null, 4));

        if (results) {
            if (len > 1) {
                for (i=0; i<len; i++) {
                    $('<a href="">' + results[i].formatted_address + '</a>').data("gmap_index", i).click(function() {
                        var result = results[$(this).data("gmap_index")];
                        updateAddressFields(result.address_components);
                        var point = result.geometry.location;
                        updateLatitudeAndLongitude(point.lat(), point.lng());
                        updateMarker(point.lat(), point.lng());
                        $foundLocations.hide();
                        return false;
                    }).appendTo($('<li>').appendTo($foundLocations));
                }
                $('<a href="">' + gettext("None of the listed") + '</a>').click(function() {
                    $foundLocations.hide();
                    return false;
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
            switch (obj.types[0]) {
                case "locality":
                    $("#id_city").val(obj.long_name);
                    break;
                case "street_number":
                    streetNumber = obj.long_name;
                    break;
                case "route":
                    streetName = obj.long_name;
                    break;
                case "postal_code":
                    $("#id_postal_code").val(obj.long_name);
                    break;
                case "country":
                    $("#id_country").val(obj.short_name);
                    break;
            }
        }
        if (streetName) {
            var streetAddress = streetName;
            if (streetNumber) {
                streetAddress += " " + streetNumber;
            }
            $("#id_street_address").val(streetAddress);
        }
    }

    $(document).ready(function(){
        $("#locate_address").click(function() {
            var oGeocoder = new google.maps.Geocoder();
            oGeocoder.geocode(
                {address: getAddress4search()},
                function(results, status) {
                    if (status === google.maps.GeocoderStatus.OK) {
                        autocompleteAddress(results);
                    } else {
                        autocompleteAddress(false);
                    }
                }
            );
        });

        $("#remove_geo").click(function() {
            $("#id_latitude").val("");
            $("#id_longitude").val("");
            gMarker.setMap(null);
            gMarker = null;
        });

        gMap = new google.maps.Map($('#map_canvas').get(0), {
            scrollwheel: false,
            zoom: 16,
            center: new google.maps.LatLng(51.511214, -0.119824),
            disableDoubleClickZoom: true
        });
        google.maps.event.addListener(gMap, 'dblclick', function(event) {
            updateLatitudeAndLongitude(event.latLng.lat(), event.latLng.lng());
            updateMarker(event.latLng.lat(), event.latLng.lng());
        });
        $('#map_locations').hide();

        var $lat = $("#id_latitude");
        var $lng = $("#id_longitude");
        if ($lat.val() && $lng.val()) {
            updateMarker($lat.val(), $lng.val());
        }
    });

}(jQuery));
