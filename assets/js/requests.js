$(document).ready(
            function() {
                setInterval(function() {
                    $('#list').empty();
                    $('#full').load(document.URL + ' #full');
                    $.ajax({
                        method: 'POST',
                        url: _URLS.requests,
                        data: $('form').serialize(),
                        contentType: "application/json; charset=utf-8",
                        dataType: "json"
                        })
                }, 5000);
            });
