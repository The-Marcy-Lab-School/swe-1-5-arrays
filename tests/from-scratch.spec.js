const path = require('path');
const ScoreCounter = require('score-tests');
const {
  addToFrontOrBack,
  reverseString,
  newArrayFullOf,
  insertIntoMiddle,
  deleteFromMiddle,
  isRightIndex,
  roundAllNumsDown,
  getAllYCoordinates,
} = require('../src/from-scratch');

const testSuiteName = 'From Scratch Tests';
const scoresDir = path.join(__dirname, '..', 'scores');
const scoreCounter = new ScoreCounter(testSuiteName, scoresDir);

describe(testSuiteName, () => {
  it('addToFrontOrBack - MUTATION - adds value to the front or back', () => {
    const arr1 = [1, 2, 3, 4, 5];
    addToFrontOrBack(arr1, 6, false);
    expect(arr1).toEqual([1, 2, 3, 4, 5, 6]);

    const arr2 = [1, 2, 3, 4, 5];
    addToFrontOrBack(arr2, 0, true);
    expect(arr2).toEqual([0, 1, 2, 3, 4, 5]);

    const arr3 = [];
    addToFrontOrBack(arr3, 1, false);
    expect(arr3).toEqual([1]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('reverseString - PURE - returns a reversed string', () => {
    expect(reverseString('hello')).toEqual('olleh');
    expect(reverseString('hello world')).toEqual('dlrow olleh');
    expect(reverseString('')).toEqual('');
    expect(reverseString('a')).toEqual('a');

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('newArrayFullOf - PURE - returns an array full of the given value', () => {
    expect(newArrayFullOf(5, 3)).toEqual([5, 5, 5]);
    expect(newArrayFullOf('a', 2)).toEqual(['a', 'a']);
    expect(newArrayFullOf(undefined, 3)).toEqual([undefined, undefined, undefined]);
    expect(newArrayFullOf(0, 0)).toEqual([]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('insertIntoMiddle - MUTATION - inserts value into the middle of an array', () => {
    const arr1 = [1, 2, 3, 4, 5];
    insertIntoMiddle(arr1, 6);
    expect(arr1).toEqual([1, 2, 6, 3, 4, 5]);

    const arr2 = [1, 2, 3];
    insertIntoMiddle(arr2, 0);
    expect(arr2).toEqual([1, 0, 2, 3]);

    const arr3 = ['a', 'b', 'c', 'd'];
    insertIntoMiddle(arr3, 'z');
    expect(arr3).toEqual(['a', 'b', 'z', 'c', 'd']);

    const arr4 = [];
    insertIntoMiddle(arr4, 1);
    expect(arr4).toEqual([1]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('deleteFromMiddle - MUTATION - deletes value from the middle of an array', () => {
    const arr1 = [1, 2, 3, 4, 5];
    deleteFromMiddle(arr1);
    expect(arr1).toEqual([1, 2, 4, 5]);

    const arr2 = [1, 2, 3];
    deleteFromMiddle(arr2);
    expect(arr2).toEqual([1, 3]);

    const arr3 = ['a', 'b', 'c', 'd'];
    deleteFromMiddle(arr3);
    expect(arr3).toEqual(['a', 'b', 'd']);

    const arr4 = [];
    deleteFromMiddle(arr4);
    expect(arr4).toEqual([]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('isRightIndex - PURE - returns true if the index is the right index', () => {
    const arr = ['a', 'b', 'c', 'd', 'e'];

    expect(isRightIndex(arr, 'a', 0)).toBeTruthy();
    expect(isRightIndex(arr, 'a', 1)).toBeFalsy();
    expect(isRightIndex(arr, 'WOW', 1)).toBeFalsy();
    expect(isRightIndex(arr, 'A', 1)).toBeFalsy();

    expect(arr).toEqual(['a', 'b', 'c', 'd', 'e']);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('roundAllNumsDown - PURE - rounds all numbers down', () => {
    const arr1 = [1.1, 2.2, 3.3];
    expect(roundAllNumsDown(arr1)).toEqual([1, 2, 3]);
    expect(arr1).toEqual([1.1, 2.2, 3.3]);

    const arr2 = [5.9, -7.9, 12.9];
    expect(roundAllNumsDown(arr2)).toEqual([5, -8, 12]);
    expect(arr2).toEqual([5.9, -7.9, 12.9]);

    const arr3 = [4.1, 12.2, 33.3];
    expect(roundAllNumsDown(arr3)).toEqual([4, 12, 33]);
    expect(arr3).toEqual([4.1, 12.2, 33.3]);

    const arr4 = [4, 5, 7];
    expect(roundAllNumsDown(arr4)).toEqual([4, 5, 7]);
    expect(arr4).toEqual([4, 5, 7]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('getAllYCoordinates - PURE - returns an array of all y coordinates', () => {
    const arr1 = [[1, 2], [3, 4], [5, 6]];
    expect(getAllYCoordinates(arr1)).toEqual([2, 4, 6]);
    expect(arr1).toEqual([[1, 2], [3, 4], [5, 6]]);

    // these are [x, y, z] coordinates
    const arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
    expect(getAllYCoordinates(arr2)).toEqual([2, 5, 8]);
    expect(arr2).toEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

    const arr3 = [[12.3, 81.3], [1.2, 3.4], [5.6, 7.8]];
    expect(getAllYCoordinates(arr3)).toEqual([81.3, 3.4, 7.8]);
    expect(arr3).toEqual([[12.3, 81.3], [1.2, 3.4], [5.6, 7.8]]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  // IGNORE PLEASE
  beforeEach(() => scoreCounter.add(expect));
  afterAll(scoreCounter.export);
});
