var aguacate = {
    x: [1, 2, 3, 4],
    y: [10, 9, 13, 17],
    type: 'scatter'
};

var trace2 = {
    x: [1, 2, 3, 4],
    y: [18, 5, 12, 9],
    type: 'scatter'
};

var data = [aguacate, trace2];

Plotly.newPlot('myDiv', data);