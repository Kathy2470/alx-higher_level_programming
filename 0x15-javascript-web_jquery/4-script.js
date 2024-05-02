$(document).ready(function() {
    // Add a click event listener to the div with id 'toggle_header'
    $('#toggle_header').click(function() {
        // Toggle the classes 'red' and 'green' on the <header> element
        $('header').toggleClass('red green');
    });
});
