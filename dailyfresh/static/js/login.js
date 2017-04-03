/**
 * Created by xlsqac on 17-4-2.
 */
$(function () {
    var oUserName, oPwd, oPwd_error, setData, oUser_error,oIsRememberUserName;

    oUserName = $('.name_input');
    oPwd = $('.pass_input');
    oPwd_error = $('.pwd_error');
    oUser_error = $('.user_error');
    oIsRememberUserName = $('#isRememberUserName');

    $('.input_submit').click(function () {
        setData = {
            'user_name': oUserName.val(),
            'pwd': oPwd.val(),
            'isRememberUserName':oIsRememberUserName.val()
        };
        $.post('/login_handle/', setData, function (data) {
            if(data.login === '0'){
                oPwd_error.html('密码错误,请重试');
                oPwd_error.show();
                oUser_error.hide()
            }else if(data.login === '1'){
                oUser_error.html('用户名不存在,请输入正确的用户名或者注册');
                oUser_error.show();
                oPwd_error.hide();
            }else {
                location.href = "/user_center_info/"
            }
        });
    });
});