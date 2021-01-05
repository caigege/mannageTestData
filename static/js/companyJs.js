function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    //加载后产生的元素，要在第一次加载的元素 　　$("父级元素").on("事件","当前元素",function(){
    // 如果 父级元素 还不行 就用 $(document).on("事件","当前元素",function(){})
    // $('body') .on("事件","当前元素",function(){})


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
                        "<td><button name='changePost'>调整岗位</button></td>" +
                        "</tr>"
                    )
                }

                $('button[name="changePost"]').click(function () {
                    var department = $(this).parent().parent().children().eq(5).text()
                    $('#postChange').attr("style", "display:block")
                    // alert("department :"+department)
                    $(document).ready(function () {
                        $('button[name="postCancel"]').click(function () {
                            alert(1)
                            $('#postChange').attr("style", "display:none")
                        })
                    })
                    $.get("/company/getPost/", {"department": department}, function (e) {
                        // todo 2021.1.5
                        // alert(data[0].postName)
                        var JSONe = JSON.parse(e)
                        // alert(typeof e)
                        $("#postSele").empty()
                        for (var i = 0; i < JSONe.length; i++) {


                            $("#postSele").append(
                                "<option>" + JSONe[0].postName + "</option>"
                            )
                        }
                        // alert(data)
                    })


                })

            },
            "json"//
        )


    });

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
        //招聘
        showOption($(".recruitment"))


    })


    $("button[name='dep']").click(function () {

        // 部门管理
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