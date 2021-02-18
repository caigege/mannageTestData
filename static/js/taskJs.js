// $(document).ready(function () {

$(document).ready(function () {
    $("#taskVerify tbody").on("click", "button[name='sava']", function () {
        // alert(1) $("#taskVerify tbody").parent().parent().find("td :eq(2)").val()
        var selec = $(this).parent().parent().find("select option:selected").attr("value");
        console.log("button[name='save'] ;" + selec)
        // 时间计算
        // TODO 工作时间为详细处理
        var finshiTimeStr = $("button[name='sava']").parent().parent().find("td").eq(3).text()
        var workTimeStr = $("button[name='sava']").parent().parent().find("td").eq(4).text().split("小时")[0]
        let finshiTime = new Date(finshiTimeStr)
        finshiTime.setHours(finshiTime.getHours() + parseInt(workTimeStr))
        finshiTime.setMinutes(finshiTime.getMinutes() + 30)
        switch (selec) {
            case "1" :
                if (finshiTime <= new Date()) {
                    alert("任务已超时,若要继续 请选择加急")
                    return
                }
                // else {
                    //todo请求任务绩效执行 单个任务失败次数记录1次
                // }
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
        $.post("/task/taskVerifyResult/", {"selec": selec}, function () {

        })
    })

})