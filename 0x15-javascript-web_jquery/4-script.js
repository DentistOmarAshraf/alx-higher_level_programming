$('DIV#toggle_header').click(()=>{
	x = $('header')
	if (x.hasClass('green')){
		x.removeClass('green')
		x.addClass('red')
	}else{
		x.removeClass('red')
		x.addClass('green')
	}
	
})
