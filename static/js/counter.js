var time = 2;
var counterElements = $('#counter').find('div');
var maxNum = 0;

counterElements.each(function(){
  var num = $(this).data('num');
  if (num > maxNum) {
    maxNum = num;
  }
});

var i = 0;
var step = (1200 * time) / maxNum;
var int = setInterval(function() {
  if (i > maxNum) {
    clearInterval(int);
  }

  counterElements.each(function(){
    var num = $(this).data('num');
    if (i <= num) {
      $(this).html(i);
    }
  });

  i++;
}, step);
