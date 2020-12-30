function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {

    function getdep() {
        // 查询部门
        $.get(
            "/company/getDep/",
            function (data, status) {
                //知识点 js 对象类型
                // console.log("data type", typeof data)
                console.log("data type: " + data[0]['name'])
                console.log("data type: " + data.length)
                // let len = data.length
                $("#DepTbody").empty()
                for (j = 0; j < data.length; j++) {
                    $("#DepTbody").append("<tr>" + "<td>" + data[j]['name'] + "</td></tr>")


                    // $("#DepTbody").append()
                    // $("#DepTbody").append()
                }


            },
            "json"//
        )
    }

    // $.ajaxSetup({
    //        data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
    //    })


    $("button[name='addDep']").click(function () {


        // alert(1)
        //  添加部门
        let depname = $("#depName").val();
        if (depname == "" || $.trim(depname).length == 0) {
            alert("不能为空");
            return
            // throw SyntaxError();
        }


        // todo token验证未处理
        var csrftoken = getCookie("csrftoken");
        // var csrftoken = Cookies.get('csrftoken');
        $.ajax({
            url: "/company/addDep/",
            type: "POST",
            // header:{
            //      "X-CSRFToken": getCookie("csrftoken")
            // },
            data: {
                depName: depname,
                // csrfmiddlewaretoken: '{{ csrf_token }}'
            },

            success: function (resulet) {
                alert(resulet.message)
                getdep()
            }
        })

    })

    $("button[name='recruitment']").click(function () {
        //招聘
        $(".dep").attr("style", "display:none;")
        $(".recruitment").attr("style", "display:block;")

    })


    $("button[name='dep']").click(function () {

        // 部门管理

        $(".dep").attr("style", "display:block;")
        $(".recruitment").attr("style", "display:none;")
        getdep();


    });


    $("button[name='add']").click(function () {

        let id = $(this).val()
        console.log("id:"+id)
        {
            // 添加员工

        }
        $.ajax({
            url: "/addEmp/" + id, success: function (result) {


            }

        });

    })

})