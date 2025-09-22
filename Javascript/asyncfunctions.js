async function printDetails(obj) {
    console.log("Name: " + obj.name);
    console.log("Age: " + obj.age);
    console.log("City: " + obj.city);   
};
printDetails({
    name : "pranav",
    age : 22,
    city : "bangalore"
}); 
printDetails({
    name : "praveen",
    age : 23,
    city : "bangalore"
});
printDetails({
    name : "anirudh",
    age : 22,
    city : "chennai"
});
