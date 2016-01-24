$(function () {

    var houseHold = [];
    var chores = [];

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
            color: '#CC495D',
            drilldown: {
                name: categories[0] + ' chores',
                userChores: categories[0].chores,
                categories: {
                    formatter: function () {
                        return userChores < 1 ? ['None'] : userChores;
                    }
                },
                color: colors[0],
                categories: ['Trash', 'Dishes'],
                data: [ 10, 10],
            }
        }, {
            y: 20,
            color: '#ED9477',
            drilldown: {
                name: categories[1] + ' chores',
                categories: ['None'],
                data: [20],
            }
        }, {
            y: 20,
            color: '#EDED72',
            drilldown: {
                name: categories[2] + ' chores',
                categories: ['Dusting', 'Sweeping'
                ],
                data: [10, 10],
            }
        }, {
            y: 20,
            color: '#6EDB7E',
            drilldown: {
                name: categories[3] + ' chores',
                categories: ['Bathroom'],
                data: [20],
            }
        }, {
            y: 20,
            color: '#64B5ED',
            drilldown: {
                name: categories[4] + ' chores',
                categories: ['Kitchen'],
                data: [20],
            }
        }, {
            y: 20,
            color: '#A489F0',
            drilldown: {
                name: categories[5] + ' chores',
                categories: ['Groceries'],
                data: [20],
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
            brightness = 0.25;
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
            backgroundColor: '#D4FFF7'
        },
        title: {
            text: 'Frosh House',
            style: {
                fontSize: '35px'
            }
        },
        exporting: { enabled: false },
        credits: { enabled: false },
        plotOptions: {
            series: {
                states: {
                    hover: {
                        enabled: false
                    }
                }
            }
        },
        tooltip: {
            enabled:false,
        },
        series: [{
            name: 'Browsers',
            data: browserData,
            size: '80%',
            dataLabels: {
                formatter: function () {
                    return this.y > 5 ? this.point.name : null;
                },
                color: '#000000',
                style: {
                    textShadow: false,
                    fontSize: '16px'
                },
                distance: -125
            }
        }, {
            name: 'Versions',
            data: versionsData,
            size: '100%',
            innerSize: '80%',
            dataLabels: {
                formatter: function () {
                    // display only if larger than 1
                    return this.y > 1 ? '<b>' + this.point.name: null;
                },
                color: '#000000',
                style: {
                    textShadow: false, 
                    fontSize: '14px'
                },
                distance: -28
            }
        }]
    });
});
