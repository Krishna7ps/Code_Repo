var john={
    name:'john',
    job:'teacher',
};

console.log(john.name);
console.log(john['job']);
john['lastName']='Miller';
john.age=29;
console.log(john['age'],john['lastName']);

console.log(john)