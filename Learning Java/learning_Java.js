var needCoffee = true;
if (needCoffee) {
    console.log('Finding coffee');
} else {
    console.log('Keep on keeping on!');
}

var moonPhase = 'full';
switch (moonPhase){
    case 'full':
    console.log('Howwwlll!!');
    break;
    case 'mostly full':
    console.log('Arms and legs are getting hairier.');
    break;
    case 'mostly new':
    console.log('Invalid moon phase');
    break;
  default:
    console.log('Invalid moon phase');
    break;
}

var orderCount = 0;
function takeOrder(topping, crustType){
  orderCount = orderCount +1 ;
  console.log('Order:'+ crustType + ' pizza toppend with ' + topping);
}

function getSubTotal(itemCount){

  return itemCount*7.5;
}

function getTax(){
  return 0.06*getSubTotal(orderCount);
}

function getTotal(){
  return getSubTotal(orderCount) + getTax();
}

takeOrder('bacon','thin');
takeOrder('pepori','thick');
takeOrder('heese','soft');
console.log(getTotal());

console.log(getSubTotal(orderCount));
var bucketList = ['learn Java','Learn Optical gates based design','Do cycling'];
var listItem = bucketList[0];
bucketList.push('cook delicious food', 'exercise');
console.log(bucketList.length);
console.log(bucketList);
bucketList.pop(); // delete the last item
console.log(bucketList);

var animals = ["Grizzly Bear", "Sloth", "Sea Lion"];

for (var i = 0; i < animals.length; i++) {
  console.log(animals[i]);
}

var cards = ['Diamond', 'Spade', 'Heart', 'Club'];

var currentCard = 'Heart';

while (currentCard !== 'Spade') {
  console.log(currentCard);
  var randomNumber = Math.floor(Math.random() * 4);

  currentCard = cards[randomNumber];
}

console.log('Found a Spade!');