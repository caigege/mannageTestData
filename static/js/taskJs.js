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
        if (finshiTime < new Date()) {
            //  继续完成  超时 todo 2021118
            var timeIn = prompt("输入加急时间，最低1小时，填写整数")
            console.log(Math.ceil(timeIn))
            if (!(timeIn < 1 || timeIn > 8) && typeof timeIn === "number") {

            } else {
                alert("时间为1-8小时")
                return
            }
        } else {
            //  继续完成  未超时
            //     $.post("/task/workGoIn/")
        }

        $.post("/task/taskVerifyResult/", {"selec": selec}, function () {

        })
    })

})