export function validation() {
    function sendAjax(dataForm) {
        for (const dataFormKey in dataForm) {
            if (dataFormKey == 'lastname') {
                dataForm['name'] = `${dataForm.firstname} ${dataForm.lastname}`
                break; // прерываем цикл после установки имени
            } else if (dataFormKey == 'firstname') {
                dataForm['name'] = `${dataForm.firstname}`;
            }
        }

    }


    $('.makeOrder').click(function () {

        let name = $('.name-fename').val();
        let phone = $('.numbers-tel').val();
        let question = $('.type-question').val();
        let category = $('.selected-category').val();

        // Create a data object to send in the AJAX request
        let data = {
            name: name,
            phone: phone,
            question: question,
            category: category
        };

        let csrftoken = $("input[name='csrfmiddlewaretoken']").val();

        // Make an AJAX POST request

        $.ajax({
            type: 'POST',
            url: '/ajax/', // Replace with your server endpoint URL
            data: JSON.stringify(data),
            dataType: 'json',
            headers: {
                'X-CSRFToken': csrftoken,
            },
            contentType: 'application/json',
            success: function (response) {
                // Handle the success response here
                console.log(response);
            },
            error: function (error) {
                // Handle any errors here
                console.error(error);
            }
        });
    });
}