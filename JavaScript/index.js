// 2 + 3
// 5
// var name = "Sai subash"
// undefined
// name
// 'Sai subash'
// name + " is super cool 🎉"
// 'Sai subash is super cool 🎉'
// 2 // 3
// 2
// 3 ** 2
// 9
// typeof(name)
// 'string'
// typeof(9)
// 'number'
// typeof(true)
// 'boolean'
// typeof(false) // False
// 'boolean'
// var marks = [70, 80, 90, 100]
// undefined
// marks
// (4) [70, 80, 90, 100]0: 701: 802: 903: 100length: 4[[Prototype]]: Array(0)
// var student =  {
//     "name" : "Tonika",
//     "batch" : 3
// }
// undefined
// typeof(student)
// 'object'
// typeof(marks)
// 'object'
// student["name"]
// 'Tonika'
// marks[0]
// 70
// student
// {name: 'Tonika', batch: 3}
// student["name"] // box syntax
// 'Tonika'
// student.name
// 'Tonika'
// student.name  + ' is in ' + student.batch
// 'Tonika is in 3'
// student.name  + ' is in batch ' + student.batch
// 'Tonika is in batch 3'
// // type casting or coercion
// undefined
// []  + []
// ''
// [5, 6, 10] + " nice"
// '5,6,10 nice'
// [5, 6,         10].toString()
//  Task - 1
function movieUrl(domain, genre, year) {
  return "http://" + domain + "?genere=" + genre + "&year=" + year;
}
console.log(movieUrl("imdb.com", "thriller", 2020));
// Template literal
function movieUrl2(domain, genre, year) {
  return `https://${domain}?genre=${genre}&year=${year}`;
}
console.log(movieUrl2("imdb.com", "thriller", 2020));

let t1 = [80, 90];
let t2 = [50, 60];
let t3 = [...t1, ...t2];
console.log(t3);
//   [80, 90, 50, 60]

//   Math operation
console.log(Math.max(6, 7, 4)); // Accepts n no. of argument

let heights = [120, 140, 190, 80, 170]; // object
//   console.log(
//     Math.max(heights[0], heights[1], heights[2], heights[3], heights[4])
//   );
console.log(Math.max(heights)); // NaN
console.log(Math.max(...heights)); // 190

//   ... rest
function own_max(...nums) {
  // code
  return nums;
}
console.log(own_max(5, 6, 10));
console.log(own_max(5, 6, 10, 7, 80, 60));
