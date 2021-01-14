// $(document).ready(function () {

$(document).ready(function () {
    // $("#taskVerify tbody").on("click", "button[name='save']", function () {
    //     alert(1)
    //     var selec = $(this).parent().parent().find("option :selected").val();
    //     console.log("button[name='save'] ;" + selec)
    // })
    // $("button[name='save']").click(function () {
    // alert(2)
    // console.log($("button [name='save']").val())
    if($("button [name='save']")){
        console.log("存在")
    }else{
        console.log("不存在")
    }

    if($("#save")){
        console.log("存在")
    }else{
        console.log("不存在")
    }

    $("#save").click(function () {
        alert(1)
        // console.log($("button [name='save']"))
        // alert(1)
        // var selec = $(this).parent().parent().find("option :selected").val();
        // console.log("button[name='save'] ;" + selec)
    })
    // $("#projectTbody").on("click","button[name='projectDetails']",function () {
// alert(3)
})