/**
 * Created by xlsqac on 2017/4/6.
 */
$(function () {
    var $add_goods, g_id;
    $add_goods = $('.add_goods');
    $add_goods.click(function () {
        g_id = $(this).attr("id");
        console.log(g_id);
        $.get('/cart/add_goods/?g_id=' + g_id + '&count=1', function (data) {
            $('.goods_count').text(data.count);
        });
    });
});