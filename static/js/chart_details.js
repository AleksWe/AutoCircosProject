$(document).ready(function() {
    $('#generate').click(function() {
        // Get the number of radio button groups from the user input
        let num = parseInt($('#numRadioGroups').val());

        // Clear previous content
        $('#radioContainer').empty();

        // Define the options
        const options = ["scatter", "bar", "line"];

        // Generate the radio button groups
        for (let i = 1; i <= num; i++) {
            let group = $('<div>').addClass('radio-group');
            group.append(`<span class="group-label">Chart ${i}: </span>`);
            for (let j = 0; j < options.length; j++) {
                group.append(`
                    <label>
                        <input type="radio" name="chart${i}" value="${options[j]}"> ${options[j]}
                    </label>
                `);
            }
            $('#radioContainer').append(group);
        }
    });
});