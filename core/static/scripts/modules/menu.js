export function menu(){
    $(".end-content-mobile").on('click', () => {
        if ($('.menu').hasClass('d-none-menu')) {
            $('.menu').removeClass('d-none-menu');
            $('.menu').addClass('d-block-menu')
            
        }
        else{
            $('.menu').removeClass('d-none-menu');
            $('.menu').addClass('d-none-menu')
        }
    });
}