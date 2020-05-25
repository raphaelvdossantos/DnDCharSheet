// Pagination Handling


/*const pages = document.querySelectorAll('#page');

const nextButton = document.getElementById('next-button');
const previousButton = document.getElementById('previous-button');
const submitButton = document.getElementById('submit-button');
var pageNumber = 0;

nextButton.addEventListener('click', () => {

	previousButton.style.display = 'block';
	pages[pageNumber].style.display = 'none';		
	pageNumber++;

	if(pageNumber<2){
		pages[pageNumber].style.display = 'block';
		console.log(pageNumber)

	}else{	
		pages[pageNumber].style.display = 'block';
		nextButton.style.display = 'none';
		submitButton.style.display= 'block';
	}
})

previousButton.addEventListener('click', () => {

	submitButton.style.display= 'none';
	pages[pageNumber].style.display = 'none';	
	pageNumber--
	pages[pageNumber].style.display = 'block';	
	console.log(pageNumber);

	if(pageNumber<1){
		previousButton.style.display = 'none';
	}else if(pageNumber>=0){
		nextButton.style.display = 'block';
	}
	
})
*/

const submitButton = document.getElementById('submit-button')

submitButton.addEventListener('click', () => {
    if(confirm("Pressione 'OK' se estiver tudo certo!")){
    $('form').submit()}
    else{
    }
})


//Attribute Values Definition

function attributeRoll(){
	attributeRolls = [];
	var attributeValue = 0;
	
	while (attributeValue<10){
		attributeValue =0;
		
		for(i=0;i<4;i++){
			attributeRolls[i] = Math.floor(Math.random()*6) + 1;
		}
		
		attributeRolls.sort()
		attributeRolls.shift()

		for(roll in attributeRolls){
			attributeValue += attributeRolls[roll]
		}
	}
	return attributeValue
}


const attributeFields = document.querySelectorAll('.basic-info-input');
const rollButton = document.getElementById('roll-button');

rollButton.addEventListener('click',() => {

  for(attribute in attributeFields){
    attributeFields[attribute].value = attributeRoll()
  }
});
