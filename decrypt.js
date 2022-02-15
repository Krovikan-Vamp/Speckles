var arr = [92, 122, 139, 125, 130];
var new_arr = [];


arr.map(function (char) {
    new_arr.push(String.fromCharCode(char - 25));

    return true;
});

console.log(new_arr.join(''))