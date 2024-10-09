const path = require('path');
const ScoreCounter = require('score-tests'); // eslint-disable-line import/no-extraneous-dependencies
const { clearArr, getFirstItem } = require('../src/debug');

const testSuiteName = 'Debug Tests';
const scoresDir = path.join(__dirname, '..', 'scores');
const scoreCounter = new ScoreCounter(testSuiteName, scoresDir);

describe(testSuiteName, () => {
  it('clearAll - removes all elements from an array as a mutation', () => {
    const arr1 = [1, 2, 3, 4, 5];
    clearArr(arr1);
    expect(arr1).toEqual([]);

    const arr2 = ['a', 'b', 'c'];
    clearArr(arr2);
    expect(arr2).toEqual([]);

    const arr3 = [];
    clearArr(arr3);
    expect(arr3).toEqual([]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('getFirstItem - returns the first item in an array WITHOUT mutating original', () => {
    const arr1 = [1, 2, 3, 4, 5];
    expect(getFirstItem(arr1)).toEqual(1);
    expect(arr1).toEqual([1, 2, 3, 4, 5]);

    const arr2 = ['a', 'b', 'c'];
    expect(getFirstItem(arr2)).toEqual('a');
    expect(arr2).toEqual(['a', 'b', 'c']);

    const arr3 = [];
    expect(getFirstItem(arr3)).toEqual(undefined);
    expect(arr3).toEqual([]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });
  // IGNORE PLEASE
  beforeEach(() => scoreCounter.add(expect));
  afterAll(scoreCounter.export);
});
