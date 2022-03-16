var testJson = {
    "length": "2",
    "results": [
        {
            "len": "2",
            "user": "admin",
            "src": "test.jpg",
            "result": [
                {
                    "class": "zhang_wu",
                    "score": "0.999",
                    "max_x": "1",
                    "min_x": "2",
                    "max_y": "3",
                    "min_y": "4"
                },
                {
                    "class": "zhang_wu",
                    "score": "0.999",
                    "max_x": "1",
                    "min_x": "2",
                    "max_y": "3",
                    "min_y": "4"
                }
            ]
        },
        {
            "len": "2",
            "user": "admin",
            "src": "test.jpg",
            "result": [
                {
                    "class": "zhang_wu",
                    "score": "0.999",
                    "max_x": "1",
                    "min_x": "2",
                    "max_y": "3",
                    "min_y": "4"
                },
                {
                    "class": "zhang_wu",
                    "score": "0.999",
                    "max_x": "1",
                    "min_x": "2",
                    "max_y": "3",
                    "min_y": "4"
                }
            ]
        }
    ]
}

function getResultTab(obj) {
    reTabInner = '<h4 class="tittle-w3-agileits mb-4">Result</h4>';
    console.log(obj)
    for (let i in obj.results) {
        var num = parseInt(i) + 1;
        var colid = 'collapse' + num;
        reTabInner += '<div class="reWrapper container-fluid"><div><div class="inline-box">' +
        '<img src="' + obj.results[i]["src"] + '" style="height: 120px; width: 160px;" class="reimg"></div>' + 
        '<div class="inline-box reTabWrapper"><table class="table reTab"><tbody><tr class="tabFirstLine">' +
        '<th>No.</th>' + '<td class="text-center">' + num + '</td></tr>' +
        '<tr><th>Num</th>' + '<td class="text-center">' + obj.results[i]["len"] + '</td></tr>' +
        '<tr class="tabLastLine"><th>User</th><td class="text-center">' + obj.results[i]["user"] + '</td></tr></tbody></table></div>' +
        '<div class="text-center"><a data-toggle="collapse" href="' + '#' + colid + '">details</a></div></div>' +
        '<div id="' + colid + '" class="panel-collapse collapse">';
        
        var reNum = parseInt(obj.results[i].len) - 1;
        for(let j in obj.results[i].result) {
            reTabInner += '<div class="detailTab"><div style="border-bottom: 1px solid #d8d8d8;" class="deTabReWarp row';
            reTabInner += j == 0? ' top-border-radius">': '">';
            reTabInner += '<div class="col text-center" >坐标:</div><div class="col text-center" >' +
            '(' + obj.results[i].result[j]["min_x"] + ',' + obj.results[i].result[j]["min_y"] + '),' + '(' + obj.results[i].result[j]["max_x"] + ',' + obj.results[i].result[j]["max_y"] + ')' +'</div></div>';
            reTabInner += j == reNum? '<div class="deTabReWarp row bottom-botder-radius">': '<div class="deTabReWarp row">';
            reTabInner += '<div class="col text-center">种类:</div>' + 
            '<div class="col text-center">' + obj.results[i].result[j]["class"] + '</div></div></div>';
        }
        reTabInner += '</div></div>';
    }
    document.getElementById('resultTable').innerHTML = reTabInner;
}

window.onload = function () {
    returnTab = $.ajax({
        url: '/charts',
        type: 'POST',
        async: false,
        data: "",
        processData: false,
        success: function (data) {
            alert("upload success");
        },
        error: function (data) {
            alert("upload failed");
        }
    });
    getResultTab(returnTab.responseJSON);
}