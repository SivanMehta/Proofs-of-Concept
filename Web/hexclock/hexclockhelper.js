function changeTime()
{
    var date = new Date();

    var hours = (date.getHours() - 1) % 12 + 1;
    var minutes = date.getMinutes();
    var seconds = date.getSeconds();

    $("#clock").html(twodigits(hours) + ":" + twodigits(minutes) + ":" + twodigits(seconds));
    document.body.style.backgroundColor = "#" + twodigits(hours) + twodigits(minutes) + twodigits(seconds);
}

function start()
{
    changeTime();
    window.setInterval(changeTime, 100);
}

function twodigits(num)
{
    var number = num.toString();

    if(number.length == 1)
    {
        return "0" + number;
    }

    return number;
}