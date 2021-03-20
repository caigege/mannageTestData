function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    // 部门名字
    var department_global = ""
    //用户唯一标识电话
    var phone_global = ""

    $("#projectTbody").on("click", "button[name='projectDetails']", function () {

        var businessName = $(this).parent().parent().children().eq(1).text()
        // alert(businessName)
        window.location = "/tobusiness/" + businessName
    })


    $("button[name='project']").click(function () {

        showOption($(".project"))
        $.get("/company/getProject/", function (data) {
            // alert(typeof  data)
            var JSONdata = JSON.parse(data)
            $("#projectTbody").empty()
            for (var i = 0; i < JSONdata.length; i++) {
                var state = ""
                switch (JSONdata[i].state) {
                    case 0:
                        state = "<td style='background-color:navajowhite'>" + "计划中" + "</td>"
                        break;
                    case 1:
                        state = "<td  style='background-color:orangered'>" + "进行中" + "</td>"
                        break;

                    case 2:
                        state = "<td style='background-color:green; color: #fff;' >" + "完成" + "</td>"
                        break;

                    case 3:
                        state = "<td style='background-color:aliceblue; color: #000000;'>" + "暂停" + "</td>"
                        break;

                    case 4:
                        state = "<td style='background-color:grey; color: #fff;'>" + "终止" + "</td>"
                        break;
                    default:
                        state = "<td style='color: red'>" + "异常" + "</td>"
                }
                description = JSONdata[i].description
                if (description.length > 10) {
                    description = description.substring(0, 10) + "..."
                }

                $("#projectTbody").append(
                    "<tr>" +
                    "<td>" + i + "</td>" +
                    "<td>" + JSONdata[i].name + "</td>" +
                    "<td>" + description + "</td>" +
                    "<td>" + JSONdata[i].schedule + "</td>" +
                    "<td>" + JSONdata[i].source + "</td>" +
                    state +
                    "<td>" + JSONdata[i].note + "</td>" +
                    "<td> <button name='projectDetails'>详情</button> </td>" +
                    "</tr>"
                )
            }

        }, "json")

    })


    //加载后产生的元素，要在第一次加载的元素 　　$("父级元素").on("事件","当前元素",function(){
    // 如果 父级元素 还不行 就用 $(document).on("事件","当前元素",function(){})
    // $('body') .on("事件","当前元素",function(){})
    $('#empTbody').on("click", "button[name='changePost']", function () {
        //部门
        department_global = $(this).parent().parent().children().eq(5).text()
        // 获取用户 唯一标识phone
        phone_global = $(this).parent().parent().children().eq(3).text()
        $.get("/company/getPost/", {"department": department_global}, function (e) {
            // 获取岗位
            // alert(data[0].postName)
            var JSONe = JSON.parse(e)
            // alert(JSONe)
            $("#postSele").empty()

            for (var i = 0; i < JSONe.length; i++) {
                if (JSONe[i].postName == "暂无") {
                    // $('#postChange').attr("style", "display:none")
                    alert("暂无:该部门暂未设置岗位,请在部门中设置岗位")

                    return
                } else {
                    $('#postChange').attr("style", "display:block")
                    $("#postSele").append(
                        "<option>" + JSONe[i].postName.split("*")[1] + "</option>"
                    )
                }
            }
        })
    })


    $("#postSave").click(function () {
        // 保存
        var postnanme = department_global + "*" + $("#postSele option:selected").val()

        // 员工修改岗位
        $.post("/company/updatePost/", {"phone": phone_global, "postnanme": postnanme}, function (postdata) {
            var JSONpostdata = JSON.parse(postdata)
            alert(JSONpostdata.message)

            $.get(
                "/company/empGet/",
                function (data, status) {
                    //知识点 js 对象类型
                    // console.log("data type", typeof data)

                    var JSONdata = JSON.parse(data)
                    showEmpthis(JSONdata);
                    // $("#postSave").remove()
                    $('#postChange').attr("style", "display:none")

                })

        })
        // return
    })
    $('button[id="postCancel"]').click(function () {
        //取消
        $('#postChange').attr("style", "display:none")
        return
    })


    function showEmpthis(JSONdata) {
        $("#empTbody").empty()
        // 注意点 差错 超出范围
        // for (j = 0; j < JSONdata.length; j++) {
        for (j = 0; j < JSONdata.length; j++) {
            $("#empTbody").append("<tr>" +
                "<td>" + JSONdata[j].name + "</td>" +
                "<td>" + (JSONdata[j].gender ? "男" : "女") + "</td>" +
                "<td>" + JSONdata[j].education + "</td>" +
                "<td>" + JSONdata[j].phone + "</td>" +
                "<td>" + (JSONdata[j].email == null ? "暂无" : 2) + "</td>" +
                "<td>" + JSONdata[j].department + "</td>" +
                "<td>" + JSONdata[j].level + "</td>" +
                "<td>" + JSONdata[j].salary + "￥</td>" +
                "<td>" + (JSONdata[j].post == null ? "暂无" : JSONdata[j].post.split("*")[1]) + "</td>" +
                "<td>" + JSONdata[j].entryTime + "</td>" +
                "<td>" + (JSONdata[j].birthday == null ? "暂无" : JSONdata[j].birthday) + "</td>" +
                "<td>" + (JSONdata[j].identityCard == null ? "暂无" : JSONdata[j].identityCard) + "</td>" +
                "<td><button name='changePost'>调整岗位</button></td>" +
                "</tr>"
            )
        }

    }


    $("button[name='empCheck']").click(function () {
        //查询员工
        // $(document).ready(function () {
        showOption($(".emp"))

        $.get(
            "/company/empGet/",
            function (data, status) {
                //知识点 js 对象类型
                // console.log("data type", typeof data)

                var JSONdata = JSON.parse(data)
                showEmpthis(JSONdata);
            }, "json")


    })


    $("button[name='addDep']").click(function () {


        //  添加部门
        let depname = $("#depName").val();
        if (depname == "" || $.trim(depname).length == 0) {
            alert("不能为空");
            return
            // throw SyntaxError();
        }
        // todo token验证未处理
        $.ajax({
            url: "/company/addDep/",
            type: "POST",
            data: {
                depName: depname,
            },
            success: function (resulet) {
                alert(resulet.message)
                getdep()
            }
        })

    })

    $("button[name='recruitment']").click(function () {

        console.log($("h2").data("data"))
        // 公司级别
        // let companyLv = $("h2").data("data")
        // if (companyLv == 1) {
        //     alert("当前公司为:" + companyLv + "星,请提升公司级别后再试")
        //     return
        // }


        //招聘
        showOption($(".recruitment"))


    })


    $("button[name='dep']").click(function () {

        // 部门管理
        showOption($(".dep"))
        getdep();


    });


    $("button[name='add']").click(function () {
        let companyLv = $("h2").data("data")
        let id = $(this).val()
        let dep = $(this).parent().parent().find("select option:selected").text()
        let bool = (id + dep).indexOf("&") != -1
        if (bool || dep == "选择部门") {
            alert("输入错误：" + bool + "选择部门")
            return
        }
        // if (companyLv <= 2) {
        //查询是否有其他人

        $.ajax({
            url: "/addEmpCheck/" + dep + "&" + companyLv,
            // error: function (e) {
            //     alert("错误：", e[])
            // },
            success: function (result) {

                if (result['message'] != "ok") {
                    alert("异常" + result['message'])
                    return
                } else {
                    $.ajax({
                        url: "/addEmp/" + id + "&" + dep,
                        error: function (e) {
                            alert("错误：", e)
                        },
                        success: function (result) {
                            alert("成功" + result['message'])
                        }

                    });
                }
            }
        });
    })

    function showOption(e) {
        //展示对应的列表 隐藏其他列表
        var eles = [$(".dep"), $(".recruitment"), $(".emp"), $(".project")]

        for (ele in eles) {


            eles[ele].attr("style", "display:none;")
        }
        // if (eles.includes(e)) {
        e.attr("style", "display:block;")
        // }


    }

    function checkDep(data) {
        $("#DepTbody").empty()

        for (j = 0; j < data.length; j++) {
            var postname = "";
            if (data[j]['postName'] == "暂无") {
                postname = "暂无"
            } else {
                let dataObj = data[j]['postName'].split(",")
                for (var dataChild in dataObj) {
                    console.log("dataChild", dataChild)
                    postname += dataObj[dataChild].split("*")[1] + ","
                }
                postname = postname.substring(0, (postname.length - 1))
            }
            $("#DepTbody").append("<tr>" +
                "<td>" + data[j]['name'] + "</td>" +
                "<td>" + postname + "</td>" +
                "<td>" + "<button name='addPost' >添加岗位</button>" + "</td>" +
                "</tr>"
            )

        }
    }

    function getdep() {
        // 查询部门
        $.get(
            "/company/getDep/",
            function (data, status) {

                checkDep(data);
                $(document).ready(function () {
                    $("button[name='addPost']").click(function () {

                        var depName = $(this).parent().parent().children().first().text()

                        var word = prompt("请输入岗位名字2-20", "")

                        if (word.length <= 20 & word.length > 1) {
                            $.post("/company/addPost/", {"depName": depName, "postName": word}, function (data) {
                                // console.log(data.message)
                                alert(data.message)
                                getdep()

                            })

                        } else {
                            alert("word :请输入岗位名字2-20字")
                        }
                    })
                })

            },
            "json"//
        )
    }
})

