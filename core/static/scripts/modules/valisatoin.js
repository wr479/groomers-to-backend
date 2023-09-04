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
    $.ajax({
        url: '/ajax/',
        method: "POST",
        data: JSON.stringify(dataForm),
        success: callBack(dataForm.type)
    })
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
   document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('orderForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        fetch('/ajax/', {  // Измените на путь к вашему маршруту
            method: 'POST',
            body: JSON.stringify(jsonData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.created) {
                alert('Заказ успешно создан!');
            } else {
                alert('Произошла ошибка при создании заказа.');
            }
        })
        .catch(error => {
            console.error('Ошибка:', error);
        });
    });
});
}