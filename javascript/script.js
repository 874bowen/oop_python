document.write("<p>I am called from outside</p>");
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