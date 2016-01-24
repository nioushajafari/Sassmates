$(function () {

    var houseHold = [];

    $.ajax({
        url: "/household",
        async: false,
    }).done(function(result) {
       houseHold = JSON.parse(result);

    });

    var colors = Highcharts.getOptions().colors,
        categories = houseHold.people,

        //categories = ['Jaclyn', 'NJ', 'Adrian', 'Jess', 'Spencer', 'Taylor'],
        data = [{
            y: 20,
            color: colors[0],
            drilldown: {
                name: categories[0] + ' chores',
                categories: ['Trash', 'Dishes'],
                data: [10, 10],
                color: colors[0]
            }
        }, {
            y: 20,
            color: colors[1],
            drilldown: {
                name: 'NJ chores',
                categories: ['None'],
                data: [20],
                color: colors[1]
            }
        }, {
            y: 20,
            color: colors[2],
            drilldown: {
                name: 'Adrian chores',
                categories: ['Dusting', 'Sweeping'
                ],
                data: [10, 10],
                color: colors[2]
            }
        }, {
            y: 20,
            color: colors[3],
            drilldown: {
                name: 'Jess chores',
                categories: ['Bathroom'],
                data: [20],
                color: colors[3]
            }
        }, {
            y: 20,
            color: colors[5],
            drilldown: {
                name: 'Spencer chores',
                categories: ['Kitchen'],
                data: [20],
                color: colors[3]
            }
        }, {
            y: 20,
            color: colors[4],
            drilldown: {
                name: 'Taylor chores',
                categories: ['Groceries'],
                data: [20],
                color: colors[4]
            }
        }],
        browserData = [],
        versionsData = [],
        i,
        j,
        dataLen = data.length,
        drillDataLen,
        brightness;


    // Build the data arrays
    for (i = 0; i < dataLen; i += 1) {

        // add browser data
        browserData.push({
            name: categories[i],
            y: data[i].y,
            color: data[i].color
        });

        // add version data
        drillDataLen = data[i].drilldown.data.length;
        for (j = 0; j < drillDataLen; j += 1) {
            brightness = 0.2 - (j / drillDataLen) / 5;
            versionsData.push({
                name: data[i].drilldown.categories[j],
                y: data[i].drilldown.data[j],
                color: Highcharts.Color(data[i].color).brighten(brightness).get()
            });
        }
    }

    // Create the chart
    $('#container').highcharts({
        chart: {
            type: 'pie',
            backgroundColor: '#DEFFF9'
        },
        title: {
            text: 'Frosh House'
        },
        plotOptions: {
            pie: {
                shadow: false,
                center: ['50%', '50%']
            }
        },
        tooltip: {
            valueSuffix: '%'
        },
        series: [{
            name: 'Browsers',
            data: browserData,
            size: '60%',
            dataLabels: {
                formatter: function () {
                    return this.y > 5 ? this.point.name : null;
                },
                color: '#ffffff',
                distance: -30
            }
        }, {
            name: 'Versions',
            data: versionsData,
            size: '80%',
            innerSize: '60%',
            dataLabels: {
                formatter: function () {
                    // display only if larger than 1
                    return this.y > 1 ? '<b>' + this.point.name: null;
                }
            }
        }]
    });
});
