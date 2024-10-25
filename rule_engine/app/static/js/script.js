$(document).ready(function() {
    function handleAjaxRequest(url, data, successCallback) {
        $.ajax({
            type: 'POST',
            url: url,
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: successCallback,
            error: function(error) {
                toastr.error('Error: ' + (error.responseJSON?.message || 'An unexpected error occurred.'));
                console.log(error);
            }
        });
    }

    $('#create-rule-form').submit(function(event) {
        event.preventDefault();
        const ruleString = $('#rule').val();
        
        handleAjaxRequest('/create_rule', { rule_string: ruleString }, function(response) {
            if (response.status === 'success') {
                toastr.success('Rule created successfully');
                $('#ast').val(JSON.stringify(response.ast, null, 2));
            } else {
                toastr.error('Error: ' + response.message);
            }
        });
    });

    $('#evaluate-rule-form').submit(function(event) {
        event.preventDefault();
        const ast = $('#ast').val();
        const data = $('#data').val();

        try {
            const parsedAST = JSON.parse(ast);
            const parsedData = JSON.parse(data);

            handleAjaxRequest('/evaluate_rule', { ast: parsedAST, data: parsedData }, function(response) {
                if (response.status === 'success') {
                    $('#result').text('Result: ' + response.result);
                    $('#result').toggleClass('result-true', response.result).toggleClass('result-false', !response.result);
                    toastr.success('Rule evaluated successfully');
                } else {
                    toastr.error('Error: ' + response.message);
                }
            });
        } catch {
            toastr.error('Invalid JSON format in AST or Data.');
        }
    });
});
