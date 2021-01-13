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


})