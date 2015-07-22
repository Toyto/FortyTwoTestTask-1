$(document).ready(function() {
        $("#btn-save").click(function() {
            $.ajax({
                method: 'POST',
                url: _URLS.requests,
                data: $('form').serialize(),
                dataType: "json"
                })
        });
        setInterval(function() {
                $('#list').empty();
                $('#full').load(document.URL + ' #full');
            }, 10000);
    });
