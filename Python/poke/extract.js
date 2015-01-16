// used to extract list of pokemon with their types from here:
// http://pokemondb.net/pokedex/national

var a = $(".infocard-tall");

for (var i = 0; i < a.length; i ++)
{
    var rep = a[i].getElementsByClassName("ent-name")[0].innerHTML;

    var b = a[i].getElementsByClassName("aside")[0].getElementsByTagName("a");

    for(var j = 0; j < b.length; j ++)
    {
        rep += " " + b[j].innerHTML;
    }
    
    console.log(rep);
}