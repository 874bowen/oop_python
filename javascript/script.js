document.write("<p>I am called from outside</p>");
gl = 123
function product(a, b) {
    // to make variable in js local we add 'var'
    var gl = 456
    val = a*b;
    return val
}
console.log("9 * 6 = " + product(9, 6) + "\nglobal = " + gl)