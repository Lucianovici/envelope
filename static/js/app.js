/**
 * Envelope app.
 */
(function ($) {
    var EnvelopeApp = {
        submitForm: function (form) {
            var $form = $(form);

            $.ajax({
                type: "POST",
                dataType: "json",
                data: $form.serialize(),
                success: this.submitSuccessCallback.bind(this),
                error: this.submitErrorCallback.bind(this)
            });
        },

        submitSuccessCallback: function (data, textStatus, jqXHR) {
            if (data && data['isResponseRecorded']) {
                window.location.href = this.formResponseUrl;
            } else {
                this.displayGeneralError();
            }
        },

        submitErrorCallback: function (jqXHR, textStatus, errorThrown) {
            this.displayGeneralError();
        },

        errorPlacement: function (error, element) {
            error.appendTo($("#" + element.data("id") + "-section"));
        },

        displayGeneralError: function () {
            $("#general-error-placeholder").append($("<p>").html("Something went wrong!"))
        },

        init: function () {
            this.$envelopeForm = $("#envelope-form");
            this.formResponseUrl = this.$envelopeForm.data("response-url");

            this.$envelopeForm.validate({
                submitHandler: this.submitForm.bind(this),
                errorPlacement: this.errorPlacement
            });
        }
    };


    EnvelopeApp.init();
})(jQuery);