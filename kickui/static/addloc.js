function addDot(data) {
    for (var i = 0; i < data.length; i++){
        var div = document.createElement('div')

        if (data[i][4] === 'T') div.className = 'dots'
        else div.className = 'boxs'

        div.style.left = data[i][1] + 'px'
        div.style.top = data[i][2] + 'px'

        // color setting
        if (data[i][3] > 75)  div.style.border = '5px solid #61D801'
        else if (data[i][3] > 50) div.style.border = '5px solid #FD9A18'
        else if (data[i][3] > 25) div.style.border = '5px solid #FDEA0B'
        else div.style.border = '5px solid #FF0301'

        document.getElementById('map').appendChild(div)
    }
}