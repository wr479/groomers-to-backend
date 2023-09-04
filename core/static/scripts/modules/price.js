export function price (){
   
      $('.price-button').on('click',()=>{
        function insert(word) {
            let inp = $('#ctr');
            let start = inp[0].selectionStart;
            inp.val(inp.val().substring(0, start) + word +
              inp.val().substring(inp[0].selectionEnd, inp.val().length));
            inp.focus();
            inp[0].setSelectionRange(start, start + word.length);
          }
      })
}