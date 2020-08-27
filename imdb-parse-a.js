// script fetches and parses the data for the first stage of processing, without merging anything
d3.tsv{"name.basics.tsv"), function(data) {
    for (var i = 0; i < data.length; i++) {
        console.log(data[1].titleId);
    }
});
    }
}

// display console output into the DOM for debug purposes - will mature into a progress bar as app proceeds


