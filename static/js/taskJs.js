// $(document).ready(function () {

$(document).ready(function () {
    $("#taskVerify tbody").on("click", "button[name='sava']", function () {
        // alert(1)
        var selec = $(this).parent().parent().find("select option:selected").attr("value");
        console.log("button[name='save'] ;" + selec)
        $.post("/task/taskVerifyResult/",{"selec":selec},function () {

        })
    })

})