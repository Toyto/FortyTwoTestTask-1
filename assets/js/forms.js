$(document).ready(function() {
    function block_form() {
        $(".btns").hide();
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
            // return false to cancel submit
            block_form();
        },
        success: function() {
            unblock_form();
            $("#form_complete").show();
            setTimeout(function() {
                $("#form_complete").hide();
            }, 5000);
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
        $("#id_photo").change(readURL)
    });
});