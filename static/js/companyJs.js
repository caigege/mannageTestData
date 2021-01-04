function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    //加载后产生的元素，要在第一次加载的元素 　　$("父级元素").on("事件","当前元素",function(){
    // 如果 父级元素 还不行 就用 $(document).on("事件","当前元素",function(){})
    // $('body') .on("事件","当前元素",function(){})
    $("#DepTbody").on('click', $("button[name='addPost']"), function () {
    // $("button[name='addPost']").on('click', function () {

        //添加岗位
        // alert($(this).parent().parent().children().first())

        // var word = prompt("请输入岗位名字2-20", "")
        // if (word) {
        //
        //     // alert("word :" + word)
        //     if (word.length <= 20 & word.length > 0) {
        //
        //
        //
        //
        //     } else {
        //         alert("word :不要超过20")
        //     }
        //
        // } else {
        //     alert("请输入岗位名字")
        // }
    })

    $("button[name='empCheck']").click(function () {
        //查询员工

        $.get(
            "/company/empGet/",
            function (data, status) {
                //知识点 js 对象类型
                // console.log("data type", typeof data)
                showOption($(".emp"))
                console.log("data type: " + data)
                // console.log("data type: " + data.length)
                var JSONdata = JSON.parse(data)
                console.log("data JSONdata", JSONdata)

                $("#empTbody").empty()
                // 注意点 差错 超出范围
                // for (j = 0; j < JSONdata.length; j++) {
                for (j = 0; j < JSONdata.length; j++) {
                    // console.log(j)
                    $("#empTbody").append("<tr>" +
                        "<td>" + JSONdata[j].name + "</td>" +
                        "<td>" + (JSONdata[j].gender ? "男" : "女") + "</td>" +
                        "<td>" + JSONdata[j].education + "</td>" +
                        "<td>" + JSONdata[j].phone + "</td>" +
                        "<td>" + JSONdata[j].email + "</td>" +
                        "<td>" + JSONdata[j].department + "</td>" +
                        "<td>" + JSONdata[j].level + "</td>" +
                        "<td>" + JSONdata[j].salary + "</td>" +
                        "<td>" + JSONdata[j].post + "</td>" +
                        "<td>" + JSONdata[j].entryTime + "</td>" +
                        "<td>" + JSONdata[j].birthday + "</td>" +
                        "<td>" + JSONdata[j].identityCard + "</td>" +
                        "</tr>"
                    )

                }


            },
            "json"//
        )


    });

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
        // var csrftoken = getCookie("csrftoken");
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
        // $(".dep").attr("style", "display:none;")
        // $(".recruitment").attr("style", "display:block;")
        showOption($(".recruitment"))


    })


    $("button[name='dep']").click(function () {

        // 部门管理

        // $(".dep").attr("style", "display:block;")
        // $(".recruitment").attr("style", "display:none;")
        showOption($(".dep"))
        getdep();


    });


    $("button[name='add']").click(function () {

        let id = $(this).val()
        let dep = $(this).parent().parent().find("select option:selected").text()
        let bool = (id + dep).indexOf("&") != -1
        if (bool || dep == "选择部门") {
            alert("输入错误：" + bool + "选择部门")
            return
        }
//        知识点
// str.indexOf(res) != -1
// str 存在的字符串(长的) res 验证的字符串(短的) true 包含 false 不包含

// str.search(res) != -1
// str 存在的字符串(长的) res 验证的字符串(短的) true 包含 false 不包含

        console.log("id:" + id)
        console.log("dep:" + dep)

        {
            // 添加员工

        }


        $.ajax({
            url: "/addEmp/" + id + "&" + dep,
            error: function (e) {
                alert("错误：", e)
            },
            // type:
            success: function (result) {
                alert("成功" + result['message'])

            }

        });

    })

    function showOption(e) {
        //展示对应的列表 隐藏其他列表
        var eles = [$(".dep"), $(".recruitment"), $(".emp")]
        // $(".dep").attr("style", "display:block;")
        // $(".recruitment").attr("style", "display:none;")
        for (ele in eles) {

            // console.log(ele)

            eles[ele].attr("style", "display:none;")
        }
        // if (eles.includes(e)) {
        e.attr("style", "display:block;")
        // }


    }

    function getdep() {
        // 查询部门
        $.get(
            "/company/getDep/",
            function (data, status) {
                //知识点 js 对象类型
                // console.log("data type", typeof data)
                // console.log("data type: " + data[0]['name'])
                // console.log("data type: " + data.length)
                // let len = data.length
                $("#DepTbody").empty()
                for (j = 0; j < data.length; j++) {
                    $("#DepTbody").append("<tr>" +
                        // "<td name=n_"+data[j]['id']+">" + data[j]['name'] + "</td>" +
                        "<td name=n_"+1+">" + data[j]['name'] + "</td>" +
                        "<td>" + data[j]['name'] + "</td>" +
                        // "<td>" + "<input type='button' name='addPost' value='添加岗位'>" + "</td>" +
                        "<td>" + "<button name='addPost' >添加岗位</button>" + "</td>" +
                        "</tr>"
                    )

             }
             $(document).ready(function(){
                 $("button[name='addPost']").click(function () {
                    alert( $(this))
                 })
             })

            },
            "json"//
        )
    }
})