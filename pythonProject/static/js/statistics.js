var chart = "";
var flag = 0;

function firstRender() {
    update(myData1, myData2, myData3)
}

window.onload = firstRender;

async function getData(text) {
    var data = fetch('/data/' + text, {
        method: "POST",
        credentials: "include",
        headers: new Headers({
            "content-type": "application/json"
        })
    })
        .then(response => response.json())
        .then(data => console.log(data));

    var p = Promise.resolve(fetch('/data/' + text, {
        method: "POST",
        credentials: "include",
        headers: new Headers({
            "content-type": "application/json"
        })
    }).then(response => response.json()));
    p.then(function (v) {
        update(v[0], v[1], v[2]); // 1
    });
}


function update(xis, yis, text) {
    var riceData = {
        labels: xis,
        datasets:
            [
                {
                    label: text,
                    strokeColor: "#ACC26D",
                    pointColor: "#fff",
                    pointStrokeColor: "#9DB86D",
                    data: yis,
                    backgroundColor: 'rgba(255,80,0, 1)'
                }
            ]
    }
    let options = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    };
    if (flag === 1) {
        chart.destroy();
    } else {
        flag = 1;
    }
    chart = new Chart(rice, {
        type: 'bar',
        data: riceData, options: options
    });
}

