$(document).ready(function(){
    function toggleViews() {
        $("#viewProducts").toggle();
        $("#addProductForm").toggle();
    }

    $("#viewProducts").show();
    $("#addProductForm").hide();

    $("#addProductBtn").click(function(){
        toggleViews();
    });

    $("#viewInventoryBtn").click(function(){
        toggleViews();
    });
});