$(document).ready(function () {
    $(function () {
        $("#createProjectForm").ajaxForm(function (dataJson) {
            console.log(dataJson, typeof dataJson)
            if (dataJson["success"] != undefined) {
                window.location.reload()
            } else {
                alert(dataJson.erro)
            }
        })
    })

    $(function () {

        $("#createTaskDiv").ajaxForm(function (data) {
            console.log(data, typeof data)
            var dataJson = JSON.parse(data)
            // if()
            if (dataJson["success"] != undefined) {
                window.location.reload()

            } else {
                alert(dataJson.erro)

            }

            alert(dataJson.getKey())
        });


    });

    /**
     *
     * @param ele
     * @returns {jQuery}
     */
    function checkSelect(ele, hint) {
        var Num = ele.find("option:selected").val()
        if (judge(Num)) {
            var result = ele.find("option:selected").text()
        } else {
            alert(hint + "未选择")
            return false
        }
        return result;
    }

    var Tasks = {}
    $("input[name='createTaskSubmit']").mouseenter(function () {
        // alert(2)
        // console.log($("input[name='nowOrNot']").prop("checked"))
        var nowDate = new Date
        // var nowDated = new Date(nowDate)
        var startDate = new Date($("#start").val())
        if ($("input[name='nowOrNot']").prop("checked")) {
            //    勾选
            // alert("勾选")

            // if(nowDate-startDate)
        } else {
            // 未勾选
            //  alert("未勾选")
            if (nowDate - startDate > 3 * 60 * 1000) {
                alert("马上开始：开始时间超过设置，重新设置时间")
                return
            }
        }


        var projectName = $("#createTaskDiv").find("input").first().attr("value")
        Tasks["projectName"] = projectName

        var taskName = $("#createTaskDiv").find("input:eq(1)").val()
        // console.log(taskName, typeof taskName)
        if ($.trim(taskName).length == 0) {
            alert("任务名不能为空")
            Tasks = {}
            return
        }
        Tasks["taskName"] = taskName


        var content = $("#createTaskDiv").find("textarea").val()
        if ($.trim(content).length == 0) {
            alert("内容不能为空")
            Tasks = {}
            return
        }
        Tasks["content"] = content


        var workTime = $("#createTaskDiv").find("input:eq(2)").val()
        if ($.trim(workTime) == 0) {
            alert("时间不能为空")
            Tasks = {}
            return
        } else if (workTime < 0 || workTime>8) {
            alert("时间不能小于0,时间不能大于8")
            Tasks = {}

            return
        }
        Tasks["workTime"] = workTime


        var strategy = checkSelect($("select[name='strategy']"), "任务策略");
        if (!strategy) {
            Tasks = {}
            return
        }
        Tasks["strategy"] = strategy


        var taskLevel = checkSelect($("select[name='taskLevel']"), "任务级别");
        if (!taskLevel) {
            Tasks = {}
            return
        }
        Tasks["taskLevel"] = taskLevel


        var selectDep = checkSelect($("select[name='selectDep']"), "部门");
        if (!selectDep) {
            Tasks = {}
            return
        }
        Tasks["selectDep"] = selectDep


        var selectPost = checkSelect($("select[name='selectPost']"), "岗位");
        if (!selectPost) {
            Tasks = {}
            return
        }
        Tasks["selectPost"] = selectPost


        var selectEmp = checkSelect($("select[name='selectEmp']"), "任务指派");
        if (!selectEmp) {
            Tasks = {}
            return
        }
        Tasks["selectEmp"] = selectEmp


    })

    function judge(num) {

        // alert(1)
        if (num == -1) {
            return false
        }
        return true

    }


    $("#createBuniness").click(function () {
        showOption($("#createTable"))


    })
    /**
     *获取员工
     */
    $("select[name='selectPost']").change(function () {
        var postName = $(this).val()
        // console.log("selectPost 获取员工"+s)
        $.get("/business/empGet/", {"postName": postName}, function (data) {
            console.log("selectPost 获取员工", data)
            var empList = JSON.parse(data)
            $("select[name='selectEmp']").empty()
            $("select[name='selectEmp']").append(
                " <option class=\"selectEmpOption\"  selected=\"true\"  value=\"-1\" disabled>-- 请选择 --</option>"
            )
            for (var a = 0; a < empList.length; a++) {
                $("select[name='selectEmp']").append(
                    "<option class=\"selectEmpOption\" value=" + empList[a].phone + " >" + empList[a].name + "</option>"
                )
            }

        }, "json")
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
                " <option class=\"selectPostOption\"  selected=\"true\" value=\"-1\" disabled>-- 请选择 --</option>"
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
        // function(){


        setTimeout(function () {
            var time = new Date()
            var second = "00"
            // var second = time.getSeconds()
            var min = time.getMinutes()
            if (min < 10) {
                min = "0" + min
            }
            var hour = time.getHours()
            if (hour < 10) {
                hour = "0" + hour
            }
            var ti = hour + ":" + min + ":" + second
            console.log("ti:" + ti)
            var day = ('0' + time.getDate()).slice(-2)
            var month = ('0' + (time.getMonth() + 1)).slice(-2)
            var today = time.getFullYear() + '-' + month + '-' + day + "T" + ti
            // $('#start').attr("value",today)
            console.log("today: " + today)
            $('#start').val(today)
        }, 100)
        // }
        // alert( $("span[name='projectName']").text())

        $("#createTaskDiv").find("input").first().attr("value", $("span[name='projectName']").text())
        // 查询部门信息
        $.get("/company/getDep/", function (data) {

            $("select[name='selectDep']").data(data)

            // console.log($("select[name='selectDep']").data())

            $("select[name='selectDep']").append(
                " <option class=\"selectDepOption\" value=-" + 1 + " selected=\"true\" disabled>-- 请选择 --</option>"
            )

            $("select[name='selectPost']").append(
                " <option class=\"selectPostOption\" value=-" + 1 + " selected=\"true\" disabled>-- 请选择 --</option>"
            )

            $("select[name='selectEmp']").append(
                " <option class=\"selectEmpOption\" value=-" + 1 + " selected=\"true\" disabled>-- 请选择 --</option>"
            )
            for (var i = 0; i < data.length; i++) {
                $("select[name='selectDep']").append(
                    " <option class=\"selectDepOption\" value=" + data[i].name + " >" + data[i].name + "</option>"
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
        // $("select[name='strategy']").find("option:selected").text()
        // console.log( $(this).find("option:selected").css("background-color"))
        var bc = $(this).find("option:selected").css("background-color")

        // console.log( $(this).find("option:selected").css("color"))
        col = $(this).find("option:selected").css("color")
        $(this).css({"background-color": bc, "color": col})


    })


})
