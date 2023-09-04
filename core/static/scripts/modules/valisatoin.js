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


    $('.makeOrder').on('click', () => {
        let numberInput = $('.numbers-tel');
        let inputs = $('.val');
        let ajaxData = {}; // Очищаем данные перед каждой отправкой

        $.each(inputs, (key, input) => {
            const type = $(input).attr('data-inputType');
            const value = $(input).val();
            if (value === '') {
                $(input).addClass('error');
            } else {
                $(input).removeClass('error').addClass('pop');
                ajaxData[type] = value;
            }
        });

        if (numberInput.val().length < 10) { // Проверка на минимальную длину номера
            numberInput.addClass('error');
        } else {
            numberInput.removeClass('error');
        }

        if ($('.error').length === 0) {
            let type = $(".popup").attr("data-type");
            sendAjax(ajaxData, type);
        }
    });

    $('.makeOrder').click(function () {
        console.log("gfdg")
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
        console.log(data)
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