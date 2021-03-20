$(document).ready(function () {
    function checkShow(ele) {
        var eles = [$("#editUserInfoDiv"), $("#taskInfoDiv"), $("#messageDiv")]
        for (e in eles) {
            eles[e].attr("style", "display:none;")
        }
        ele.attr("style", "display:block;")

    }

    $("#taskInfo").click(function () {
        checkShow($("#taskInfoDiv"))
    })

    $("#editUserInfo").click(function () {
        checkShow($("#editUserInfoDiv"))
    })

    $("#message").click(function () {
        checkShow($("#messageDiv"))
    })

    $("#task_verify").click(function () {
        self.location = "/task/taskVerify/"
    })
    /**
     * 确认任务
     */
    $('#taskInfoDiv tbody').on("click", "button[name='taskSure']", function () {
        var data = $(this).parent().parent().data("data")
        console.log(data)
        $.post("/task/sureTask/", {"data": data}, function (e) {

        })
        getTaskInof()
    })

    $('button[id="postCancel"]').click(function () {
        //取消
        $('#postChange_user').attr("style", "display:none")
        return
    })

    // $("#postSave").click(function () {
    //     // 保存
    //     // var postnanme = department_global + "*" + $("#postSele option:selected").val()
    //     //
    //     // // 员工修改岗位
    //     // $.post("/company/updatePost/", {"phone": phone_global, "postnanme": postnanme}, function (postdata) {
    //     //     var JSONpostdata = JSON.parse(postdata)
    //     //     alert(JSONpostdata.message)
    //     //
    //     //     $.get(
    //     //         "/company/empGet/",
    //     //         function (data, status) {
    //     //             //知识点 js 对象类型
    //     //             // console.log("data type", typeof data)
    //     //
    //     //             var JSONdata = JSON.parse(data)
    //     //             showEmpthis(JSONdata);
    //     //             // $("#postSave").remove()
    //     //             $('#postChange').attr("style", "display:none")
    //     //
    //     //         })
    //     //
    //     // })
    //     // return
    // })
    /**
     * 分解任务
     */
    $('#taskInfoDiv tbody').on("click", "button[name='taskGoResolvej']", function () {
        var data = $(this).parent().parent().data("data")
        console.log(data)
        console.log(data.split("*"), typeof data.split("*"))

        //获取id 下个任务的 upTaskId
        var task_upTaskId = data.split("*")[0]
        $("input[name='upTaskId']").attr("value", task_upTaskId)
        var task_projectId = data.split("*")[2]
        $("input[name='projectName']").attr("value", task_projectId)

        //获取项目id
        //projectName
        //
        //


        $('#postChange_user').attr("style", "display:block")
        // $("#postSele").append(
        //
        //     "<option>" + 1 + "</option>"
        // )
        $.post("/task/secondTaskResolvej/", {"data": data}, function (e) {

        })
        // getTaskInof()
    })

    /**
     * 获取任务 刷新任务列表
     */

    function getTaskInof() {
        $.get("/task/getUser/", function (ee) {
            console.log(ee, typeof ee)
            var dataEe = JSON.parse(ee)
            $("#taskInfoDiv tbody").empty()

            for (dataNum in dataEe) {
                var dataE = dataEe[dataNum]
                var dataEF = dataE.fields
                var strategy = ""
                var taskLevel = ""
                var stataTd = ""
                switch (dataEF.state) {

                    case 0:
                        stataTd = '<button class="taskSure" name="taskSure">任务确认</button>'
                        break;

                    case 1:
                        stataTd = '执行中\n' +
                            '\n' +
                            '                        <button name="submitTaskCheck">执行完成</button>'
                        if (dataEF.strategy == 1 || dataEF.strategy == 2) {
                            //todo 调整未处理
                            stataTd += "<button class='orderBtn'>调整执行顺序</button>"
                        }
                        if (dataEF.taskLevel == 1) {
                            stataTd += '<button class="taskGoResolvej" name="taskGoResolvej">继续分解任务</button>'
                        }
                        break;

                    case 2:
                        stataTd = '<span style="color:yellow;background-color: rgba(79,102,206,0.87)">执行完成 ,验收中</span>'
                        break;

                    case 3:
                        stataTd = '<span style="background-color:chartreuse">验收后,提前完成</span>'
                        break;

                    case 4:
                        stataTd = '<span style="background-color:chartreuse">验收后,顺利完成(计划时间 前10分钟 后20分钟内）</span>'
                        break;

                    case 5:
                        stataTd = '<span style="background-color:chartreuse"> 验收后,超时完成(计划时间20分钟后）</span>'
                        break;

                }

                if (dataEF.taskLevel == 1) {
                    taskLevel = "需再分解"
                } else if (dataEF.taskLevel == 2) {
                    taskLevel = "可执行"
                }
                switch (dataEF.strategy) {
                    case 1:
                        strategy = '<td style="background-color: white;color:black; ">普通按开始时间排序</td>'
                        break;

                    case 2:
                        strategy = '<td style="background-color: orange;color:black; ">执行者自行调整执行顺序</td>'
                        break;

                    case 3:
                        strategy = '<td style="background-color: blue;color:white; ">1级管理者安排</td>'
                        break;

                    case 4:
                        strategy = '<td style="background-color: darkviolet;color:white; ">管理级安排</td>'
                        break;

                    case 5:
                        strategy = '<td style="background-color: red;color:black; ">紧急</td>'
                        break;

                }


                $("#taskInfoDiv tbody").append(
                    "<tr data-data='" + dataE.pk + "*" + dataEF.taskCreater + "'>" +
                    "<td>" + dataNum + "</td>" +
                    "<td>" + dataEF.taskName + "</td>" +
                    "<td>" + dataEF.content + "</td>" +
                    "<td>" + dataEF.startTime + "</td>" +
                    "<td>" + dataEF.taskTime + "小时</td>" +
                    strategy +
                    "<td>" + taskLevel + "</td>" +
                    "<td>" + dataEF.selectPost + "</td>" +
                    "<td>" + dataEF.selectEmp + "</td>" +
                    "<td>" + stataTd + "</td>" +

                    "</tr>"
                )
            }
        })
    }

    /**
     * 处理完成任务提交
     */
    $('#taskInfoDiv tbody').on("click", "button[name='submitTaskCheck']", function () {
        var data = $(this).parent().parent().data("data")

        $.get("/task/taskFinshiSubmit", {"data": data}, function (e) {
            console.log(e)
            getTaskInof();
        })
    })

    // $(function () {
    //     $("button[name='submitTaskCheck']").click(function () {
    //
    //     })
    // })
})