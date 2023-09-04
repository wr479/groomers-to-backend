export function utils() {
    var element = document.querySelectorAll('input[name="phone"]');
    var maskOptions = {
        mask: '+{7} (000) 000-00-00',
        prepare: function (value, maskedInput) {
            if (value === '8' && maskedInput._value.length === 0) {
                return '';
            }
            return value;
        }
    }
    element.forEach((el) => {
        new IMask(el, maskOptions);
    })
}