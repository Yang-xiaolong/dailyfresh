/**
 * Created by xlsqac on 2017/4/7.
 */
$(function () {
    var price, count, subtotal, num,total_goods_count,subtotals,cartId;
    num = 0;
    subtotals = 0;
    goodsList = [];
    cartId = 0;
    total_goods_count = $('.total_goods_count');
        $('.col07').each(function () {
            num++;
            price = parseFloat($(this).prev().prev().attr("id"));
            count = parseInt($(this).prev().text());
            subtotal = price * count;
            $(this).text(subtotal.toFixed(2) + '元');
            subtotals += subtotal;
            cartId = $(this).parent().attr("id");
            goodsList.push(cartId)
        });
       total_goods_count.children('em').text(num ).next().text(subtotals.toFixed(2) +  '元');
       $('.total_pay').children('b').text((subtotals+10).toFixed(2) + '元');
        $('#order_btn').click(function () {
            var setData;
            setData = {
                'address':$('dd').attr("id"),
                'count': num,
                'subtotals': (subtotals+10).toFixed(2),
                'goods_list':goodsList.join(",")
            };
            console.log(goodsList);
            $.post('/order/submit/',setData,function (data) {
                console.log(data.state);
                if (data.state === "0"){
                    alert('库存不足，购买失败，请重新购买');
                    location.href = "/cart/";
                }else if(data.state === 1){
                    console.log(".......");
                    location.href = "/user/user_center_order/";
                }else if(data.state === "2"){
                    alert("购买失败,原因不详,请重试");
                    location.href = "/cart/";
                }
            });
        });
});