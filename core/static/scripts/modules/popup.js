export function popup() {

    $(document).ready(function ($) {
        $('.makeOrder').click(function (e) {
            e.preventDefault();

            // Получение данных из формы
            let fio = $('.name-fename').val();
            let phoneNumber = $('.numbers-tel').val();
            let service = $('.selected-category').val();
            var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
            // Создание объекта с данными
            let formData = {
                name: fio,
                phone: phoneNumber,
                category: service,
                'csrfmiddlewaretoken': csrftoken
            };

            // Отправка данных на сервер
            $.ajax({
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: "{% url 'contact_form' %}",
                // on success
                success: function (response) {
                    alert("Thankyou for reaching us out " + response.name);
                },
                // on error
                error: function (response) {
                    // alert the error if any error occurred
                    alert(response.responseJSON.errors);
                    console.log(response.responseJSON.errors)
                }
            });
        });

        $('.popup-open').click(function () {
            $('.popup-fade').fadeIn();
            return false;
        });

        $('.popup-close').click(function () {
            $(this).parents('.popup-fade').fadeOut();
            return false;
        });

        $(document).keydown(function (e) {
            if (e.keyCode === 27) {
                e.stopPropagation();
                $('.popup-fade').fadeOut();
            }
        });

        $('.popup-fade').click(function (e) {
            if ($(e.target).closest('.popup').length == 0) {
                $(this).fadeOut();
            }
        });

        $('.popup-close').click(function () {
            $(this).parents('.popup-fade-2').fadeOut();
            return false;
        });

        $('.call').on('click', function () {
            $('.type-question').removeClass('d-none')
            $('.type-category').addClass('d-none')
            let popup = $(".popup")
            popup.attr("data-type", "recall")
        })

        $('.application').on('click', function () {
            $('.type-question').addClass('d-none')
            $('.type-category').removeClass('d-none')
            let popup = $(".popup")
            popup.attr("data-type", "makeOrder")
        })
    });

}


