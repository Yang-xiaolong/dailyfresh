/**
 * Created by xlsqac on 2017/4/6.
 */
$(function () {
    var add, minus, numberBox;
    add = $('.add');
    minus = $('.minus');
    subtotal();
    $('#check_all').click(function () {
        var state;
        state = $(this).prop('checked');
        $(':checkbox:not(#check_all)').prop('checked', state)
    });
    add.click(function () {
        numberBox = $(this).next();
        numberBox.val(parseInt(numberBox.val()) + 1).blur();
    });
    minus.click(function () {
        numberBox = $(this).prev();
        if(numberBox.val() <= 1){
            numberBox.val(1).blur();
        }else{
            numberBox.val(parseInt(numberBox.val()) - 1).blur();
        }
    });
   $('.num_show').blur(function () {
       var count, cart_id;
       count = $(this).val();
       cart_id = $(this).parents('.cart_list_td').attr("id");
        $.get('/cart/change/?cart_id=' + cart_id  +  '&count='+ count,function (data) {
            $(this).val(data.count);
            subtotal();
            if (data.is_error === 'ok'){
                alert('修改失败，请刷新页面后重试！')
            }
        });
    });

    $('.col08').click(function () {
        var cart_id, cart_list;
        cart_list = $(this).parent();
        cart_id = cart_list.attr("id");
        console.log(cart_id);
        $.get('/cart/del/?cart_id=' + cart_id, function (data) {
            alert('是否删除');
            console.log(data.is_delete);
            if (data.is_delete === 'ok') {
                cart_list.remove();
            }
        });
    });
    $(':checkbox').click(function () {
        subtotal();
    });
    $(':checkbox:not(#check_all)').click(function () {
        if(!$(this).prop('checked')){
            $('#check_all').prop('checked',false);
        }else if($(':checkbox:not(#check_all)').prop('checked')){
            $('#check_all').prop('checked',true);
        }
    });
    
    function subtotal() {
        var counts , subtotals;
        counts = 0;
        subtotals = 0;
        $('.col07').each(function () {
            var one_price, count, subtotal;
            one_price = parseFloat($(this).prev().prev().attr("id"));
            count = parseFloat($(this).prev().find('.num_add').find('.num_show').val());
            subtotal = one_price * count ;
            $(this).text(subtotal.toFixed(2) + '元');
            if ($(this).parent().find('.col01').find('#check').prop('checked')){
                counts++;
                subtotals+=subtotal;
            }
            $('.total_count').find('em').text(counts);
            $('.settlements').find('.col03').find('em').text(subtotals.toFixed(2)).next().next().text(counts);

        });
    }
});