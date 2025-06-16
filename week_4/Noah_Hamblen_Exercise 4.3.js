// Noah Hamblen
// 6/15/25

// a. Display all users in the collection (with pretty format for readability)
db.users.find().pretty();

// b. Display the user with the email address jbach@me.com (with pretty format for readability)
db.users.find({ email: "jbach@me.com" }).pretty();

// c. Display the user with the last name Mozart (with pretty format for readability)
db.users.find({ lastName: "Mozart" }).pretty();

// d. Display the user with the first name Richard (with pretty format for readability)
db.users.find({ firstName: "Richard" }).pretty();

// e. Display the user with employeeId 1010 (with pretty format for readability)
db.users.find({ employeeId: "1010" }).pretty();
