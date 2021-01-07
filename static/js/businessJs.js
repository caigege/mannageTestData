$(document).ready(function () {
    $("#createBuniness").click(function () {
        showOption($("#createTable"))


    })
    /**
     * 分解任务
     */
    $("#resolve").click(function () {

        showOption($("#createTaskDiv"))

        // alert( $("span[name='projectName']").text())
        $("#createTaskDiv").find("input").first().attr("value", $("span[name='projectName']").text())


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
    $("select[name='strategy']").change(function () {
        // console.log( $(this).text())
        // console.log( $(this).selectedIndex)
        // $(this).mouseover(function () {
        //     var sty = $(this).find("option :selected").css("background-color")
            var sty = $(this).find("option :selected").val()
            console.log(sty)
        // })

        // var sty = $(this).find("option :selected").css("background-color")
        // //
        // alert(sty)
        // var sty=$(this).find("option : selected").attr("value")
        // var sty=$(this).selectedIndex;
        // var obj = document.getElementsByName("strategy");
        // var index = obj.selectedIndex;
        //
        // var store_num = obj.options[index].getAttribute("style"); // 选中值
        //

        // $(this).attr("style",$(this).options[1].attr("style"))
    })


})
