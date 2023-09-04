export function choice(){
    $(document).ready(function() {
        $(".price-button").click(function() {
          $(".selected-category").val("Гигиенический груминг");
        });
      });
    $(document).ready(function() {
        $(".profesional-button").click(function() {
          $(".selected-category").val("Профессиональный груминг");
        });
      });
    $(document).ready(function() {
        $(".aesthetics-button").click(function() {
          $(".selected-category").val("Эстетический груминг");
        });
      });
}