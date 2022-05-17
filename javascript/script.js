document.write("<p>I am called from outside</p>");
var materials = [
    'Hydrogen',
    'Helium',
    'Lithium',
    'Beryllium'
]
var materialsLength1 = materials.map(function(material){
    return material.length;
});
var materialsLength2 = materials.map((material) => {
    return material.length;
});
var materialsLength3 = materials.map(material => material.length);
console.log(materialsLength3);
console.log(materialsLength2);
console.log(materialsLength1);

var sum = (a, b) => a * b;
console.log(sum(2, 3));
var isPositive = number => number >= 0;
console.log(isPositive(3));
var randomNum = () => Math.random
console.log(randomNum);
gl = 123
function product(a, b) {
    // to make variable in js local we add 'var'
    var gl = 456
    val = a*b;
    return val
}
console.log("9 * 6 = " + product(9, 6) + "\nglobal = " + gl)

// class PartyAnimal with name as a parameter constructor
function PartyAnimal(nam){
    // each object created has some data(variables)
    this.x = 0;
    this.name = nam;
    console.log("I am constructed");
    // each object created has some code(function)
    this.party = function() { // function party
        this.x = this.x + 1;
        console.log("x is " + this.x);
    }
}
// create an instance of class PartyAnimal
an = new PartyAnimal("Jim");
// call function party() on object an
an.party();
an.party();
an.party();
dog = new PartyAnimal("Simba");
dog.party();
dog.party();
counter = 0
console.log(document.getElementById("the_list"));
    function add() {
        var x = document.createElement('li');
        x.className = "list_item";
        x.innerHTML = "Counter is " + counter;
        document.getElementById("the_list").appendChild(x);
        counter++
    }
