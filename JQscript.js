var main = function(){
	var to_append_to = $('.to_append'); 
	for (var i = 1; i <= 13; i++) {
		if (i === 1){
			to_append_to.append('<td><table class="cards A"><tr><td>♠</td></tr><tr><td>A</td></tr></table><td>'); 
		} else if (i===11 ){
			to_append_to.append('<td><table class="cards J"><tr><td>♠</td></tr><tr><td>J</td></tr></table><td>'); 
		} else if (i===12){
			to_append_to.append('<td><table class="cards Q"><tr><td>♠</td></tr><tr><td>Q</td></tr></table><td>'); 		
		} else if (i===13){
			to_append_to.append('<td><table class="cards K"><tr><td>♠</td></tr><tr><td>K</td></tr></table><td>'); 	
		} else {
			to_append_to.append('<td><table class="cards '+i+'"><tr><td>♠</td></tr><tr><td>'+i+'</td></tr></table><td>'); 
		}

		to_append_to.append('<td><table class="emptycards"><tr><td> </td></tr></table></td>'); 
		
	};

	var spade = $('.spadebtn'); 
	var club = $('.clubbtn'); 
	var heart = $('.heartbtn'); 
	var diamond = $('.diamondbtn'); 
	var cardtable = $('.cardtable');
	//var to_remov);  
	spade.click(function(){
		if(cardtable.hasClass("spade")){
			return; 
		} else { 
			if(cardtable.hasClass("heart")){
				cardtable.removeClass("heart"); 
			} else if(cardtable.hasClass("club")){
				cardtable.removeClass("club"); 
			} else if(cardtable.hasClass("diamond")){
				cardtable.removeClass("diamond"); 
			}; 
			//to_remove.remove(); 
			to_append_to.empty(); 
			cardtable.addClass("spade"); 
			for (var i = 1; i <= 13; i++) {
				if (i === 1){
					to_append_to.append('<td><table class="cards A"><tr><td>♠</td></tr><tr><td>A</td></tr></table><td>'); 
				} else if (i===11 ){
					to_append_to.append('<td><table class="cards J"><tr><td>♠</td></tr><tr><td>J</td></tr></table><td>'); 
				} else if (i===12){
					to_append_to.append('<td><table class="cards Q"><tr><td>♠</td></tr><tr><td>Q</td></tr></table><td>'); 		
				} else if (i===13){
					to_append_to.append('<td><table class="cards K"><tr><td>♠</td></tr><tr><td>K</td></tr></table><td>'); 	
				} else {
					to_append_to.append('<td><table class="cards '+i+'"><tr><td>♠</td></tr><tr><td>'+i+'</td></tr></table><td>'); 
				}

				to_append_to.append('<td><table class="emptycards"><tr><td> </td></tr></table></td>'); 
				
			};
		}
	});
	club.click(function(){
		if(cardtable.hasClass("club")){
			return; 
		} else { 
			if(cardtable.hasClass("heart")){
				cardtable.removeClass("heart"); 
			} else if(cardtable.hasClass("spade")){
				cardtable.removeClass("spade"); 
			} else if(cardtable.hasClass("diamond")){
				cardtable.removeClass("diamond"); 
			}; 
			cardtable.addClass("club"); 
			//to_remove.remove(); 
			to_append_to.empty(); 	
			for (var i = 1; i <= 13; i++) {
				if (i === 1){
					to_append_to.append('<td><table class="cards A"><tr><td>♣</td></tr><tr><td>A</td></tr></table><td>'); 
				} else if (i===11 ){
					to_append_to.append('<td><table class="cards J"><tr><td>♣</td></tr><tr><td>J</td></tr></table><td>'); 
				} else if (i===12){
					to_append_to.append('<td><table class="cards Q"><tr><td>♣</td></tr><tr><td>Q</td></tr></table><td>'); 		
				} else if (i===13){
					to_append_to.append('<td><table class="cards K "><tr><td>♣</td></tr><tr><td>K</td></tr></table><td>'); 	
				} else {
					to_append_to.append('<td><table class="cards '+i+'"><tr><td>♣</td></tr><tr><td>'+i+'</td></tr></table><td>'); 
				}

				to_append_to.append('<td><table class="emptycards"><tr><td> </td></tr></table></td>'); 
				
			};
		}
	});
	heart.click(function(){
		if(cardtable.hasClass("heart")){
			return; 
		} else { 
			if(cardtable.hasClass("spade")){
				cardtable.removeClass("spade"); 
			} else if(cardtable.hasClass("club")){
				cardtable.removeClass("club"); 
			} else if(cardtable.hasClass("diamond")){
				cardtable.removeClass("diamond"); 
			}; 
			cardtable.addClass("heart"); 
	
			to_append_to.empty(); 		
			for (var i = 1; i <= 13; i++) {
				if (i === 1){
					to_append_to.append('<td><table class="redcards cards A"><tr><td>♥</td></tr><tr><td>A</td></tr></table><td>'); 
				} else if (i===11 ){
					to_append_to.append('<td><table class="redcards cards J"><tr><td>♥</td></tr><tr><td>J</td></tr></table><td>'); 
				} else if (i===12){
					to_append_to.append('<td><table class="redcards cards Q"><tr><td>♥</td></tr><tr><td>Q</td></tr></table><td>'); 		
				} else if (i===13){
					to_append_to.append('<td><table class="redcards cards K"><tr><td>♥</td></tr><tr><td>K</td></tr></table><td>'); 	
				} else {
					to_append_to.append('<td><table class="redcards cards '+i+'"><tr><td>♥</td></tr><tr><td>'+i+'</td></tr></table><td>'); 
				}

				to_append_to.append('<td><table class="emptycards"><tr><td> </td></tr></table></td>'); 
				
			};
		}
	});
	diamond.click(function(){
		if(cardtable.hasClass("diamond")){
			return; 
		} else { 
			if(cardtable.hasClass("heart")){
				cardtable.removeClass("heart"); 
			} else if(cardtable.hasClass("club")){
				cardtable.removeClass("club"); 
			} else if(cardtable.hasClass("spade")){
				cardtable.removeClass("spade"); 
			}; 
			cardtable.addClass("diamond"); 
			to_append_to.empty();
			for (var i = 1; i <= 13; i++) {
				if (i === 1){
					to_append_to.append('<td><table class="redcards cards"><tr><td>♦</td></tr><tr><td>A</td></tr></table><td>'); 
				} else if (i===11 ){
					to_append_to.append('<td><table class="redcards cards"><tr><td>♦</td></tr><tr><td>J</td></tr></table><td>'); 
				} else if (i===12){
					to_append_to.append('<td><table class="redcards cards"><tr><td>♦</td></tr><tr><td>Q</td></tr></table><td>'); 		
				} else if (i===13){
					to_append_to.append('<td><table class="redcards cards"><tr><td>♦</td></tr><tr><td>K</td></tr></table><td>'); 	
				} else {
					to_append_to.append('<td><table class="redcards cards"><tr><td>♦</td></tr><tr><td>'+i+'</td></tr></table><td>'); 
				}

				to_append_to.append('<td><table class="emptycards"><tr><td> </td></tr></table></td>'); 
				
			};
		}
	}); 
}


$(document).ready(main); 