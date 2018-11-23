var WordCloud = {
    init: function () {
        var _this = this;
        $("#btn_download").click(function () {
            _this.download(this)
        });

        $("#btn_wordcloud").click(function () {
            _this.wordcloud(this)
        });

    },
    wordcloud: function () {
        var worddata = $("#words").val();
        var name = $("#name").val()
        var pic_src = '/static/wordcloud_pic/'+ name+'.png'
        $.ajax({
            url: '/D3js/generate/',
            type: 'GET',
            data : {'words':worddata,
                    'name': name},
            beforeSend: function () {
                if (name == ""){
                    alert('本云需要一个名字')
                }
            },
            error :function(){
                alert('error')
            },
            success: function () {
                 if (name !== ""){
                 document.getElementById('imgsrc').src = pic_src
                 }
            },
        });
    },
    download :function () {
        var name = $("#name").val()
        $.ajax({
            url: '/D3js/download/',
            type: 'GET',
            data : {'name': name},
            beforeSend: function () {
                alert('1')
            },
            error :function(){
                alert('error')
            },
        });

    },




}

$(function(){
   WordCloud.init();
});