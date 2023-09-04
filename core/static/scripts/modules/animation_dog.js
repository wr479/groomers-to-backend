
export function animation_dog(){

    $('.types-grooming').hover(function(){
        const img = $(this).attr('data-image')
        changeImage(img)
    }, resetImage())

    function changeImage(newImage) {
        var image = document.getElementById('image');
        if(image){
            image.srcset = newImage;
        }
    }
    
    function resetImage() {
        var image = document.getElementById('image');
        if(image){
            image.srcset = '/static/images/animate-image/funny-dog.png';
        }
    }
}