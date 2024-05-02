$(document).ready(function() {
    // Perform an AJAX request to fetch the translation
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            // Display the translation in the <div> element with id 'hello'
            $('#hello').text(data.hello);
        },
        error: function() {
            // Handle error if the request fails
            $('#hello').text('Error fetching translation');
        }
    });
});
