// a. Display all students
db.students.find().pretty();

// b. Add a new student with fields matching the existing documents
db.students.insertOne({
  firstName: "Noah",
  lastName: "Hamblen",
  studentId: "s1019",
  houseId: "h1010",
});

// Prove the new student was added
db.students.find({ firstName: "Noah", lastName: "Hamblen" }).pretty();

// c. Update houseId
db.students.updateOne(
  { firstName: "Noah", lastName: "Hamblen" },
  { $set: { houseId: "h1009" } } // Ravenclaw
);

// Prove the update
db.students.find({ firstName: "Noah", lastName: "Hamblen" }).pretty();

// d. Delete from the collection
db.students.deleteOne({ firstName: "Noah", lastName: "Hamblen" });

// Prove deletion
db.students.find({ firstName: "Noah", lastName: "Hamblen" }).pretty();

// e. Group all students by their house
db.students
  .aggregate([
    { $group: { _id: "$houseId", students: { $push: "$firstName" } } },
  ])
  .pretty();

// f. Display all students in house Gryffindor
db.houses
  .aggregate([
    { $match: { houseId: "h1007" } },
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "students",
      },
    },
    {
      $project: {
        _id: 0,
        houseName: "Gryffindor",
        students: {
          $map: {
            input: "$students",
            as: "student",
            in: {
              fullName: {
                $concat: ["$$student.firstName", " ", "$$student.lastName"],
              },
            },
          },
        },
      },
    },
  ])
  .pretty();

// g. Display all students in the house with an Eagle mascot
db.houses
  .aggregate([
    { $match: { mascot: "Eagle" } },
    {
      $lookup: {
        from: "students",
        localField: "houseId",
        foreignField: "houseId",
        as: "students",
      },
    },
    {
      $project: {
        _id: 0,
        houseName: "$founder", // or "$houseId" if there's no house name field
        students: {
          $map: {
            input: "$students",
            as: "student",
            in: {
              fullName: {
                $concat: ["$$student.firstName", " ", "$$student.lastName"],
              },
            },
          },
        },
      },
    },
  ])
  .pretty();
