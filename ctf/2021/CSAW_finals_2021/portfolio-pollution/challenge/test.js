import merge from 'merge-objects';


let body = {"name": "qwd", "email": "wdqwd@gmail.com", "phone": "wdqwd", "message": "wdwqdqwd", "emergency": true};
let details = {"name": "Anonymous", "email": "n/a", "phone": "n/a", "emergency": false};

merge(details, body);

console.log(details);
