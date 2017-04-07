/**
 * Created by xlsqac on 17-4-2.
 */
$(function () {
    var user_name, name,span;
    user_name = $('#user_name');
    span = user_name.siblings('span');
    user_name.blur(function () {
        name = user_name.val();
        console.log(name);
        $.get('/user/user_is_exist/?user_name=' + name,function (data) {
            console.log(data);
            if(data.exist==='1'){
                span.html('用户名已存在,请重新输入');
                span.show();
            }else{
                span.hide();
            }
        });
    });
});