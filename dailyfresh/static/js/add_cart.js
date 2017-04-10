/**
 * Created by xlsqac on 2017/4/6.
 */
$(function () {
    var add_cart, g_id, count;
    add_cart = $('#add_cart');
    count = 0;
    g_id = 0;
    add_cart.click(function () {
        count = $('.num_show').val();
        g_id = $(this).attr("data-id");
        $.get('/cart/add_goods/?g_id=' + g_id + '&count=' + count, function (data) {
            $('.goods_count').text(data.count);
        });
    });
    $('.buy_btn').click(function () {
        count = $('.num_show').val();
        g_id = add_cart.attr("data-id");
        $.get('/cart/add_goods/?g_id=' + g_id + '&count=' + count, function (data) {
                location.href = "/order/?cart_id=" + data.cart_id
        })
    });
});