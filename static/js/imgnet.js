var Imgnet = {
    init: function () {
        var _this = this;

        $("#ImgA").click(function () {
            $("#showImg").hide()
            $("#fileneme").hide()
            _this.imgA(this)
        });


    },
    imgA: function () {
        var name = "图像被识别为:"
        $.ajax({
            url: '/D3js/imgA/',
            type: 'POST',
            error: function () {
                alert('error')
            },
            success: function (result) {
                // alert(result.res)
                document.getElementById('res').innerHTML = name + result.res

            },
        });
    },

}

$(function(){
   Imgnet.init();
});