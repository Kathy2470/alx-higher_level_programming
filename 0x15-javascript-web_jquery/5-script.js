$(document).ready(function() {
    // Add a click event listener to the div with id 'add_item'
    $('#add_item').click(function() {
        // Create a new <li> element with text "Item"
        var newItem = $('<li>Item</li>');

        // Append the new <li> element to the <ul> element with class 'my_list'
        $('.my_list').append(newItem);
    });
});
