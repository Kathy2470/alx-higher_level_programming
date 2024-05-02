$(document).ready(function() {
    // Perform an AJAX request to fetch the character data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        type: 'GET',
        success: function(data) {
            // Update the text of the <div> element with id 'character' with the character name
            $('#character').text(data.name);
        },
        error: function() {
            // Handle error if the request fails
            $('#character').text('Error fetching character data');
        }
    });
});
