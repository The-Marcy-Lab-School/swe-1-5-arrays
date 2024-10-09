const path = require('path');
const ScoreCounter = require('score-tests');
const { uppercaseAll, destructureCoordinates } = require('../src/modify');

const testSuiteName = 'Modify Tests';
const scoresDir = path.join(__dirname, '..', 'scores');
const scoreCounter = new ScoreCounter(testSuiteName, scoresDir);

describe(testSuiteName, () => {
  it('uppercaseAll - No matter how many words passed in, they are uppercased', () => {
    const result1 = uppercaseAll('hello', 'world');
    expect(result1).toEqual(['HELLO', 'WORLD']);

    const result2 = uppercaseAll('hello', 'my', 'name', 'is', 'bob');
    expect(result2).toEqual(['HELLO', 'MY', 'NAME', 'IS', 'BOB']);

    const result3 = uppercaseAll('hello');
    expect(result3).toEqual(['HELLO']);

    // randomly generated string of lowercase letters
    // eslint-disable-next-line
    const randStr = Math.random().toString(36).slice(2).split('').filter((char) => Number.isNaN(Number(char))).join('');
    const result4 = uppercaseAll(randStr);
    expect(result4).toEqual([randStr.toUpperCase()]);

    const result5 = uppercaseAll();
    expect(result5).toEqual([]);

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  it('destructureCoordinates - Destructures the coordinates array into x and y variables', () => {
    const textContent = destructureCoordinates.toString();

    expect(textContent).not.toMatch(/const x/);
    expect(textContent).not.toMatch(/const y/);
    expect(textContent).toMatch(/`X is: \${x}, Y is: \${y}`/);

    const result1 = destructureCoordinates([1, 2]);
    expect(result1).toEqual('X is: 1, Y is: 2');

    const result2 = destructureCoordinates([3, 4]);
    expect(result2).toEqual('X is: 3, Y is: 4');

    scoreCounter.correct(expect); // DO NOT TOUCH
  });

  // IGNORE PLEASE
  beforeEach(() => scoreCounter.add(expect));
  afterAll(scoreCounter.export);
});
