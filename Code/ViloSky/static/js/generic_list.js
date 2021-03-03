$(".entry-row").click(function(e){
    if(e.currentTarget){
        const to = e.currentTarget.getAttribute('to');
        if(to){
            window.location.href = to;
        }    
    }
});