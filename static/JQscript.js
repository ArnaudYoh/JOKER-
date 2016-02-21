var getsuit = function(){					//Get the suit of the clicked card
	if(!$('.spade').hasClass('myhidden')){
		return "♠"
	} else if(!$('.club').hasClass('myhidden')){
		return "♣"
	} else if(!$('.heart').hasClass('myhidden')){
		return "♥"
	} else {
		return "♦"
	}; 
}

var getnumber = function(target){		//Get the number of the clicked card
	for(i = 2; i<11; i++){ 
		if(target.hasClass(i)){ 
			return i; 
		}
	}
	if (target.hasClass('A')){
		return "A"; 
	} else if ((target).hasClass('J')){
		return "J"; 
	} else if ((target).hasClass('Q')){
		return "Q"; 
	} else if ((target).hasClass('K')){
		return "K"; 
	}
}


var writecard = function(target) {			//Write the clicked card "value" in the text area
	var suit = getsuit(); 
	var card = getnumber(target); 
	console.log(card); 
	console.log(suit); 
	$('.myinput').val(function(_,val){
		return val + card + suit; 
	}); 
}



var main = function(){
	
	var spade = $('.spadebtn'); 
	var club = $('.clubbtn'); 
	var heart = $('.heartbtn'); 
	var diamond = $('.diamondbtn'); 
	var cardtable = $('.cardtable');
	
	spade.click(function(){
		if(!$('.spade').hasClass("myhidden")){
			return; 
		} else { 
			if(!$('.heart').hasClass("myhidden")){
				$('.heart').addClass("myhidden");  
			} else if(!$('.club').hasClass("myhidden")){
				$(".club").addClass("myhidden"); 
			} else {
				$(".diamond").addClass("myhidden");  
			}; 
			$('.spade').removeClass("myhidden");  
		}
	});
	
	club.click(function(){
		if(!$('.club').hasClass("myhidden")){
			return; 
		} else { 
			if(!$('.heart').hasClass("myhidden")){
				$('.heart').addClass("myhidden");  
			} else if(!$('.spade').hasClass("myhidden")){
				$(".spade").addClass("myhidden"); 
			} else {
				$(".diamond").addClass("myhidden");  
			};  
			$('.club').removeClass("myhidden");
		}
	});	 

	heart.click(function(){
		if(!$('.heart').hasClass("myhidden")){
			return; 
		} else { 
			if(!$('.spade').hasClass("myhidden")){
				$('.spade').addClass("myhidden");  
			} else if(!$('.club').hasClass("myhidden")){
				$(".club").addClass("myhidden"); 
			} else {
				$(".diamond").addClass("myhidden");  
			};  
			$('.heart').removeClass("myhidden");
		}
	});

	diamond.click(function(){
		if(!$('.diamond').hasClass("myhidden")){
			return; 
		} else { 
			if(!$('.heart').hasClass("myhidden")){
				$('.heart').addClass("myhidden");  
			} else if(!$('.club').hasClass("myhidden")){
				$(".club").addClass("myhidden"); 
			} else {
				$(".spade").addClass("myhidden");  
			};  
			$('.diamond').removeClass("myhidden");
		}
	});	
	$('.cards').click(function(event){ 
		var target = event.target;
		console.log($(this).hasClass('cards'));  
		writecard($(this));
	}); 

}


$(document).ready(main); 