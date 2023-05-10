const uppercaseAll = (word1, word2, word3) => {
  return [
    word1.toUpperCase(),
    word2.toUpperCase(),
    word3.toUpperCase(),
  ];
};

const destructureCoordinates = (coordinates) => {
  const x = coordinates[0];
  const y = coordinates[1];
  return `X is: ${x}, Y is: ${y}`; // no touching this line!
};

module.exports = {
  uppercaseAll,
  destructureCoordinates,
};
