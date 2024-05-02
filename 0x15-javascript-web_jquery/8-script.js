$(document).ready(function() {
    // Perform an AJAX request to fetch the movie data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        type: 'GET',
        success: function(data) {
            // Loop through each movie and append its title to the <ul> element with id 'list_movies'
            $.each(data.results, function(index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function() {
            // Handle error if the request fails
            $('#list_movies').append('<li>Error fetching movies data</li>');
        }
    });
});
