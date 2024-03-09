var time = 1;

function startCounter(id, maxNum) {
    var counterElement = $('#' + id).find('.indicators-title');
    var i = 0;
    var step = (1000 * time) / maxNum;

    var int = setInterval(function () {
        if (i > maxNum) {
            clearInterval(int);
        }

        if (i <= maxNum) {
            counterElement.html(i);
        }

        i++;
    }, step);
}

// Пример использования
var totalClients = $('#counter-1').find('.indicators-title').data('num');
var totalBanquets = $('#counter-2').find('.indicators-title').data('num');
var totalOnline = $('#counter-3').find('.indicators-title').data('num');
var totalDishes = $('#counter-4').find('.indicators-title').data('num');

startCounter('counter-1', totalClients);
startCounter('counter-2', totalBanquets);
startCounter('counter-3', totalOnline);
startCounter('counter-4', totalDishes);
