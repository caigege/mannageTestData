$(document).ready(function () {
    $("#createBuniness").click(function () {
        showOption($("#createTable"))


    })
    /**
     *获取员工
     */
    $("select[name='selectPost']").change(function () {
        var postName = $(this).val()
        // console.log("selectPost 获取员工"+s)
        $.get("/business/empGet/",{"postName":postName},function (data) {
            console.log("selectPost 获取员工",data)
            var empList=JSON.parse(data)
            for(var a=0;a<empList.length;a++)
            $("select[name='selectPost']").append(

            )






        },"json")
    })

    /**
     * 处理json数组 关联多个元素的值,
     * @param data
     * @param objK 匹配的对象K
     * @param objV  匹配的对象V
     * @param bcObjK 目标K
     */
    function getSelect(data, objK, objV, bcObj) {
        var reslt = eval("function f() {for (da in data) {" +
            "if (data[da]." + objK + "==\'" + objV + "\') { return data[da]." + bcObj + "}}};f()")
        console.log("reslt" + reslt)
        return reslt

    }

    $("select[name='selectDep']").change(function () {
        var selectDepData = $(this).data()
        var selected = $(this).find("option:selected").text()
        var selec = getSelect(selectDepData, "name", selected, "postName")
        // console.log("selec", typeof selec)
        if (selec == "暂无") {
            //    todo 跳转到添加岗位页面
            alert("添加岗位")
            return
        } else {
            var posts = selec.split(",")
            $("select[name='selectPost']").empty()
            $("select[name='selectPost']").append(
                " <option class=\"selectPostOption\"  selected=\"true\" disabled>-- 请选择 --</option>"
            )
            for (var j = 0; j < posts.length; j++) {
                $("select[name='selectPost']").append(
                    "<option class=\"selectPostOption\" value=" + posts[j] + " >" + posts[j].split("*")[1] + "</option>"
                )
            }
        }

    })


    /**
     * 分解任务
     */
    $("#resolve").click(function () {

        showOption($("#createTaskDiv"))

        // alert( $("span[name='projectName']").text())

        $("#createTaskDiv").find("input").first().attr("value", $("span[name='projectName']").text())
        // 查询部门信息
        $.get("/company/getDep/", function (data) {

            $("select[name='selectDep']").data(data)

            console.log($("select[name='selectDep']").data())
            $("select[name='selectDep']").append(
                " <option class=\"selectDepOption\" value=" + i + " selected=\"true\" disabled>-- 请选择 --</option>"
            )
            for (var i = 0; i < data.length; i++) {
                $("select[name='selectDep']").append(
                    " <option class=\"selectDepOption\" value=" + i + " >" + data[i].name + "</option>"
                )
            }
        }, "json")

    })

    function f() {
        var sty = this.css("background-color")
        console.log(sty)

    }

    function showOption(e) {
        //展示对应的列表 隐藏其他列表
        var eles = [$("#createTable"), $("#createTaskDiv"), $("#detail")]
        for (ele in eles) {
            eles[ele].attr("style", "display:none;")
        }
        e.attr("style", "display:block;")
    }

// $("select[name='strategy']").find("option :selected").mouseover(function () {
//     var sty = $(this).css("background-color")
//         console.log(sty)
// })

//


    $(".strategyOption").click(function () {
        var sty = $(this).css("background-color")
        // var sty = $(this).val()
        console.log(sty)
    })

    $("select[name='strategy']").change(function () {
        // console.log( $(this).find("option:selected").text())
        // console.log( $(this).find("option:selected").css("background-color"))
        var bc = $(this).find("option:selected").css("background-color")

        // console.log( $(this).find("option:selected").css("color"))
        col = $(this).find("option:selected").css("color")
        $(this).css({"background-color": bc, "color": col})


    })


})
