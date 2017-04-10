/**
 * Created by xlsqac on 2017/4/5.
 */
$(function () {
    var add, minus, numberBox, number;
    add = $('.add');
    minus = $('.minus');
    numberBox = $('.num_show');
    number = numberBox.val();
    add.click(function () {
        number = numberBox.val();
        number++;
        numberBox.val(number);
        price_change();
    });
    minus.click(function () {
        number = numberBox.val();
        number--;
        if(number <= 1){
            number = 1;
        }
        numberBox.val(number);
        price_change();
    });
    function  price_change() {
        var $total = $('.total'), prices, onePrice;
        onePrice = $('.show_pirze').children('em').text();
        prices = number * parseFloat(onePrice);
        $total.children('em').text(prices.toFixed(2) + '元');
    }
   numberBox.blur(function () {
        price_change();
    });
});