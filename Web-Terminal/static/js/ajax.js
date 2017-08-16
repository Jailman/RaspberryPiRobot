function ExecGet(url) {
  $(document).ready(function(){
    $("button").click(function(){
      $.get(url);
    });
  });
}