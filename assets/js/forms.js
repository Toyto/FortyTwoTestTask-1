$(document).ready(function() {

    $.ajax({
        method: 'GET',
        url: _URLS.person_info,
        data: $('#register_form').serialize(),
        dataType: 'json',
        success: function(json){
            var name = json['name'];
            var surname = json['surname'];
            var bio = json['bio'];
            var birth = json['birth_date'];
            var contacts = json['contacts'];
            var skype = json['skype'];
            var jabber = json['jabber'];
            var email = json['email'];
            var photo = json['photo'];
            $('#id_photo').attr('type', 'text');
            $('#id_name').val(name);
            $('#id_surname').val(surname);
            $('#id_birth_date').val(birth);
            $('#id_bio').val(bio);
            $('#id_skype').val(skype);
            $('#id_jabber').val(jabber);
            $('#id_contacts').val(contacts);
            $('#id_email').val(email);
            $('#id_photo').val(photo);
            $('#photo').attr('src', photo);
        }
    });

    $("#id_photo").click(function() {
        var photo_url = $('#id_photo').val();
        $('#photo').attr('src', photo_url);
    });

    function block_form() {
        $("#loading").show();
        $('textarea').attr('disabled', 'disabled');
        $('input').attr('disabled', 'disabled');
    }

    function unblock_form() {
        $('#loading').hide();
        $('textarea').removeAttr('disabled');
        $('input').removeAttr('disabled');
    }

    var callback = {
        beforeSubmit: function(form, options) {
            block_form();
        },
        success: function(data) {
            unblock_form();
            $("#form_complete").show();
            setTimeout(function() {
                $("#form_complete").hide();
            }, 5000);
        },
        error: function() {
            unblock_form();
            $("#form_error").show();
            setTimeout(function() {
                $("#form_error").hide();
            }, 5000);
            alert('You make some errors, fix it and try again');
        }
    }

    $('#register_form').ajaxForm(callback);

    function readURL() {
        var input = this;
        if (input.files && input.files[0]) {
            var preview = new FileReader();
            preview.onload = function (event) {
                $(".picture").attr('src', event.target.result);
            }
            preview.readAsDataURL(input.files[0]);}}

    $(function () {
        $("#id_photo").change(readURL);
        $(".picture").show();
    });

});
