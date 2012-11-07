var APIBrowser = $.Class.extend({

    EMPTY_RESPONSE: "(EMPTY RESPONSE)",
    SLIDE_DURATION: 100,
    FADE_DURATION: 500,
    HIGHLIGHT_DURATION: 2000,

    selectors: {
        input_fields: "input[type='text'], input[type='checkbox'], textarea, select",
        copied_fields: "input[isacopy], textarea[isacopy], select[isacopy]",

        // Global elements
        global_inputs : "#global-form input[type='text'], #global-form input[type='checkbox'], #global-form textarea, #global-form select",
 
        // API Resources
        endpoint_form : ".endpoint form",
        endpoint_anchor: ".endpoint a",
        try_it: ".try-it",
        request: ".request",
        code: "code",
        response_status: ".response-status",
        response_headers: ".response-headers",
        response_body: ".response-body",
        url_parameters: ".url-parameters input",

        // API Feedback
        feedback_form: "#submit-feedback form",
        feedback_response: "#submit-feedback #feedback-response",
        feedback_show_button: "#submit-feedback-button",
        feedback_endpoint: ".endpoint a.give-feedback",
        feedback_resource_field: "#id_resource"
    },

    init: function () {
        this.load_rest_form();
        this.load_feedback_form();
        this.make_expandable(this.selectors.endpoint_anchor, this.selectors.try_it, this.SLIDE_DURATION);
        this.make_expandable(this.selectors.feedback_show_button, this.selectors.feedback_form, this.SLIDE_DURATION);
        this.fill_url_parameters(this.selectors.url_parameters, this.selectors.endpoint_form);
    },

    load_rest_form: function () {
        $(this.selectors.endpoint_form).restForm({
            "presubmit": this.presubmit_form.bind(this),
            "submit": this.submit_form.bind(this),
            "complete": this.complete_ajax_request.bind(this)
        });
    },

    presubmit_form: function (form) {
        // Copy global paramaters to submitted form.
        $(this.selectors.global_inputs).not(':submit').clone().hide().attr('isacopy','y').appendTo(form);
    },

    submit_form: function (form, request_headers) {
        form.siblings(this.selectors.request).show().
            find(this.selectors.code).html(request_headers.join("\n"));
    },

    complete_ajax_request: function (form, xhr) {
        // Clear copied elements (prevent duplicates)
        $(this.selectors.copied_fields).remove();

        form.siblings(this.selectors.response_status).show().find(
            this.selectors.code).html(xhr.statusText + " (" + xhr.status + ")");

        form.siblings(this.selectors.response_headers).show().find(
            this.selectors.code).html(xhr.getAllResponseHeaders());

        var responseText = xhr.responseText || this.EMPTY_RESPONSE;
        try {
            responseText = JSON.stringify(JSON.parse(responseText), null, 2);
        } catch (err) {}

        form.siblings(this.selectors.response_body).show().find(
            this.selectors.code).text(responseText);
    },

    make_expandable: function (click_element, show_element, slide_duration) {
        $(click_element).click(function () {
            $(this).siblings(show_element).slideToggle(slide_duration || "normal");
            return false;
        });
    },

    fill_url_parameters: function (url_parameters, form_selector) {
        $(url_parameters).change(function () {
            var form = $(this).parents(form_selector);
            var rendered_url = form.data("endpoint-url");

            form.find("input[data-token]").each(function () {
                rendered_url = rendered_url.replace($(this).data("token"), $(this).val());
            });

            form.attr("action", rendered_url)
        })
    },

    load_feedback_form: function () {

        $(this.selectors.feedback_endpoint).click(function (event) {
            $(this.selectors.feedback_form)
                    .slideToggle(this.SLIDE_DURATION)
                    .find(this.selectors.feedback_resource_field)
                    .val($(event.target).data("endpoint"));
        }.bind(this));

        $(this.selectors.feedback_form).submit(function () {
            var form = $(this.selectors.feedback_form);
            $.post(form.attr("action"), form.serialize(), this.show_feedback_response.bind(this), "json");
            return false;
        }.bind(this));
    },

    show_feedback_response: function (response) {
        var feedback_response = $(this.selectors.feedback_response);
        var feedback_form = $(this.selectors.feedback_form);
        if (response.success) {
            feedback_form.hide();
            feedback_response.fadeIn(this.FADE_DURATION);
            feedback_response.delay(this.HIGHLIGHT_DURATION).fadeOut(this.FADE_DURATION);
            this.clear_feedback_form(feedback_form);
        }
    },

    clear_feedback_form: function (form) {
        form.find(this.selectors.input_fields).val("");
    }


});
