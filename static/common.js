function watchTrailer(name,url){
    var html1 = '<iframe width="1165" height="545" src="'+url+'" frameborder="0" allowfullscreen></iframe>';
    $(document).ready(function(){
    $('<div />').html(html1).dialog({
      resizable: false,
      height: 600,
      title: name,
      width: 1200,
      modal: true,
      close: function(){$(this).remove();}
    });
    });
}

function createSeatArray() {
    var seats_per_row = 15;
    var seats = {'Platinum':2, 'Gold':2, 'Silver':6};
    var rows = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O'];
    var seat_array = "<div id='seat_array'>";
    var count = 0;
    for(var key in seats)
    {
        seat_array += "<table class='"+key+"'>";
        for(var i=0; i<seats[key]; i++)
        {
            seat_array += "<tr class='"+rows[count]+"'>";
            for(var j=1; j<=seats_per_row; j++)
            {
                seat_array += "<td><div class='"+key+"'><a>"+rows[count]+j+"</a></div></td>";
            }
            seat_array += "</tr>";
            count++;
        }
            seat_array += "</table>";
        }
        seat_array += "</div>";
    return seat_array;
}

$(document).ready(function(){

    //create seat array
    $('.seatArray').append(createSeatArray());

    //show available seats of particular type
    $('#id_seat_type').change(function(){
        seat_dict = {};
        $('#selected_seat').attr('value','');
        $('.selectable').removeClass('selectable selected');
        var selector = $(this).val();
        $('table.'+selector+' td div').addClass('selectable');
    });

    var seat_dict = {};

    //change color of selected seat
    $(document).on('click', 'div.selectable', function(){
        var curr_seat = $(this).text();
        if(curr_seat in seat_dict){
            delete seat_dict[curr_seat];
        }
        else{
            seat_dict[curr_seat] = curr_seat;
        }
        $(this).toggleClass('selected');
        var selected_seat = [];
        for(var key in seat_dict)
        {
            selected_seat.push(key);
        }
        $('input#selected_seat').attr('value',selected_seat);
        $('#no_of_seats').text(selected_seat.length);
    });
});