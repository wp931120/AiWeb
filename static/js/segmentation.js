var Segmentation= {
    init: function () {
        var _this = this;
        $("#btn_download").click(function () {
            _this.download(this)
        });

        $("#btn_segmentation").click(function () {
            _this.segmentation(this)
        });

    },
    segmentation: function () {
        var sentance = $("#sentance").val();
        var stopwords = $("#stopwords").val();
        $.ajax({
            url: '/D3js/fenci/',
            type: 'POST',
            data : {'sen':sentance ,
                    'stop':stopwords , },
            error :function(){
                alert('error')
            },
            success: function (result) {
                // alert(result.segwords)
                document.getElementById('segword').innerHTML = result.segwords
            },
        });
    },





}

$(function(){
   Segmentation.init();
});