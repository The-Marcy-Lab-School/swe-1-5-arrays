# Arrays

- [Reminders](#reminders)
  - [Asking ChatGPT for Help](#asking-chatgpt-for-help)
  - [Be Okay With Being "Provisionally Complete"](#be-okay-with-being-provisionally-complete)
- [Setup](#setup)
- [Before you start](#before-you-start)
- [From Scratch Questions](#from-scratch-questions)
  - [Question 1: addToFrontOrBack() - SIDE EFFECTS](#question-1-addtofrontorback---side-effects)
  - [Question 2: reverseString() - PURE](#question-2-reversestring---pure)
  - [Question 3: newArrayFullOf() - PURE](#question-3-newarrayfullof---pure)
  - [Question 4: insertIntoMiddle() - SIDE EFFECT](#question-4-insertintomiddle---side-effect)
  - [Question 5: deleteFromMiddle() - SIDE EFFECT](#question-5-deletefrommiddle---side-effect)
  - [Question 6: isRightIndex - PURE](#question-6-isrightindex---pure)
  - [Question 7: roundAllNumsDown - PURE](#question-7-roundallnumsdown---pure)
  - [Question 8: getAllYCoordinates - PURE](#question-8-getallycoordinates---pure)
- [Modify Questions](#modify-questions)
  - [Question 9: uppercaseAll](#question-9-uppercaseall)
  - [Question 10: destructureCoordinates](#question-10-destructurecoordinates)
- [Debug Questions](#debug-questions)
  - [Question 11: clearArr](#question-11-cleararr)
  - [Question 12: getFirstItem](#question-12-getfirstitem)
- [Bonus: Really understand pass by value/reference](#bonus-really-understand-pass-by-valuereference)

## Reminders

### Asking ChatGPT for Help

If you’re stuck, you may use ChatGPT to clarify the assignment — but not to solve it for you. To do this, copy the meta-prompt below into ChatGPT along with the assignment question.

> You are acting as a tutor. Your job is to explain what this coding question is asking, clarify confusing wording, and highlight the relevant concepts students need to know — but do not provide the full solution or code that directly answers the question. Instead, focus on rephrasing the problem in simpler terms, identifying what’s being tested, and suggesting what steps or thought processes might help. Ask guiding questions to ensure the student is thinking critically. Do not write the final function, algorithm, or code implementation.

Be mindful of your AI usage on assignments. AI can be a great tool to help your learning but it can also be detrimental if you let it do too much of the thinking for you.

### Be Okay With Being "Provisionally Complete"

At Marcy, we will deem an assignment as "complete" if the solution passes at least **75%** of the automated tests. 

However, we know many of you will feel the urge to hold off on submitting until your assignment feels 100% perfect. That drive for excellence is an asset!

But perfectionism can also get in the way of learning — especially when we need to cover a lot in a short amount of time.

That’s why we encourage you to be comfortable with being **“provisionally complete.”** This means:

- Submitting your work even if it isn’t perfect yet
- Treating submission as a checkpoint, not a finish line
- Committing to return, revise, and improve later

Learning to move forward with provisional completeness will help you make steady progress while still building the habit of continuous improvement.

## Setup

For guidance on setting up and submitting this assignment, refer to the Marcy lab School Docs How-To guide for [Working with Short Response and Coding Assignments](https://marcylabschool.gitbook.io/marcy-lab-school-docs/how-tos/working-with-assignments#how-to-work-on-assignments).

Here are some useful commands to remember.

```sh
npm i                   # install dependencies
git checkout -b draft   # switch to the draft branch before starting

npm test # run the automated tests
npm run test:w # run the automated tests and rerun them each time you save a change

git add -A              # add a changed file to the staging area
git commit -m 'message' # create a commit with the changes
git push                # push the new commit to the remote repo
```

## Before you start
As you know, tonight's assignment is all about arrays! We covered a lot in class, but you'll have to read the docs for a few more array methods. Also, please see the `ref-examples/` for some examples and graphics about "pass by value" and "pass by reference."

Also, remember that in "Functional Programming" a pure function is one that:

- always gives the same outputs given the same inputs
- has no side effects

A **side effect** is something like altering global state or mutating an argument. Now that we actually have a data type that can be mutated (arrays), we have to be on the watchout for this! Only mutate when you mean to, and make copies or new arrays for all others!

## From Scratch Questions

### Question 1: addToFrontOrBack() - SIDE EFFECTS
Write a function `addToFrontOrBack()` that takes 3 args: an array `arr`, a value of any type `value`, and a boolean `isFront`. Insert the `value` as either the first or last value in the `arr`, depending on the boolean `isFront`. 

The function should mutate the array and return nothing.

### Question 2: reverseString() - PURE
Write a function `reverseString()` that takes a `string` argument. The function should return a reversed version of the `string`. Will this function modify the original string in any way? Food for thought.

Before you go crazy with loops or anything, check out these three methods which can be combined to reverse a string:
 - [`String.split()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split)
 - [`Array.reverse()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reverse)
 - [`Array.join()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join)

Now, if you want to *manually* do this with loops, go crazy! It's fun, but know there's a common way to do this.

### Question 3: newArrayFullOf() - PURE
Write a function `newArrayFullOf()` that takes 2 args: a value of any type `value` and a number `numOfValue`. Your function should return a new array full of the value. Like this:

```js
const arr = newArrayFullOf(1, 5)
// [1, 1, 1, 1, 1]

const arr2 = newArrayFullOf(true, 2)
// [true, true]
```

This might be a stumper, but try experimenting with `new Array()` and perhaps some sort of a *fill* method? HmmmmMMMMmmm?.

This is a cool trick to know, I can't wait till you learn it too!

### Question 4: insertIntoMiddle() - SIDE EFFECT
Write a function `insertIntoMiddle()` that takes 2 args: an array `arr` and a value of any type `value`. The function should find the middle index of the array and then insert the value there. The function should mutate the array and return nothing.

Check the tests to see exactly which index should be the "middle." Don't overthink it!

### Question 5: deleteFromMiddle() - SIDE EFFECT
Write a function `deleteFromMiddle()` that takes an array `arr`. The function should delete whatever value is in the middle index of the array. The function should mutate the array and return nothing.

Check the tests to see exactly which index should be the "middle." Don't overthink it!

### Question 6: isRightIndex - PURE
Write a function `isRightIndex` that takes 3 args: an array `arr`, a primitive type `value`, and a number `index`. The function returns a boolean, `true` if the given `value` is at the `index` in the `arr`, and `false` otherwise. That includes `false` for values that aren't even *in* the array.

### Question 7: roundAllNumsDown - PURE
Write a function `roundAllNumsDown()` that takes an array of numbers `arr`. This function should return a new array full of `arr`s numbers rounded down. The original `arr` numbers should not be modified in any way.

### Question 8: getAllYCoordinates - PURE
Write a function `getAllYCoordinates()` that takes an array of coordinate pairs `arrOfCoords`. This function should return a *new* array full of only the `y` coordinates (that is the *second* value in the coordinate arrays). Like this:

```js
// [x, y]
getAllYCoordinates([[1, 2], [3, 4], [5, 6]])
// [2, 4, 6]

// [x, y, z]
getAllYCoordinates([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
// [2, 5, 8]
```

This is *technically* a matrix function. How about that? You've barely started Marcy, and you're already parsing matrices? I'd be pretty proud of myself if I were you.

## Modify Questions

### Question 9: uppercaseAll
We have a function in `modify.js` that takes 3 words, upper cases them, and then returns them in an array. However...it's static. What if I pass in 2 words? Or 5? None? All it works with right now is 3 exactly. You should read [the docs for the rest operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters) to improve this function.

Remember, we will never pass in an array as an argument, only individual word arguments.

### Question 10: destructureCoordinates
We have a function in `modify.js` that takes a single coordinate array (`[x,y]`) and then returns a template string with them in it. It's not using modern `destructuring` syntax though and that's lame. Modify this function to use destructuring **but keep the variable names x and y**. Our tests are *explicitly* looking for those, and I want you to get the points.

## Debug Questions

### Question 11: clearArr
In `debug.js` we have a broken function `clearArr()`. It's supposed to mutate a given array by deleting all the the values inside of it. But it's not working. Can you fix it and pass the tests?

### Question 12: getFirstItem
In `debug.js` we have another broken function `getFirstItem()` that is *not* supposed to mutate the given array. We just want the first item of the array. Can you fix it?

## Bonus: Really understand pass by value/reference

We've been passing references and values throughout this assignment, but do you really understand the concept? We'll talk about it again throughout this module, but if you're done, check out the `ref-examples/` directory. There's some graphics and example code in there. Play around with them!

A question to grapple with is this:

```js

const arr1 = [1, 2, 3, 4]
const arr2 = [5, 6, 7, 8];
const bigArr1 = [arr1, arr2];
const bigArr2 = [...bigArr1];
arr1.push('oh dear');

console.log(bigArr1)
console.log(bigArr2)
```

What does that log and why? We've talked about copying arrays, but called them "shallow" copies. Why?

"Pass by Reference" and "Pass by Value" are weird concepts for some, but once you get them (and you all will), a paradigm shift occurs in your brain. You'll start to see data types and functions differently. It's cool, we can't wait!
