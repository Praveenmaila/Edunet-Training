
obj1 ={
    name : "pranav",
    age : 22,
    city : "Hyderabad"
};
obj2 ={
    name : "praveen",
    age : 23,
    city : "bangalore"
};
obj3 ={
    name : "anirudh",
    age : 22,
    city : "chennai"
};
console.log(obj1);
console.log(obj2);
console.log(obj3);
function printDetails(obj) {
    console.log("Name: " + obj.name);
    console.log("Age: " + obj.age);
    console.log("City: " + obj.city);
}
printDetails(obj1);
printDetails(obj2);
printDetails(obj3);
