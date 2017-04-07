/**
 * Created by xlsqac on 2017/4/6.
 */
$(function () {
    var add_cart, g_id;
    add_cart = $('#add_cart');
    add_cart.click(function () {
        count = $('.num_show').val();
        g_id = $(this).attr("data-id");
        $.get('/cart/add_goods/?g_id=' + g_id + '&count=' + count, function (data) {
            $('.goods_count').text(data.count);
        });
    });
});