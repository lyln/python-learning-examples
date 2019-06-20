/**
 * Created by ljd on 2016/8/26.
 */

$(document).ready(function(){
    //删除操作
    $('a.btn-danger-delete').click(function(){
//        var data = {}
//        data['host_name'] = 'stat1'
//        data['ip_internet'] = $('#ip_internet').val()
//        data['ip_intranet'] = $('#ip_intranet').val()
//        data['cpu_num'] = $('#cpu_num').val()
//        data['mem'] = $('#mem').val()
//        data['disk'] = $('#disk').val()
//        data['user_name'] = $('#user_name').val()
//        data['passwd'] = $('#passwd').val()
        var m_id = $(this).attr('m_id')
		console.log(m_id)

        $.ajax({
            type: "POST",
            url: "/delete_rules",
            data: { "m_id": m_id},
            success: function(data){
                if (data = 'ok')
                    alert("删除成功！");
                else
                    alert("删除失败！");
//                for (var i in data)
//                    {
//                        txt = txt + i;
//                        $("#console").val(txt);
//                    }
            },
            error: function(jqXHR){
                alert("错误:" + jqXHR.status);
            }

        });
    });
});