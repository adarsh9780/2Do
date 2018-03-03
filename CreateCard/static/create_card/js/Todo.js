jQuery(document).ready(function($){
	//open popup
	$('.cd-popup-trigger').on('click', function(event){
		event.preventDefault();
		$('.cd-popup').addClass('is-visible');
	});
	
	//close popup
	$('.cd-popup').on('click', function(event){
		if( $(event.target).is('.cd-popup-close') || $(event.target).is('.cd-popup') ) {
			event.preventDefault();
			$(this).removeClass('is-visible');
		}
	});
	//close popup when clicking the esc keyboard button
	$(document).keyup(function(event){
    	if(event.which=='27'){
    		$('.cd-popup').removeClass('is-visible');
	    }
    });
});

function incrementNum(){
	var parent = document.getElementById("container");
	var a = document.createElement("div");
	var b = document.createElement("div");
	a.className = "card";
	a.setAttribute("id", "hodor");
	b.className = "caption";
	a.appendChild(b);
	parent.appendChild(a);
	$('.cd-popup').removeClass('is-visible');
}