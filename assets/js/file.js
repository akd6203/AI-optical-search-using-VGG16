
function previewFile(input){
    var file = $("#image-file-btn").get(0).files[0];
    
    if(file){
        var reader = new FileReader();

        reader.onload = function(){
            alert("hii")
            $("#previewImg").attr("src", reader.result);
           
        }

        reader.readAsDataURL(file);
    }
}
