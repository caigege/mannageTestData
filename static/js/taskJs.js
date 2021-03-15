// $(document).ready(function () {

$(document).ready(function () {
    function DateToStr(date) {
        let Y = date.getFullYear()
        let M = date.getMonth() + 1
        let D = date.getDay()
        let hh = date.getHours()
        let mm = date.getMinutes()
        let ss = date.getSeconds()
        return Y + "-" + M + "-" + D + " " + hh + ":" + mm + ":" + ss
    }

    $("#taskVerify tbody").on("click", "button[name='sava']", function () {
        console.log("111")
        // 方案选择
        var selec = $(this).parent().parent().find("select option:selected").attr("value");
        console.log("button[name='save'] ;" + selec)
        // 时间计算
        // TODO 工作时间为详细处理
        //id

        var taskId = $("button[name='sava']").parent().parent().find("td").eq(0).attr("id")
        console.log("taskId：" + taskId)
        //工作开始时间
        var workStartTime = $("button[name='sava']").parent().parent().find("td").eq(3).text()
        //工作时长
        var workTimeStr = $("button[name='sava']").parent().parent().find("td").eq(4).text().split("小时")[0]
        //结束时间
        let finshiTime = new Date(workStartTime)
        let finshiTimeWF = finshiTime.setHours(finshiTime.getHours() + parseInt(workTimeStr))
        finshiTime.setMinutes(finshiTime.getMinutes() + 30)


        switch (selec) {

            case "1" :
                //todo finshiTime >= new Date()  测试用调试
                if (finshiTime >= new Date()) {
                    alert("任务已超时,若要继续 请选择加急")
                    return
                } else {
                    // todo请求任务绩效执行,单个任务失败次数记录1次

                }
                break;
            case "2" :
                if (finshiTime <= new Date()) {
                    //  继续完成  超时 todo 2021118
                    var timeIns = prompt("输入加急时间，最低1小时，填写整数")
                    if (timeIns) {
                        console.log(Math.ceil(timeIns))
                        var timeIn = Math.ceil(timeIns)
                        console.log(typeof timeIn)
                        if (!(timeIn < 1 || timeIn > 8) && typeof timeIn === "number") {
                            //请求 todo
                            $(this).parent().parent().remove()
                        } else {
                            alert("时间为1-8小时")
                            return
                        }
                    } else if (timeIns === "") {
                        alert("请输入时间")
                        return
                    } else {
                        //    取消
                        return
                    }
                } else {
                    //  继续完成  未超时
                    alert("未超时，请选择继续（暂不支持预计超时）")
                    return
                }
                break;
            case "3" :
                //延期执行
                if (finshiTime > new Date()) {
                    //todo延期执行，包括其子任务
                    //  继续完成  未超时
                    alert("未超时，请选择继续（暂不支持预计超时）")
                    return
                }
                break;
            case 4 :
                //废除(终止任务）
                if (finshiTime > new Date()) {
                    //todo请求终止任务 包括其子任务
                    //  继续完成  未超时
                    alert("未超时，请选择继续（暂不支持预计超时）")
                    return
                }
                break;

            case 5 :
                //回收再发布
                if (finshiTime > new Date()) {
                    //  继续完成  未超时
                    alert("未超时，请选择继续（暂不支持预计超时）")
                    return
                }
                //todo终止任务包括子任务
                break;
            case 6 :
                //暂停，项目封闭(包括其子任务）
                break;

        }
        timeIns
        $.post("/task/taskVerifyResult/", {
            "finshiTime": finshiTime.getTime(),
            "taskId": taskId,
            "selec": selec,
            "finshiTimeWF": finshiTimeWF,
            "workTime": timeIns
        }, function (postdata) {
            var JSONpostdata = JSON.parse(postdata)
            if (JSONpostdata.result == "erro") {
                alert(JSONpostdata.content)
            }

                window.location.reload()


            // alert(JSONpostdata.message)
            // $(this).parent().parent().remove()


        })
    })

})