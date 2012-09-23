/*
*   restForm
*
*   fatiherikli at gmail dot com
*   http://fatiherikli.com
*
* */
!(function ($) {

    $.fn.restForm = function (_options) {
        var options = $.extend({
            "submit": function () {},
            "complete": function () {}
        }, _options);

        var build_request_headers = function (method, url, data, content_type) {
            var result = [];
            result.push(method + " " + url); // method and url.
            result.push("Content-Type: " + content_type +"; charset=utf-8"); // content type
            if (!$.isEmptyObject(data)) {
                result.push(""); // blank line
                result.push(JSON.stringify(data)); // body
            }
            return result;
        };

        this.each(function () {
            $(this).submit(function () {
                var form = $(this);
                var data = form.form2json();
                var method = form.attr("method");
                var url = form.attr("action");
                var content_type = 'application/json';

                // firing submit event
                options.submit.call(this, form, build_request_headers(method, url, data,
                                                                content_type));

                // calling api resource
                $.ajax({
                    url: url,
                    type: method,
                    data: JSON.stringify(data),
                    contentType: content_type,
                    dataType: 'json',
                    processData: false
                }).complete(options.complete.bind(this, form));

                return false;

            });
        });
    };

})(window.jQuery)