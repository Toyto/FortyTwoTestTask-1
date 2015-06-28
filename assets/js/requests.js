$(document).ready(
            function() {
                setInterval(function() {
                    $('#list').empty();
                    $('#full').load(document.URL + ' #full');
                }, 1000);
            });