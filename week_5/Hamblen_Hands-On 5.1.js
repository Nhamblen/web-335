// Add a new user document to the users collection
db.users.insertOne({
  firstName: "Noah",
  lastName: "Hamblen",
  email: "noah.hamblen@example.com",
  age: 26,
  city: "Omaha",
});

// Find the newly added user to confirm insertion
db.users.findOne({ email: "noah.hamblen@example.com" });

// Update Mozart's email address in the users collection
db.users.updateOne(
  { firstName: "Wolfgang", lastName: "Mozart" }, // Filter
  { $set: { email: "mozart@me.com" } } // Update operation
);

// Find Mozart to confirm email update
db.users.findOne({ firstName: "Wolfgang", lastName: "Mozart" });

// Retrieve all users, projecting only firstName, lastName, and email fields
db.users.find(
  {},
  { firstName: 1, lastName: 1, email: 1, _id: 0 } // Projection
);
